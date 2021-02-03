from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#수업기록
class Lecture(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_lecture')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    round = models.IntegerField()
    voter = models.ManyToManyField(User, related_name='voter_lecture')  # voter 추가
    def __str__(self):
        return self.subject

#수업기록 댓글
class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_feedback')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_feedback')

#수업기록 댓글의 댓글(코멘트)
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    lecture = models.ForeignKey(Lecture, null=True, blank=True, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, null=True, blank=True, on_delete=models.CASCADE)

#공지사항
class Info(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject
