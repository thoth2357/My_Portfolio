from pyexpat import model
from django.db import models

# Create your models here.

class User_info(models.Model):
    Fullname = models.CharField(("FullName"), max_length=50, help_text='Fie')
    

    class Meta:
        verbose_name = ("User_info")
        verbose_name_plural = ("User_infos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_info_detail", kwargs={"pk": self.pk})
