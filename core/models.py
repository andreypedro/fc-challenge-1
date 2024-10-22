from django.db import models

# Create your models here.
# Você deverá criar um app do Django com o nome core e os seguintes models:
# Post
# Dados: title, content, created_at, tags (um post tem uma ou várias tags e uma tag pode ter um ou vários posts)
# Tag
# Dados: name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title
    
