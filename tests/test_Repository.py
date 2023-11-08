import pytest
from classes.Repository import Repository


@pytest.fixture
def test_repository():
    return Repository('TestRepo', 100, '2023-01-01', '2023-01-02')


def test_getRepositoryName(test_repository):
    assert test_repository.getRepositoryName() == 'TestRepo'


def test_getStarsCount(test_repository):
    assert test_repository.getStarsCount() == 100


def test_getCreationDate(test_repository):
    assert test_repository.getCreationDate() == '2023-01-01'


def test_getLastUpdatedDate(test_repository):
    assert test_repository.getLastUpdatedDate() == '2023-01-02'


def test_to_dict(test_repository):
    expected_dict = {
        "name": "TestRepo",
        "stars": 100,
        "created_at": "2023-01-01",
        "updated_at": "2023-01-02"
    }
    assert test_repository.to_dict() == expected_dict


def test_eq():
    repo = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    repo_same = Repository('TestRepo', 100, '2023-01-01', '2023-01-02')
    repo_diff = Repository('DiffRepo', 50, '2023-01-01', '2023-01-02')
    assert (repo == repo_same) == True
    assert (repo == repo_diff) == False


def test_str(test_repository):
    expected_str = "Repository{repositoryName=TestRepo, starsCount=100, created_at=2023-01-01, updated_at=2023-01-02}"
    assert str(test_repository) == expected_str
