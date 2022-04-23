from django.contrib import admin
from .models import Person, Items_listed, borrower
admin.site.register(Person)
admin.site.register(Items_listed)
admin.site.register(borrower)

# Register your models here.
