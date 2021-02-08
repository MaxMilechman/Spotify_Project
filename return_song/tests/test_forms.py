from django.test import SimpleTestCase
from return_song.forms import SearchForm


class TestForms(SimpleTestCase):

    def setUp(self):
        self.form = SearchForm(data={'artist_search': 'Elton John'})

    def tearDown(self):
        pass

    def test_search_form_is_valid(self):
        self.assertTrue(self.form.is_valid())

    def test_search_form_max_length(self):
        self.assertEquals(self.form.fields['artist_search'].max_length, 100)

    def test_search_form_label(self):
        self.assertEquals(self.form.fields['artist_search'].label, 'Artist search')

    def test_search_form_is_not_valid(self):
        form = SearchForm(data={'artist_search': ''})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
