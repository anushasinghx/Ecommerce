from django.contrib import admin

from .models import Category,Offer,Gadget,CartItem,Review,Favorite,Order

admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Gadget)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Order)

