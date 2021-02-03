from django import forms
from cdctManage.models import Lecture, Feedback, Comment


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['subject', 'content']

        labels = {
            'subject': '수업주제',
            'content': '수업내용',
        }
        
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

