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

class Skill(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50, default="#")
    icon = models.FileField(upload_to="./skill")
    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50, default="#")
    icon = models.FileField(upload_to="./social")
    def __str__(self):
        return self.name

class Project(models.Model):
    description = models.TextField()
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

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="./project")

class BlogPost(models.Model):
    content = models.TextField()
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

class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="./blog")
