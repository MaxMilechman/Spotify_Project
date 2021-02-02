from django.test import TestCase
from return_song.models import Search


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        Search.objects.create(artist_search='Elton John')

    def test_artist_search_label(self):
        search = Search.objects.get()
        field_label = search._meta.get_field('artist_search').verbose_name
        self.assertEquals(field_label, 'artist search')

    def test_object_search(self):
        search = Search.objects.get()
        artist_search = f'{search.artist_search}'
        self.assertEquals(str(search), artist_search)

    def test_artist_search_max_length(self):
        search = Search.objects.get()
        max_length = search._meta.get_field('artist_search').max_length
        self.assertEquals(max_length, 100)
