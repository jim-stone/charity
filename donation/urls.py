from django.urls import path
from .views import LandingPage, Login, Register, AddDonation

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
    path('index/', LandingPage.as_view()),
    path('donate/', AddDonation.as_view(), name='donate'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register')
]
