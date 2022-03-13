from django.db import models

from cartuchos.utils.models import BaseCreatedUpdatedModel


# Create your models here.

from cartuchos.cartridge.models import SubFamilyIntern, Family


class Fees(BaseCreatedUpdatedModel):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    fee = models.FloatField(
        null=True,
        blank=True,
        default=0
    )
    family = models.ForeignKey(Family,
        related_name='fee',
        related_query_name='fee',
        on_delete=models.DO_NOTHING,
    )
    sub_family_intern = models.ForeignKey(SubFamilyIntern,
        related_name='fee',
        related_query_name='fee',
        on_delete=models.DO_NOTHING,
    )
    
    class Meta:
        verbose_name = ("Tarifa")
        verbose_name_plural = ("Tarifas")

    def __str__(self):
        return f"Nombre: {self.name} - Tarifa: {self.fee} - \
            Familia: {self.family} - Sub Familia Interno{self.sub_family_intern}"