from django.contrib import admin

# Register your models here.
from .models import Category, Skill, Social, Project, BlogPost, ProjectImage, BlogPostImage

class InlineProjectImage(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlineProjectImage]

class InlineBlogPostImage(admin.TabularInline):
    model = BlogPostImage

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [InlineBlogPostImage]

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Social)
admin.site.register(Project, ProjectAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ProjectImage)
admin.site.register(BlogPostImage)