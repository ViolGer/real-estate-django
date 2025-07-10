from email.policy import default

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_image_size(image):
    max_size_mb = 5
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер изображения — {max_size_mb}MB")

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    ownership_type = models.CharField(max_length=50, choices=[('freehold', 'Freehold'), ('leasehold', 'Leasehold')], default='freehold')

    distance_to_center_m = models.PositiveIntegerField(null=True, blank=True)
    distance_to_airport_km = models.PositiveIntegerField(null=True, blank=True)
    roi_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_furnished = models.BooleanField(default=False)
    has_management_company = models.BooleanField(default=False)
    has_guaranteed_income = models.BooleanField(default=False)
    yutree_score = models.CharField(max_length=50, null=True, blank=True)

    def price_per_m2(self):
        if self.area and self.area > 0:
            return round(self.price / self.area, 2)
        return None

    def __str__(self):
        return f"{self.title} in {self.city}, {self.country}"

    # Метод строкового представления — удобно видеть в админке
    def __str__(self):
        return f"{self.title} in {self.city}, {self.country}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/', validators=[validate_image_size])
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.property.title}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')