import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from listings.models import Property, Favorite

@pytest.mark.django_db
def test_favorite_creation():
    user = User.objects.create_user(username="testuser")
    prop = Property.objects.create(
        title="Test House", description="...", country="FR", city="Nice", price=100000,
        owner=user
    )

    fav = Favorite.objects.create(user=user, property=prop)
    assert fav.pk is not None
    assert str(fav) == "testuser - Test House"

@pytest.mark.django_db
def test_favorite_unique_constraint():
    user = User.objects.create_user(username="testuser")
    prop = Property.objects.create(
        title="Test House", description="...", country="FR", city="Nice", price=100000,
        owner=user
    )
    Favorite.objects.create(user=user, property=prop)

    with pytest.raises(Exception):
        Favorite.objects.create(user=user, property=prop)


@pytest.mark.django_db
def test_toggle_favorite_api_adds_and_removes():
    user = User.objects.create_user(username="apitester", password="secret")
    prop = Property.objects.create(
        title="API House", description="...", country="FR", city="Nice", price=100000,
        owner=user
    )

    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('toggle_favorite_api', args=[prop.pk])

    response = client.post(url)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        'status': 'added',
        'message': 'Added to favorites'
    }
    assert Favorite.objects.filter(user=user, property=prop).exists()

    response = client.post(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'status': 'removed',
        'message': 'Removed from favorites'
    }
    assert not Favorite.objects.filter(user=user, property=prop).exists()


@pytest.mark.django_db
def test_toggle_favorite_api_requires_authentication(client):
    owner = User.objects.create_user(username="owner", password="secret")
    prop = Property.objects.create(
        title="Public House", description="...", country="FR", city="Nice", price=120000,
        owner=owner
    )

    url = reverse('toggle_favorite_api', args=[prop.pk])

    response = client.post(url)

    assert response.status_code in {status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN}
    assert not Favorite.objects.filter(property=prop).exists()
