from faker import Faker
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from .db_populate import populate_categories, populate_institutions
from .models import Donation, Institution


FAKE = Faker('pl_PL')


class LandingPageTest(StaticLiveServerTestCase):

    """
    Jako gość/użytkownik mogę na stronie głównej zobaczyć statystyki
    dotyczące liczby oddanych worków z rzeczami oraz liczby
    wspartych instytucji.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        populate_categories()
        populate_institutions()
        Donation.objects.create(
            quantity=7,
            institution=Institution.objects.get(pk=10),
            address=FAKE.street_address(),
            city=FAKE.city(),
            zip_code=FAKE.postcode(),
            pick_up_date=FAKE.date_object(),
            pick_up_time=FAKE.time_object(),
            pick_up_comment=FAKE.text(max_nb_chars=100)
        )
        Donation.objects.create(
            quantity=7,
            institution=Institution.objects.get(pk=12),
            address=FAKE.street_address(),
            city=FAKE.city(),
            zip_code=FAKE.postcode(),
            pick_up_date=FAKE.date_object(),
            pick_up_time=FAKE.time_object(),
            pick_up_comment=FAKE.text(max_nb_chars=100)
        )
        Donation.objects.create(
            quantity=6,
            institution=Institution.objects.get(pk=12),
            address=FAKE.street_address(),
            city=FAKE.city(),
            zip_code=FAKE.postcode(),
            pick_up_date=FAKE.date_object(),
            pick_up_time=FAKE.time_object(),
            pick_up_comment=FAKE.text(max_nb_chars=100)
        )
        cls.driver.get(cls.live_server_url + '/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_01_page_shows_correct_quantity_statistics(self):
        quantity = self.driver.find_elements(
            By.CLASS_NAME, 'stats--item')[0].find_element(
            By.TAG_NAME, 'em').text
        self.assertEqual(quantity, '20')   # 7 + 7 + 6

    def test_02_page_shows_correct_institution_statistics(self):
        institutions = self.driver.find_elements(
            By.CLASS_NAME, 'stats--item')[1].find_element(
            By.TAG_NAME, 'em').text
        self.assertEqual(institutions, '2')
        # test obejmuje 3 donacje ale 2 unikalne instytucje
