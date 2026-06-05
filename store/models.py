from django.db import models


class Entry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    date_of_birth = models.DateField()

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)

    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True)

    postcode = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    GIFT_CARD_CHOICES = [
    ("Amazon", "Amazon"),
    ("Apple", "Apple"),
    ("Google Play", "Google Play"),
    ("PlayStation", "PlayStation"),
    ("Xbox", "Xbox"),
    ("Tesco", "Tesco"),
    ("Asos", "ASOS"),
    ("One4All", "One4All"),
    ("Paypal", "PayPal"),
]

    preferred_gift_card = models.CharField(
    max_length=50,
    choices=GIFT_CARD_CHOICES
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"