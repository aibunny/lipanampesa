from django.shortcuts import render
from django.contrib.auth.models import User
from serializers import ViaLipaNaMpesa
from rest_framework.generics import CreateAPIView
from models import LipaNaMpesa
 
class LNMView(CreateAPIView):
    serializer_class = ViaLipaNaMpesa
    
    def create(self,request):
        print(request.data,"this is request.data")
