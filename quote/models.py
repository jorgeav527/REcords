from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title}"


class Quote(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    quote = models.TextField()
    author_quote = models.CharField(max_length=50)
    publish_quote = models.DateTimeField(default=timezone.now)  
    created_quote = models.DateTimeField(auto_now_add=True)     #timestamp 
    updated_quote = models.DateTimeField(auto_now=True)         
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
        
    def __str__(self):
        return f"{self.quote} by {self.author_quote} status {self.status}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments_count(self):
        return self.comments.all().count()


class Comment(models.Model):
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"Comment by {self.user} on {self.quote}"
