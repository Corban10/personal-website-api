# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Category, Skill, Social, Project, ProjectImage, BlogPost, BlogPostImage

import json

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
    data = json.dumps(list(map(lambda x: add_image_json(x), Project.objects.all())))
    print(data)
    return HttpResponse(data)

def add_image_json(project):
    images = []
    for image in list(ProjectImage.objects.filter(project=project)):
        images.append({
            'id' : image.id,
            'image' : str(image.image)
        })
    return {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "github": project.github,
        "url": project.url,
        "show": project.show,
        "date": str(project.date),
        "created_at": str(project.created_at),
        "updated_at": str(project.updated_at),
        'images' : images
    }

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
