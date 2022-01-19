from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name

class SubFamilyIntern(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name
    

class SubFamily(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name
    

class Reference(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name
    
    
class ColorReference(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name

class Size(models.Model):
    value = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.value


class Clase(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name
    
    
class GroupUnity(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name


class ReferenceGroup(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name


class FboCode(models.Model):
    name = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name


class Cartridges(models.Model):
    code = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    manufacturer = models.ForeignKey(Manufacturer,
        related_name='manufacturer',
        related_query_name='manufacturer',
        on_delete=models.DO_NOTHING,
    )
    family = models.ForeignKey(Family,
        related_name='family',
        related_query_name='family',
        on_delete=models.DO_NOTHING,
    )
    sub_family_intern = models.ForeignKey(SubFamilyIntern,
        related_name='sub_family_intern',
        related_query_name='sub_family_intern',
        on_delete=models.DO_NOTHING,
    )
    family_intern = models.ForeignKey(SubFamily,
        related_name='family_intern',
        related_query_name='family_intern',
        on_delete=models.DO_NOTHING,
    )
    reference = models.ForeignKey(Reference,
        related_name='reference',
        related_query_name='reference',
        on_delete=models.DO_NOTHING,
    )
    selling_price_base = models.FloatField()
    weitgh = models.IntegerField()
    color_reference = models.ForeignKey(ColorReference,
        related_name='color_reference',
        related_query_name='color_reference',
        on_delete=models.DO_NOTHING,
    )
    color = models.ForeignKey(Color,
        related_name='color',
        related_query_name='color',
        on_delete=models.DO_NOTHING,
    )
    size = models.ForeignKey(Size,
        related_name='size',
        related_query_name='size',
        on_delete=models.DO_NOTHING,
    )
    clase = models.ForeignKey(Clase,
        related_name='clase',
        related_query_name='clase',
        on_delete=models.DO_NOTHING,
    )
    date = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    group_unity = models.ForeignKey(GroupUnity,
        related_name='group_unity',
        related_query_name='group_unity',
        on_delete=models.DO_NOTHING,
    )
    reference_group = models.ForeignKey(ReferenceGroup,
        related_name='reference_group',
        related_query_name='reference_group',
        on_delete=models.DO_NOTHING,
    )
    fbo_code = models.ForeignKey(FboCode,
        related_name='fbo_code',
        related_query_name='fbo_code',
        on_delete=models.DO_NOTHING,
    )
    
    class Meta:
        verbose_name = ("Cartucho")
        verbose_name_plural = ("Cartuchos")

    def __str__(self):
        return self.code
