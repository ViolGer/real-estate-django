import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from listings.models import Property, PropertyImage

@pytest.mark.django_db
def test_property_image_upload():
    user = User.objects.create_user(username="testuser")
    prop = Property.objects.create(
        title="Test House", description="...", country="FR", city="Nice", price=100000,
        owner=user
    )

    image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")

    img = PropertyImage.objects.create(
        property=prop,
        image=image,
        caption="Front view"
    )

    assert img.pk is not None
    assert img.caption == "Front view"
    assert str(img) == "Image for Test House"
