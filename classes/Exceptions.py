class InvalidTokenException(Exception):
    """Raised when the provided GitHub token is invalid."""
    def __init__(self):
        super().__init__("The provided GitHub token is invalid.")

class RateLimitExceededException(Exception):
    """Raised when the rate limit of the GitHub API is exceeded."""
    def __init__(self):
        super().__init__("The rate limit of the GitHub API has been exceeded.")

class UserNotFoundException(Exception):
    """Raised when the specified user is not found."""
    def __init__(self, user_id):
        super().__init__(f"The user '{user_id}' was not found.")

class RepositoryNotFoundException(Exception):
    """Raised when the specified repository is not found."""
    def __init__(self, repo_id):
        super().__init__(f"The repositorium '{repo_id}' was not found.")

