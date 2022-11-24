from django.contrib import admin
from .models import Client, Courier, Order, Cake, Delivery, NumberLevel, Form, Topping, Berry, Decor


# Register your models here.


@admin.register(Client)
class Client(admin.ModelAdmin):
    fields = ('name', 'birthday', 'contact', 'address')
    list_display = ('name', 'birthday', 'contact', 'address')


@admin.register(Courier)
class Courier(admin.ModelAdmin):
    fields = ('name', 'contact')
    list_display = ('name', 'contact')


@admin.register(Order)
class Order(admin.ModelAdmin):
    fields = ('client', 'cake', 'comment', 'delivery_address', 'delivery_date', 'delivery_time', 'total')
    list_display = ('client', 'cake', 'comment', 'delivery_address', 'delivery_date', 'delivery_time', 'total')


@admin.register(Cake)
class Cake(admin.ModelAdmin):
    fields = ('name', 'price', 'level', 'form', 'topping', 'berry', 'decor')
    list_display = ('name', 'level', 'form', 'topping', 'berry', 'decor', 'price')


@admin.register(NumberLevel)
class NumberLevel(admin.ModelAdmin):
    fields = ('level', 'price')
    list_display = ('level', 'price')


@admin.register(Form)
class Form(admin.ModelAdmin):
    fields = ('form', 'price')


@admin.register(Topping)
class Topping(admin.ModelAdmin):
    fields = ('topping', 'price')


@admin.register(Berry)
class Berry(admin.ModelAdmin):
    fields = ('berry', 'price')


@admin.register(Decor)
class Decor(admin.ModelAdmin):
    fields = ('decor', 'price')


@admin.register(Delivery)
class Delivery(admin.ModelAdmin):
    fields = ('courier', 'order', 'delivery_time')



