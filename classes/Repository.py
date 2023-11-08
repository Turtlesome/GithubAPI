class Repository:
    """
    A class to represent a GitHub repository.

    Attributes:
        repositoryName (str): The name of the repository.
        starsCount (int): The number of stars the repository has.
        created_at (str): The creation date of the repository.
        updated_at (str): The last updated date of the repository.

    Methods:
        getRepositoryName(): Returns the name of the repository.
        getStarsCount(): Returns the number of stars the repository has.
        getCreationDate(): Returns the creation date of the repository.
        getLastUpdatedDate(): Returns the last updated date of the repository.
        to_dict(): Returns a dictionary representation of the repository.
        __eq__(other): Determines if this repository is equal to another repository in terms of being an object.
        __str__(): Returns a string representation of the repository.
    """    

    def __init__(self, repositoryName, starsCount, created_at, updated_at):
        self.repositoryName = repositoryName
        self.starsCount = starsCount
        self.created_at = created_at
        self.updated_at = updated_at

    def getRepositoryName(self):
        return self.repositoryName

    def getStarsCount(self):
        return self.starsCount

    def getCreationDate(self):
        return self.created_at

    def getLastUpdatedDate(self):
        return self.updated_at
    
    def to_dict(self):
        return {
            "name": self.repositoryName,
            "stars": self.starsCount,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __eq__(self, other):
        if self is other:
            return True
        
        if other is None or type(self) != type(other):
            return False
        return self.starsCount == other.starsCount and self.repositoryName == other.repositoryName and self.created_at == other.created_at and self.updated_at == other.updated_at

    def __str__(self):
        return f"Repository{{repositoryName={self.repositoryName}, starsCount={self.starsCount}, created_at={self.created_at}, updated_at={self.updated_at}}}"
