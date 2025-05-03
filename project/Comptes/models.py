from django.db import models
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from product.models import Category,Product,Article
from django.contrib.auth.models import User

class Compte(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    date_nes = models.DateTimeField(null=True)
    adresse= models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=255, null=True)
    typeC = models.CharField(max_length=50, null=True)
    num_ident= models.IntegerField(null=True)

class Magasin(models.Model):
     magasin_category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
     product = models.ForeignKey(Product,default="" ,on_delete=models.PROTECT)
     nom = models.CharField(max_length=255)
     slug = models.SlugField(default="")
     adresse = models.CharField(max_length=255)
     telephone = models.IntegerField()
     type_livr = models.CharField(max_length=255)
     image = models.ImageField(upload_to='uploads/', blank=True, null=True)
     thumbnail = models.ImageField(blank=True, null=True, default='uploads/store.png')

def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''


def make_thumbnail(self, image, size=(200, 300)):
        try:
            img = Image.open(image)
            img.convert('RGB')
            img.thumbnail(size)

            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG', quality=85)

            thumbnail = File(thumb_io, name=image.name)

            return thumbnail

        except IOError:
            # Log the error or raise a custom exception as needed
            return None
      
      
class Meta:
    ordering = ('nom',) 

class Gérant_de_magasin(models.Model):
    compte_id  = models.ForeignKey(Compte , on_delete=models.CASCADE)
    magasin_id = models.ForeignKey(Magasin, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ('compte_id',)
    def __str__(self):
         return self.compte_id
 
class depot(models.Model):
    compte_id  = models.ForeignKey(Compte , on_delete=models.CASCADE)
    magasin_id = models.ForeignKey(Magasin, on_delete=models.PROTECT)
    qty = models.IntegerField()
    adresse  = models.CharField(max_length=255)

    class Meta:
        ordering = ('compte_id',)
    def __str__(self):
        return self.compte_id



class Commande  (models.Model) :
    quantité = models.IntegerField() 
    date_commande = models.DateTimeField()
    statut= models.CharField(max_length=255)
    compte_id = models.ForeignKey(Compte, on_delete=models.PROTECT)
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)

class List_Favoris  (models.Model) :
    compte_id = models.ForeignKey(Compte, on_delete=models.PROTECT)
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)

class Sous_catégorie(models.Model):
    parent_cat_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    nom = models.CharField(max_length=50)
    

    class Meta:
        ordering = ('nom',)

    def __str__(self):
         return self.nom     
           
class Livraison (models.Model) :
    type_livr = models.CharField(max_length=255)
    adresse_livraison = models.CharField(max_length=255)
    commande_id =  models.ForeignKey(Commande, on_delete=models.PROTECT)
    date_livraison = models.DateTimeField(auto_now_add=True)
    
class  Paiement (models.Model):
    montant = models.IntegerField()
    date_paiement  = models.DateTimeField(auto_now_add=True)
    typePaiement  = models.CharField(max_length=50)
    commande_id =  models.ForeignKey(Commande, on_delete=models.PROTECT)  
    
class reclamation  (models.Model) :
    compte_id  = models.ForeignKey(Compte, on_delete=models.PROTECT) 
    message  = models.CharField(max_length=50)
    type_reclm = models.CharField(max_length=50)
    date_reclamation  = models.DateTimeField(auto_now_add=True)
   
       
class Meta:
   ordering = ('date_reclamation')
 
class Demand (models.Model) :
    compte_id  = models.ForeignKey(Compte, on_delete=models.PROTECT) 
    Categorie  = models.CharField(max_length=255)
    Motivation = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
   
    def __str__(self):
        return self. compte_id
    
class mode_de_paiement(models.Model):
    nom =models.CharField(max_length=255 , default=1)
    code=models.CharField(max_length=255 )
    valeur= models.IntegerField(default=1) 
    date_expirée=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self. nom
    
class  Evaluation (models.Model):
      compte_id  = models.ForeignKey(Compte, on_delete=models.PROTECT) 
      article_id = models.ForeignKey(Article, on_delete=models.PROTECT,default=1)
      commentaire = models.CharField(max_length=255)
      note = models.IntegerField() 
      date_ajoutée = models.DateTimeField(auto_now_add=True)
   
      class Meta:
        ordering = ('date_ajoutée',) 

      def str(self):
        return self.compte_id


