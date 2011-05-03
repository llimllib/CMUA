from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=1024, verbose_name="First Name")
    last_name = models.CharField(max_length=1024, verbose_name="Last Name")
    nickname = models.CharField(max_length=1024, verbose_name="Nickname", null=True, blank=True)
    addressline1 = models.CharField(max_length=1024, verbose_name="Address Line 1")
    addressline2 = models.CharField(max_length=1024, verbose_name="Address Line 2", null=True, blank=True)
    city = models.CharField(max_length=1024)
    state = models.CharField(max_length=1024)
    zip = models.CharField(max_length=1024, verbose_name="Zip Code")
    phone1 = models.CharField(max_length=1024, verbose_name="Home Phone", null=True, blank=True)
    phone2 = models.CharField(max_length=1024, verbose_name="Cell Phone", null=True, blank=True)
    phone3 = models.CharField(max_length=1024, verbose_name="Work Phone", null=True, blank=True)
    dob = models.DateField(verbose_name="Date of Birth (mm/dd/yy)")

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    email_address = models.CharField(max_length=1024)

    CATEGORY_CHOICES = (
        ('1', 'Novice Player'),
        ('2', 'Pickup/Organized League Player'),
        ('3', 'Experienced Organized League Player'),
        ('4', 'Experienced Club Player (8 tournament minimum)'),
        ('5', 'Franchise Club Player'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name="Categorize Yourself")

    club_experience = models.CharField(max_length=1024, verbose_name="Last Team I Played For", null=True, blank=True)
    monday_league = models.BooleanField(verbose_name="Monday Night Co-ed League")
    wednesday_league = models.BooleanField(verbose_name="Wednesday Night Co-ed League")

    monday_chum_request = models.CharField(max_length=1024, verbose_name="Monday Night Chum Request", null=True, blank=True)
    wednesday_chum_request = models.CharField(max_length=1024, verbose_name="Wednesday Night Chum Request", null=True, blank=True)

    unable_to_play = models.TextField(verbose_name="Exceptions: Dates you'll be late or unable to play", null=True, blank=True)

    i_agree_to_terms = models.BooleanField(verbose_name="I HEREBY AFFIRM THAT I AM EIGHTEEN (18) YEARS OF AGE OR OLDER, I HAVE READ THIS DOCUMENT AND I UNDERSTAND ITS CONTENTS.")

    last_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
