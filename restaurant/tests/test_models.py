from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=1, Inventory=30)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 1")