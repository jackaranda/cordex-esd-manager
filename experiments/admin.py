from django.contrib import admin
from experiments.models import TimePeriod, Project, MetaExperiment, Experiment, Dataset, ExperimentTimePeriods, ExperimentDatasets

# Register your models here.

class TimePeriodAdmin(admin.ModelAdmin):
	pass

class TimePeriodInline(admin.TabularInline):

	model = ExperimentTimePeriods
	fields = ('category', 'timeperiod',)

class DatasetInline(admin.TabularInline):

	model = ExperimentDatasets


class ProjectAdmin(admin.ModelAdmin):
	
	fields = ('title', 'slug', 'description')
	list_display = ('title', 'description')
	prepopulated_fields = {"slug": ("title",)}

class MetaExperimentAdmin(admin.ModelAdmin):

	fields = ('project', 'title', 'slug', 'description', 'created', 'created_by', 'modified')
	readonly_fields = ('created', 'modified')
	list_display = ('title', 'description', 'created', 'created_by', 'modified')
	list_display_links = ('title',)
	prepopulated_fields = {"slug": ("title",)}

class ExperimentAdmin(admin.ModelAdmin):

	fields = ('meta', 'title', 'slug', 'description', 'created', 'created_by', 'modified')
	readonly_fields = ('created', 'modified')
	list_display = ('meta', 'title', 'description', 'created', 'created_by', 'modified')
	list_display_links = ('title',)
	prepopulated_fields = {"slug": ("title",)}
	inlines = (DatasetInline, TimePeriodInline, )

class DatasetAdmin(admin.ModelAdmin):

	fields = ('title', 'slug', 'description', 'category', 'source_url')
	list_display = ('title', 'description', 'category', 'source_url')
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(TimePeriod, TimePeriodAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MetaExperiment, MetaExperimentAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Dataset, DatasetAdmin)


