from rest_framework import serializers
from .models import Soildata

class SoildataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soildata
        fields = ["id", "ec", "ph", "type"]
