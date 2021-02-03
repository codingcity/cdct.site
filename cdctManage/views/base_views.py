from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count


from ..models import Lecture


# Create your views here.
import logging
logger = logging.getLogger('cdctManage')

def index(request):
    logger.info("INFO LEVEL")
    #cdctManage list
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어


    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        lecture_list = Lecture.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        lecture_list = Lecture.objects.annotate(num_feedback=Count('feedback')).order_by('-num_feedback', '-create_date')
    else:  # recent , 조회
        lecture_list = Lecture.objects.order_by('-create_date')

    if kw:
        lecture_list = lecture_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(feedback__author__username__icontains=kw) | # 답변 글쓴이검색
            Q(comment__author__username__icontains=kw)
        ).distinct()


    paginator = Paginator(lecture_list, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'lecture_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # <------ so 추가
    return render(request, 'cdctManage/lecture_list.html',context)

def detail(request, lecture_id):
    """
    pybo 내용 출력
    """
    #lecture = Lecture.objects.get(id=lecture_id)
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    context = {'lecture': lecture}
    return render(request, 'cdctManage/lecture_detail.html', context)