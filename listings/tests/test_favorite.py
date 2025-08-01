import pytest
from django.contrib.auth.models import User
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
