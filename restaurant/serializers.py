from .models import Menu, Booking
from rest_framework import serializers
        
class MenuItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = Menu
            fields = ['id','title','price','inventory']
            
class BookingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Booking
            fields = '__all__'
            
