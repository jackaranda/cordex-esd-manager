from django.contrib import admin
from experiments.models import TimePeriod, Project, MetaExperiment, Experiment, Dataset, Variable, ExperimentTimePeriods, ExperimentDatasets, ExperimentVariables
from experiments.models import MetaCategory, MetaTerm, MetaDependency, MetaValue

# Register your models here.

class TimePeriodAdmin(admin.ModelAdmin):
	pass

class TimePeriodInline(admin.TabularInline):

	model = ExperimentTimePeriods
	fields = ('category', 'timeperiod')

class DatasetInline(admin.TabularInline):
	model = ExperimentDatasets

class VariableInline(admin.TabularInline):
	model = ExperimentVariables


class VariableAdmin(admin.ModelAdmin):
	pass


class ProjectAdmin(admin.ModelAdmin):
	
	fields = ('title', 'slug', 'description', 'url')
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
	inlines = (DatasetInline, TimePeriodInline, VariableInline, )

class DatasetAdmin(admin.ModelAdmin):

	fields = ('title', 'slug', 'description', 'category', 'source_url')
	list_display = ('title', 'description', 'category', 'source_url')
	prepopulated_fields = {"slug": ("title",)}

class MetaTermInline(admin.TabularInline):
	model = MetaTerm

class MetaCategoryAdmin(admin.ModelAdmin):
	model = MetaCategory
	fields = ('slug', 'description')
	inlines = (MetaTermInline,)

class MetaValueInline(admin.TabularInline):
	model = MetaValue

class MetaTermAdmin(admin.ModelAdmin):
	model = MetaTerm
	fields = ('category', 'name', 'long_name', 'help_text', 'multiple')
	inlines = (MetaValueInline,)


admin.site.register(MetaCategory, MetaCategoryAdmin)
admin.site.register(MetaTerm, MetaTermAdmin)
#admin.site.register(MetaValues)
#admin.site.register(MetaDependencies)

admin.site.register(TimePeriod, TimePeriodAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MetaExperiment, MetaExperimentAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Variable, VariableAdmin)


