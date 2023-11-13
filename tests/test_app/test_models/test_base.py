# tests/test_app/test_models/test_base.py

from unittest import TestCase, mock
from app.models.base import BaseModel
from datetime import datetime


class BaseModelTestCase(TestCase):
    """
    Test case for the BaseModel class.
    """

    @mock.patch('app.models.base.db.session.add')
    @mock.patch('app.models.base.db.session.commit')
    def test_id_generation(self, mock_commit, mock_add):
        """
        Test that a BaseModel instance is assigned an id upon creation.
        """
        model = BaseModel()
        self.assertIsNotNone(model.id)

    @mock.patch('app.models.base.datetime')
    @mock.patch('app.models.base.db.session.add')
    @mock.patch('app.models.base.db.session.commit')
    def test_created_at(self, mock_commit, mock_add, mock_datetime):
        """
        Test that the created_at attribute of a BaseModel instance is set correctly.
        """
        mock_datetime.utcnow.return_value = datetime(1990, 8, 16)
        model = BaseModel()
        model.created_at = mock_datetime.utcnow()
        self.assertEqual(model.created_at, datetime(1990, 8, 16))
        self.assertIsInstance(model.created_at, datetime)

    @mock.patch('app.models.base.datetime')
    @mock.patch('app.models.base.db.session.add')
    @mock.patch('app.models.base.db.session.commit')
    def test_updated_at(self, mock_commit, mock_add, mock_datetime):
        """
        Test that the updated_at attribute of a BaseModel instance is set correctly.
        """
        mock_datetime.utcnow.return_value = datetime(2023, 8, 16)
        model = BaseModel()
        model.updated_at = mock_datetime.utcnow()
        self.assertEqual(model.updated_at, datetime(2023, 8, 16))
        self.assertIsInstance(model.updated_at, datetime)
