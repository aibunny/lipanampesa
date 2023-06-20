
from utils import generate_base64_password,generate_access_token
from wallet.models import successful_stk_pushes 
from rest_framework.response import Response
from dotenv import load_dotenv
import requests
import os

load_dotenv()





def LipaNaMpesaOnline():
    
    time_stamp, password =generate_base64_password()
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" %access_token}
    payload = {
        "BusinessShortCode":os.getenv("BusinessShortCode"),
        "Password":password,
        "Timestamp":time_stamp,
        "TransactionType":"CustomerPayBillOnline",
        "Amount":"1",
        "PartyA":"254759008773",
        "PartyB":os.getenv("BusinessShortCode"),
        "PhoneNumber":"254759008773",
        "CallBackURL":os.getenv("CALLBACKURL"),
        "AccountReference":"12345678",
        "TransactionDesc":"Pay Something",   
        
    }

    response = requests.post(api_url, json = payload, headers = headers)
    json_response = response.text
    
    print(json_response)
    
    if json_response["ResponseCode"] == 0:
        CheckoutRequestID = json_response['CheckoutRequestID']
        ResponseCode = json_response["ResponseCode"]
        MerchantRequestID = json_response["MerchantRequestID"]
        
        my_model = successful_stk_pushes.objects.create(CheckoutRequestID = CheckoutRequestID,
                                                        MerchantRequestID= MerchantRequestID,
                                                        ResponseCode=ResponseCode 
                                                        )
        my_model.save()
    else:
        Response({'message':"Error sending STK Push"})
    

LipaNaMpesaOnline()
