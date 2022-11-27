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


