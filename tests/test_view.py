import unittest

from etp_api import app as application


class TestBase(unittest.TestCase):

    def setUp(self):
        """Setup a test client"""
        self.app = application.test_client()

    def tearDown(self):
        pass

    def test_server_is_up_and_running(self):
        # sends HTTP GET request to the application on the specified path
        result = self.app.get('/api/v0/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_api_render(self):
        result = self.app.get('/api/v0/')

        # assert the data of the response
        self.assertIn('ETP-API', str(result.data))


if __name__ == '__main__':
    unittest.main()
