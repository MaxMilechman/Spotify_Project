from django.test import SimpleTestCase
from django.urls import reverse, resolve
from return_song.views import home


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
