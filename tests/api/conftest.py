import pytest
import requests
from config.config import BASE_URL

@pytest.fixture
def api():
    #base_url = "https://fakestoreapi.com"
    session = requests.Session()
    #return session, base_url
    return session, BASE_URL