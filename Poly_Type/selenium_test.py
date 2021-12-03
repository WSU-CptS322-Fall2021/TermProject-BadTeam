import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from app import create_app, db
from config import TestConfig
from time import sleep

@pytest.fixture(scope='module')
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)

    db.init_app(flask_app)
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield  testing_client 
    # this is where the testing happens!
 
    ctx.pop()

@pytest.fixture
def init_database():
    # Create the database and the database table
    db.create_all()

    yield  # this is where the testing happens!

    db.drop_all()

"""
Download the chrome driver and make sure you have chromedriver executable in your PATH variable. 
To download the ChromeDriver to your system navigate to its download page. 
https://sites.google.com/chromium.org/driver/
https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/
"""
@pytest.fixture
def browser():
    CHROME_PATH = "c:\\test"
    print(CHROME_PATH)
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(options=opts, executable_path = CHROME_PATH + '/chromedriver.exe')
    driver.implicitly_wait(5)
    
    yield driver

    driver.quit()


def test_registration(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_name("reg_username").send_keys("test user")
    browser.find_element_by_name("reg_password").send_keys("123")
    browser.find_element_by_name("reg_password2").send_keys("123")
    browser.find_element_by_name("register").click()
    sleep(3)
    url = browser.current_url
    name = browser.find_element_by_id("name")
    assert 'view_challenges' in url
    assert 'test user' == name.text

def test_login(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_name("username").send_keys("test user")
    browser.find_element_by_name("password").send_keys("123")
    browser.find_element_by_name("login").click()
    sleep(2)
    url = browser.current_url
    name = browser.find_element_by_id("name")
    assert 'view_challenges' in url
    assert 'test user' == name.text

def test_logout(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_name("username").send_keys("test user")
    browser.find_element_by_name("password").send_keys("123")
    browser.find_element_by_name("login").click()
    sleep(3)
    url = browser.current_url
    name = browser.find_element_by_id("name")
    assert 'view_challenges' in url
    assert 'test user' == name.text

    browser.find_element_by_id("logout").click()
    sleep(2)
    assert 'http://localhost:5000/index' == browser.current_url
    

if __name__ == "__main__":
    pytest.main()