from django.test import SimpleTestCase
from return_song.forms import SearchForm


class TestForms(SimpleTestCase):

    def test_search_form_is_valid(self):
        form = SearchForm(data={'artist_search': 'Elton John'})
        self.assertTrue(form.is_valid())

    def test_search_form_is_not_valid(self):
        form = SearchForm(data={'artist_search': ''})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
