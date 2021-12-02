import os
import unittest
import pytest
import sys
from config import Config
from app import create_app, db
from app.Model.models import Host
from app.Controller.hostRoutes import *
#from app.Controller.hostRoutes import createCode, view_challenges, create_challenge
from app.Controller.challengerRoutes import *


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_class=TestConfig)

    db.init_app(flask_app)
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield  testing_client 
    # this is where the testing happens!
 
    ctx.pop()

# Function to create a user for testing
def new_user(uname, passwd):
    user = Host(username=uname)
    user.set_password(passwd)
    return user

# Function to intialize the database
@pytest.fixture
def init_database():
    #Create the database
    db.create_all()

    #Create the test user
    user = new_user('test_login', '1234')

    #Add the user to the database
    db.session.add(user)
    db.session.commit()

    yield

    db.drop_all()

def test_index(test_client):
    # Test to see if the create challenge page loads
    response = test_client.get('/index')
    assert response.status_code == 200
    assert b'Join' in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data

def test_index_register(test_client, init_database):

    #IMPORTANT - If you want to specify the form make sure to set the submit value to the name of the button
    response = test_client.post('/index', data=dict(reg_username='test_register',reg_password='12345', reg_password2='12345', submit='Register'), follow_redirects=True)
    assert response.status_code == 200

    s = db.session.query(Host).filter(Host.username=='test_register').first()
    assert s.username == 'test_register'
    assert s.check_password('12345')

    #Check if the page is redirected to the createChallenge page
    assert b'Create a New Challenge' in response.data
def test_login_logout(test_client, init_database):
    #First login
    response = test_client.post('/index', data=dict(username='test_login', password='1234', submit='Login'), follow_redirects=True)
    assert response.status_code == 200

    s = db.session.query(Host).filter(Host.username=='test_login').first()
    assert s.username == 'test_login'
    assert s.check_password('1234')

    #Then log out the user
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Join' in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data

def test_create_challenge(test_client, init_database):
    #First login
    response = test_client.post('/index', data=dict(username='test_login', password='1234', submit='Login'), follow_redirects=True)
    assert response.status_code == 200

    s = db.session.query(Host).filter(Host.username=='test_login').first()
    assert s.username == 'test_login'
    assert s.check_password('1234')
    #Then create a challenge
    test_prompt = [Prompt(text="The brown foxed jumped over the white fence"), Prompt(text="Please take your dog, Cali, out for a walk – he really needs some exercise!"), Prompt(text="When do you think they will get back from their adventure in Cairo, Egypt?")]
    
    response = test_client.post('/create_challenge', data=dict(title='test_challenge', prompts=test_prompt), follow_redirects=True)
    assert response.status_code == 200
    c = db.session.query(Challenge).filter(Challenge.title=='test_challenge').first()
    assert c.host_id == s.id
'''
class TestRoutes(unittest.TestCase):
    def test_createcode(self):
        code = createCode()
        self.assertTrue(len(code) == 6)
        for i in range(0, 5):
            self.assertTrue(code[i] in 'ABCDEFGHJKLMNPQRSTUVWXYZ1234567890')
    def test_view_challenges(self):
        print("test")
        #tester = view_challenges(self)x
        #response = tester.get('/view_challenges')
        #self.assertTrue(response.status_code,xzx 200)
'''