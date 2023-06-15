from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from . models import LipaNaMpesa
from . serializers import ViaLipaNaMpesa
class LNMView(CreateAPIView):
    serializer_class = ViaLipaNaMpesa
    permission_classes= [AllowAny]
    def create(self,request):
        print(request.data,"this is request.data")
