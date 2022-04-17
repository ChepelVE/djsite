from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import *


def index(request):  # HttpRequest
    posts = Women.objects.all()

    context = {
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=context)


def about(request):  # HttpRequest
    context = {
        'title': 'О сайте',
    }
    return render(request, 'women/about.html', context=context)


def contact(request):
    return HttpResponse(f"<h1>Обратная связь</h1>")


def add_page(request):
    context = {
        'title': "Добавление статьи",
    }
    return render(request, 'women/add_page.html', context=context)


def login(request):
    return HttpResponse(f"<h1>Войти</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat.id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'cat_selected': cat.id
    }
    return render(request, 'women/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
