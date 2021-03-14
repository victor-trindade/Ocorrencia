from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Store


class StoreResource(resources.ModelResource):

    class Meta:
        model = Store
        fields = ('id', 'sf_id', 'name', 'addr', 'cnp',)



class StoreAdmin(ImportExportModelAdmin):
    resource_class = StoreResource

admin.site.register(Store, StoreAdmin)