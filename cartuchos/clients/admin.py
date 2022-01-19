from django.contrib import admin
from django.urls import path
from django import forms
import csv
import io
from django.shortcuts import redirect, render
# Register your models here.

from .models import PrincipalCIF, NombreRazonSocial, TarifaAsignada, Tipo, \
                    Perfil, CpZip, Poblacion, ZonaGeografica, Provincia, \
                    Pais, Clasificacion, Campaña, Frecuencia, Nima, \
                    ContratoFirmado, Cliente


@admin.register(Frecuencia)
class FrecuenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(Nima)
class NimaAdmin(admin.ModelAdmin):
    pass


@admin.register(ContratoFirmado)
class ContratoFirmadoAdmin(admin.ModelAdmin):
    pass
                    
                    
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    pass


@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Campaña)
class CampañaAdmin(admin.ModelAdmin):
    pass
                    
                    
@admin.register(Poblacion)
class PoblacionAdmin(admin.ModelAdmin):
    pass


@admin.register(ZonaGeografica)
class ZonaGeograficaAdmin(admin.ModelAdmin):
    pass


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    pass
                    
                    
@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    pass


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass


@admin.register(CpZip)
class CpZipAdmin(admin.ModelAdmin):
    pass
                    
                    
@admin.register(PrincipalCIF)
class PrincipalCIFAdmin(admin.ModelAdmin):
    pass


@admin.register(NombreRazonSocial)
class NombreRazonSocialAdmin(admin.ModelAdmin):
    pass


@admin.register(TarifaAsignada)
class TarifaAsignadaAdmin(admin.ModelAdmin):
    pass


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    change_list_template = "client/client_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = io.TextIOWrapper(request.FILES["csv_file"].file, encoding='utf-8')
            reader = csv.reader(csv_file)
            
            counter = 0
            for row in reader:
                if counter == 0:  #  They are the HEADERS
                    counter += 1
                    continue
                
                cifrc = row[1].lower()
                _cif_principal = row[2].lower()
                sucursal = row[3].lower()
                _nombre_razon_social = row[4].lower()
                _tarifa_asignada = row[5].lower()
                _tipo = row[6].lower()
                _perfil = row[7].lower()
                direccion = row[8].lower()
                _cp_zip = row[9].lower()
                _poblacion = row[10].lower()
                _zona_geografica = row[11].lower()
                _provincia = row[12].lower()
                _pais = row[13].lower()
                email = row[14].lower()
                email_respaldo = row[15].lower()
                telefono = row[16].lower()
                _clasificacion = row[17].lower()
                persona_contacto = row[18].lower()
                horario_recogida = row[19].lower()
                _campaña = row[20].lower()
                _frecuencia = row[21].lower()
                fecha_ingreso = row[22].lower()
                _nima = row[23].lower()
                numero_cuenta = row[24].lower()
                proximo_aviso = row[25].lower()
                num_ct1 = row[26].lower()
                _contrato_firmado = row[27].lower()
                cnae = row[28].lower()
                mini_broker = row[29].lower()
                nro_productor = row[30].lower()
                
                cif_principal, _ = PrincipalCIF.objects.get_or_create(nombre=_cif_principal)
                nombre_razon_social, _ = NombreRazonSocial.objects.get_or_create(nombre=_nombre_razon_social)
                tarifa_asignada, _ = TarifaAsignada.objects.get_or_create(nombre=_tarifa_asignada)
                tipo, _ = Tipo.objects.get_or_create(nombre=_tipo)
                perfil, _ = Perfil.objects.get_or_create(nombre=_perfil)
                cp_zip, _ = CpZip.objects.get_or_create(nombre=_cp_zip)
                poblacion, _ = Poblacion.objects.get_or_create(nombre=_poblacion)
                zona_geografica, _ = ZonaGeografica.objects.get_or_create(nombre=_zona_geografica)
                provincia, _ = Provincia.objects.get_or_create(nombre=_provincia)
                pais, _ = Pais.objects.get_or_create(nombre=_pais)
                try:
                    clasificacion, _ = Clasificacion.objects.get_or_create(nombre=_clasificacion)
                except Exception as e:
                    import pdb; pdb.set_trace()
                campaña, _ = Campaña.objects.get_or_create(nombre=_campaña)
                frecuencia, _ = Frecuencia.objects.get_or_create(nombre=_frecuencia)
                nima, _ = Nima.objects.get_or_create(nombre=_nima)
                contrato_firmado, _ = ContratoFirmado.objects.get_or_create(nombre=_contrato_firmado)
                
                cliente, _ = Cliente.objects.get_or_create(
                    cifrc=cifrc,
                    sucursal=sucursal,
                    direccion=direccion,
                    cif_principal=cif_principal,
                    email=email,
                    telefono=telefono,
                    persona_contacto=persona_contacto,
                    horario_recogida=horario_recogida,
                    fecha_ingreso=fecha_ingreso,
                    numero_cuenta=numero_cuenta,
                    proximo_aviso=proximo_aviso,
                    num_ct1=num_ct1,
                    cnae=cnae,
                    nro_productor=nro_productor,
                    mini_broker=mini_broker,
                    email_respaldo=email_respaldo,
                    nombre_razon_social=nombre_razon_social,
                    tarifa_asignada=tarifa_asignada,
                    tipo=tipo,
                    perfil=perfil,
                    cp_zip=cp_zip,
                    poblacion=poblacion,
                    zona_geografica=zona_geografica,
                    provincia=provincia,
                    pais=pais,
                    clasificacion=clasificacion,
                    campaña=campaña,
                    frecuencia=frecuencia,
                    nima=nima,
                    contrato_firmado=contrato_firmado
                )
                
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "custom/csv_form.html", payload
        )