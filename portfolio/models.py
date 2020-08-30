import datetime
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def was_updated(self):
        return self.updated_at >= self.created_at 

class Job(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company
    def was_updated(self):
        return self.updated_at >= self.created_at # timezone.now() - datetime.timedelta(days=1)

class Project(models.Model):
    description = models.TextField()
    image = models.BinaryField(default=b"123")
    github = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    featured = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.description
    def was_updated(self):
        return self.updated_at >= self.created_at 

class BlogPost(models.Model):
    content = models.TextField()
    image = models.BinaryField(default=b"123")
    slug = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.desc
    def was_updated(self):
        return self.updated_at >= self.created_at 
