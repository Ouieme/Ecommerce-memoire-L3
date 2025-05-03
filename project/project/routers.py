from rest_framework import routers
from admins.viewsets import Adminsets
from Comptes.viewsets import Compteset 
from Comptes.viewsets import getCompts
from Comptes.viewsets import mode_de_paiement_set
from Comptes.viewsets import Demandset
from Comptes.viewsets import reclamationset
# from product.viewsets import Categoryset


router = routers.DefaultRouter()
router.register(r'admin', Adminsets)  # Register Adminsets for the 'admin' endpoint
router.register(r'Comptes', Compteset)
router.register(r'reclamationset', reclamationset)
router.register(r'mode_de_paiement',mode_de_paiement_set)
router.register(r'getCompts',getCompts)
router.register(r'Demandset', Demandset)
# router.register(r'Categoryset',Categoryset)