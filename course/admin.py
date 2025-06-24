from django.contrib import admin
from .models import Lesson, Achievement, UserProgress

admin.site.register(Lesson)
admin.site.register(Achievement)
admin.site.register(UserProgress)
