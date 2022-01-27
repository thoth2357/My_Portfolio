from django.contrib import admin
from .models import *

# Register your models here.
class Personalization_Inline(admin.TabularInline):
    model = Personlization

@admin.register(Portfolio)
class HeroAdmin(admin.ModelAdmin):
    ...
    inlines = [Personalization_Inline]




# admin.site.register(Portfolio)
admin.site.register(User_info)
admin.site.register(Personlization)