# будут создаваться будущие модели нашего проекта
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from transliterate import translit
from decimal import Decimal
from shop.validator import Validator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def get_absolute_url(self):
        result = ''
        if Validator.check_str_is_not_none_and_not_empty(self.slug):
            result = reverse('category_detail', kwargs={'category_slug': self.slug})
        return result

    def __str__(self):
        return self.name


def image_folder(instance, filename):
    result = ''
    if Validator.check_str_is_not_none_and_not_empty(instance.slug) and Validator.check_str_is_not_none_and_not_empty(filename):
        filename = instance.slug + '.' + filename.split('.')[1]
        result = "{0}/{1}".format(instance.slug, filename)
    return result


class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Order(models.Model):
    category = models.ForeignKey(Category)
    # brand = models.ForeignKey(Brand)
    # color = models.ForeignKey(Color)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)
    objects = ProductManager()

    def get_absolute_url(self):
        result = ''
        if Validator.check_str_is_not_none_and_not_empty(self.slug):
            result = reverse('order_detail', kwargs={'order_slug': self.slug})
        return result

    def __str__(self):
        return self.title


class CartItem(models.Model):
    order = models.ForeignKey(Order)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for order {0}".format(self.order.title)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def add_to_cart(self, order_slug):
        cart = self
        order = Order.objects.get(slug=order_slug)
        new_item, _ = CartItem.objects.get_or_create(order=order, item_total=order.price)

        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()
        return

    def remove_from_cart(self, order_slug):
        cart = self
        order = Order.objects.get(slug=order_slug)
        for cart_item in cart.items.all():
            if cart_item.order == order:
                cart.items.remove(cart_item)
                cart.save()
        return

    def change_qty(self, qty, item_id):
        cart = self
        cart_item = CartItem.objects.get(id=int(item_id))
        cart_item.qty = int(qty)
        cart_item.item_total = int(qty) * Decimal(cart_item.order.price)
        cart_item.save()
        new_cart_total = 0.00
        for item in cart.items.all():
            new_cart_total += float(item.item_total)
        cart.cart_total = new_cart_total
        cart.save()
        return

    def __str__(self):
        return str(self.id)


def pre_save_category_slug(instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), 'ru', reversed=True))
        instance.slug = slug
    return


pre_save.connect(pre_save_category_slug, sender=Category)


ORDER_STATUS_CHOICES = (
    ('Принят в обработку', 'Принят в обработку'),
    ('Выполняется', 'Выполняется'),
    ('Оплачен', 'Оплачен')
)


class Ord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    items = models.ForeignKey(Cart)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    buying_type = models.CharField(max_length=40, choices=(('Самовывоз', 'Самовывоз'),
                                                           ('Доставка', 'Доставка')), default='Самовывоз')
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='Принят в обработку')

    def __str__(self):
        return "Заказ №{0}".format(str(self.id))