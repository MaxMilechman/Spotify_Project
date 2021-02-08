from django.test import SimpleTestCase, RequestFactory, Client
from django.urls import reverse
from return_song import views


class TestViews(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_home(self):
        request = RequestFactory().get('home')
        response = views.home(request)
        self.assertEquals(response.status_code, 200)

    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'return_song/home.html')
        self.assertTemplateUsed(response, 'return_song/base.html')
