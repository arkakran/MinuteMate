import unittest
import json
from backend.app import app
from backend.data_store import store

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_process_endpoint(self):
        response = self.app.post('/process')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('transcript', data)
        self.assertIn('summary', data)
        self.assertIn('action_items', data)
        self.assertIn('follow_ups', data)

    def test_clear_endpoint(self):
        self.app.post('/process')

        response = self.app.post('/clear')
        self.assertEqual(response.status_code, 200)

        cleared_data = json.loads(response.data)
        self.assertEqual(cleared_data['transcript'], "")
        self.assertEqual(cleared_data['summary'], "")
        self.assertEqual(cleared_data['action_items'], [])
        self.assertEqual(cleared_data['follow_ups'], [])

if __name__ == '__main__':
    unittest.main()
