from rest_framework import serializers
from .models import Duenos

class DuenosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duenos
        fields = '__all__'
        # fields = ['nombre', 'Dirreccion']