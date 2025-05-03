from rest_framework import serializers
from django.contrib.auth.models import User

from admins.serializers import ProfileAdminSerializer
from .models import Compte ,mode_de_paiement,Magasin,reclamation,Demand
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView  



class reclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reclamation
        fields = (
            "id",
            "compte_id",
            "message  ",
            "type_reclm",
            "date_reclamation" 
           ) 
                
class ComptesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = (
            "id",
            'user',
            'date_nes',
            'adresse',
            'telephone',
            'typeC',
            'num_ident',
           ) 

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = (
            "id",
            "compte_id",
            "Categorie",
            "nom",
            "Motivation",
            ) 


class ProfileCompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = ['id', 'date_nes', 'adresse', 'telephone', 'typeC', 'num_ident', 'user_id']

def NestedSerializer(read_only):
    pass
class ProfileUserSerializer(serializers.ModelSerializer):
    compte = ProfileCompteSerializer()  # Instantiate the ProfileCompteSerializer
    admin = ProfileAdminSerializer()  # instantiate the ProfileAdminSerializer

    def update(self, instance, validated_data):
        compte_data = validated_data.pop('compte', {})  # Retrieve compte data if present
        # Update the fields of the instance with the validated data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)

        # Update the fields of the nested compte object if data is provided
        if compte_data:
            compte = instance.compte
            compte_serializer = ProfileCompteSerializer(instance.compte, data=compte_data)
            compte_serializer.is_valid(raise_exception=True)
            compte_serializer.save()
            compte.date_nes = compte_data.get('date_nes', compte.date_nes)
            compte.adresse = compte_data.get('adresse', compte.adresse)
            compte.telephone = compte_data.get('telephone', compte.telephone)
            compte.typeC = compte_data.get('typeC', compte.typeC)
            compte.num_ident = compte_data.get('num_ident', compte.num_ident)
            compte.save()

        # Save the updated instance
        instance.save()
        

        return instance

    nested_field = NestedSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'id', 'compte', 'admin']




class mode_de_paiementSerializer(serializers.ModelSerializer): 
     class Meta:
        model = mode_de_paiement
        fields = (
              'nom',
              'valeur',
              'date_expirée',
        )


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magasin
        fields = (
            "id",
            "nom",
            "adresse",
            "thumbnail",
            "image",
            "slug",
            "magasin_category",
            
        )     

class category_store(serializers.Serializer):
    class Meta:
    
        magasin_category=serializers.CharField()
        magasin=serializers.CharField()
        store_name=serializers.CharField()


