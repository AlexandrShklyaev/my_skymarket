from django.contrib import admin

from ads.models import Ad, Comment


# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "price", "image")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text")
