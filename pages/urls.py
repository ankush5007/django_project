from django.urls import path
from .views import homePageview,bingoPageView,dataPageView



urlpatterns = [
    path('', homePageview, name='home'),
    path('bingo/',bingoPageView,name='bingo'),
    path('data/',dataPageView,name='data'),
]
