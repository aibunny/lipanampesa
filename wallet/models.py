from django.db import models

# Create your models here.

class LipaNaMpesaTransactions(models.Model):
    MerchantRequestID = models.CharField(max_length=50)
    CheckOutRequestID = models.CharField(max_length=50)
    ResultCode = models.IntegerField()
    ResultDesc = models.CharField(max_length=150)
    Amount = models.FloatField()
    MpesaReceiptNumber = models.TextField(max_length=15)
    TransactionDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=13)
    