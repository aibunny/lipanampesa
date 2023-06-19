import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from requests.auth import HTTPBasicAuth
from utils import generate_base64_password,generate_access_token
import base64

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
        "PartyA":os.getenv("PartyA"),
        "PartyB":os.getenv("BusinessShortCode"),
        "PhoneNumber":"254759008773",
        "CallBackURL":os.getenv("CALLBACKURL"),
        "AccountReference":"12345678",
        "TransactionDesc":"Pay Something",   
        
    }

    response = requests.post(api_url, json = payload, headers = headers)

    print(response.text)

LipaNaMpesaOnline()
