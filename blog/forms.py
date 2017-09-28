from django import forms
from .models import Post, Comment

# using built-in form for the form to write a new post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# using built-in form for form to write a comment 
class CommentForm(forms.ModelForm):
 
    class Meta:
        model = Comment
        fields = ('author', 'text',)
