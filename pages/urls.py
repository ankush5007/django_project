from django.urls import path
from .views import homePageview,bingoPageView,dataPageView,addPageview



urlpatterns = [
    path('', homePageview, name='home'),
    path('bingo/',bingoPageView,name='bingo'),
    path('data/',dataPageView,name='data'),
    path('add/',addPageview,name='add'),

]
