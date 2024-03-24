from django.shortcuts import get_object_or_404, get_list_or_404, render
from blog.models import Post, Category
from datetime import datetime


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lt=datetime.now())[0:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    pk = id
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post.objects,
                             is_published=True,
                             category__is_published=True,
                             pub_date__date__lt=datetime.now(),
                             pk=pk)
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category.objects,
                                 slug=category_slug,
                                 is_published=True)
    post_list = get_list_or_404(Post.objects, is_published=True,
                                pub_date__date__lt=datetime.now(),
                                category__slug=category_slug)
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
