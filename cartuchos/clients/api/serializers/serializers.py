from rest_framework import serializers
from cartuchos.clients.models import PrincipalCIF, NombreRazonSocial, TarifaAsignada, Tipo, \
    Perfil, CpZip, Poblacion, ZonaGeografica, Provincia, \
    Pais, Clasificacion, Campaña, Frecuencia, Nima, \
    ContratoFirmado, Cliente


class ContratoFirmadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratoFirmado
        fields = ['nombre']


class NimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nima
        fields = ['nombre']


class FrecuenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frecuencia
        fields = ['nombre']


class CampañaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaña
        fields = ['nombre']


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = ['nombre']


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre']


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['nombre']


class ZonaGeograficaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaGeografica
        fields = ['nombre']


class PoblacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poblacion
        fields = ['nombre']


class CpZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpZip
        fields = ['nombre']


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['nombre']


class NombreRazonSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = NombreRazonSocial
        fields = ['nombre']


class PrincipalCIFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalCIF
        fields = ['nombre']


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['nombre']


class TarifaAsignadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifaAsignada
        fields = ['nombre']


class ClientLargeSerializer(serializers.ModelSerializer):
    nombre_razon_social = serializers.SerializerMethodField()
    contrato_firmado = serializers.SerializerMethodField()
    clasificacion = serializers.SerializerMethodField()
    pais = serializers.SerializerMethodField()
    tarifa_asignada = serializers.SerializerMethodField()
    poblacion = serializers.SerializerMethodField()
    zona_geografica = serializers.SerializerMethodField()
    provincia = serializers.SerializerMethodField()
    
    class Meta:
        model = Cliente
        fields = [
            "id",
            "cifrc",
            "direccion",
            "telefono",
            "persona_contacto",
            "email",
            "nombre_razon_social",
            "contrato_firmado",
            "clasificacion",
            "pais",
            "tarifa_asignada",
            "poblacion",
            "zona_geografica",
            "provincia",
        ]
        
    def get_clasificacion(self, obj):
        _return = None
        if hasattr(obj, 'clasificacion'):
            _return = obj.clasificacion.nombre
        return _return

    def get_contrato_firmado(self, obj):
        _return = None
        if hasattr(obj, 'contrato_firmado'):
            _return = obj.contrato_firmado.nombre
        return _return

    def get_nombre_razon_social(self, obj):
        _return = None
        if hasattr(obj, 'nombre_razon_social'):
            _return = obj.nombre_razon_social.nombre
        return _return

    def get_pais(self, obj):
        _return = None
        if hasattr(obj, 'pais'):
            _return = obj.pais.nombre
        return _return

    def get_tarifa_asignada(self, obj):
        _return = None
        if hasattr(obj, 'tarifa_asignada'):
            _return = obj.tarifa_asignada.nombre
        return _return

    def get_poblacion(self, obj):
        _return = None
        if hasattr(obj, 'poblacion'):
            _return = obj.poblacion.nombre
        return _return

    def get_zona_geografica(self, obj):
        _return = None
        if hasattr(obj, 'zona_geografica'):
            _return = obj.zona_geografica.nombre
        return _return

    def get_provincia(self, obj):
        _return = None
        if hasattr(obj, 'provincia'):
            _return = obj.provincia.nombre
        return _return

class ClientShortSerializer(serializers.ModelSerializer):
    nombre_razon_social = serializers.SerializerMethodField()
    cifrc = serializers.SerializerMethodField()
    
    class Meta:
        model = Cliente
        fields = [
            "id",
            "cifrc",
            "nombre_razon_social",
        ]
        
    def get_nombre_razon_social(self, obj):
        _return = None
        if hasattr(obj, 'nombre_razon_social'):
            _return = obj.nombre_razon_social.nombre.upper()
        return _return
        
    def get_cifrc(self, obj):
        _return = None
        if hasattr(obj, 'cifrc'):
            _return = obj.cifrc.upper()
        return _return


class ClientAllSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = "__all__"