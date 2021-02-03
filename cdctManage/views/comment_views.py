from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Lecture, Feedback, Comment


@login_required(login_url='common:login')
def comment_create_feedback(request, feedback_id):
    """
    pybo 답글댓글등록
    """
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.feedback = feedback
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('cdctManage:detail', lecture_id=comment.feedback.lecture.id), comment.id))

    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'cdctManage/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_feedback(request, comment_id):
    """
    pybo 답글댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('cdctManage:detail', lecture_id=comment.feedback.lecture.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('cdctManage:detail', lecture_id=comment.feedback.lecture.id)
            return redirect('{}#comment_{}'.format(resolve_url('cdctManage:detail', lecture_id=comment.feedback.lecture.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'cdctManage/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_feedback(request, comment_id):
    """
    pybo 답글댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('cdctManage:detail', lecture_id=comment.feedback.lecture.id)
    else:
        comment.delete()
    return redirect('cdctManage:detail', lecture_id=comment.feedback.lecture.id)

@login_required(login_url='common:login')
def comment_delete_lecture(request, comment_id):
    """
    pybo 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('cdctManage:detail', lecture_id=comment.lecture_id)
    else:
        comment.delete()
    return redirect('cdctManage:detail', lecture_id=comment.lecture_id)

@login_required(login_url='common:login')
def comment_modify_lecture(request, comment_id):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('cdctManage:detail', lecture_id=comment.lecture.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('cdctManage:detail', lecture_id=comment.lecture.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'cdctManage/comment_form.html', context)

@login_required(login_url='common:login')
def comment_create_lecture(request, lecture_id):
    """
    pybo 질문댓글등록
    """
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.lecture = lecture
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('cdctManage:detail', lecture_id=comment.lecture.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'cdctManage/comment_form.html', context)
