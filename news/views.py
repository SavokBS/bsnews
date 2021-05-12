from django.shortcuts import render
from .models import Genre, Article
from django.core.paginator import Paginator


def index(request):
    articles = Article.objects.all().reverse()[:9]

    return render(
        request,
        'index.html',
        context={'articles': articles}
    )
