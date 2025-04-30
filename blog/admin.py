from django.contrib import admin
from .models import Image, Post, Project
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']


class ImageInline(admin.TabularInline):
    model = Image
    max_num =15
    fields = ['image']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    fields = ['title', 'desctription', 'body', 'likes', 'views', 'github_url']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [ImageInline]
    fields = ['title', 'slug', 'body', 'views', 'likes']
    prepopulated_fields = {'slug' : ['title', ]}