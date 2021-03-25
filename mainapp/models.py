from django.db import models
from django.contrib.auth.models import User


class OurMembers3 (models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, help_text='Please select from the list')
    EXPERTISES = (
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend Developer', 'Backend Developer'),
        ('Full Stack Developer', 'Full Stack Developer'),
    )
    expertise = models.CharField(max_length=100, choices=EXPERTISES)
    ekleme_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.member)

class OurCustomers2 (models.Model):
    customer_name = models.CharField(max_length=250)
    customer_surname = models.CharField(max_length=250)
    customer_email = models.CharField(max_length=250)
    customer_website = models.CharField(max_length=250)
    customer_phone = models.CharField(max_length=15)
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer_name)