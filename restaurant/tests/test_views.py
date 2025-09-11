from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=10.0, inventory=50)
        Menu.objects.create(title="Burger", price=8.5, inventory=10)
        
    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)