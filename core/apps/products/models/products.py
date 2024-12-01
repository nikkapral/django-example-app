from django.db import models
from core.apps.common.models import TimedBaseModel

class Product(TimedBaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name='Product title'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Product description'
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name='Is product visivle on website'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
