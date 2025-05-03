from django import views
from django.urls import path
from . import views
from .views import ProfileUserCreateView, RetrieveCompteView, RetrieveUserView,StoresView,category_store,complaines_and_comptes_pic,delete_expired_cards,get_row_by_code

urlpatterns = [

    path('create/', ProfileUserCreateView.as_view(), name='profile-user-create'),
    path('compte/<int:id>', RetrieveCompteView.as_view(), name='profile-compte-retrieve'),
    path('user/<int:id>', RetrieveUserView.as_view(), name='profile-user-retrieve'),
    path ('complaines_and_comptes_pic/',complaines_and_comptes_pic.as_view(),name='complaines_and_comptes_pic'),
    path('delete_expired_cards/', views.delete_expired_cards, name='delete_expired_cards'),
    path('get_row_by_code/<str:code>/', views.get_row_by_code, name='get_row_by_code'),
    path('Stores/', StoresView.as_view(), name='Stores'),
    path('categoryStore/', category_store.as_view()),
   

]