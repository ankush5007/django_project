from django.urls import path
from .views import homePageview,bingoPageView



urlpatterns = [
    path('', homePageview, name='home'),
    path('bingo/',bingoPageView,name='bingo'),
]
