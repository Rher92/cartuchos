from django.db import models

from utils.models import BaseCreatedUpdatedModel

# Create your models here.

class PrincipalCIF(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class NombreRazonSocial(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class TarifaAsignada(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Tipo(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Perfil(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class CpZip(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Poblacion(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class ZonaGeografica(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Provincia(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)

class Pais(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Clasificacion(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Campaña(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Frecuencia(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class Nima(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)


class ContratoFirmado(BaseCreatedUpdatedModel):
    nombre = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        return super().save(*args, **kwargs)
    

class Cliente(BaseCreatedUpdatedModel):
    cifrc = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    cif_principal = models.ForeignKey(PrincipalCIF,
        related_name='cif_principal',
        related_query_name='cif_principal',
        on_delete=models.DO_NOTHING,
    )
    sucursal = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    nombre_razon_social = models.ForeignKey(NombreRazonSocial,
        related_name='nombre_razon_social',
        related_query_name='nombre_razon_social',
        on_delete=models.DO_NOTHING,
    )
    tarifa_asignada = models.ForeignKey(TarifaAsignada,
        related_name='tarifa_asignada',
        related_query_name='tarifa_asignada',
        on_delete=models.DO_NOTHING,
    )
    tipo = models.ForeignKey(Tipo,
        related_name='tipo',
        related_query_name='tipo',
        on_delete=models.DO_NOTHING,
    )
    perfil = models.ForeignKey(Perfil,
        related_name='perfil',
        related_query_name='perfil',
        on_delete=models.DO_NOTHING,
    )
    direccion = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    cp_zip = models.ForeignKey(CpZip,
        related_name='cp_zip',
        related_query_name='cp_zip',
        on_delete=models.DO_NOTHING,
    )
    poblacion = models.ForeignKey(Poblacion,
        related_name='settlement',
        related_query_name='settlement',
        on_delete=models.DO_NOTHING,
    )
    zona_geografica = models.ForeignKey(ZonaGeografica,
        related_name='zona_geografica',
        related_query_name='zona_geografica',
        on_delete=models.DO_NOTHING,
    )
    provincia = models.ForeignKey(Provincia,
        related_name='province',
        related_query_name='province',
        on_delete=models.DO_NOTHING,
    )
    pais = models.ForeignKey(Pais,
        related_name='pais',
        related_query_name='pais',
        on_delete=models.DO_NOTHING,
    )
    email = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    email_respaldo = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    telefono = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    clasificacion = models.ForeignKey(Clasificacion,
        related_name='clasificacion',
        related_query_name='clasificacion',
        on_delete=models.DO_NOTHING,
    )
    persona_contacto = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    horario_recogida = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    campaña = models.ForeignKey(Campaña,
        related_name='campaña',
        related_query_name='campaña',
        on_delete=models.DO_NOTHING,
    )
    frecuencia = models.ForeignKey(Frecuencia,
        related_name='frecuencia',
        related_query_name='frecuencia',
        on_delete=models.DO_NOTHING,
    )
    fecha_ingreso = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    nima = models.ForeignKey(Nima,
        related_name='nima',
        related_query_name='nima',
        on_delete=models.DO_NOTHING,
    )
    numero_cuenta = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    proximo_aviso = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    num_ct1 = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    contrato_firmado = models.ForeignKey(ContratoFirmado,
        related_name='nima',
        related_query_name='nima',
        on_delete=models.DO_NOTHING,
    )
    cnae = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    mini_broker = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    nro_productor = models.CharField(
        null=True,
        blank=True, 
        max_length=255
    )
    
    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return f"{self.nombre_razon_social.nombre} - {self.cifrc}"
    
    def save(self, *args, **kwargs):
        self.cifrc = self.cifrc.lower()
        self.sucursal = self.sucursal.lower()
        self.direccion = self.direccion.lower()
        self.email = self.email.lower()
        self.email_respaldo = self.email_respaldo.lower()
        self.telefono = self.telefono.lower()
        self.persona_contacto = self.persona_contacto.lower()
        self.horario_recogida = self.horario_recogida.lower()
        self.fecha_ingreso = self.fecha_ingreso.lower()
        self.numero_cuenta = self.numero_cuenta.lower()
        self.proximo_aviso = self.proximo_aviso.lower()
        self.pronum_ct1ximo_aviso = self.num_ct1.lower()
        self.cnae = self.cnae.lower()
        self.mini_broker = self.mini_broker.lower()
        self.nro_productor = self.nro_productor.lower()
        return super().save(*args, **kwargs)