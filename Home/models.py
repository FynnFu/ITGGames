from datetime import datetime

from colorfield.fields import ColorField
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import models
from django.http import request
from django.urls import reverse
from django.utils.text import slugify
from multiupload.fields import MultiImageField
from ckeditor.fields import RichTextField


# Create your models here.
class Link(models.Model):
    text = models.CharField(max_length=100, verbose_name="Текст")
    visible = models.BooleanField(default=True, verbose_name="Видимость")
    target = models.BooleanField(default=False, verbose_name="Открывать в новой вкладке")
    dropdown = models.BooleanField(default=False, verbose_name="Выпадающий список")
    https = models.BooleanField(default=False, verbose_name="Внешний сайт")
    dynamic_page = models.BooleanField(default=False, verbose_name="Динамическая страница")
    href = models.CharField(max_length=2000, default='', verbose_name="Ссылка")

    def get_absolute_url(self):
        if self.https:
            return self.href
        else:
            if self.dynamic_page:
                return reverse("dynamic_page", kwargs={"slug": self.href})
            else:
                return reverse(self.href)

    def __str__(self):
        return self.text


class DropdownLink(models.Model):
    link = models.ForeignKey(Link, on_delete=models.PROTECT, verbose_name="Главная ссылка")
    text = models.CharField(max_length=250, verbose_name="Текст")
    target = models.BooleanField(default=False, verbose_name="Открывать в новой вкладке")
    https = models.BooleanField(default=False, verbose_name="Внешний сайт")
    href = models.CharField(max_length=2000, default='', verbose_name="Ссылка")
    slug = models.SlugField(unique=True, blank=True, default='', verbose_name="URL")

    def get_absolute_url(self):
        if self.https:
            return self.href
        else:
            return reverse(self.href, kwargs={"slug": self.slug})

    def __str__(self):
        return self.text


class MultipleImageUpload(models.Model):
    images = models.FileField()
    sequence = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.sequence)


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, default='', verbose_name="URL")
    main_image = models.ImageField(upload_to='images/news/', null=True, blank=True)
    short_text = models.TextField(default='')
    text = RichTextField()
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class DynamicPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, default='', verbose_name="URL")
    image = models.ImageField(upload_to='images/dynamic_page/', null=True, blank=True)
    text = RichTextField()
    background_color = ColorField(default='#282e39', verbose_name="Цвет фона")

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    alt = models.CharField(max_length=250, verbose_name="Название")
    link = models.CharField(max_length=2000, verbose_name="Ссылка")
    image = models.ImageField(upload_to='images/social/')

    def __str__(self):
        return self.alt


class Genre(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, default='', verbose_name="URL")

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, default='')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='images/game/main_photo/')
    video_src = models.CharField(max_length=2000, default='')
    release_date = models.DateField()
    short_description = RichTextField(default='')
    steam_widget_src = models.CharField(max_length=2000, default='')
    description = RichTextField(default='')

    def __str__(self):
        return self.name


class SystemRequirements(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    operating_system_name = models.CharField(max_length=250)
    requirements = RichTextField(default='')
    requirements_recommended = RichTextField(default='')

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = "System Requirements"
        verbose_name_plural = "System Requirements"


class MultipleImageGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    images = models.FileField()
    sequence = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = "MultipleImages Game"
        verbose_name_plural = "Multiple Images Game"


class MultipleImageNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    images = models.FileField()
    sequence = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = "Multiple Images News"
        verbose_name_plural = "Multiple Images News"


class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logo"

    def save(self, *args, **kwargs):
        if not self.pk and Logo.objects.exists():
            raise ValidationError('Слишком много записей типа Logo!')
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Logo'


