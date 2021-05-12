from django.shortcuts import render
from .models import Genre, Article
from django.views import generic


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
    paginate_by = 1


class NewsDetailView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'news_detail.html'

