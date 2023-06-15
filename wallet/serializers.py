from rest_framework import serializers
from models import LipaNaMpesa


class ViaLipaNaMpesa(serializers.Serializer):
   class Meta:
       models = LipaNaMpesa
       fields = '__all__'
       
       