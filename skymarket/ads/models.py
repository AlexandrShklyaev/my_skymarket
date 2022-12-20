

from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}
NOTNULLABLE = {'null': False, 'blank': False}

class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=100, verbose_name="название",**NULLABLE)
    price = models.IntegerField(verbose_name="цена",**NULLABLE)
    description = models.CharField(max_length=2000, verbose_name="описание",**NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ads", verbose_name="автор",**NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявление"
        ordering = ["-created_at"]


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=2000, verbose_name="содержание",**NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="автор",**NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="объявление",**NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
