from pyexpat import model
from turtle import color
from xml.dom import VALIDATION_ERR
from django.db import models
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Portfolio(models.Model):
    Portfolio_name = models.CharField(_("portfolio_name/id"), max_length=50, null=True, default='MY PORTFOLIO CONFIG')

    # User_info = models.OneToOneField("portfolio.User_info", verbose_name=_("user_info"), on_delete=models.CASCADE)
    # Personlization = models.OneToOneField("portfolio.Personlization", verbose_name=_("personalization"), on_delete=models.CASCADE)

    # def save(self, *args, **kwargs) -> None:
    #     if self.Portfolio_name != "MY PORTFOLIO CONFIG":
    #         return PermissionDenied
    #     else:
    #         return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Portfolio Config'


class User_info(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE,
                                     null=True)
    Fullname = models.CharField(_("FullName"), max_length=50, help_text='Full name to be displayed on portfolio',
                                default='Enter Full Name')
    Country = CountryField(help_text="Country of Residence", default='Choose Country')
    City = models.CharField(_('City_Name'), max_length=50,
                            help_text="name of city that would be displayed on front page", default='Enter City Name')
    Phone_number = PhoneNumberField(_("Phone Number"), help_text="Phone number to display on home page",
                                    default='Enter phone number')
    profession = models.CharField(_("Professions"), max_length=100,
                                  help_text='professions to be placed on homepage. Use comma to separate profession',
                                  null=True)
    Curriculum_vitae = models.FileField(_("Curriculum_Vitae"), upload_to='upload/', max_length=100,
                                        help_text='File upload for CV', null=True)

    class Meta:
        verbose_name = ("User_Information")
        verbose_name_plural = ("User_Information")

    def __str__(self):
        return self.Fullname


class Personlization(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE,
                                     null=True)
    CHOICES = (
        ('yellow', 'yellow'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('orange', 'orange')
    )

    Color_theme = models.CharField(_("Color Theme for Portfolio Colors"), choices=CHOICES, max_length=50,
                                   default='Choose color theme', help_text='Choose the portfolio color scheme')
    Terminal_icon_blink = models.BooleanField(_("Blink terminal icon"), default=True, null=True)
    Animation = models.BooleanField(_("animation on homepage"), default=True, null=True)
    Background_picture = models.ImageField(_("home page bg "), upload_to='images/', height_field=None, width_field=None,
                                           max_length=None, null=True)
    Service_background_picture = models.ImageField(_("service page bg"), upload_to='images/', height_field=None,
                                                   width_field=None, max_length=None, null=True)
    Experience_background_picture = models.ImageField(_("experience page bg"), upload_to='images/', height_field=None,
                                                      width_field=None, max_length=None, null=True)
    Contact_background_picture = models.ImageField(_("contact page bg"), upload_to='images/', height_field=None,
                                                      width_field=None, max_length=None, null=True)

    Service_background_picture_switch = models.BooleanField(_("service page bg switch"), default=True, null=True)
    Experience_background_picture_switch = models.BooleanField(_("experience page bg switch"), default=True, null=True)
    Contact_background_picture_switch = models.BooleanField(_("contact page bg switch"), default=True, null=True)
    class Meta:
        verbose_name = ("Personalization")
        verbose_name_plural = ("Personalization")

    def __str__(self):
        return self.Color_theme


class Social_info(models.Model):
    Portfolio = models.OneToOneField("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE,
                                     null=True)
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


class Services(models.Model):
    Portfolio = models.ForeignKey("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE,
                                  null=True)
    Icon_name = models.CharField(_("icon name"), max_length=50, help_text='icon to be used for describing this service')
    Title = models.CharField(_("Title of services"), max_length=60,
                             help_text="title to be used for this particular services")
    Description = models.TextField(_("Description of services"), help_text='Description of this service')

    class Meta:
        verbose_name = _("Services")
        verbose_name_plural = _("Servicess")

    def __str__(self):
        return f'{self.Title}'


class Work(models.Model):
    Title = models.CharField(_("The Title of Post/Job"), max_length=70)
    Description = models.TextField(_("Description of Job done"))
    Start_date = models.DateField(_("Date Job Started"), auto_now=False, auto_now_add=False)
    End_date = models.DateField(_("Date Job Ended"), auto_now=False, auto_now_add=False)
    Experience = models.ForeignKey("portfolio.Experience", verbose_name=_("User Experience"), on_delete=models.CASCADE,
                                   null=True)

    class Meta:
        verbose_name = _("Work")
        verbose_name_plural = _("Works")

    def __str__(self):
        return f'{self.Title}'


class Education(models.Model):
    Year_of_graduation = models.DateField(_("Year of graduation"), auto_now=False, auto_now_add=False)
    Degree_awarded = models.CharField(_("Degree Awarded"), max_length=50)
    Description = models.TextField(_("Description of degree awarded"))
    Experience = models.ForeignKey("portfolio.Experience", verbose_name=_("User Experience"), on_delete=models.CASCADE,
                                   null=True)

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")

    def __str__(self):
        return f'Education'


class Experience(models.Model):
    User_story = models.TextField(_("User Experience Story"))

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    def __str__(self):
        return f'Experience'


class PortfolioExhibit(models.Model):
    Title = models.CharField(_("Title of Work"), max_length=20)
    Short_Description = models.TextField(_("Work Short Description"))
    Date = models.DateField(_("Date of project"), auto_now=False, auto_now_add=False)
    # client = models.CharField()


class Contact(models.Model):
    Portfolio = models.ForeignKey("portfolio.Portfolio", verbose_name=_("User_info"), on_delete=models.CASCADE,
                                null=True)
    E_mail = models.EmailField(_("Contact E-Mail"), max_length=254)
    Phone = PhoneNumberField(_("Phone Number"), help_text="Phone number to display on home page")
    Website = models.URLField(_("Website Link"), max_length=200, help_text="Website Link")
    Address = models.TextField(_("Address of Contact"), help_text='Contact Address')
    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return f'Cotacts'

    