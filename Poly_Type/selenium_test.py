import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app import create_app, db
from config import TestConfig
import os
basedir = os.path.abspath(os.path.dirname(__file__))


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
https://sites.google.com/a/chromium.org/chromedriver/home 
"""
@pytest.fixture
def browser():
    CHROME_PATH = "c:\\test"
    print(CHROME_PATH)
    opts = Options()
    opts.headless = False
    driver = webdriver.Chrome(options=opts, executable_path = CHROME_PATH + '/chromedriver.exe')
    driver.implicitly_wait(10)
    
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_registration(browser):
    #verification
    browser.get('http://localhost:5000/')
    content = browser.page_source
    assert 'Join' in content

if __name__ == "__main__":
    pytest.main()


# import unittest
# import urllib3

# from flask import url_for
# from flask_testing import LiveServerTestCase
# from selenium import webdriver

# from app import create_app, db
# from config import Config

# class TestConfig(Config):
#     TESTING = True

# class TestBase(LiveServerTestCase):

#     def create_app(self):
#         app = create_app()
#         app.config.update(LIVESERVER_PORT=8847, TESTING=True)
#         return app

#     def setUp(self):
#         """
#         Will be called before every test
#         """
#         self.driver = webdriver.Chrome("c:\\test" + "chromedriver.exe")
#         self.driver.get(self.get_server_url())

#         db.session.commit()
#         db.drop_all()
#         db.create_all()

#         db.session.commit()

#     def tearDown(self):
#         """
#         Will be called after every test
#         """
#         self.driver.quit()

# class TestViews(TestBase):
#     def test_homepage_view(self):
#         """
#         Test that homepage is accessible without login
#         """
#         response = self.client.get(url_for('challenger.index'))
#         self.assertEqual(response.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()