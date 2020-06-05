from django.urls import path
from .views import indexPageview



urlpatterns = [
    path('', indexPageview, name='index'),
]
