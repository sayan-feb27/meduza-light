from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel


class News(UUIDModel, TimeStampedModel):
    title = models.CharField("заголовок", max_length=256)
    slug = models.SlugField("семантический URL", max_length=256, unique=True)
    body = models.TextField("контент")
    published = models.DateField("дата публикации")
    is_archived = models.BooleanField("в архиве?", default=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ("-published",)

    def __str__(self):
        return self.title
