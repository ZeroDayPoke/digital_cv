# ./tests/test_models.py

import unittest
from datetime import datetime, timedelta
from app.models import db, User, Role
from app import create_app

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')  # Replace 'testing' with your test configuration
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User(username='john', email='john@example.com', password='cat')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        self.assertTrue(self.user.password_hash is not None)

    def test_no_password_getter(self):
        with self.assertRaises(AttributeError):
            self.user.password

    def test_password_verification(self):
        self.assertTrue(self.user.check_password('cat'))
        self.assertFalse(self.user.check_password('dog'))

    def test_roles(self):
        admin_role = Role(name='ADMIN')
        db.session.add(admin_role)
        db.session.commit()
        self.user.roles.append(admin_role)
        db.session.add(self.user)
        db.session.commit()
        self.assertTrue(self.user.has_role('ADMIN'))

    def test_token_expiration(self):
        self.user.token_generated_at = datetime.utcnow() - timedelta(hours=25)
        self.assertTrue(self.user.token_expired())

if __name__ == '__main__':
    unittest.main()
