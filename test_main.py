import pytest
from src.main import app  # Import the Flask app

@pytest.fixture
def client():
    """Fixture to set up the test client."""
    app.testing = True  # Enable testing mode
    with app.test_client() as client:
        yield client

def test_main_route(client):
    """Test if the main route (/) returns status code 200."""
    response = client.get("/")  # Send GET request to the main route
    assert response.status_code == 200  # Assert that the status code is 200