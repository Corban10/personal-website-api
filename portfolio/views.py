# Response imports
from django.http import HttpResponse, JsonResponse

# Json serializers
from django.core import serializers
import json

# Email imports 
from django.core.mail import send_mail
from django.conf import settings

# Models
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
    projects = Project.objects.all()
    data = json.dumps(list(map(lambda x: get_project_images_json(x), projects)))
    return HttpResponse(data)

def projects_one(request, id):
    projects = [Project.objects.get(pk=id)]
    data = json.dumps(list(map(lambda x: get_project_images_json(x), projects)))
    return HttpResponse(data)
    
def get_project_images_json(project):
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


def blog_posts_all(request):
    blog_posts = BlogPost.objects.all()
    data = json.dumps(list(map(lambda x: get_blog_images_json(x), blog_posts)))
    return HttpResponse(data)

def blog_posts_one(request, id):
    blog_posts = [BlogPost.objects.get(pk=id)]
    data = json.dumps(list(map(lambda x: get_blog_images_json(x), blog_posts)))
    return HttpResponse(data)

def blog_posts_by_tag(request, id):
    blog_posts = BlogPost.objects.filter(category=id)
    data = json.dumps(list(map(lambda x: get_blog_images_json(x), blog_posts)))
    return HttpResponse(data)

def get_blog_images_json(blog_post):
    images = []
    for image in list(BlogPostImage.objects.filter(blog_post=blog_post)):
        images.append({
            'id' : image.id,
            'image' : str(image.image)
        })
    return {
        "id": blog_post.id,
        "content": blog_post.content,
        "slug": blog_post.slug,
        "desc": blog_post.desc,
        "date": str(blog_post.date),
        "category": {
            "id": blog_post.category.id,
            "name": blog_post.category.name,
            "created_at": str(blog_post.category.created_at),
            "updated_at": str(blog_post.category.updated_at)
        },
        "created_at": str(blog_post.created_at),
        "updated_at": str(blog_post.updated_at),
        'images' : images
    }
