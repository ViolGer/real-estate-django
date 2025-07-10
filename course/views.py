from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson, UserProgress
from django.contrib.auth.decorators import login_required
#from achievements.models import Badge, UserBadge
from achievements.utils import check_course_completion


@login_required
def mark_complete(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress, _ = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
    progress.completed = True
    progress.save()

    check_course_completion(request.user)

    return redirect('lesson_list')



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
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'course/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        for question in questions:
            selected = request.POST.get(f"question_{question.id}")
            if selected:
                choice = get_object_or_404(Choice, id=selected)
                UserAnswer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'selected_choice': choice}
                )
        return redirect('quiz_result', quiz_id=quiz.id)

    return render(request, 'course/quiz_detail.html', {
        'quiz': quiz,
        'questions': questions
    })

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    user_answers = UserAnswer.objects.filter(user=request.user, question__in=questions)

    correct = 0
    total = questions.count()

    for answer in user_answers:
        if answer.selected_choice.is_correct:
            correct += 1

    score = int((correct / total) * 100) if total > 0 else 0

    return render(request, 'course/quiz_result.html', {
        'quiz': quiz,
        'score': score,
        'correct': correct,
        'total': total
    })