from course.models import Lesson, UserProgress
from .models import Badge, UserBadge

def check_course_completion(user):
    total_lessons = Lesson.objects.count()
    completed_lessons = UserProgress.objects.filter(user=user, completed=True).count()

    if total_lessons > 0 and completed_lessons == total_lessons:
        badge, _ = Badge.objects.get_or_create(
            name="Курс пройден",
            defaults={"description": "Ты прошел(а) все уроки курса! 🎉"}
        )
        UserBadge.objects.get_or_create(user=user, badge=badge)
