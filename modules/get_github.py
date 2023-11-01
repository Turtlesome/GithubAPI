import requests

import classes.Exceptions as Exceptions
from classes.Repository import Repository
from modules.logger import setup_logger
from modules.paths import create_logger


log_filename = create_logger()
log = setup_logger(log_filename)


def fetch_github_repositories(user_id, token):
    """
    Sends a GET request to the GitHub API and retrieves the list of repositories 
    for the given username. It then creates instances of the Repository class 
    for each repository and returns them.

    Args:
        username (str): The GitHub username to fetch repositories for.
        token (str): The personal access token for GitHub API authentication.

    Returns:
        list of Repository objects or None: A list of Repository instances representing the user's 
                                            repositories, or None if the request fails.

    Raises:
        requests.exceptions.RequestException: If a request error occurs.
    """    
    
    headers = {
        "User-Agent": "GitHub Repository Fetcher",
        "Authorization": f"token {token}"
    }

    page = 1
    repository_objects = []

    while True:
        url = f"https://api.github.com/users/{user_id}/repos?page={page}&per_page=100"
        
        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                repositories = response.json()
                
                if not repositories:
                    break
                
                repository_objects.extend([
                    Repository(repo['name'], repo['stargazers_count'], repo['created_at'], repo['updated_at'])
                    for repo in repositories
                ])
                page += 1 
            
            elif response.status_code == 401:
                raise Exceptions.InvalidTokenException()
            
            elif response.status_code == 403:
                raise Exceptions.RateLimitExceededException()
            
            elif response.status_code == 404:
                raise Exceptions.UserNotFoundException(user_id)
            
            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    return repository_objects


def fetch_github_user(user_id, token):
    """
    Sends a GET request to the GitHub API and returns the user's data as a JSON object.

    Args:
        user_id (str): The username of the GitHub user to fetch.
        token (str): The personal access token for GitHub API authentication.

    Returns:
        dict: A dictionary containing the user's data if the request is successful.
        str: An error message if the request is unsuccessful.
    """
    
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/users/{user_id}'
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
        
        elif response.status_code == 401:
            raise Exceptions.InvalidTokenException()
        
        elif response.status_code == 403:
            raise Exceptions.RateLimitExceededException()
        
        elif response.status_code == 404:
            raise Exceptions.UserNotFoundException(user_id)
        
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
    return user_data
    

def fetch_github_pull_requests(user_id, repo_id, token):
    """
    Sends a GET request to the GitHub API and returns the pull requests data as a JSON object.

    Args:
        user_id (str): The username of the GitHub user to fetch.
        repo_id (str): The ID of the GitHub repository to fetch pull requests from.
        token (str): The personal access token for GitHub API authentication.

    Returns:
        dict: A dictionary containing the pull requests data if the request is successful.
        str: An error message if the request is unsuccessful.
    """
    
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/repos/{user_id}/{repo_id}/pulls'
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            pulls_data = response.json()
        
        elif response.status_code == 401:
            raise Exceptions.InvalidTokenException()
        
        elif response.status_code == 403:
            raise Exceptions.RateLimitExceededException()
        
        elif response.status_code == 404:
            raise Exceptions.UserNotFoundException(user_id)

        elif response.status_code == 409:
            raise Exceptions.RepositoryNotFoundException(repo_id)

        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    
    return pulls_data


import requests

def list_files_in_repo(user_id, repo_id, token):
    """
    Lists all files in a specific GitHub repository.

    Args:
        user_id (str): The username of the GitHub user.
        repo_id (str): The ID of the GitHub repository.
        token (str): The personal access token for GitHub API authentication.

    Returns:
        list: A list of file paths in the repository.
    """
    
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/repos/{user_id}/{repo_id}/git/trees/master?recursive=1'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            files = [file['path'] for file in data['tree'] if file['type'] == 'blob']
        
        elif response.status_code == 401:
            raise Exceptions.InvalidTokenException()
        
        elif response.status_code == 403:
            raise Exceptions.RateLimitExceededException()
        
        elif response.status_code == 404:
            raise Exceptions.UserNotFoundException(user_id)
        
        elif response.status_code == 409:
            raise Exceptions.RepositoryNotFoundException(repo_id)
        
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
            
    return files
