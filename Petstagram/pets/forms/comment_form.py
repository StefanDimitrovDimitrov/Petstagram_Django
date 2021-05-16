from django import forms

from pets.models import Comment


# class CommentForms(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2'
            }
        )
    )