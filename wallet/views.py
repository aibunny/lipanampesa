from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from . models import LipaNaMpesa
from . serializers import ViaLipaNaMpesa
class LNMView(CreateAPIView):
    serializer_class = ViaLipaNaMpesa
    permission_classes= [AllowAny]
    def create(self,request):
        print(request.data,"this is request.data")
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
        mpesa_response = request.data

        MerchantRequestID = mpesa_response['Body']['stkCallback']['MerchantRequestID']
        CheckoutRequestID = mpesa_response['Body']['stkCallback']['CheckoutRequestID']
        ResultCode = mpesa_response['Body']['stkCallback']['ResultCode']
        ResultDesc = mpesa_response['Body']['stkCallback']['ResultDesc']

        metadata = mpesa_response['Body']['stkCallback']['CallbackMetadata']['Item']
        Amount = next((item['Value'] for item in metadata if item['Name'] == 'Amount'), None)
        MpesaReceiptNumber = next((item['Value'] for item in metadata if item['Name'] == 'MpesaReceiptNumber'), None)
        TransactionDate = next((item['Value'] for item in metadata if item['Name'] == 'TransactionDate'), None)
        PhoneNumber = next((item['Value'] for item in metadata if item['Name'] == 'PhoneNumber'), None)

        print(MerchantRequestID, CheckoutRequestID, ResultCode, ResultDesc, Amount, MpesaReceiptNumber, TransactionDate, PhoneNumber)