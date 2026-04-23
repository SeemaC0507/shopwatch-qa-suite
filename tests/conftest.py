import pytest
import requests
from config.config import BASE_URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def api():
    #base_url = "https://fakestoreapi.com"
    session = requests.Session()
    #return session, base_url
    return session, BASE_URL

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    d = webdriver.Chrome(service=service, options=options)
    yield d
    d.quit()