from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    """Model for single post in blog"""
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
        """Return absolute path using 'slug' for single post"""
        return ('view_blog_post', None, {'slug': self.slug})


class Category(models.Model):
    """Category model for grouping post"""
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        """Return absolute path using 'slug' for single category"""
        return ('view_blog_category', None, {'slug': self.slug})


class Tag(models.Model):
    """Category model for grouping post"""
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        """Return absolute path using 'slug' for single tag"""
        return ('view_blog_tags', None, {'slug': self.slug})
