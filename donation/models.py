from django.db import models
from django.contrib.auth.models import User


INSTITUTIONS = [
    (0, 'fundacja'),
    (1, 'organizacja pozarządowa'),
    (2, 'zbiórka lokalna')
]


class Category(models.Model):
    name = models.CharField(max_length=250)


class Institution(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    kind = models.PositiveSmallIntegerField(choices=INSTITUTIONS, default=0)
    categories = models.ManyToManyField(Category, related_name='institutions')


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, related_name='donations',
                                    on_delete=models.PROTECT)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=500)
    user = models.ForeignKey(to=User, related_name='donations', null=True,
                             default=None, on_delete=models.CASCADE)

