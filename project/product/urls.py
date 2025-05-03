from django.urls import path, include
from rest_framework import views
from .views import LatestProductsList,ProductDetail,CategoriesView,Products,CategoryProduct,CategoryBySlugView





urlpatterns = [

    path('latest-products/',LatestProductsList.as_view()),
    path('Shop/',Products.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), ),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('CategoryProduct/', CategoryProduct.as_view()),
    path('procat/<slug:category_slug>/', CategoryBySlugView.as_view()),
    
    
]




