from django.test import SimpleTestCase, RequestFactory
from django.urls import reverse, resolve
from return_song import views


class TestViews(SimpleTestCase):

    def test_home(self):
        # Are these the same thing??
        request = RequestFactory().get('/')
        response = views.home(request)
        assert response.status_code == 200

        # ^^^
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.home)
