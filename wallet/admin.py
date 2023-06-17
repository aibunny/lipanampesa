from django.contrib import admin
from . models import LipaNaMpesaTransactions, C2BPayments
# Register your models here.

admin.site.register(LipaNaMpesaTransactions)
admin.site.register(C2BPayments)