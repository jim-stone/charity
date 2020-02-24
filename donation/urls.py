from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView

from .views import LandingPage, Login, Register, AddDonation

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
    path('index/', LandingPage.as_view()),
    path('donate/', AddDonation.as_view(), name='donate'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
