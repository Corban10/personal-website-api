# from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Category, Skill, Social, Project, ProjectImage, BlogPost, BlogPostImage


def index(request):
    return HttpResponse("")

def categories_all(request):
    data = serializers.serialize("json", Category.objects.all())
    return HttpResponse(data)

def categories_one(request, id):
    data = serializers.serialize("json", [Category.objects.get(pk=id)])
    return HttpResponse(data)

def skills_all(request):
    data = serializers.serialize("json", Skill.objects.all())
    return HttpResponse(data)

def socials_all(request):
    data = serializers.serialize("json", Social.objects.all())
    return HttpResponse(data)

def projects_all(request):
    # projects = serializers.serialize("json", Project.objects.prefetch_related('image'))
    data = serializers.serialize("json", ProjectImage.objects.prefetch_related('project'))
    return HttpResponse(data)

def projects_one(request, id):
    data = serializers.serialize("json", [Project.objects.get(pk=id)])
    return HttpResponse(data)

def blog_posts_all(request):
    data = serializers.serialize("json", BlogPost.objects.all())
    return HttpResponse(data)

def blog_posts_one(request, id):
    data = serializers.serialize("json", [BlogPost.objects.get(pk=id)])
    return HttpResponse(data)

def blog_posts_by_tag(request, id):
    data = serializers.serialize("json", BlogPost.objects.filter(category=id))
    return HttpResponse(data)
