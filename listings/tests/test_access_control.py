import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from listings.models import Property


@pytest.fixture
def owner(db):
    return User.objects.create_user(username='catalog_owner', password='strong-pass-123')


@pytest.fixture
def property_obj(owner):
    return Property.objects.create(
        title='Cozy Loft',
        description='Уютная квартира в центре города',
        country='ES',
        city='Barcelona',
        price=150000,
        owner=owner,
        is_available=True,
    )


@pytest.mark.django_db
def test_navigation_for_anonymous_shows_login_only(client):
    response = client.get(reverse('property_list'))

    assert response.status_code == 200
    content = response.content.decode('utf-8')

    assert reverse('login') in content
    assert 'Войти' in content
    assert reverse('favorite_properties') not in content
    assert reverse('lesson_list') not in content
    assert reverse('collection_list') not in content


@pytest.mark.django_db
def test_navigation_for_authenticated_shows_avatar(client, owner):
    client.force_login(owner)

    response = client.get(reverse('property_list'))

    assert response.status_code == 200
    content = response.content.decode('utf-8')

    assert reverse('favorite_properties') in content
    assert reverse('lesson_list') in content
    assert reverse('collection_list') in content
    assert owner.profile.avatar.url in content
    assert owner.username in content or owner.get_full_name() in content


@pytest.mark.django_db
def test_property_detail_accessible_for_anonymous(client, property_obj):
    response = client.get(reverse('property_detail', args=[property_obj.pk]))

    assert response.status_code == 200
    content = response.content.decode('utf-8')

    assert 'Войдите, чтобы добавить в избранное' in content
    assert 'favorite-btn' not in content


@pytest.mark.django_db
def test_property_detail_shows_favorite_button_for_authenticated(client, owner, property_obj):
    client.force_login(owner)

    response = client.get(reverse('property_detail', args=[property_obj.pk]))

    assert response.status_code == 200
    content = response.content.decode('utf-8')

    assert 'favorite-btn' in content
    assert 'Войдите, чтобы добавить в избранное' not in content
