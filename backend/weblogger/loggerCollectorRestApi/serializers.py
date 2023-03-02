
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import ValidationError


from .models import Device,Log

class DeviceSerializer(ModelSerializer):

    class Meta:
        model = Device
        fields = ['id','ipaddress','datetime']

class LogSerializer(ModelSerializer):


    device = serializers.CharField()

    class Meta:
        model = Log
        fields = ['id','device','content','datetime']


    def create(self, validated_data:dict):

        device_ipaddress = validated_data.pop('device')

        founded_device = Device.objects.filter(
            ipaddress=device_ipaddress
        )
        device = None
        if founded_device.count()==0:
            device = Device.objects.create(
                ipaddress=device_ipaddress
            )
        else:
            device= founded_device.first()

        return Log.objects.create(
            **validated_data,
            device = device
        )


    #return ExampleModel.objects.create(**validated_data)
