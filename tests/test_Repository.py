import pytest
from classes.Repository import Repository


def test_getRepositoryName():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    assert repo.getRepositoryName() == 'TestRepo'

def test_getStarsCount():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    assert repo.getStarsCount() == 100

def test_getCreationDate():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    assert repo.getCreationDate() == '2023-01-01'

def test_getLastUpdatedDate():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    assert repo.getLastUpdatedDate() == '2023-01-02'

def test_to_dict():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    expected_dict = {
        "name": "TestRepo",
        "stars": 100,
        "created_at": "2023-01-01",
        "updated_at": "2023-01-02"
    }
    assert repo.to_dict() == expected_dict

def test_eq():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    repo_same = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    repo_diff = Repository('DiffRepo', 50, '2023-01-01', '2023-01-02')
    assert (repo == repo_same) == True
    assert (repo == repo_diff) == False

def test_str():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    expected_str = "Repository{repositoryName=TestRepo, starsCount=100, created_at=2023-01-01, updated_at=2023-01-02}"
    assert str(repo) == expected_str
