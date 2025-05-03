from itertools import product
# from click.core import F
from django.http import Http404, HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer,CategoryProductSerializer

from rest_framework import status

from django.core.mail import send_mail
from django.http import JsonResponse

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class Products(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryBySlugView(APIView):
    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            products = category.products.all()
            
            category_data = {
                'category_name': category.name,
                'category_thumbnail': category.thumbnail.url,
                'products': ProductSerializer(products, many=True).data
            }
            
            return JsonResponse(category_data)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)

# def contact_view(request):
#     if request.method == 'POST':
#         serializer = ContactSerializer(data=request.POST)
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             name = validated_data['name']
#             email = validated_data['email']
#             phone = validated_data['phone']
#             subject = validated_data['subject']
#             message = validated_data['message']

#             # Compose the email message
#             email_subject = f"New Message: {subject}"
#             email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage: {message}"

#             # Send the email
#             send_mail(email_subject, email_message, 'ouiemeyassed@gmail.com', ['ouieme.yessad@univ-constantine2.dz'])

#             # Return a JSON response indicating success
#             return JsonResponse({'message': 'Message sent successfully'})
#         else:
#             # Return a JSON response with validation errors
#             return JsonResponse({'errors': serializer.errors}, status=400)

#     # Return a JSON response indicating failure for other HTTP methods
#     return JsonResponse({'message': 'Invalid request method'}, status=400)


# class SubmitFormView(APIView):
#     @api_view(['POST'])
#     def post(self, request):
#         if request.method == 'POST':
#             name = request.data.get('name')
#             email = request.data.get('email')
#             phone = request.data.get('phone')
#             subject = request.data.get('subject')
#             message = request.data.get('message')


#             send_mail('Contact Form',
#                       message,
#                       settings.EMAIL_HOST_USER,
#                       ['ouiemeyassed@gmail.com'],
#                       fail_silently=False)
            
#             return Response({'message': 'Email sent successfully'})
        
#         return Response({'message': 'Invalid request method'}, status=400)


# class SubmitFormView(APIView):
#     def post(self, request):
#         name = request.data.get('name')
#         email = request.data.get('email')
#         phone = request.data.get('phone')
#         subject = request.data.get('subject')
#         message = request.data.get('message')

#         # Compose the email
#         email_message = f"""
#         Name: {name}
#         Email: {email}
#         Phone: {phone}
#         Subject: {subject}
#         Message: {message}

#         """

#         # Send the email
#         send_mail(
#             subject=subject,
#             message=email_message,
#             from_email=email,
#             recipient_list=['ouiemeyassed@gmail.com'],  # your email address
#             fail_silently=False,
#         )

#         return HttpResponse('Email sent successfully')



# def get_category_product():
#     category_product = Product.objects.select_related('Category').values(
#         product=F('Product'),
#         category=F('Category'),
#     )
#     return category_product

# class CategoryProduct(APIView):
#     def get(self, request):
#         category_product = get_category_product()
#         return Response(CategoryProduct)


def get_category_product():
    category_products = Product.objects.select_related('category').all()
    return category_products

class CategoryProduct(APIView):
    def get(self, request):
        category_products = get_category_product()
        serialized_data = CategoryProductSerializer(category_products, many=True).data
        return Response(serialized_data)