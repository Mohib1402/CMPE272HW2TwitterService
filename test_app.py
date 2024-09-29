import unittest
from unittest.mock import patch
from app import app
#written by Praful John
class TestMastodonService(unittest.TestCase):

    @patch('app.mastodon.status_post')
    def test_create_post(self, mock_status_post):
        # Mocking the status_post function so that it does not tamper the UI data 
        mock_status_post.return_value = {'id': '12345'}
        with app.test_client() as client:
            response = client.post('/create_post', data={'status': 'Hello from create post'})
            self.assertEqual(response.status_code, 302)  # Redirect after post creation

    @patch('app.mastodon.timeline_home')
    def test_retrieve_all_posts(self, mock_timeline_home):
        # Mocking the timeline_home function so that it does not tamper the UI data 
        mock_timeline_home.return_value = [{'id': '12345', 'content': 'Hello from retrieve all post!'}]
        with app.test_client() as client:
            response = client.post('/retrieve_post')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello from retrieve all post!', response.data)

    @patch('app.mastodon.status')
    def test_retrieve_post_by_id(self, mock_status):
        # Mock the status function so that it does not tamper the UI data 
        mock_status.return_value = {'id': '12345', 'content': 'Hello from retieve post by id'}
        with app.test_client() as client:
            response = client.post('/retrieve_post_by_id', data={'post_id': '12345'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello from retieve post by id', response.data)

    @patch('app.mastodon.status_delete')
    def test_delete_post(self, mock_status_delete):
        # Mocking the status_delete function so that it does not tamper the UI data 
        mock_status_delete.return_value = None  # No content for deletion
        with app.test_client() as client:
            response = client.post('/delete_post', data={'post_id': '12345'})
            self.assertEqual(response.status_code, 302)  # Redirect after deletion

if __name__ == '__main__':
    unittest.main()
