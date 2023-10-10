# tests/test_app/test_utils/test_file_upload_helper.py

from unittest import TestCase, mock
from flask import Flask
from app.utils.file_upload_helper import allowed_file, handle_file_upload

class FileUploadHelperTestCase(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['UPLOAD_FOLDER'] = '/uploads'
        self.app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_allowed_file(self):
        self.assertTrue(allowed_file('test.png'))
        self.assertFalse(allowed_file('test.pdf'))

    @mock.patch('app.utils.file_upload_helper.os.path.exists', return_value=False)
    @mock.patch('app.utils.file_upload_helper.os.makedirs')
    def test_handle_file_upload(self, mock_makedirs, mock_exists):
        with self.app.test_request_context():
            with mock.patch('app.utils.file_upload_helper.request') as mock_request:
                mock_request.files = {'image': mock.MagicMock()}
                mock_request.files['image'].filename = 'test.png'
                with mock.patch('app.utils.file_upload_helper.allowed_file', return_value=True):
                    with mock.patch('app.utils.file_upload_helper.secure_filename', return_value='test.png'):
                        filename = handle_file_upload('model_name')

        mock_makedirs.assert_called_once_with('/uploads/model_name')
        self.assertEqual(filename, 'test.png')

    @mock.patch('app.utils.file_upload_helper.flash')
    def test_handle_file_upload_error(self, mock_flash):
        with self.app.test_request_context():
            with mock.patch('app.utils.file_upload_helper.request') as mock_request:
                mock_request.files = {}
        
                filename = handle_file_upload('model_name')

        mock_flash.assert_called_once_with('Error: File not found or not allowed.', 'danger')
        self.assertIsNone(filename)
