import unittest
import os
from flask import Flask
from werkzeug.datastructures import FileStorage
from src.main import app

class MyTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        self.client = app.test_client()
        self.cwd = os.getcwd()

    # executed after each test
    def tearDown(self):
        pass

    def test_flask_application_is_up_and_running(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_flask_application_wrong_url(self):
        response = self.client.get('/wrongURL', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
    
    def test_flask_handles_uploads_mid_file(self):
        my_file = FileStorage(
            stream=open(os.path.join(self.cwd, 'src/tests/Melody_guitar.mid'), 'rb'),
            filename="Melody_guitar.mid",
            name="Melody_guitar.mid"
        )

        data = { "file": my_file }
        response = self.client.post('/upload', content_type='multipart/form-data', follow_redirects=True, data=data)
        self.assertEqual(response.status_code, 200)

    def test_flask_handles_uploads_same_mid_file(self):
        my_file = FileStorage(
            stream=open(os.path.join(self.cwd, 'src/tests/Melody_guitar.mid'), 'rb'),
            filename="Melody_guitar.mid",
            name="Melody_guitar.mid"
        )

        data = { "file": my_file }
        response = self.client.post('/upload', content_type='multipart/form-data', follow_redirects=True, data=data)
        self.assertEqual(response.status_code, 203)

    def test_flask_handles_uploads_other_file(self):
        my_file = FileStorage(
            stream=open(os.path.join(self.cwd, 'src/tests/Melody_guitar.mid'), 'rb'),
            filename="Melody_guitar.txt",
            name="Melody_guitar.txt"
        )

        data = { "file": my_file }
        response = self.client.post('/upload', content_type='multipart/form-data', follow_redirects=True, data=data)
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()