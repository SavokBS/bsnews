from django.shortcuts import render
from .models import Genre, Article


def index(request):
    genries = Genre.objects.all()
    articles = Article.objects.all().reverse()[:9]

    return render(
        request,
        'index.html',
        context={'genries': genries, 'articles': articles}
    )
