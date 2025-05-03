from rest_framework import serializers
from django.core.mail import send_mail
from .models import Category, Product 
from django.conf import settings



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"


        )
def get_absolute_url(self, obj):
        return obj.get_absolute_url()

def get_image(self, obj):
        return obj.get_image()

def get_thumbnail(self, obj):
        return obj.get_thumbnail()

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "thumbnail",
            "slug",
            "products"
        )



# class ContactSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()
#     subject = serializers.CharField()
#     message = serializers.CharField()

#     def create(self, validated_data):
#         # Handle the creation of the contact message
#         # Here you can add your code to send an email or process the message data
#         # For example:
#         name = validated_data.get('name')
#         email = validated_data.get('email')
#         phone = validated_data.get('phone')
#         subject = validated_data.get('subject')
#         message = validated_data.get('message')

#         # Send the email or process the message data here


class CategoryProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_thumbnail = serializers.ImageField(source='category.thumbnail')
    category_slug = serializers.SlugField(source='category.slug')
    product_name = serializers.CharField(source='name')
    product_slug = serializers.SlugField(source='slug')
    product_description = serializers.CharField(source='description')
    product_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='price')
    product_image = serializers.ImageField(source='image')
    product_thumbnail = serializers.ImageField(source='thumbnail')
    product_date_added = serializers.DateTimeField(source='date_added')

    class Meta:
        model = Product
        fields = [
            'category_name',
            'category_thumbnail',
            'category_slug',
            'product_name',
            'product_slug',
            'product_description',
            'product_price',
            'product_image',
            'product_thumbnail',
            'product_date_added',
        ]


      
        