from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Occurrence
# Register your models here.


class OccResource(resources.ModelResource):

    class Meta:
        model = Occurrence
        fields = ('date', 'timestamp', 'store__name', 'obs', 'photo')

    def before_export(self, queryset, *args, **kwargs):
        pass


class OccAdmin(ImportExportModelAdmin):
    resource_class = OccResource

admin.site.register(Occurrence, OccAdmin)
