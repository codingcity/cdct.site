from django.urls import path

from .views import base_views, lecture_views, feedback_views, comment_views, vote_views

app_name = 'cdctManage'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:lecture_id>/', base_views.detail, name='detail'),

    path('lecture/create/', lecture_views.lecture_create, name='lecture_create'),
    path('lecture/modify/<int:lecture_id>/', lecture_views.lecture_modify, name='lecture_modify'),
    path('lecture/delete/<int:lecture_id>/', lecture_views.lecture_delete, name='lecture_delete'),

    path('feedback/create/<int:lecture_id>/', feedback_views.feedback_create, name='feedback_create'),
    path('feedback/modify/<int:feedback_id>/', feedback_views.feedback_modify, name='feedback_modify'),
    path('feedback/delete/<int:feedback_id>/', feedback_views.feedback_delete, name='feedback_delete'),

    path('comment/create/lecture/<int:lecture_id>/', comment_views.comment_create_lecture, name='comment_create_lecture'),
    path('comment/modify/lecture/<int:comment_id>/', comment_views.comment_modify_lecture, name='comment_modify_lecture'),
    path('comment/delete/lecture/<int:comment_id>/', comment_views.comment_delete_lecture, name='comment_delete_lecture'),
    path('comment/create/feedback/<int:feedback_id>/', comment_views.comment_create_feedback, name='comment_create_feedback'),
    path('comment/modify/feedback/<int:comment_id>/', comment_views.comment_modify_feedback, name='comment_modify_feedback'),
    path('comment/delete/feedback/<int:comment_id>/', comment_views.comment_delete_feedback, name='comment_delete_feedback'),
    path('vote/lecture/<int:lecture_id>/', vote_views.vote_lecture, name='vote_lecture'),
    path('vote/feedback/<int:feedback_id>/', vote_views.vote_feedback, name='vote_feedback'),
]

