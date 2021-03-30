from rest_framework import serializers
from .models import Lead

# Serializador lead
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


 