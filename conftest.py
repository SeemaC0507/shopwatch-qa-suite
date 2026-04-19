import pytest
import requests

@pytest.fixture
def api():
    base_url = "https://fakestoreapi.com"
    session = requests.Session()
    return session, base_url