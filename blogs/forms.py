from django import forms
from .models import PostModel, CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post', 'created_at']