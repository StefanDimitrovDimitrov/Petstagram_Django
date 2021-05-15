from django import forms

from pets.models import Comment


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
