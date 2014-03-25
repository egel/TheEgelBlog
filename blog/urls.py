from django.conf.urls import patterns, url
from blog.models import Post, Category

urlpatterns = patterns('',

  url(r'^$', 'blog.views.index'),

  url(r'^posts/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),

  url(r'^categories/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),

  url(r'^categories/$', 'blog.views.view_categories', name='view_blog_categories'),

  url(r'^tags/(?P<slug>[^\.]+).html', 'blog.views.view_tag', name='view_blog_tag'),

  url(r'^tags/$', 'blog.views.view_tags', name='view_blog_tags'),

  url(r'^archives/$', 'blog.views.view_archives', name='view_blog_archives'),
)
