from rest_framework import serializers

from cartridge.models import Cartridges


class CartridgesSerializer(serializers.ModelSerializer):
    familia = serializers.SerializerMethodField()
    subfamilia = serializers.SerializerMethodField()
    referencia = serializers.SerializerMethodField()
    marca = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    peso = serializers.SerializerMethodField()
    codigo = serializers.SerializerMethodField()
    modelo = serializers.SerializerMethodField()

    class Meta:
        model = Cartridges
        fields = [
            "id",
            "codigo",
            "peso",
            "color",
            "familia",
            "subfamilia",
            "referencia",
            "marca",
            "modelo"
        ]
        
    def get_familia(self, obj):
        _return = None
        if hasattr(obj, 'family'):
            _return = obj.family.name
        return _return
        
    def get_subfamilia(self, obj):
        _return = None
        if hasattr(obj, 'family_intern'):
            _return = obj.family_intern.name
        return _return
        
    def get_marca(self, obj):
        _return = None
        if hasattr(obj, 'manufacturer'):
            _return = obj.manufacturer.name
        return _return
        
    def get_color(self, obj):
        _return = None
        if hasattr(obj, 'color'):
            _return = obj.color.name
        return _return

    def get_modelo(self, obj):
        _return = None
        if hasattr(obj, 'reference'):
            _return = obj.reference.name
        return _return
    
    def get_referencia(self, obj):
        _return = None
        if hasattr(obj, 'color'):
            _return = obj.reference_group.name
        return _return
        
    def get_codigo(self, obj):
        return  obj.code
        
    def get_peso(self, obj):
        return  obj.weitgh
        
