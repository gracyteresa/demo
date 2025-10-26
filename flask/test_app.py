import pytest
from app import app

# Fixture to provide a test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test that the home page returns 200 OK
def test_home_status(client):
    res = client.get('/')
    assert res.status_code == 200

# Test that some expected content exists on the page
def test_home_content(client):
    res = client.get('/')
    html = res.data.decode('utf-8')  # decode bytes to string
    # Check for some text that will definitely be in the HTML
    assert "Created by Gracy" in html
