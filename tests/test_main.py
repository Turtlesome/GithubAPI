from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_user_repos():
    response = client.get("/users/torvalds/repos")
    assert response.status_code == 200
    data = response.json()
    
    # Check that the response is a list
    assert isinstance(data, list)
    
    # Check that each item in the list is a dictionary (representing a repository)
    for item in data:
        assert isinstance(item, dict)
    
    # Check that each repository has the necessary keys
    necessary_keys = ['repositoryName', 'starsCount', 'created_at', 'updated_at']
    for repo in data:
        for key in necessary_keys:
            assert key in repo


def test_read_user_profile():
    response = client.get("/users/torvalds")
    assert response.status_code == 200
    data = response.json()
    
    # Check that the response is a dictionary (representing a user)
    assert isinstance(data, dict)
    
    # Check that the user dictionary has the necessary keys
    necessary_keys = ['login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 
                      'url', 'html_url', 'followers_url', 'following_url', 
                      'gists_url', 'starred_url', 'subscriptions_url', 
                      'organizations_url', 'repos_url', 'events_url', 
                      'received_events_url', 'type', 'site_admin']
    for key in necessary_keys:
        assert key in data


def test_read_repo_pulls():
    response = client.get("/torvalds/linux/pulls")
    assert response.status_code == 200
    data = response.json()
    
    # Check that the response is a list
    assert isinstance(data, list)
    
    # Check that each item in the list is a dictionary (representing a pull request)
    for item in data:
        assert isinstance(item, dict)
    
    # Check that each pull request has the necessary keys
    necessary_keys = ['id', 'url', 'title', 'user', 'state']
    for pull_request in data:
        for key in necessary_keys:
            assert key in pull_request


