from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories_all/', views.categories_all, name='categories_all'),
    path('categories_one/<int:id>/', views.categories_one, name='categories_one'),
    path('jobs_all/', views.jobs_all, name='jobs_all'),
    path('jobs_one/<int:id>/', views.jobs_one, name='jobs_one'),
    path('projects_all/', views.projects_all, name='projects_all'),
    path('projects_one/<int:id>/', views.projects_one, name='projects_one'),
    path('blog_posts_all/', views.blog_posts_all, name='blog_posts_all'),
    path('blog_posts_one/<int:id>/', views.blog_posts_one, name='blog_posts_one'),
    path('blog_posts_by_tag/<int:id>/', views.blog_posts_by_tag, name='blog_posts_by_tag')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)