from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^news/$', views.NewsListView.as_view(), name="news"),
    url(r'^news/(?P<id>\d+)$', views.news_detail, name='news-detail'),
    url(r'^news/(?P<id>\d+)/like', views.like, name="like")
]