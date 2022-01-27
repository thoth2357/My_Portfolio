from django.contrib import admin
from .models import *
from django import forms

# Register your models here.

class User_info_inline(admin.StackedInline):
    model = User_info

class Personalization_Inline(admin.TabularInline):
    model = Personlization
    def has_delete_permission(self, request, obj=None):
        return False

class Social_info_inline(admin.StackedInline):
    model = Social_info

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [Personalization_Inline, User_info_inline, Social_info_inline]

    readonly_fields = ['Portfolio_name']