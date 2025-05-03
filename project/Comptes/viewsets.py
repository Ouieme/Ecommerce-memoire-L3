from djoser.conf import User
from rest_framework import viewsets
from Comptes.serializers import ProfileUserSerializer,mode_de_paiementSerializer
from .models import mode_de_paiement,reclamation,Demand
from .serializers import reclamationSerializer,ComptesSerializer,DemandSerializer,Compte


class Compteset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileUserSerializer

class mode_de_paiement_set(viewsets.ModelViewSet):
        queryset = mode_de_paiement.objects.all()
        serializer_class = mode_de_paiementSerializer
      


class reclamationset(viewsets.ModelViewSet):
    queryset = reclamation.objects.all()
    serializer_class = reclamationSerializer
# get only comptes      
class getCompts (viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = ComptesSerializer


class Demandset(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer  