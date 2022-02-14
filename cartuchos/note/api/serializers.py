from rest_framework import serializers
from django.contrib.auth import get_user_model


from clients.models import Cliente
from note.models import Notes, SelectedCartridges
from cartridge.models import Cartridges

User = get_user_model()


class CartridgeSerializer(serializers.Serializer):
    cartridge = serializers.IntegerField(required=True)
    quantity = serializers.FloatField(required=True)
    weight = serializers.FloatField(required=True)


class CreateNoteModelSerializer(serializers.ModelSerializer):
    cartridges = CartridgeSerializer(many=True, required=True)
    note = serializers.CharField(required=False, allow_blank=True)
    code = serializers.CharField(required=False, allow_blank=True)
    box_weight = serializers.FloatField(required=True)
    total_weight =  serializers.FloatField(required=True)
    laser_weight = serializers.FloatField(required=True)
    laser_weight_residual = serializers.FloatField(required=True)
    laser_percent = serializers.FloatField(required=True)
    inkjet_weight = serializers.FloatField(required=True)
    inkjet_weight_residual = serializers.FloatField(required=True)
    inkjet_percent = serializers.FloatField(required=True)
    total_items = serializers.IntegerField(required=True)
    salesman = serializers.IntegerField(required=True)
    client = serializers.IntegerField(required=True)
    
    class Meta:
        model = Notes
        fields = '__all__'
        
    def validate_salesman(self, data):
        try:
            salesman = User.objects.get(pk=data)
        except User.DoesNotExist:
            raise serializers.ValidationError(f'A Salesman with pk: {data} does not exists.')
        return salesman
        
    def validate_client(self, data):
        try:
            client = Cliente.objects.get(pk=data)
        except Cliente.DoesNotExist:
            raise serializers.ValidationError(f'A Cliente with pk: {data} does not exists.')
        return client
        
    def validate_cartridges(self, data):
        cartridge_list = []
        for item in data:
            try:
                cartridge = Cartridges.objects.get(pk=item['cartridge'])
                selected = SelectedCartridges.objects.create(
                    selected=cartridge,
                    quantity=item['quantity'],
                    weight=item['weight']
                )
                cartridge_list.append(selected)
            except User.DoesNotExist:
                raise serializers.ValidationError(f'A Cartridge with pk: {item["id"]} does not exists.')
        return cartridge_list

    def create(self, validated_data):
        selected_cartridges = validated_data.pop('cartridges')
        instance = super().create(validated_data)
        for selected in selected_cartridges:
            selected.note = instance
            selected.save()
        return instance