from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True # Testing mode
        self.app = app.test_client()
