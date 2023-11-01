class InvalidTokenException(Exception):
    """Raised when the provided GitHub token is invalid."""
    def __init__(self):
        # When you define your own __init__ method in your exception classes, you’re overriding the __init__ method of the Exception class. 
        # But you still want to keep the functionality of the original __init__ method, which is to accept an error message as an argument and store it in the exception object.
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

