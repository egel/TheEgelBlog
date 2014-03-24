from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
  title = models.CharField(max_length=140, unique=True)
  slug = models.SlugField(max_length=140, unique=True)
  body = models.TextField()
  created = models.DateTimeField()
  categories = models.ManyToManyField('blog.Category')

  def __unicode__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('view_blog_post', None, { 'slug': self.slug })


class Category(models.Model):
  name = models.CharField(max_length=100, db_index=True)
  slug = models.SlugField(max_length=100, db_index=True)

  def __unicode__(self):
    return self.name

  @models.permalink
  def get_absolute_url(self):
    return ('view_blog_category', None, { 'slug': self.slug })
