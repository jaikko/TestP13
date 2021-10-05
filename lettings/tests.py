from .models import Address, Letting
import pytest
from django.urls import reverse


@pytest.mark.django_db()
class TestLettings:

    # prepopulate testing DB with data
    def setup(self):
        address = Address.objects.create(number=1, street="test", city="New York", state="NY",
                                         zip_code=45465, country_iso_code='USA')
        Letting.objects.create(title="topto", address=address)

    def test_index(self, client):
        url = reverse('lettings:lettings_index')
        rv = client.get(url)
        assert rv.status_code == 200
        assert '<title>Lettings</title>' in rv.content.decode('utf-8')
        assert 'topto' in rv.content.decode('utf-8')
        assert '<a href="/lettings/1/">' in rv.content.decode('utf-8')

    def test_letting(self, client):
        url = reverse('lettings:letting', args=[1])
        print(url)
        rv = client.get(url)
        assert rv.status_code == 200
        assert '<title>topto</title>' in rv.content.decode('utf-8')
