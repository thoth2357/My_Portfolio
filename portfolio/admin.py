from django.contrib import admin
from .models import *

# Register your models here.
class User_info_inline(admin.StackedInline):
    model = User_info

class Personalization_Inline(admin.TabularInline):
    model = Personlization

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [Personalization_Inline, User_info_inline]







# admin.site.register(Portfolio)
# admin.site.register(User_info)
# admin.site.register(Personlization)