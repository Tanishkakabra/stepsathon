from rest_framework import serializers
from steps.models import Event
from cryptography import fernet

class EventsMiniSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'thumb_image', 'location', 'datetime']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     if instance.encryption_key is not None:

