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


class NewsDetailView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'news_detail.html'


def like(request, id):
    article = Article.objects.get(id=id)
    article.likes += 1
    article.save()
    
    return HttpResponse(status=204)

