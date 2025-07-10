from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Choice, UserAnswer
from django.contrib.auth.decorators import login_required
from achievements.models import Badge, UserBadge
from quizzes.models import QuizResult


def check_quiz_completion(user):
    total_quizzes = Quiz.objects.count()
    passed_quizzes = QuizResult.objects.filter(user=user, passed=True).count()

    if total_quizzes == passed_quizzes:
        badge, _ = Badge.objects.get_or_create(name="Квиз-мастер", defaults={
            "description": "Ты сдал все квизы! 🎓"
        })
        UserBadge.objects.get_or_create(user=user, badge=badge)


@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

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

    return render(request, 'quizzes/quiz_detail.html', {
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

    return render(request, 'quizzes/quiz_result.html', {
        'quiz': quiz,
        'score': score,
        'correct': correct,
        'total': total
    })