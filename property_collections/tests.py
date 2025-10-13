from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from listings.models import Property, Favorite


class FavoritePropertiesAccessTests(TestCase):
    def test_requires_login(self):
        response = self.client.get(reverse('favorite_properties'))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)


class FavoritePropertiesViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='violet', password='password123')
        self.client.force_login(self.user)

    def _create_property(self, **kwargs):
        defaults = {
            'title': 'Test Villa',
            'description': 'A beautiful villa by the sea',
            'country': 'ES',
            'city': 'Barcelona',
            'price': 250000,
            'owner': self.user,
        }
        defaults.update(kwargs)
        return Property.objects.create(**defaults)

    def test_favorite_properties_lists_user_favorites(self):
        property_obj = self._create_property()
        Favorite.objects.create(user=self.user, property=property_obj)

        response = self.client.get(reverse('favorite_properties'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, property_obj.title)

    def test_favorite_properties_empty_state_message(self):
        response = self.client.get(reverse('favorite_properties'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Избранное пока пусто')
        self.assertContains(response, 'У вас пока нет избранных объектов')
