from django import forms
from apps.blog.models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text', 'is_checked', 'article']
