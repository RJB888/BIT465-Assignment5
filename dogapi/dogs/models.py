from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Breed(models.Model):
    SIZE_OPTIONS = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    )
    name = models.CharField(max_length=100, blank=True, default="")
    size = models.CharField(max_length=1, choices=SIZE_OPTIONS)
    friendliness = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    trainability = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    sheddingamount = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    exerciseneeds = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Dog(models.Model):
    GENDER_OPTIONS = (
        ("M", "Male"),
        ("F", "Female")
    )
    name = models.CharField(max_length=50, blank=True, default="Spot")
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, related_name='dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    color = models.CharField(max_length=100, blank=True, default="")
    favorite_food = models.CharField(max_length=100, blank=True, default="")
    favorite_toy = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
