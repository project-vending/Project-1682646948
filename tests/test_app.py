
import unittest

from src.app import app


class TestApp(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, world!')

    def test_data_endpoint(self):
        tester = app.test_client(self)
        response = tester.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        # add additional assertions for the expected structure/content of the response


if __name__ == '__main__':
    unittest.main()
