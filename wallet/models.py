from django.db import models

# Create your models here.

class successful_stk_pushes(models.Model):
    MerchantRequestID = models.CharField(max_length=25)
    CheckoutRequestID = models.CharField(max_length=25)
    ResponseCode = models.CharField(max_length=25)
    
    

class LipaNaMpesaTransactions(models.Model):
    MerchantRequestID = models.CharField(max_length=50)
    CheckOutRequestID = models.CharField(max_length=50)
    ResultCode = models.IntegerField()
    ResultDesc = models.CharField(max_length=150)
    Amount = models.FloatField()
    MpesaReceiptNumber = models.TextField(max_length=15)
    TransactionDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=13)


class C2BPayments(models.Model):
    TransactionType = models.CharField(max_length=15)
    TransID = models.CharField(max_length=12)
    TransTime = models.CharField(max_length=14)
    TransAmount = models.CharField(max_length=12)
    BusinessShortCode = models.CharField(max_length=6,blank= True, null = True) 
    BillRefNumber = models.CharField(max_length=20,blank= True, null = True)
    InvoiceNumber = models.CharField(max_length=20,blank= True, null = True)
    OrgAccountBalance = models.CharField(max_length=12,blank= True, null = True)
    ThirdPartyTransID = models.CharField(max_length=20,blank= True, null = True) 
    MSISDN = models.CharField(max_length = 12,blank= True, null = True)
    FirstName = models.CharField(max_length=25,blank= True, null = True)
    MiddleName = models.CharField(max_length=25,blank= True, null = True)
    LastName = models.CharField(max_length=25,blank= True, null = True)
    
