
from django.contrib import admin

from django.contrib import admin

from .models import Compte,Magasin,Gérant_de_magasin,depot,Evaluation,Commande,Livraison,reclamation,Paiement

admin.site.register(Compte)
admin.site.register(Magasin)
admin.site.register(Gérant_de_magasin)
admin.site.register(depot)
admin.site.register(Evaluation)
admin.site.register(Commande)
admin.site.register(Livraison)
admin.site.register(Paiement)
admin.site.register(reclamation)
