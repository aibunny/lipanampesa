from django.contrib import admin
from . models import LipaNaMpesaTransactions, C2BPayments
# Register your models here.


class LNMTransactionsList(admin.ModelAdmin):
    list_display= ("PhoneNumber","Amount","MpesaReceiptNumber","TransactionDate")

class C2BTransactionsList(admin.ModelAdmin):
    list_display= ("MSISDN","TransAmount","TransID","TransTime","OrgAccountBalance")    
    


admin.site.register(LipaNaMpesaTransactions,LNMTransactionsList)
admin.site.register(C2BPayments,C2BTransactionsList)
