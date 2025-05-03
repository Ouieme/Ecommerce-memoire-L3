from ast import comprehension
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
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

class Variation(models.Model):
    nom = models.CharField(max_length=50)
    Categorie_id = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
         ordering = ('nom',)
 
    def __str__(self):
         return self.nom
 
class  Variation_Opt (models.Model):
      value = models.CharField(max_length=50)
      variation_id  = models.ForeignKey(Variation , on_delete=models.CASCADE)
      class Meta:
        ordering = ('value',) 

      def __str__(self):
        return self. variation_id
    


class Article (models.Model) :
    nom = models.CharField(max_length=255)
    qty = models.IntegerField()
    prix = models.IntegerField()
    date_ajoutée = models.DateTimeField(auto_now_add=True)
    Produit_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    class Meta:
        ordering = ('date_ajoutée',) 

    def __str__(self):
        return self. nom

class  Produit_Configuration (models.Model):   
   article_id = models.ForeignKey(Article, on_delete=models.PROTECT)
   variation_opt =models.ForeignKey(Variation_Opt, on_delete=models.PROTECT)

class Promotion  (models.Model) :
    code_promo  = models.CharField(max_length=50)
    pourcentage_reduction = models.FloatField()
    date_debut  = models.DateField()
    date_fin = models.DateField ()

    def __str__(self):
        return self. code_promo
 

class Promotion_Produit  (models.Model) :
    Promotion_id = models.ForeignKey(Promotion, on_delete=models.PROTECT)
    Produit_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    def __str__(self):
        return self. Promotion_id
 
