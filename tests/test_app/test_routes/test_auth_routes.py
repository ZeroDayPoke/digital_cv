#!/usr/bin/env python3

import unittest
from app import create_app, db
from app.models import User

import unittest

class AuthRoutesTestCase(unittest.TestCase):
    """
    Test case for authentication routes.

    This class contains unit tests for the authentication routes of the Flask app.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a Flask app instance, a test client, and a test user.
        """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

        # Create a test user
        self.user = User(email='test@example.com', password='testpassword')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        """
        Tear down the test environment.

        This method removes the test user and drops the test database.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_signin_valid_user(self):
        """
        Test signing in with valid user credentials.

        This method tests the '/signin' route with valid user credentials.
        """
        response = self.client.post('/signin', data={
            'email': 'test@example.com',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as session:
            self.assertIn(('message', 'Successfully signed in.'), session['_flashes'])

    def test_signin_invalid_user(self):
        """
        Test signing in with invalid user credentials.

        This method tests the '/signin' route with invalid user credentials.
        """
        response = self.client.post('/signin', data={
            'email': 'invalid@example.com',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as session:
            self.assertIn(('message', 'Invalid email or password.'), session['_flashes'])

if __name__ == '__main__':
    unittest.main()
