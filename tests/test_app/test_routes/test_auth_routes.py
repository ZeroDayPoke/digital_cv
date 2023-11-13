# Path: tests/test_app/test_routes/test_auth_routes.py

import unittest
from app.models import User
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from unittest.mock import patch, Mock
from app import create_app, db


class AuthRoutesTestCase(unittest.TestCase):
    """
    Test case for the authentication routes of the Flask app.

    This test case sets up a Flask app instance, pushes an app context, creates a test client, creates a test user,
    and commits the user to the database. It also includes tests for signing in, signing up, signing out, changing
    passwords, and verifying account emails.
    """

    def setUp(self):
        """
        Set up the test environment by creating a Flask app instance, pushing an app context, creating a test client,
        creating a test user, and committing the user to the database.
        """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

        self.user = User(email='test@example.com', password='testpassword', username='testuser',
                         verification_token='faketoken', token_generated_at=datetime.utcnow())
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        """
        This method is called after each test function has been executed. It removes the database session,
        drops all tables, and pops the application context.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login_user(self, email, password):
        """
        Logs in a user with the given email and password.

        Args:
            email (str): The email of the user to log in.
            password (str): The password of the user to log in.

        Returns:
            The response object from the server.
        """
        return self.client.post('/signin', data={
            'email': email,
            'password': password
        }, follow_redirects=True)

    def test_signin_valid_user(self):
        """
        Test that a valid user can sign in successfully.

        Uses the Flask test client to simulate a POST request to the '/signin' route with valid user credentials.
        Asserts that the response status code is 200 and that the 'Successfully signed in' message is displayed.
        """
        with self.app.test_client() as client:
            response = client.post('/signin', data={
                'email': 'test@example.com',
                'password': 'testpassword'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('Successfully signed in' in message.get_text()
                            for message in flashed_messages))

    def test_signin_invalid_user(self):
        """
        Test that a user with invalid credentials cannot sign in.

        Uses the Flask test client to simulate a POST request to the '/signin' route
        with invalid email and password credentials. Asserts that the response contains
        an alert message indicating that the email does not exist.
        """
        with self.app.test_client() as client:
            response = client.post('/signin', data={
                'email': 'invalid@example.com',
                'password': 'wrongpassword'
            }, follow_redirects=True)

            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('Email does not exist.' in message.get_text()
                            for message in flashed_messages))

    def test_signup_success(self):
        """
        Test that a user can successfully sign up for an account using the '/signup' route.
        """
        with self.app.test_client() as client:
            response = client.post('/signup', data={
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password': 'newpassword',
                "confirm_password": "newpassword"
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('Congratulations, you are now a registered user!' in message.get_text(
            ) for message in flashed_messages))
            new_user = User.query.filter_by(email='newuser@example.com').first()
            self.assertIsNotNone(new_user)
            self.assertEqual(new_user.username, 'newuser')

    def test_signup_username_taken(self):
        """
        Test that a user cannot sign up with a username that is already taken.
        """
        with self.app.test_client() as client:
            response = client.post('/signup', data={
                'username': 'testuser',
                'email': 'different@example.com',
                'password': 'newpassword',
                'confirm_password': 'newpassword'
            }, follow_redirects=True)
            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('Username already in use.' in message.get_text()
                            for message in flashed_messages))

    def test_signup_email_taken(self):
        """
        Test that a user cannot sign up with an email that is already in use.
        """
        with self.app.test_client() as client:
            response = client.post('/signup', data={
                'username': 'differentuser',
                'email': 'test@example.com',
                'password': 'newpassword',
                'confirm_password': 'newpassword'
            }, follow_redirects=True)
            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('Email address already in use.' in message.get_text(
            ) for message in flashed_messages))

    def test_signup_page_render(self):
        """
        Test that the signup page is rendered successfully.

        Uses Flask's test client to send a GET request to the '/signup' route and
        checks that the response status code is 200 (OK).
        """
        with self.app.test_client() as client:
            response = client.get('/signup')
            self.assertEqual(response.status_code, 200)

    def test_successful_signout(self):
        """
        Test that a user can successfully sign out of the application.

        Uses the Flask test client to simulate a user signing in with test credentials,
        then sends a GET request to the signout route and checks that the response
        contains a success message indicating that the user has been signed out.
        """
        with self.app.test_client() as client:
            self.client.post(
                '/signin', data={'email': 'test@example.com', 'password': 'testpassword'}, follow_redirects=True)

            response = self.client.get('/signout', follow_redirects=True)
            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('Successfully signed out' in message.get_text()
                            for message in flashed_messages))

    def test_signout_when_not_signed_in(self):
        """
        Test that the user is redirected to the sign-in page and sees a message indicating that they are not signed in
        when they attempt to sign out without being signed in.
        """
        with self.app.test_client() as client:
            response = self.client.get('/signout', follow_redirects=True)
            soup = BeautifulSoup(response.data, 'html.parser')
            flashed_messages = soup.find_all(
                'div', class_='alert alert-success')
            self.assertTrue(any('You are not signed in.' in message.get_text()
                            for message in flashed_messages))

    def test_account_page_render(self):
        """
        Test that the account page is rendered successfully after a user logs in.
        """
        self.login_user('test@example.com', 'testpassword')
        response = self.client.get('/account')
        content = response.data.decode()
        self.assertIn('Account', content)

    def test_successful_password_change(self):
        """
        Test that a user can successfully change their password by sending a POST request to the /account route with the 
        correct current password, a new password, and a confirmation of the new password. The test checks that the response 
        contains the message 'Password changed successfully.'.
        """
        self.login_user('test@example.com', 'testpassword')

        response = self.client.post('/account', data={
            'current_password': 'testpassword',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }, follow_redirects=True)
        content = response.data.decode()
        self.assertIn('Password changed successfully.', content)

    def test_incorrect_current_password(self):
        """
        Test that an error message is displayed when the user enters an incorrect current password.
        """
        self.login_user('test@example.com', 'testpassword')

        response = self.client.post('/account', data={
            'current_password': 'wrongpassword',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }, follow_redirects=True)
        content = response.data.decode()
        self.assertIn('Incorrect current password.', content)

    def test_non_matching_new_passwords(self):
        """
        Test that the user is unable to change their password if the new password and confirm password do not match.
        """
        self.login_user('test@example.com', 'testpassword')

        response = self.client.post('/change_password', data={
            'current_password': 'testpassword',
            'new_password': 'newpassword',
            'confirm_password': 'differentnewpassword'
        }, follow_redirects=True)
        soup = BeautifulSoup(response.data, 'html.parser')
        flashed_messages = soup.find_all('div', class_='alert alert-success')
        self.assertTrue(any('New password and confirm password do not match.' in message.get_text(
        ) for message in flashed_messages))

    @patch('requests.post')
    def test_send_verification_email_success(self, mock_post):
        """
        Test case for testing the send_verification_email_success function.

        This function tests if the verification email is sent successfully by mocking the post request and checking the response.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'token': 'faketoken'}
        mock_post.return_value = mock_response

        self.login_user('test@example.com', 'testpassword')
        response = self.client.get(
            '/send_verification_email', follow_redirects=True)
        self.assertIn('Verification email sent!', response.data.decode())

    def test_verify_account_email_success(self):
        """
        Test that the account verification email is successfully sent and the account is verified.
        """
        response = self.client.get(
            '/verify_account_email/faketoken', follow_redirects=True)
        self.assertIn('Account successfully verified!', response.data.decode())
        self.assertTrue(self.user.verified)

    def test_verify_account_email_invalid_token(self):
        """
        Test case to verify that an invalid token returns an error message.

        The test sends a GET request to the '/verify_account_email' route with an invalid token.
        It then checks that the response contains the error message 'Invalid verification link.'.
        """
        response = self.client.get(
            '/verify_account_email/invalid-token', follow_redirects=True)
        self.assertIn('Invalid verification link.', response.data.decode())

    def test_verify_account_email_expired_token(self):
        """
        Test case to verify that an expired token generates an error message when trying to verify an account email.
        """
        self.user.token_generated_at = datetime.utcnow() - timedelta(days=99)
        db.session.commit()
        response = self.client.get(
            '/verify_account_email/faketoken', follow_redirects=True)
        self.assertIn('Expired verification link.', response.data.decode())


if __name__ == '__main__':
    unittest.main()
