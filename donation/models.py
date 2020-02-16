from django.db import models


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
    categories = models.ManyToManyField(Category)
