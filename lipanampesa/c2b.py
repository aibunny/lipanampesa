from datetime import datetime
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from utils import generate_base64_password, generate_access_token
import base64
import requests
import os

load_dotenv()


time_stamp, password = generate_base64_password()

# Runs once to allow safaricom register the urls
def register_url():
    '''
    This registers the callback and validation urls
    '''
    
    api_url= "https://sandbox.safaricom.co.ke/oauth/v1/registerurl"
    headers = {"Authorization":"Bearer %s" % access_token}
    access_token = generate_access_token()
    requests = {
        "ShortCode":os.getenv("ShortCode"),
        "ResponseType":os.getenv("ResponseType"),
        "ConfirmationURL":os.getenv("ConfirmationURL"),
        "ValidationURL":os.getenv("ValidationURL"),
        }
    response = response.post(api_url, json = request, headers = headers)
    print (response.text)

def simulate_C2b_Transaction():
    api_url= "https://sandbox.safaricom.co.ke/oauth/v1/registerurl"
    headers = {"Authorization":"Bearer %s" % access_token}
    
    requests = {
        "ShortCode":os.getenv("ShortCode"),
        "CommandId":"CustomerPayBillOnline",
        "Amount":"2",
        "Msisdn":"",
        }
    response = response.post(api_url, json = request, headers = headers)
    print (response.text) 







access_token = Access_Token
api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
headers = {"Authorization": "Bearer %s" %access_token}
request = {
    "BusinessShortCode":"",
    "Password":"bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    "Timestamp":time_stamp,
    "TransactionType":"",
    "Amount":"5",
    "PartyA":"600980",
    "PartyB":"600000",
    "PhoneNumber":"254759008773",
    "CallBackURL":"",
    "AccountReference":"",
    "TransactionDesc":"",   
    
}

response = requests.post(api_url, json=request, headers = headers)

print(response.text)

