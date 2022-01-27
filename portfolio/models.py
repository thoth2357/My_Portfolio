from pyexpat import model
from turtle import color
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Portfolio(models.Model):
    pass
    # User_info = models.OneToOneField("portfolio.User_info", verbose_name=_("user_info"), on_delete=models.CASCADE)
    # Personlization = models.OneToOneField("portfolio.Personlization", verbose_name=_("personalization"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Portfolio'
class User_info(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE, null=True)
    Fullname = models.CharField(_("FullName"), max_length=50, help_text='Full name to be displayed on portfolio')
    Country = CountryField(help_text="Country of Residence")
    City = models.CharField(_('City_Name'), max_length=50, help_text="name of city that would be displayed on front page")
    Phone_number = PhoneNumberField(_("Phone Number"), help_text="Phone number to display on home page")
    class Meta:
        verbose_name = ("User_Information")
        verbose_name_plural = ("User_Information")

    def __str__(self):
        return self.Fullname

class Personlization(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE, null=True)
    CHOICES = (
        ('YELLOW', 'YELLOW'),
        ('RED', 'RED'),
        ('BLUE', 'BLUE'),
        ('ORANGE', 'ORANGE')
    )

    Color_theme = models.CharField(_("Color Theme for Portfolio Colors"),choices=CHOICES, max_length=50)
    class Meta:
        verbose_name = ("Personalization")
        verbose_name_plural = ("Personalization")

    def __str__(self):
        return self.Color_theme

    


