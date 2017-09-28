from django.contrib import admin
from .models import Post, Comment

# register Post, Comment models with built-in /admin interface
admin.site.register(Post)
admin.site.register(Comment) 
