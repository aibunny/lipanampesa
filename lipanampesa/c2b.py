from datetime import datetime
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from utils import generate_base64_password, generate_access_token
import base64
import requests
import os

load_dotenv()


time_stamp, password = generate_base64_password()
print(time_stamp,password)
# Runs once to allow safaricom register the urls
def register_url():
    '''
    This registers the callback and validation urls
    '''
    
    api_url= "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    access_token = generate_access_token()
    headers = {"Authorization":"Bearer %s" % access_token}
    
    request= {
        "ShortCode":os.getenv("ShortCode"),
        "ResponseType":"Completed",
        "ConfirmationURL":os.getenv("ConfirmationURL"),
        "ValidationURL":os.getenv("ValidationURL"),
        }
    response = requests.post(api_url, json = request, headers = headers)
    print (response.text)
    
    
#register_url()
  

def simulate_C2b_Transaction():
    access_token = generate_access_token()
    api_url= "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization":"Bearer %s" % access_token}
    
    payload = {
        "ShortCode":os.getenv("ShortCode"),
        "CommandID":"CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn":"254705912645",
        "BillRefNumber":"12345678"
        }
    response = requests.post(api_url, json = payload, headers = headers)
    print (response.text) 



simulate_C2b_Transaction()




