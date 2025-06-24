from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Агент')
    client_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    property_name = models.CharField(max_length=255, verbose_name='Объект')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    status = models.CharField(max_length=50, default='в работе', verbose_name='Статус')
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Комиссия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return f"{self.client_name} ({self.property_name}) — {self.agent.username}"
