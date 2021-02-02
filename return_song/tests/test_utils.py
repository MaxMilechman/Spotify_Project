from django.test import SimpleTestCase
from django.test.client import Client
from return_song import utils
from return_song.forms import SearchForm
from return_song.utils import spotify_helper


class TestUtils(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_utils(self):
        response = self.client.post('/', {
            'form': SearchForm,
            'artist_name': 'Elton John',
            'top_track': '',
            'error': '',
            'searched': 1
        })
        self.assertEquals(response.status_code, 200)
