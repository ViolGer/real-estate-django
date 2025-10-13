import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from listings.models import Property


@pytest.fixture
def user(db):
    return User.objects.create_user(username='owner', password='password123')


@pytest.fixture
def create_property(user):
    def _create(**kwargs):
        defaults = {
            'title': 'Sample property',
            'description': 'Test description',
            'country': 'ES',
            'city': 'Barcelona',
            'price': 100000,
            'owner': user,
            'is_available': True,
        }
        defaults.update(kwargs)
        return Property.objects.create(**defaults)

    return _create


@pytest.mark.django_db
def test_property_list_search_filters_results(client, create_property):
    create_property(title='Sunny Villa', city='Valencia')
    create_property(title='Nordic Apartment', city='Oslo')

    response = client.get(reverse('property_list'), {'q': 'villa'})

    assert response.status_code == 200
    content = response.content.decode()
    assert 'Sunny Villa' in content
    assert 'Nordic Apartment' not in content


@pytest.mark.django_db
def test_property_list_sorts_by_price_desc(client, create_property):
    cheap = create_property(title='Budget Loft', price=75000)
    premium = create_property(title='Premium Penthouse', price=250000)

    response = client.get(reverse('property_list'), {'sort': 'price_desc'})

    assert response.status_code == 200
    content = response.content.decode()
    premium_index = content.index('Premium Penthouse')
    cheap_index = content.index('Budget Loft')
    assert premium_index < cheap_index


@pytest.mark.django_db
def test_property_list_excludes_unavailable(client, create_property):
    available = create_property(title='Open House')
    create_property(title='Hidden Gem', is_available=False)

    response = client.get(reverse('property_list'))

    assert response.status_code == 200
    content = response.content.decode()
    assert 'Open House' in content
    assert 'Hidden Gem' not in content
