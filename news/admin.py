from django.contrib import admin
from news.models import Genre, Article


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('genre', 'title', 'author', 'likes')
    list_filter = ('genre', 'author')
    fields = ('genre', 'title', 'spoiler', 'promo', 'text', 'publish_date', 'author')
    readonly_fields = ('publish_date', 'likes')
    search_fields = ('genre', 'title', 'author')
