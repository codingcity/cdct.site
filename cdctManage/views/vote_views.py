from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Lecture, Feedback


@login_required(login_url='common:login')
def vote_lecture(request, lecture_id):
    """
    질문추천등록
    """
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.user == lecture.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        lecture.voter.add(request.user)
    return redirect('cdctManage:detail', lecture_id=lecture.id)

@login_required(login_url='common:login')
def vote_feedback(request, feedback_id):
    """
    pybo 답글추천등록
    """
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    if request.user == feedback.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        feedback.voter.add(request.user)
    return redirect('cdctManage:detail', lecture_id=feedback.lecture.id)