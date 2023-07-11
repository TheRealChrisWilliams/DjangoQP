from django.contrib import admin
from .models import QPModel


class QPAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(QPModel, QPAdmin)



