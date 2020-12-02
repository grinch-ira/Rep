from django.test import TestCase
from django.core.management import call_command
from shop.models import (
Category,
image_folder,
Order,
Cart,
pre_save_category_slug
)


class TestModels(TestCase):

    # load database
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'tests_models_db', verbosity=0)
    
    
    def test_category_get_absolute_url_get_true_url_expected_slash_category_slash_cactus_slash(self):
        category: Category = Category(
            name='cactus',
            slug='cactus'
        )
        actual = category.get_absolute_url()
        expected = '/category/cactus/'
        self.assertEquals(actual, expected)
    
    def test_category_get_absolute_url_get_true_url_expected_slash_category_slash_succulent_slash(self):
        category: Category = Category(
            name='succulent',
            slug='succulent'
        )
        actual = category.get_absolute_url()
        expected = '/category/succulent/'
        self.assertEquals(actual, expected)
    
    def test_category_get_absolute_url_get_false_url_if_slug_is_empty_expected_empty_string(self):
        category: Category = Category(
            name='cactus',
            slug=''
        )
        actual = category.get_absolute_url()
        expected = ''
        self.assertEquals(actual, expected)
    
    def test_category_get_absolute_url_get_false_url_if_slug_is_None_expected_empty_string(self):
        category: Category = Category(
            name='cactus',
            slug=None
        )
        actual = category.get_absolute_url()
        expected = ''
        self.assertEquals(actual, expected)
    
    def test_image_folder_get_true_image_folder_expected_hoya_hyphen_kerry_slash_hoya_hyphen_kerry_dot_jpg(self):
        instance = Order(slug='hoya-kerry')
        filename = 'photo_2019-12-24_00-20-22.jpg'
    
        actual = image_folder(instance, filename)
        expected = 'hoya-kerry/hoya-kerry.jpg'
    
        self.assertEquals(actual, expected)
    
    def test_image_folder_get_false_image_folder_if_slug_is_empty_expected_empty_string(self):
        instance = Order(slug='')
        filename = 'photo_2019-12-24_00-20-22.jpg'
    
        actual = image_folder(instance, filename)
        expected = ''
    
        self.assertEquals(actual, expected)
    
    def test_image_folder_get_false_image_folder_if_slug_is_None_expected_empty_string(self):
        instance = Order(slug=None)
        filename = 'photo_2019-12-24_00-20-22.jpg'
    
        actual = image_folder(instance, filename)
        expected = ''
    
        self.assertEquals(actual, expected)
    
    def test_image_folder_get_false_image_folder_if_filename_is_empty_expected_empty_string(self):
        instance = Order(slug='photo_2019-12-24_00-20-22.jpg')
        filename = ''
    
        actual = image_folder(instance, filename)
        expected = ''
    
        self.assertEquals(actual, expected)
    
    def test_image_folder_get_false_image_folder_if_filename_is_None_expected_empty_string(self):
        instance = Order(slug='hoya-kerry')
        filename = None
    
        actual = image_folder(instance, filename)
        expected = ''
    
        self.assertEquals(actual, expected)
    
    def test_order_get_absolute_url_get_true_url_expected_slash_order_slash_hoya_hyphen_kerry_slash(self):
        order: Order = Order(
            slug='hoya-kerry'
        )
        actual = order.get_absolute_url()
        expected = '/order/hoya-kerry/'
        self.assertEquals(actual, expected)
    
    def test_order_get_absolute_url_get_true_url_expected_slash_order_slash_pakhifitum_slash(self):
        order: Order = Order(
            slug='pakhifitum'
        )
        actual = order.get_absolute_url()
        expected = '/order/pakhifitum/'
        self.assertEquals(actual, expected)
    
    def test_order_get_absolute_url_get_false_url_if_slug_is_empty_expected_empty_string(self):
        order: Order = Order(
            slug=''
        )
        actual = order.get_absolute_url()
        expected = ''
        self.assertEquals(actual, expected)
    
    def test_order_get_absolute_url_get_false_url_if_slug_is_None_expected_empty_string(self):
        order: Order = Order(
            slug=None
        )
        actual = order.get_absolute_url()
        expected = ''
        self.assertEquals(actual, expected)

    def test_cart_add_to_cart_add_one_order_expected_2(self):
        cart = Cart.objects.get(id=53)
        cart.add_to_cart('echeverias')
        cart.save()

        actual = cart.items.count()
        expected = 2

        self.assertEquals(actual, expected)

    def test_cart_add_to_cart_add_one_replay_order_expected_1(self):
        cart = Cart.objects.get(id=53)
        cart.add_to_cart('krassula-hobbit')
        cart.save()

        actual = cart.items.count()
        expected = 1

        self.assertEquals(actual, expected)

    def test_cart_add_to_cart_add_two_order_expected_3(self):
        cart = Cart.objects.get(id=53)
        cart.add_to_cart('echeverias')
        cart.add_to_cart('tefrokaktus-artikulatus')
        cart.save()

        actual = cart.items.count()
        expected = 3

        self.assertEquals(actual, expected)

    def test_cart_add_to_cart_add_three_order_expected_4(self):
        cart = Cart.objects.get(id=53)
        cart.add_to_cart('echeverias')
        cart.add_to_cart('tefrokaktus-artikulatus')
        cart.add_to_cart('agabus-potatorum')
        cart.save()

        actual = cart.items.count()
        expected = 4

        self.assertEquals(actual, expected)

    def test_cart_remove_from_cart_remove_one_order_expected_0(self):
        cart = Cart.objects.get(id=53)
        cart.remove_from_cart('krassula-hobbit')
        cart.save()

        actual = cart.items.count()
        expected = 0

        self.assertEquals(actual, expected)

    def test_cart_remove_from_cart_if_cart_is_empty_expected_0(self):
        cart = Cart.objects.get(id=54)
        cart.remove_from_cart('krassula-hobbit')
        cart.save()

        actual = cart.items.count()
        expected = 0

        self.assertEquals(actual, expected)

    def test_cart_remove_from_cart_remove_second_order_from_cart_expected_1(self):
        cart = Cart.objects.get(id=55)
        cart.remove_from_cart('cacti-in-ceramics-in-size-S')
        cart.save()

        actual = cart.items.count()
        expected = 1

        self.assertEquals(actual, expected)

    def test_cart_remove_from_cart_remove_first_order_from_cart_expected_1(self):
        cart = Cart.objects.get(id=55)
        cart.remove_from_cart('hoya-kerry')
        cart.save()

        actual = cart.items.count()
        expected = 1

        self.assertEquals(actual, expected)

    def test_cart_change_qty_if_cart_is_not_empty_expected_1188(self):
        cart = Cart.objects.get(id=53)
        cart.change_qty(22, 29)

        actual = cart.cart_total
        expected = 187

        self.assertEquals(actual, expected)

    def test_cart_change_qty_if_cart_is_empty_expected_0(self):
        cart = Cart.objects.get(id=54)
        cart.change_qty(22, 29)

        actual = cart.cart_total
        expected = 0

        self.assertEquals(actual, expected)

    def test_pre_save_product_slug_if_slug_is_empty_expected_bomber(self):
        category: Category = Category(
            name='кактус',
            slug=''
        )
        pre_save_category_slug(category)

        actual = category.slug
        expected = 'kaktus'

        self.assertEquals(actual, expected)

    def test_pre_save_product_slug_if_slug_is_not_empty_expected_bombers(self):
        category: Category = Category(
            name='кактус',
            slug='cactus'
        )
        pre_save_category_slug(category)

        actual = category.slug
        expected = 'cactus'

        self.assertEquals(actual, expected)