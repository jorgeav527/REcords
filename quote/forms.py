from django import forms

from .models import Comment, Quote

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type your Comment here',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ["comment"]


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type your Quote here',
        'rows': '4',
    }))

    author_quote = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Was written by...',
    }))

    class Meta:
        model = Quote 
        fields = ("quote", "author_quote", "status", "category")