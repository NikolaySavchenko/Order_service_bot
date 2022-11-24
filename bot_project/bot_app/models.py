from django.db import models


class Client(models.Model):
    name = models.CharField('ФИО', max_length=200)
    birthday = models.DateField('День рождения', null=True)
    contact = models.CharField('Телефон', max_length=200)
    address = models.CharField('Адрес', max_length=200)

    def __str__(self):
        return self.name


class Courier(models.Model):
    name = models.CharField('ФИО', max_length=200)
    contact = models.CharField('Телефон', max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    date_time = models.DateField('Дата заказа', auto_now_add=True, null=True)
    cake = models.ForeignKey('Cake', default='Торт', on_delete=models.CASCADE)
    comment = models.TextField('Комментарий к заказу', max_length=200, null=True, blank=True)
    delivery_address = models.CharField('Адрес доставки', max_length=200)
    delivery_date = models.DateField('Дата доставки')
    delivery_time = models.DateField('Желаемое время доставки')
    total = models.DecimalField(verbose_name='Всего', max_digits=20,  decimal_places=2, default=0)


class Cake(models.Model):
    name = models.CharField(verbose_name='Название торта', max_length=200, default='Торт')
    price = models.DecimalField(verbose_name='Цена', max_digits=20,  decimal_places=2, default=0)
    level = models.ForeignKey('NumberLevel', on_delete=models.DO_NOTHING, null=True, blank=True, default=0)
    form = models.ForeignKey('Form', on_delete=models.DO_NOTHING, null=True, blank=True, default=0)
    topping = models.ForeignKey('Topping', on_delete=models.DO_NOTHING, null=True, blank=True, default=0)
    berry = models.ForeignKey('Berry', on_delete=models.DO_NOTHING, null=True, blank=True, default=0)
    decor = models.ForeignKey('Decor', on_delete=models.DO_NOTHING, null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'

    def __str__(self):
        return self.name


class NumberLevel(models.Model):
    level = models.CharField(verbose_name='Уровни', max_length=50)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    # cake = models.ForeignKey('Cake', verbose_name='Торт', on_delete=models.CASCADE)

    def __str__(self):
        return self.level


class Form(models.Model):
    form = models.CharField(verbose_name='Форма торта', max_length=50)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.form


class Topping(models.Model):
    topping = models.CharField(verbose_name='Топпинг', max_length=50)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.topping


class Berry(models.Model):
    berry = models.CharField(verbose_name='Ягоды', max_length=50)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.berry


class Decor(models.Model):
    decor = models.CharField(verbose_name='Декор', max_length=50)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.decor


class Delivery(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    courier = models.ForeignKey('Courier', on_delete=models.CASCADE)
    delivery_time = models.DateField('Предполагаемое время доставки')
