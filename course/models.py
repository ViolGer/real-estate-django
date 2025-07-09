from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название урока')
    description = models.TextField(blank=True, verbose_name='Описание')
    video = models.FileField(upload_to='lessons/videos/', blank=True, null=True, verbose_name='Видеофайл')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок показа')

    def __str__(self):
        return self.title

class Achievement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ачивки')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} — {self.lesson.title}"