from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import FeedbackForm
from ..models import Lecture, Feedback


@login_required(login_url='common:login')
def feedback_delete(request, feedback_id):
    """
    pybo 답변삭제
    """
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    if request.user != feedback.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        feedback.delete()
    return redirect('cdctManage:detail', lecture_id=feedback.lecture.id)

@login_required(login_url='common:login')
def feedback_modify(request, feedback_id):
    """
    pybo 답변수정
    """
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    if request.user != feedback.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('cdctManage:detail', feedback_id=feedback.lecture.id)

    if request.method == "POST":
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.modify_date = timezone.now()
            feedback.save()

            return redirect('{}#feedback_{}'.format(resolve_url('cdctManage:detail', lecture_id=feedback.lecture.id), feedback.id))
    else:
        form = FeedbackForm(instance=feedback)
    context = {'feedback': feedback, 'form': form}
    return render(request, 'cdctManage/feedback_form.html', context)



@login_required(login_url='common:login')
def feedback_create(request, lecture_id):
    #cdctManage Feedback regist
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user  # 추가한 속성 author 적용
            feedback.create_date = timezone.now()
            feedback.lecture = lecture
            feedback.save()

            return redirect('{}#feedback_{}'.format(resolve_url('cdctManage:detail', lecture_id=lecture.id), feedback.id))
    else:
        form = FeedbackForm()
    context = {'lecture': lecture, 'form': form}
    return render(request, 'cdctManage/lecture_detail.html', context)



