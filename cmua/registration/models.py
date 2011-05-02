from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    state = models.CharField(max_length=1024)
    zip = models.CharField(max_length=1024)
    phone1 = models.CharField(max_length=1024)
    phone2 = models.CharField(max_length=1024)
    dob = models.CharField(max_length=1024)
    gender = models.CharField(max_length=1024)
    mailing_address = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    rating = models.CharField(max_length=1024)
    club_experience = models.CharField(max_length=1024)
    baggage = models.CharField(max_length=1024)
    league = models.CharField(max_length=1024)
    last_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'register'
