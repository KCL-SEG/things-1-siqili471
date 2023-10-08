from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(
        blank=False,
        max_length=30,
        unique=True,
        help_text="A short string that identifies a thing."
    )
    description = models.CharField(
        blank=True,
        max_length=120,
        unique=False,
        help_text="A slightly longer string that describes a thing."
    )
    quantity = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0,"cannot less than 0"),
            MaxValueValidator(100, "Quantity cannot be more than 100.")
        ],
        help_text="An integer value between 0 and 100 (inclusive) representing the quantity of items."
    )
