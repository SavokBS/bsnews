from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from datetime import datetime

class Genre(models.Model):
    name = models.CharField("Название категории", max_length=100, help_text="Максимальная длина: 100 символов")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Article(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, verbose_name="Категория")
    title = models.CharField("Название статьи", max_length=300, help_text="Максимальная длина: 300 символов")
    promo = models.ImageField("Изображение")
    spoiler = models.CharField("Спойлер", max_length=400, help_text="Максимальная длина: 400 символов")
    text = RichTextField(verbose_name="Текст статьи", blank=True, null=True)
    publish_date = models.DateTimeField(verbose_name="Дата публикации", default=datetime.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Автор статьи")
    likes = models.IntegerField(verbose_name="Количество лайков", default=0)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.title} ({self.author})"
