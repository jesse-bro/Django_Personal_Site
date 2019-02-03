from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    pub_date = models.DateTimeField()
    publisher = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Comment(models.Model):
    publisher = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.body
