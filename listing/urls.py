from django.urls import path
from .views import listingview



urlpatterns = [
    path('listing/', listingview, name='listing'),
]
