from django.db import models
from django.utils import timezone

# Post model (gets represented as table in DB schema) 
class Post(models.Model):
    author = models.ForeignKey('auth.User') # using built-in User model as FK 
    title = models.CharField(max_length=200) 
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) # we don't want a default because drafts won't have a published_date

    # publish a post by setting the published_date to now & saving to DB
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # returns only the comments whose approved_comment field is True by filtering using ORM
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # string method override
    def __str__(self):
        return self.title

# Comment model 
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments') # each comment has a corresponding Post object it belongs to 
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # to approve a comment, set its approved_comment field to True
    def approve(self):
        self.approved_comment = True
        self.save()

    # string method override 
    def __str__(self):
        return self.text


