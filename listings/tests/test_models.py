import pytest
from django.contrib.auth.models import User
from listings.models import Property

@pytest.mark.django_db
def test_property_creation():
    user = User.objects.create_user(username="testuser", password="12345")

    prop = Property.objects.create(
        title="Ocean View Apartment",
        description="Beautiful sea-facing apartment.",
        country="Spain",
        city="Barcelona",
        price=300000.00,
        currency="EUR",
        owner=user,
        area=75.0,
        is_furnished=True,
        has_management_company=True,
        has_guaranteed_income=False,
    )

    assert prop.pk is not None
    assert prop.price_per_m2() == round(300000.00 / 75.0, 2)
    assert str(prop) == "Ocean View Apartment in Barcelona, Spain"
