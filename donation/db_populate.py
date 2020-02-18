from faker import Faker
from random import choice, sample
from .models import Category, Institution, Donation


FAKE = Faker('pl_PL')


def prepare():
    Category.objects.all().delete()
    Institution.objects.all().delete()
    Donation.objects.all().delete()


def populate_categories():
    categories = [
        'odzież', 'zabawki', 'książki', 'elektronika'
    ]
    for cat in categories:
        Category.objects.create(name=cat)


def populate_institutions():
    for i in range(20):
        cats_number = i % 4 + 1
        selected_cats = sample(list(Category.objects.all()), cats_number)
        new = Institution.objects.create(
            name=FAKE.company(),
            description=FAKE.text(max_nb_chars=500),
            kind=choice([0, 1, 2]),
        )
        new.categories.set(selected_cats)


def populate_donations():
    for i in range(40):
        cats_number = i % 4 + 1
        selected_cats = sample(list(Category.objects.all()), cats_number)
        new = Donation.objects.create(
            quantity=choice(range(3, 30)),
            institution=choice(list(Institution.objects.all())),
            address=FAKE.street_address(),
            city=FAKE.city(),
            zip_code=FAKE.postcode(),
            pick_up_date=FAKE.date_object(),
            pick_up_time=FAKE.time_object(),
            pick_up_comment=FAKE.text(max_nb_chars=100)
        )
        new.categories.set(selected_cats)


prepare()
populate_categories()
populate_institutions()
populate_donations()
