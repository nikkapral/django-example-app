from django.db import models

class TimedBaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creation'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of update',
        blank=True
    )

    class Meta:
        abstract = True
