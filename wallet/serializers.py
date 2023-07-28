from rest_framework import serializers
from . models import LipaNaMpesaTransactions, C2BPayments


class ViaLipaNaMpesa(serializers.ModelSerializer):
   class Meta:
       models = LipaNaMpesaTransactions
       fields = '__all__'
       


class C2BSerializer(serializers.Serializer):
   class Meta:
       model = C2BPayments
       fields = ('TransactionType', 
                'TransID',
                'TransTime',
                'TransAmount', 
                'BusinessShortCode',
                'BillRefNumber', 
                'InvoiceNumber', 
                'OrgAccountBalance', 
                'ThirdPartyTransID', 
                'MSISDN', 
                'FirstName', 
                'MiddleName',
                'LastName',
                )