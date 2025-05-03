from django.contrib import admin

from .models import Category, Article,Product,Produit_Configuration,Promotion,Promotion_Produit,Variation,Variation_Opt

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Produit_Configuration)
admin.site.register(Promotion)
admin.site.register(Promotion_Produit)
admin.site.register(Variation)
admin.site.register(Variation_Opt)