import os
import json
from typing import Optional
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, Query, HTTPException, Request

import modules.paths as paths
from modules.get_github import fetch_github_repositories, fetch_github_user, fetch_github_pull_requests, list_files_in_repo


config_data = paths.open_config()
contact_data = config_data.get("contact")

token = os.getenv('GITHUB_TOKEN')

app = FastAPI(
    title="Custom API for github functionalities",
    version=config_data.get("api_version"),
    contact={"name": contact_data.get("name"), "email": contact_data.get("email")},
)

# Create a limiter instance
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(HTTPException)
async def _http_exception_handler(request, exc):
    if exc.status_code == 429:
        return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

cache = {}

@app.get('/users/{user_id}/repos')
@limiter.limit("10/minute")
def read_user_repos(request: Request, 
                    user_id: str, 
                    sort_by: Optional[str] = Query(None), 
                    min_stars: Optional[int] = Query(None),
                    max_stars: Optional[int] = Query(None),
                    created_after: Optional[str] = Query(None),
                    updated_after: Optional[str] = Query(None)):
    try:
        if user_id in cache:
            repos = cache[user_id]
        else:
            repos = fetch_github_repositories(user_id, token)
            cache[user_id] = repos

        if repos is not None:
            # Filter and sort the repositories based on the query parameters
            if min_stars is not None:
                repos = [repo for repo in repos if repo.getStarsCount() >= min_stars]
            if max_stars is not None:
                repos = [repo for repo in repos if repo.getStarsCount() <= max_stars]
            if created_after is not None:
                repos = [repo for repo in repos if repo.created_at > created_after]
            if updated_after is not None:
                repos = [repo for repo in repos if repo.updated_at > updated_after]
                
            if sort_by == 'starsR':
                repos.sort(key=lambda repo: repo.getStarsCount(), reverse=True)
            elif sort_by == 'stars':
                repos.sort(key=lambda repo: repo.getStarsCount(), reverse=False)
            elif sort_by == 'created':
                repos.sort(key=lambda repo: repo.created_at, reverse=True)
            elif sort_by == 'updated':
                repos.sort(key=lambda repo: repo.updated_at, reverse=True)
                
            repos_dicts = [repo.to_dict() for repo in repos]
            with open(fr'info\output_read_user_repos.json', 'w') as f:
                json.dump(repos_dicts, f, indent=4)
            return repos
        else:
            return "Failed to fetch repositories."
    except Exception as e:
        return str(e)


@app.get('/users/{user_id}')
@limiter.limit("10/minute")
def read_user_profile(request: Request, user_id: str):
    try:
        user = fetch_github_user(user_id, token)
        return user
    except Exception as e:
        return str(e)


@app.get('/{user_id}/{repo_id}/pulls')
@limiter.limit("10/minute")
def read_repo_pulls(request: Request, user_id: str, repo_id: str):
    try:
        pulls = fetch_github_pull_requests(user_id, repo_id, token)
        return pulls
    except Exception as e:
        return str(e)


@app.get("/{user_id}/{repo_id}/files")
@limiter.limit("10/minute")
def read_repo_files(request: Request, user_id: str, repo_id: str):
    try:
        files = list_files_in_repo(user_id, repo_id, token)
        with open(fr'info\output_read_repo_files.json', 'w') as f:
            json.dump(files, f, indent=4)
        return files
    except Exception as e:
        return str(e)