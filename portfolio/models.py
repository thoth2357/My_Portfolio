from pyexpat import model
from turtle import color
from django.db import models
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Portfolio(models.Model):
    Portfolio_name = models.CharField(_("portfolio_name/id"), max_length=50, null=True, unique=True, default='MY PORTFOLIO CONFIG')
    # User_info = models.OneToOneField("portfolio.User_info", verbose_name=_("user_info"), on_delete=models.CASCADE)
    # Personlization = models.OneToOneField("portfolio.Personlization", verbose_name=_("personalization"), on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs) -> None:
        if Portfolio.objects.count() >= 1:
            raise PermissionDenied
        else:
            return super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f'Portfolio Config'
class User_info(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE, null=True)
    Fullname = models.CharField(_("FullName"), max_length=50, help_text='Full name to be displayed on portfolio', default='Enter Full Name')
    Country = CountryField(help_text="Country of Residence", default='Choose Country')
    City = models.CharField(_('City_Name'), max_length=50, help_text="name of city that would be displayed on front page", default='Enter City Name')
    Phone_number = PhoneNumberField(_("Phone Number"), help_text="Phone number to display on home page", default='Enter phone number')
    profession = models.CharField(_("Professions"), max_length=100, help_text='professions to be placed on homepage. Use comma to separate profession', null=True)
    Curriculum_vitae = models.FileField(_("Curriculum_Vitae"), upload_to='upload/', max_length=100, help_text='File upload for CV', null=True)
    class Meta:
        verbose_name = ("User_Information")
        verbose_name_plural = ("User_Information")

    def __str__(self):
        return self.Fullname

class Personlization(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE, null=True)
    CHOICES = (
        ('yellow', 'yellow'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('orange', 'orange')
    )

    Color_theme = models.CharField(_("Color Theme for Portfolio Colors"),choices=CHOICES, max_length=50, default='Choose color theme', help_text='Choose the portfolio color scheme')
    Terminal_icon_blink = models.BooleanField(_("ON or OFF blink terminal icon on homepage"), default=True, null=True)
    Animation = models.BooleanField(_("ON or OFF animation on homepage"), default=True, null=True)
    Background_picture = models.ImageField(_("Background picture for home page"), upload_to='images/', height_field=None, width_field=None, max_length=None, null=True)
    class Meta:
        verbose_name = ("Personalization")
        verbose_name_plural = ("Personalization")

    def __str__(self):
        return self.Color_theme

class Social_info(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE, null=True)
    Facebook_url = models.URLField(_("Facebook Account Url"), max_length=200, default='None')
    Instagram_url = models.URLField(_("Instagram Account Url"), max_length=200, default='None')
    Twitter_url = models.URLField(_("Twitter Account Url"), max_length=200, default='None')
    LinkedIn_url = models.URLField(_("LinkedIn Account Url"), max_length=200, default='None')
    Email_account_name = models.EmailField(_("Email Name"), max_length=254, default='None')
    Github_url = models.URLField(_("Github Account Url"), max_length=200, default='None')
    class Meta:
        verbose_name = _("Social_info")
        verbose_name_plural = _("Social_infos")

    def __str__(self):
        return f'Social Info'
    


    


