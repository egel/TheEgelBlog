from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    body = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('blog.Category')
    tags = models.ManyToManyField('blog.Tag', blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_tags', None, {'slug': self.slug})
