import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from app import create_app, db
from config import TestConfig
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from app.Model.models import Host, Challenge, Prompt

test_joincode = "AAAAAA"



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
    # db.drop_all()
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
    opts.headless = False
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
    browser.find_element_by_name("username").send_keys("tyler")
    browser.find_element_by_name("password").send_keys("123")
    browser.find_element_by_name("login").click()
    sleep(2)
    url = browser.current_url
    name = browser.find_element_by_id("name")
    assert 'view_challenges' in url
    assert 'test user' == name.text

def test_logout(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_name("username").send_keys("tyler")
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
    

def test_create_challenge(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_name("username").send_keys("tyler")
    browser.find_element_by_name("password").send_keys("123")
    browser.find_element_by_name("login").click()
    sleep(2)
    url = browser.current_url
    name = browser.find_element_by_id("name")
    assert 'view_challenges' in url
    assert 'test user' == name.text

    browser.find_element_by_id("create_challenge").click()
    sleep(2)
    browser.find_element_by_id("title").send_keys("test challenge")
    browser.find_element_by_id("prompts-0-prompt").send_keys("test prompt zero")
    browser.find_element_by_id("prompts-1-prompt").send_keys("test prompt one")
    browser.find_element_by_id("create_challenge").click()
    sleep(2)
    assert 'view_challenges' in url
    assert "test challenge" in browser.page_source

def test_open_challenge(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_name("username").send_keys("test user")
    browser.find_element_by_name("password").send_keys("123")
    browser.find_element_by_name("login").click()
    sleep(2)
    browser.find_element_by_id("open").click()
    joinCode = browser.find_element_by_class_name("challengeJoinCode").text
    global test_joincode 
    test_joincode = joinCode[1:-1]
    # "[123456]" => "123456"

    assert joinCode[0] == '['
    assert joinCode[-1] == ']'


# def test_join_challenge(browser):
#     browser.get('http://localhost:5000/')
#     browser.find_element_by_id("joincode").send_keys(test_joincode)
#     browser.find_element_by_id("nickname").send_keys("test challenger")
#     browser.find_element_by_id("join_challenge").click()
#     sleep(2)
#     assert 'take_challenge' in browser.current_url
#     assert 'test challenger' in browser.page_source

def test_take_challenge(browser):
    browser.get('http://localhost:5000/')
    browser.find_element_by_id("joincode").send_keys("AAAAAA")
    browser.find_element_by_id("nickname").send_keys("test challenger")
    browser.find_element_by_id("join_challenge").click()
    sleep(2)

    actions = ActionChains(browser)
    #test prompt zero
    #test incorrect zero [ENTER]
    actions.send_keys('test incorrect zero')
    actions.perform()
    sleep(1)
    correctLetter = browser.find_element_by_id("letter-0")
    assert correctLetter.get_attribute("class") == "letter correct-letter"
    incorrectLetter = browser.find_element_by_id("letter-4")
    assert incorrectLetter.get_attribute("class") == "letter incorrect-letter"

    actions.send_keys(Keys.ENTER)
    actions.perform()
    sleep(1)

if __name__ == "__main__":
    pytest.main()