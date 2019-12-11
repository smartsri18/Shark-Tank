from django.contrib import admin
from .models import Season, Episode, Company, Product

# Register your models here.
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Company)
admin.site.register(Product)
