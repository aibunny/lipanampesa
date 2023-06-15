from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from datetime import datetime
import base64
import requests
import os

load_dotenv()


def generate_base64_password():
    '''
    Uses code, passkey and timestamp to generate a base64 encoded password
    '''
    code = os.getenv("BusinessShortCode")
    passkey = os.getenv("PassKey")
    #format date to Ymdhms no spaces 
    time_stamp = datetime.now().strftime("%Y%m%d%H%I%S")
    data_to_encode = code + passkey + time_stamp
    encoded_data = base64.b64encode(data_to_encode.encode())
    password = encoded_data.decode('utf-8')
    '''
    Return timestamp and password
    '''
    return time_stamp,password
    
def generate_access_token():
    '''
    Function generates access token
    '''
    consumer_secret = os.getenv("CONSUMER_SECRET")
    consumer_key = os.getenv("CONSUMER_KEY")
    api_URL = ("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials")
    
    #request access_token from safaricom sandbox
    response = requests.get(api_URL,auth=HTTPBasicAuth(consumer_key,consumer_secret))
    #returns this {'access_token': '0RxdwuGHAGcDokGQKBB7mp****0E', 'expires_in': '3599'}
    json_response = response.json()
    Access_Token = json_response['access_token']
    
    return Access_Token 

   
    