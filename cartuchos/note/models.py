import imp
from django.db import models
from django.contrib.auth import get_user_model


from utils.models import BaseCreatedUpdatedModel


User = get_user_model()


class NoteCodeReference(BaseCreatedUpdatedModel):
    number = models.IntegerField(default=1)
    prefix = models.CharField(
        null=True,
        blank=True, 
        max_length=10,
        default='A'
    )
    
    def __str__(self):
        return f"{self.prefix}-{self.number}"
    
    def get_code(self):
        _return = f"{self.prefix}-{self.number}"
        self.number += 1
        self.save()
        return _return


class Notes(BaseCreatedUpdatedModel):
    box_weight = models.FloatField()
    total_weight =  models.FloatField()
    laser_weight = models.FloatField()
    laser_percent = models.FloatField()
    inkjet_weight = models.FloatField()
    inkjet_percent = models.FloatField()
    total_items = models.IntegerField()
    code = models.CharField(
        null=True,
        blank=True, 
        max_length=30
    )
    note = models.TextField(
        null=True,
        blank=True, 
    )
    salesman = models.ForeignKey(User,
        related_name='salesman',
        related_query_name='salesman',
        on_delete=models.DO_NOTHING,
    )
    client = models.ForeignKey('clients.Cliente',
        related_name='client',
        related_query_name='client',
        on_delete=models.DO_NOTHING,
    )
    
    class Meta:
        verbose_name = ("Albaran")
        verbose_name_plural = ("Albaranes")

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        reference_code = NoteCodeReference.objects.filter().last()
        if not reference_code:
            reference_code = NoteCodeReference.objects.create()
        self.code = reference_code.get_code()
        return super().save(*args, **kwargs)


class SelectedCartridges(BaseCreatedUpdatedModel):
    selected = models.ForeignKey('cartridge.Cartridges',
        related_name='selected_cartridges',
        related_query_name='selected_cartridges',
        on_delete=models.DO_NOTHING,
    )
    quantity = models.IntegerField()
    weight = models.FloatField()
    note = models.ForeignKey(Notes,
        related_name='notes',
        related_query_name='notes',
        on_delete=models.DO_NOTHING,
        null=True
    )