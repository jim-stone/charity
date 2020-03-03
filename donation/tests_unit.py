from django.test import TestCase
from .models import Institution, Category
from .forms import RegistrationForm


# views

class LandingPageTest(TestCase):

    def test_00_landing_page_exists(self):
        response = self.client.get(path='')
        header = bytes("Zacznij pomagać", encoding='utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='index.html')
        self.assertIn(header, response.content)


# models

class InstitutionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        fundacja = Institution.objects.create(
                   name="Fundacja Dzieciom",
                   description="Uczciwy i wiarygodny NGO pełen dedykowanych\
                   i empatycznych pracowników",
                   kind=0)
        fundacja.categories.add(Category.objects.create(name="pieniądze"))
        fundacja.categories.add(Category.objects.create(
            name="papiery wartościowe"))
        fundacja.categories.add(Category.objects.create(name="wolontariat"))

    def test_00_get_categories_string_returns_correctly(self):
        obj = Institution.objects.get(pk=1)
        categories_string = "pieniądze, papiery wartościowe, wolontariat"
        self.assertEqual(obj.get_categories_string(), categories_string)


# forms

class RegistrationFormTest(TestCase):

    def test_valid_form(self):
        data = {'first_name': 'guido',
                'last_name': 'VR',
                'email': 'guido@guido.pl',
                'password1': "Abracadabra1!",
                'password2': "Abracadabra1!"}
        form = RegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'first_name': 'guido',
                'last_name': 'VR',
                'email': 'guido@guido.pl',
                'password1': "Abracadabra1",
                'password2': "Abracadabra1!!!"}
        form = RegistrationForm(data)
        self.assertFalse(form.is_valid())
