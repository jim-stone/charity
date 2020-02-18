from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from .models import Category, Institution, Donation


class LandingPage(View):

    def get(self, request):
        # distinct(*field) works only with postgres
        institutions_count = Donation.objects.distinct('institution').count()
        donated_pieces = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        ctx = {}
        ctx['institutions_count'] = institutions_count
        ctx['donated_pieces'] = donated_pieces
        return render(request, 'index.html', ctx)


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')
