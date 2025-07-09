from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson, UserProgress
from django.contrib.auth.decorators import login_required

@login_required
def lesson_list(request):
    lessons = Lesson.objects.all().order_by('order')
    user_progress = UserProgress.objects.filter(user=request.user)
    completed_ids = user_progress.filter(completed=True).values_list('lesson_id', flat=True)
    return render(request, 'course/lesson_list.html', {
        'lessons': lessons,
        'completed_ids': completed_ids
    })

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
    return render(request, 'course/lesson_detail.html', {'lesson': lesson})

@login_required
def mark_complete(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, created = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
    progress.completed = True
    progress.save()
    return redirect('lesson_list')