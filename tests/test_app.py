"""Tests for the Mergington High School FastAPI app.

Using Arrange-Act-Assert (AAA) pattern.
"""

def test_get_activities(client):
    # Arrange: none
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "tester@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]


def test_signup_duplicate(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing})

    # Assert
    assert resp.status_code == 400


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": existing})

    # Assert
    assert resp.status_code == 200
    assert existing not in client.get("/activities").json()[activity]["participants"]


def test_unregister_nonexistent(client):
    # Arrange
    activity = "Chess Club"
    email = "no-such-user@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 404
