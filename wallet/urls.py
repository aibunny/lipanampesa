from django.urls import path
from . views import CallBackAPIView,C2BValidationAPIView, C2BConfirmationAPIView


urlpatterns = [
    path('callback/',CallBackAPIView.as_view(),name ='callback'),
    path('validation/',C2BValidationAPIView.as_view(),name ='validation'),
    path('confirmation/',C2BConfirmationAPIView.as_view(),name ='confirmation'),
]
