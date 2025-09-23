'''
Base Test
This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
'''

from unittest import TestCase
from starter_code.app import app
from starter_code.db import db

class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        # Configure the database to use an in-memory SQLite database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

        # Create an application context so Flask and SQLAlchemy can work properly
        with app.app_context():
            # Initialize SQLAlchemy with the Flask app
            db.init_app(app)

            # Create all tables defined in the models for a fresh test database
            db.create_all()

        # Get a test client
        # Create a test client to simulate requests to the application
        # Example: self.app.get('/item/pen') instead of running a live server
        self.app = app.test_client()

        # Keep a reference to the app context for use in tests
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        # Clean up the database after each test
        # Remove the current session and drop all tables
        with app.app_context():
            db.session.remove()
            db.drop_all()