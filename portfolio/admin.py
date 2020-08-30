from django.contrib import admin

# Register your models here.
from .models import Category, Job, Project, BlogPost

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Project)
admin.site.register(BlogPost)
