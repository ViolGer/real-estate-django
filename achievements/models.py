from django.db import models
from django.contrib.auth.models import User

class Badge(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бейджа")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='badges/', blank=True, null=True, verbose_name="Иконка")

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_badges")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_awarded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.badge.name}"
