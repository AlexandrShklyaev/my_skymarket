from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name="фото", **NULLABLE)
    title = models.CharField(max_length=100, verbose_name="название")
    price = models.PositiveIntegerField(verbose_name="цена", **NULLABLE)
    description = models.CharField(max_length=2000, verbose_name="описание", **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ads",
                               verbose_name="автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявление"
        ordering = ["-created_at"]


class Comment(models.Model):
    text = models.CharField(max_length=2000, verbose_name="содержание", **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="автор",
                               related_name="comments")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="объявление", related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
