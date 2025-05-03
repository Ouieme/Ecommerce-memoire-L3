from http.client import HTTPResponse
from django.db import connection
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gérant_de_magasin,Compte
from django.db.models import F
from django.contrib.auth.models import User
from .serializers import ProfileCompteSerializer, ProfileUserSerializer
from .mixins import MultipleFieldLookupMixin
from .models import Magasin ,reclamation,mode_de_paiement
from .serializers import StoreSerializer
from django.db.models import F
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.templatetags.static import static



def delete_expired_cards(request):
    with connection.cursor() as cursor:
        cursor.execute("CALL delete_expired_rows();")
    return HTTPResponse("Expired cards deleted successfully")        
#  get gift cards by code
def get_row_by_code(request, code):
    row = get_object_or_404(mode_de_paiement, code=code)
    return HttpResponse(f"Row with code {code}: {row}")

def get_complaines_and_comptes_pic():
    complaines_and_comptes_pic = reclamation.objects.select_related('compte_id').all()
    return complaines_and_comptes_pic
#  show te jointeur


class complaines_and_comptes_pic(APIView):
    def get(self, request):
        complaines_and_comptes_pic = get_complaines_and_comptes_pic()  # Call the function to retrieve complaints and corresponding pictures
        serialized_data = []
        for reclamation in complaines_and_comptes_pic:
            serialized_data.append({
                'message': reclamation.message,
                "type_reclm": reclamation.type_reclm,
                "date_reclamation": reclamation.date_reclamation ,
                'compte_picture': reclamation.compte_id.image.url if reclamation.compte_id.image else static('defoultpic.png')
            })
        return Response(serialized_data)


def get_owner_and_store():
    owner_and_store = Gérant_de_magasin.objects.select_related('compte_id', 'magasin_id').values(
        owner=F('compte_id__nom'),
        store_name=F('magasin_id__nom')
    )
    return owner_and_store 



class OwnerAndStoreView(APIView):
    def get(self, request):
        owner_and_store = get_owner_and_store()  # Call the function to retrieve owner and store data
        return Response(owner_and_store)
    


class ProfileUserCreateView(generics.CreateAPIView):
    queryset = Compte.objects.all()
    serializer_class = ProfileCompteSerializer

    def perform_create(self, serializer):
        # Get the current user from the request object

        user = User.objects.create_user(self.request.data.get('username'), self.request.data.get('email'), self.request.data.get('password'), first_name=self.request.data.get('firstname'), last_name=self.request.data.get('lastname'))

        data = {}
        if self.request.data.get('role') == 'stormanager':
            data = {
                'date_nes': self.request.data.get('date_nes'),
                'adresse': self.request.data.get('adresse'),
                'telephone': self.request.data.get('phone'),
                'num_ident': self.request.data.get('num_ident'),
            }
        # Set the user field in the serializer to the current user
        serializer.save(user=user, typeC=self.request.data.get('role'), **data)
        

class RetrieveCompteView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Compte.objects.all()
    serializer_class = ProfileCompteSerializer
    lookup_fields = ['typeC']

class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUserSerializer
    lookup_fields = ['id']

class StoresView(APIView):
    def get(self, request, format=None):
        Magasins = Magasin.objects.all()
        serializer = StoreSerializer(Magasins, many=True)
        return Response(serializer.data)

def get_category_store():
    category_store = Magasin.objects.select_related('magasin_category').values(
       magasin=F('id'),
       store_name=F('nom'),
       magasin_category=F('magasin_category__name'),
    )
    return category_store

class category_store(APIView):
    def get(self, request):
        category_store = get_category_store() 
        return Response(category_store)
    

