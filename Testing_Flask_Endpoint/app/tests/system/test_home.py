from unittest import TestCase
from app import app
import json

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