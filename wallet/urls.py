from django.urls import path
from . views import LNMView
urlpatterns = [
    path('callback/',LNMView.as_view(),name ='callback'),
]
