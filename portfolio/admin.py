from django.contrib import admin
from .models import *
from django import forms

# Register your models here.

class User_info_inline(admin.StackedInline):
    model = User_info
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

class Personalization_Inline(admin.StackedInline):
    model = Personlization
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

class Social_info_inline(admin.StackedInline):
    model = Social_info
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

class ServicesInline(admin.StackedInline):
    model = Services

class ExperienceInline(admin.StackedInline):
    model = Experience

    def has_delete_permission(self, request, obj=None) -> bool:
        return True
    
    

class WorkInline(admin.StackedInline):
    model = Work

class EducationInline(admin.StackedInline):
    model = Education

class ContactInline(admin.StackedInline):
    model = Contact



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [Personalization_Inline, User_info_inline, Social_info_inline, ServicesInline,ExperienceInline, WorkInline, EducationInline, ContactInline ]

    readonly_fields = ['Portfolio_name']

    
    # if Portfolio.objects.count() >=1:
    #     def has_add_permission(self, request, obj=None) -> bool:
    #         return False
    #     def has_delete_permission(self, request, obj=None) -> bool:
    #         return False
    # else:
    #     def has_add_permission(self, request, obj=None) -> bool:
    #         return True
    #     def has_delete_permission(self, request, obj=None) -> bool:
    #         return False


    