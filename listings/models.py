from django.db import models  # Импортируем модуль моделей Django
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_image_size(image):
    max_size_mb = 5
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер изображения — {max_size_mb}MB")


# Определяем модель свойство — она будет представлять объект недвижимости
class Property(models.Model):
    # Название объявления, например: "Квартира у моря"
    title = models.CharField(max_length=255)

    # Полное описание — можно вставить много текста
    description = models.TextField()

    # Страна, в которой находится объект
    country = models.CharField(max_length=100)

    # Город или населённый пункт
    city = models.CharField(max_length=100)

    # Цена объекта (до 9999999999.99 — 12 цифр, 2 после точки)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    # Валюта (например, USD, EUR, GBP)
    currency = models.CharField(max_length=10, default='USD')

    # Флаг, доступен ли объект для продажи/аренды
    is_available = models.BooleanField(default=True)

    # Дата и время создания объявления
    created_at = models.DateTimeField(auto_now_add=True)

    #добавляем изображение
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    #площадь
    area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

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
