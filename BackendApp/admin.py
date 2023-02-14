from django.contrib import admin
from BackendApp.models import admindb,categorydb,Vehicledatabase,Contactdb,Bookingdb
# Register your models here.
admin.site.register(admindb)
admin.site.register(categorydb)
admin.site.register(Vehicledatabase)
admin.site.register(Contactdb)
admin.site.register(Bookingdb)