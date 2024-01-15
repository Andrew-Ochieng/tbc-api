from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey(User, related_name='articles', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = RichTextField()
    image = models.ImageField(upload_to='tbc_blog/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_author_username(self):
        return self.author.username if self.author else None
