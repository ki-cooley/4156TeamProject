"""View test example."""
from django.urls import reverse, resolve


class TestUrls:
    def test_url_dashboard_home(self):
        path = reverse('dashboard-home', kwargs={})
        assert resolve(path).view_name == 'dashboard-home'
    def test_url_summary(self):
        path = reverse('summary', kwargs={})
        assert resolve(path).view_name == 'summary'
    def test_url_detail(self):
    	path = reverse('detail', kwargs={'pk' : 1})
    	assert resolve(path).view_name == 'detail'