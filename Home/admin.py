from urllib.parse import urlencode

from django.contrib import admin
from django.urls import path
from django.utils.safestring import mark_safe

from .models import *
from .views import upload_images_game, upload_images_news


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'visible', 'dropdown', 'https', 'href')
    list_editable = ('visible', 'dropdown', 'https', 'href')


class DropdownLinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'https', 'href', 'slug',)
    list_editable = ('https', 'href',)
    prepopulated_fields = {"slug": ("text",)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('alt', 'link', 'display_image')
    list_editable = ('link',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No image'

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'slug', 'display_image', 'upload_image',)
    list_editable = ('slug',)

    def display_image(self, obj):
        if obj.main_photo:
            return mark_safe(f'<img src="{obj.main_photo.url}" width="80" height="45" />')
        return 'No image'

    def upload_image(self, obj):
        upload_url = reverse('upload_game', kwargs={'slug': obj.slug})
        result = f"<a href=\"{upload_url}\" " \
                 "style=\"display: inline-block; " \
                 "background: #8C959D; color: #fff; " \
                 "padding: 1rem 1.5rem; " \
                 "text-decoration: none; " \
                 "border-radius: 3px; \">" \
                 "Upload photo" \
                 "</a>"
        return mark_safe(result)

    readonly_fields = ["preview"]

    def preview(self, obj):
        result = f'<img src="{obj.main_photo.url}" style="max-height: 200px;">'
        result += '<br><br><hr>'
        # Generating the URL for the upload view using reverse
        upload_url = reverse('upload_game', kwargs={'slug': obj.slug})
        result += f"<a href=\"{upload_url}\" " \
                  "style=\"display: inline-block; " \
                  "background: #8C959D; color: #fff; " \
                  "padding: 1rem 1.5rem; " \
                  "text-decoration: none; " \
                  "border-radius: 3px; \">" \
                  "Upload photo" \
                  "</a>"
        result += '<br><br><hr>'
        return mark_safe(result)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'up', 'down', 'views', 'display_image', 'upload_image',)
    list_editable = ('slug',)

    def display_image(self, obj):
        if obj.main_image:
            return mark_safe(f'<img src="{obj.main_image.url}" width="80" height="45" />')
        return 'No image'

    def upload_image(self, obj):
        upload_url = reverse('upload_news', kwargs={'slug': obj.slug})
        result = f"<a href=\"{upload_url}\" " \
                 "style=\"display: inline-block; " \
                 "background: #8C959D; color: #fff; " \
                 "padding: 1rem 1.5rem; " \
                 "text-decoration: none; " \
                 "border-radius: 3px; \">" \
                 "Upload photo" \
                 "</a>"
        return mark_safe(result)

    readonly_fields = ["preview"]

    def preview(self, obj):
        result = f'<img src="{obj.main_photo.url}" style="max-height: 200px;">'
        result += '<br><br><hr>'
        # Generating the URL for the upload view using reverse
        upload_url = reverse('upload', kwargs={'slug': obj.slug})
        result += f"<a href=\"{upload_url}\" " \
                  "style=\"display: inline-block; " \
                  "background: #8C959D; color: #fff; " \
                  "padding: 1rem 1.5rem; " \
                  "text-decoration: none; " \
                  "border-radius: 3px; \">" \
                  "Upload photo" \
                  "</a>"
        result += '<br><br><hr>'
        return mark_safe(result)


class SystemRequirementsAdmin(admin.ModelAdmin):
    list_display = ('game', 'visible', 'operating_system_name')
    list_editable = ('visible', )
    list_filter = ('game', 'operating_system_name', 'visible')


class MultipleImageGameAdmin(admin.ModelAdmin):
    list_display = ('game', 'display_image', 'sequence')
    list_filter = ('game', 'sequence')

    def display_image(self, obj):
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="160" height="90" />')
        return 'No image'


class MultipleImageNewsAdmin(admin.ModelAdmin):
    list_display = ('news', 'display_image', 'sequence')
    list_filter = ('news', 'sequence')

    def display_image(self, obj):
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="160" height="90" />')
        return 'No image'


class LogoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_image', )

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="160" height="90" />')
        return 'No image'

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.error(request, e.message)
        else:
            messages.success(request, 'Объект успешно сохранен!')


admin.site.register(Link, LinkAdmin)
admin.site.register(DropdownLink, DropdownLinkAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(DynamicPage)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirements, SystemRequirementsAdmin)
admin.site.register(MultipleImageGame, MultipleImageGameAdmin)
admin.site.register(MultipleImageNews, MultipleImageNewsAdmin)
admin.site.register(Logo, LogoAdmin)

