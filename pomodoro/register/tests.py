import pytest
from django.test import Client, TestCase
from requests import Session

from .views import *


class moduleTest(TestCase):
    @classmethod
    def test_register(cls):
        url = "http://127.0.0.1:8000/register/"
        data_post = {"username": "aaa", "firstname": "bbb", ' \
                    '"lastname": "ccc", "email": "ddd@111.com", ' \
                    '"password1": "fffggghh1", "password2": "fffggghh1"}
        cls.session = Session()
        resp = cls.session.post(url, json=data_post)
        assert resp.status_code == 200


    @classmethod
    def test_logout_page(cls):
        url = "http://127.0.0.1:8000/logout_page/"
        cls.session = Session()
        resp = cls.session.get(url)
        assert resp.status_code == 200

    @classmethod
    def test_github_token(cls):
        req_code = "04ad04faf3f025a67681"
        assert github_token(req_code) == 400

    @classmethod
    def test_github_user(cls):
        access_token = "AFjx1pKHtNyjtDyPtWFWLD7bKG88jp2DFI7fuJvKIMTyUdC4fyGFJARmKtujSDn2"
        result = github_user(access_token)
        assert result == 400


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pomodoro.pomodoro.settings')
    pytest.main()
