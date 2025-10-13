import pytest
from datetime import timedelta
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

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


@pytest.mark.django_db
def test_property_list_defaults_to_newest_first(client, create_property):
    recent = create_property(title='Brand New Condo')
    older = create_property(title='Vintage Loft')

    Property.objects.filter(pk=older.pk).update(created_at=timezone.now() - timedelta(days=3))

    response = client.get(reverse('property_list'))

    assert response.status_code == 200
    content = response.content.decode()
    assert content.index('Brand New Condo') < content.index('Vintage Loft')


@pytest.mark.django_db
def test_property_list_sorts_by_area_desc(client, create_property):
    spacious = create_property(title='Spacious Loft', area=180)
    compact = create_property(title='Compact Studio', area=48)

    response = client.get(reverse('property_list'), {'sort': 'area_desc'})

    assert response.status_code == 200
    content = response.content.decode()
    assert content.index('Spacious Loft') < content.index('Compact Studio')


@pytest.mark.django_db
def test_property_list_sorts_by_area_asc(client, create_property):
    spacious = create_property(title='Wide Villa', area=220)
    compact = create_property(title='Tiny Flat', area=36)

    response = client.get(reverse('property_list'), {'sort': 'area_asc'})

    assert response.status_code == 200
    content = response.content.decode()
    assert content.index('Tiny Flat') < content.index('Wide Villa')


@pytest.mark.django_db
def test_property_list_sorts_by_oldest(client, create_property):
    newer = create_property(title='New Tower')
    older = create_property(title='Heritage House')

    Property.objects.filter(pk=older.pk).update(created_at=timezone.now() - timedelta(days=7))

    response = client.get(reverse('property_list'), {'sort': 'oldest'})

    assert response.status_code == 200
    content = response.content.decode()
    assert content.index('Heritage House') < content.index('New Tower')
