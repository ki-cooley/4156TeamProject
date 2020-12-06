"""View test example."""
from django.urls import reverse, resolve


class TestUrls:
    def test_url_home(self):
        path = reverse('home', kwargs={})
        assert resolve(path).view_name == 'home'
