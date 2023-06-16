from rest_framework import serializers
from . models import LipaNaMpesaTransactions


class ViaLipaNaMpesa(serializers.Serializer):
   class Meta:
       models = LipaNaMpesaTransactions
       fields = '__all__'
       
       