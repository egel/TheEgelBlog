from blog.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
  return render_to_response('blog.html', {
    'categories': Category.objects.all(),
    'posts': Post.objects.all()[:5],
  })

def view_post(request, slug):
  return render_to_response('post.html', {
    'post': get_object_or_404(Post, slug=slug),
  })

def view_category(request, slug):
  category = get_object_or_404(Category, slug=slug)
  return render_to_response('category.html', {
    'category': category,
    'posts': Post.objects.filter(categories = category)[:5],
  })

def view_categories(request):
  return render_to_response('categories.html', {
    'categories': Category.objects.all()
  })

def view_archives(request):
  return render_to_response('archives.html', {
    'posts': Post.objects.all().order_by("-created"),
  })
