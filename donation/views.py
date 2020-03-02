from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView
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


class AddDonation(LoginRequiredMixin, CreateView):
    model = Donation
    fields = ['quantity', 'categories', 'institution', 'address', 'phone_number',
              'city', 'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment']
    template_name = 'form.html'
    success_url = '/donate-confirmation/'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        institutions_list = []
        for inst in institutions:
            inst_dict = model_to_dict(inst)
            inst_dict['categories'] = inst.get_categories_list()
            institutions_list.append(inst_dict)
        kwargs['categories'] = categories
        kwargs['institutions'] = institutions_list
        print(institutions_list[0])
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        donation = form.save(commit=False)
        donation.user = self.request.user
        donation.save()
        # form.save_m2m()
        # return redirect('/donate-confirmation/')
        return super().form_valid(form)


class FormConfirmation(View):

    def get(self, request):
        return render(request, 'form-confirmation.html')


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
                pass
        else:
            return redirect('register')


class Register(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/login/'


def logout_view(request):
    logout(request)
    return render(request, 'login')


class UserProfileView(View):

    def get(self, request, pk):
        return render(request, 'profile.html')


class UserDonationsView(ListView):
    template_name = 'my_donations.html'
    context_object_name = 'donations'

    def get_queryset(self):
        return Donation.objects.filter(user=self.request.user)




