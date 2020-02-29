from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LandingPage, Login, Register, AddDonation,\
    FormConfirmation, UserProfileView, UserDonationsView

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
    path('index/', LandingPage.as_view()),
    path('donate/', AddDonation.as_view(), name='donate'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('user/donations/<int:pk>/', UserDonationsView.as_view(),
         name='my_donations'),
    path('donate-confirmation/', FormConfirmation.as_view(),
         name='confirmation')
]
