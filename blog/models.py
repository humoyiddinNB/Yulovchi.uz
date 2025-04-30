
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    body = RichTextField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='posts/images/')
    uploaded_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"images for {self.post.title}"



class Project(models.Model):
    title  = models.CharField(max_length=200)
    desctription = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    github_url = models.CharField(max_length=400)

    def __str__(self):
        return self.title


