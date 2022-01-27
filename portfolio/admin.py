from django.contrib import admin
from .models import *
from django import forms

# Register your models here.
class User_info_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Fullname'].required = True

    class Meta:
        model = User_info
        fields = '__all__'
class User_info_inline(admin.StackedInline):
    form  = User_info_Form
    model = User_info

class Personalization_Inline(admin.TabularInline):
    model = Personlization

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [Personalization_Inline, User_info_inline]

    readonly_fields = ['Portfolio_name']





# admin.site.register(Portfolio)
# admin.site.register(User_info)
# admin.site.register(Personlization)