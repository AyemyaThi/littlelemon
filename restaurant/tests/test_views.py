from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from decimal import Decimal

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.menu_attributes = {
            'Title': 'Roasted Duck',
            'Price': Decimal('12.5'),
            'Inventory': Decimal('10'),
        }

        self.serializer_data = {
            'Title': 'Roasted Duck',
            'Price': '12.5',
            'Inventory': '10',
        }
        self.menu = Menu.objects.create(**self.menu_attributes)
        self.serializer = MenuSerializer(instance=self.menu)

    def test_getall(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['Title', 'Price', 'Inventory']))