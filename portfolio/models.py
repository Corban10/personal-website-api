from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Project(models.Model):
    description = models.TextField()
    image = models.BinaryField()
    github = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    featured = models.CharField(max_length=30)
    date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class BlogPost(models.Model):
    content = models.TextField()
    image = models.TextField()
    slug = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField(auto_now=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
