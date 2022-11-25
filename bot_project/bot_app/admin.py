from django.contrib import admin
from .models import Client, Courier, Order, Cake, Delivery, Level, Form, Topping, Berry, Decor


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
    fields = ('client', 'cake','delivery_address', 'delivery_date', 'delivery_time', 'total', 'comment')
    list_display = ('client', 'cake', 'delivery_address', 'delivery_date', 'delivery_time', 'total', 'comment')


@admin.register(Cake)
class Cake(admin.ModelAdmin):
    fields = ('name', 'level', 'form', 'topping', 'berry', 'decor', 'price')
    list_display = ('name', 'level', 'form', 'topping', 'price')


@admin.register(Level)
class Level(admin.ModelAdmin):
    fields = ('level', 'price')
    list_display = ('level', 'price')


@admin.register(Form)
class Form(admin.ModelAdmin):
    fields = ('form', 'price')
    list_display = ('form', 'price')


@admin.register(Topping)
class Topping(admin.ModelAdmin):
    fields = ('topping', 'price')
    list_display = ('topping', 'price')


@admin.register(Berry)
class Berry(admin.ModelAdmin):
    fields = ('berry', 'price')
    list_display = ('berry', 'price')


@admin.register(Decor)
class Decor(admin.ModelAdmin):
    fields = ('decor', 'price')
    list_display = ('decor', 'price')


@admin.register(Delivery)
class Delivery(admin.ModelAdmin):
    fields = ('courier', 'order', 'delivery_time')
    list_display = ('courier', 'order', 'delivery_time')



