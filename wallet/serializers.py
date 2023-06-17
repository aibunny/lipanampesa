from rest_framework import serializers
from . models import LipaNaMpesaTransactions, C2BPayments


class ViaLipaNaMpesa(serializers.Serializer):
   class Meta:
       models = LipaNaMpesaTransactions
       fields = '__all__'
       


class C2BSerializer(serializers.Serializer):
   class Meta:
       model = C2BPayments
       fields = '__all__'