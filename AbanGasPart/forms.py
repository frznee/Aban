from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'نام شما (اختیاری)',
                'class': 'form-control',
                'style': 'background-color:#1a1a1a;color:#f0f0f0;'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'نظرات خود را اینجا وارد کنید...',
                'class': 'form-control',
                'rows': 4,
                'style': 'background-color:#1a1a1a;color:#f0f0f0;'
            }),
        }