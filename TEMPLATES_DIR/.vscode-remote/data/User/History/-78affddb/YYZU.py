from django.contrib import admin
from .models import CreateTable


# Register your models here.
@admin.register(CreateTable)
class CreateTableAdmin(admin.ModelAdmin):
    list_display = ('status', 'table_num', 'capacity', 'table_position', 'wheelchair_accessible',
    'created_on', 'updated_on')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone_number', 'createtable')


