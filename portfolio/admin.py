from django.contrib import admin

# Register your models here.
from .models import Category, Skill, Job, Project, BlogPost, ProjectImage, BlogPostImage

class InlineProjectImage(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlineProjectImage]

class InlineBlogPostImage(admin.TabularInline):
    model = BlogPostImage

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [InlineBlogPostImage]

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
