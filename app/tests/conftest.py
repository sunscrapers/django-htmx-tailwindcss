import pytest

from tests.fixtures.todo_tracker import *  # noqa


@pytest.fixture(scope="session", autouse=True)
def db_setup(django_db_setup):
    ...


@pytest.fixture(autouse=True)
def get_db_access(db):
    ...
