from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from . models import LipaNaMpesaTransactions
from . serializers import ViaLipaNaMpesa


from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class LNMView(CreateAPIView):
    serializer_class = ViaLipaNaMpesa
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        mpesa_response = request.data
        
        '''
        SAMPLE REQUEST
        {'Body': {'stkCallback':   
            {'MerchantRequestID': '1452-135513598-1', 
            'CheckoutRequestID': 'ws_CO_15062023192557849759008773', 
            'ResultCode': 0,
            'ResultDesc': 'The service request is processed successfully.',
            'CallbackMetadata':   
            {'Item':
                [{'Name': 'Amount', 'Value': 5.0}, 
                {'Name': 'MpesaReceiptNumber', 'Value': 'RFF65H3JY8'}, 
                {'Name': 'Balance'},
                {'Name': 'TransactionDate', 'Value': 20230615192452}, 
                {'Name': 'PhoneNumber', 'Value': 254759008773}]
                }
            }
            }
        }
        '''

        MerchantRequestID = mpesa_response['Body']['stkCallback']['MerchantRequestID']
        CheckoutRequestID = mpesa_response['Body']['stkCallback']['CheckoutRequestID']
        ResultCode = mpesa_response['Body']['stkCallback']['ResultCode']
        ResultDesc = mpesa_response['Body']['stkCallback']['ResultDesc']

        metadata = mpesa_response['Body']['stkCallback']['CallbackMetadata']['Item']
        Amount = next((item['Value'] for item in metadata if item['Name'] == 'Amount'), None)
        MpesaReceiptNumber = next((item['Value'] for item in metadata if item['Name'] == 'MpesaReceiptNumber'), None)
        transaction_date = next((item['Value'] for item in metadata if item['Name'] == 'TransactionDate'), None)
        TransactionDate = datetime.strptime(str(transaction_date), "%Y%m%d%H%M%S")
        PhoneNumber = next((item['Value'] for item in metadata if item['Name'] == 'PhoneNumber'), None)

        
        
        my_model = LipaNaMpesaTransactions.objects.create(
            MerchantRequestID =MerchantRequestID,
            CheckOutRequestID = CheckoutRequestID,
            ResultCode = ResultCode,
            ResultDesc = ResultDesc,
            Amount = Amount,
            TransactionDate = TransactionDate,
            PhoneNumber = PhoneNumber,
            MpesaReceiptNumber = MpesaReceiptNumber
        )
        
        my_model.save()
        
        return Response(status=201)

        