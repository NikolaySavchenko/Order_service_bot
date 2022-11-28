import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_project.settings')

django.setup()

from bot_app.models import Client, Level, Form, Berry, Courier, Decor, Delivery,  Order, Topping, Cake


def get_levels():
    levels = Level.objects.all().values()
    cake_levels = []
    for lev in levels:
        level = lev.get('level')
        price = lev.get('price')
        cake_levels.append(f'{level} - {price} руб.')
    return cake_levels


def get_form():
    forms = Form.objects.all().values()
    cake_forms = []
    for frm in forms:
        form = frm.get('form')
        price = frm.get('price')
        cake_forms.append(f'{form} - {price} руб.')
    return cake_forms


def get_toppings():
    toppings = Topping.objects.all().values()
    cake_toppings = []
    for topping in toppings:
        form = topping.get('topping')
        price = topping.get('price')
        cake_toppings.append(f'{form} - {price} руб.')
    return cake_toppings


def get_berry():
    berries = Berry.objects.all().values()
    cake_berry = []
    for berr in berries:
        berry = berr.get('berry')
        price = berr.get('price')
        cake_berry.append(f'{berry} - {price} руб.')
    return cake_berry


def get_decor():
    decors = Decor.objects.all().values()
    cake_decor = []
    for dec in decors:
        decor = dec.get('decor')
        price = dec.get('price')
        cake_decor.append(f'{decor} - {price} руб.')
    return cake_decor

