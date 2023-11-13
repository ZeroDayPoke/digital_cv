# Path: tests/test_app/test_routes/test_auth_routes.py
import unittest
from app import create_app, db
from app.models import User


class AuthRoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

        self.user = User(email='test@example.com', password='testpassword')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_signin_valid_user(self):
        response = self.client.post('/signin', data={
            'email': 'test@example.com',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as session:
            try:
                self.assertIn(('flash', 'Successfully signed in'),
                              session['_flashes'])
            except KeyError:
                self.fail("_flashes not set in the session")

    def test_signin_invalid_user(self):
        response = self.client.post('/signin', data={
            'email': 'invalid@example.com',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as session:
            try:
                self.assertIn(('flash', 'Email does not exist.'),
                              session['_flashes'])
            except KeyError:
                self.fail("_flashes not set in the session")


if __name__ == '__main__':
    unittest.main()
