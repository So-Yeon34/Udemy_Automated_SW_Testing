'''
from unittest import TestCase
from app import app
'''
from app.tests.system.base_test import BaseTest
import json

'''
class TestHome(TestCase):
    # app.test_client() → Flask creates a special test client object
    # c.get('/') → Simulates a GET request to http://localhost:5000/
    # resp → The Response object returned by Flask
    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200) # 200 is default status
            self.assertEqual(
                json.loads(resp.get_data()), # String to dictionary
                {'message' : 'Hello, world!'}
            )
'''

class TestHome(BaseTest):
    def test_home(self):
        # self.app is already a test client
            resp = self.app.get('/')

            self.assertEqual(resp.status_code, 200) # 200 is default status
            self.assertEqual(
                json.loads(resp.get_data()), # String to dictionary
                {'message' : 'Hello, world!'}
            )