from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body'] #모델 중 어떤 항목을 입력받을 것인가?