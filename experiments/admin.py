from django.contrib import admin
from experiments.models import Experiment, Dataset, ExperimentDatasets

# Register your models here.

class DatasetInline(admin.TabularInline):

	model = ExperimentDatasets

class ExperimentAdmin(admin.ModelAdmin):

	fields = ('short_name', 'description', 'created', 'created_by', 'modified')
	readonly_fields = ('created', 'created_by', 'modified')
	list_display = ('short_name', 'description', 'created', 'created_by', 'modified')
	inlines = (DatasetInline,)

class DatasetAdmin(admin.ModelAdmin):

	fields = ('short_name', 'description', 'category', 'source_url')
	list_display = ('short_name', 'description', 'category', 'source_url')

admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Dataset, DatasetAdmin)


