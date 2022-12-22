import pytest
from selenium import webdriver
driver = None
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.fixture
def setup(request):
    global driver
    request.cls.driver = webdriver.Chrome(executable_path="E:\\DOWNLOADS\\chromedriver.exe")
    request.cls.driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    yield
    request.cls.driver.quit()


