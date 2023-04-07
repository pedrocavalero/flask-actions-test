import unittest
from app import app

class TestHello(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello!')
