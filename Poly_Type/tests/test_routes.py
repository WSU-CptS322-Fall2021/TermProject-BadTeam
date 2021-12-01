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
    user = new_user('test', '1234')

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
    # Test to see if the create challenge page loads
    response = test_client.get('/index',data=dict(username='test3',password='1234', password2='1234'), follow_redirects=True)
    assert response.status_code == 200

    s = db.session.query(Host).filter(Host.username=='test3').first()
    assert s.username == 'test3'

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