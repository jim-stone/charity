from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict

from .models import Institution, Donation, Category
from .forms import RegistrationForm


class LandingPage(View):

    def get(self, request):

        institutions_count = Donation.objects.values(
                             'institution').distinct().count()
        donated_pieces = Donation.objects.aggregate(
                         Sum('quantity'))['quantity__sum']
        ctx = {}
        ctx['institutions_count'] = institutions_count
        ctx['donated_pieces'] = donated_pieces
        ctx['foundations'] = Institution.objects.filter(kind=0)
        ctx['ngos'] = Institution.objects.filter(kind=1)
        ctx['locals'] = Institution.objects.filter(kind=2)

        return render(request, 'index.html', ctx)


class AddDonation(LoginRequiredMixin, View):

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()

        institutions_list = []
        for inst in institutions:
            inst_dict = model_to_dict(inst)
            inst_dict['categories'] = inst.get_categories_list()
            print(inst_dict)
            institutions_list.append(inst_dict)

        ctx = {}
        ctx['categories'] = categories
        ctx['institutions'] = institutions_list
        return render(request, 'form.html', ctx)


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            try:
                login(request, user)
                return redirect('index')
            except Exception:
                print(Exception)
        else:
            return redirect('register')


class Register(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/login/'


def logout_view(request):
    logout(request)
    return render(request, 'login')