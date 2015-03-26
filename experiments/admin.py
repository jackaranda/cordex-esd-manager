from django.contrib import admin
from experiments.models import TimePeriod, Project, Experiment, Dataset, ExperimentTimePeriods, ExperimentDatasets

# Register your models here.

class TimePeriodAdmin(admin.ModelAdmin):
	pass

class TimePeriodInline(admin.TabularInline):

	model = ExperimentTimePeriods
	fields = ('category', 'timeperiod',)

class DatasetInline(admin.TabularInline):

	model = ExperimentDatasets

class ProjectAdmin(admin.ModelAdmin):
	
	fields = ('short_name', 'description')
	list_display = ('short_name', 'description')


class ExperimentAdmin(admin.ModelAdmin):

	fields = ('project', 'meta', 'parent', 'short_name', 'description', 'created', 'created_by', 'modified')
	readonly_fields = ('created', 'modified')
	list_display = ('project', 'parent', 'meta', 'short_name', 'description', 'created', 'created_by', 'modified')
	list_display_links = ('short_name',)
	inlines = (DatasetInline, TimePeriodInline, )

class DatasetAdmin(admin.ModelAdmin):

	fields = ('short_name', 'description', 'category', 'source_url')
	list_display = ('short_name', 'description', 'category', 'source_url')

admin.site.register(TimePeriod, TimePeriodAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Dataset, DatasetAdmin)


