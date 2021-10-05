from django.urls import reverse


class TestHome:

    def test_home(self, client):
        url = reverse('index')
        rv = client.get(url)
        assert rv.status_code == 200
        assert '<title>Holiday Homes</title>' in rv.content.decode('utf-8')

    def test_dummy(self):
        assert 1
