#!/usr/bin/env python3

from unittest.mock import patch, MagicMock
from flask import url_for
from admin import AdminModelView

class TestAdminModelView:
    @patch('admin.current_user')
    def test_is_accessible_returns_false_when_user_is_not_authenticated(self, mock_current_user):
        mock_current_user.is_authenticated = False
        mock_current_user.has_role = MagicMock(return_value=True)
        view = AdminModelView()
        assert view.is_accessible() == False

    @patch('admin.current_user')
    def test_is_accessible_returns_false_when_user_does_not_have_admin_role(self, mock_current_user):
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=False)
        view = AdminModelView()
        assert view.is_accessible() == False

    @patch('admin.current_user')
    def test_is_accessible_returns_true_when_user_is_authenticated_and_has_admin_role(self, mock_current_user):
        mock_current_user.is_authenticated = True
        mock_current_user.has_role = MagicMock(return_value=True)
        view = AdminModelView()
        assert view.is_accessible() == True

    def test_inaccessible_callback_redirects_to_login(self):
        view = AdminModelView()
        response = view.inaccessible_callback('test_name')
        assert response.status_code == 302
        assert response.location == url_for('auth_routes.login')
