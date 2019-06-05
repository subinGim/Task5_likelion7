from django import forms
from .models import Blog, Comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image', 'hashtags'] #모델 중 어떤 항목을 입력받을 것인가?

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = "__all__"