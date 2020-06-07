from django.urls import path
from .views import indexPageview,registerPageview,manage_authPageview,logoutPageview



urlpatterns = [
    path('', indexPageview, name='index'),
    path('register/',registerPageview,name='register'),
    path('login/',manage_authPageview,name = 'login'),
    path('logout/',logoutPageview,name = 'logout')
]
