from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import LectureForm
from ..models import Lecture

@login_required(login_url='common:login')
def lecture_create(request):
    #cdctManage Lecture regist

    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.author = request.user  # 추가한 속성 author 적용
            lecture.create_date = timezone.now()
            lecture.round = 1            #str( int(lecture.round) + 1 )
            lecture.save()
            return redirect('cdctManage:index')
    else:
        form = LectureForm()
    context = {'form': form}
    return render(request, 'cdctManage/lecture_form.html', context)


@login_required(login_url='common:login')
def lecture_modify(request, lecture_id):
    #lecture modify
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.user != lecture.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('cdctManage:detail', lecture_id=lecture.id)

    if request.method == "POST":
        form = LectureForm(request.POST, instance=lecture)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.author = request.user
            lecture.modify_date = timezone.now()  # 수정일시 저장
            lecture.save()
            return redirect('cdctManage:detail', lecture_id=lecture.id)
    else:
        form = LectureForm(instance=lecture)
    context = {'form': form}
    return render(request, 'cdctManage/lecture_form.html', context)

@login_required(login_url='common:login')
def lecture_delete(request, lecture_id):
    #lecture delete
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.user != lecture.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('cdctManage:detail', lecture_id=lecture.id)
    lecture.delete()
    return redirect('cdctManage:index')
