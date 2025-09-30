"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'  # 'postgresql://postgres:1234@localhost:5432/test'
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        # Make sure database exists
        with app.app_context():
            db.create_all()
        # Get a test client

        # app.test_client() → calls the method immediately and returns a FlaskClient instance.
        #                    So self.app is an actual client object ready to send requests.
        #                    Example: response = self.app.get('/users')

        # app.test_client  → stores the method itself without calling it.
        #                    So self.app is just a reference to the function, not a client yet.
        #                    You must call it later: client = self.app(); response = client.get('/users')

        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
