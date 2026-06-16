import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def snapshot_restore_activities():
    """Snapshot and restore the in-memory `activities` dict around each test."""
    original = copy.deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(original)
