from django import forms

from .models import Comment


class EmailForm(forms.Form):
    name = forms.CharField(max_length=30)
    email_from = forms.EmailField()
    email_to = forms.EmailField()
    title = forms.CharField(max_length=30)
    text = forms.CharField(required=True, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
