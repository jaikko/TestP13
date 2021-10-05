from profiles.models import Profile
from django.contrib.auth.models import User
import pytest
from django.urls import reverse


@pytest.mark.django_db()
class TestProfiles:

    # prepopulate testing DB with data
    def setup(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Profile.objects.create(favorite_city='paris', user=user)

    def test_index(self, client):
        url = reverse('profiles:profiles_index')
        rv = client.get(url)
        assert rv.status_code == 200
        assert '<title>Profiles</title>' in rv.content.decode('utf-8')
        assert 'john' in rv.content.decode('utf-8')
        assert '<a href="/profiles/john/">' in rv.content.decode('utf-8')

    def test_profile(self, client):
        url = reverse('profiles:profile', args=['john'])
        rv = client.get(url)
        assert rv.status_code == 200
        assert '<title>john</title>' in rv.content.decode('utf-8')
