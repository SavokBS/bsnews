from django.shortcuts import render
from .models import Genre, Article
from django.views import generic
from django.http import HttpResponse


def index(request):
    articles = Article.objects.all().reverse()[:9]

    return render(
        request,
        'index.html',
        context={'articles': articles}
    )


class NewsListView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'news.html'
    paginate_by = 9


def news_detail(request, id):
    article = Article.objects.get(id=id)
    if request.session.get(f'like_{id}', 'False') == 'False':
        request.session[f'like_{id}'] = 'False'

    print("nenen", like)

    return render(
        request,
        'news_detail.html',
        context={'article': article, 'like': request.session[f'like_{id}']}
    )


def like(request, id):
    request.session[f'like_{id}'] = 'True'
    article = Article.objects.get(id=id)
    article.likes += 1
    article.save()

    return HttpResponse(status=204)

