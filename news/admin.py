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
    fields = ('genre', 'title', 'author', 'spoiler', 'promo', 'text')
    readonly_fields = ('likes', )
    search_fields = ('genre', 'title', 'author')
