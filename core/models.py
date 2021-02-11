from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)
