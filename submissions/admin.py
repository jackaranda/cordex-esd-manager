from django.contrib import admin
from experiments.models import MetaValue
from submissions.models import Model, ModelMeta, Submission, Upload

# Register your models here.

class UploadInline(admin.TabularInline):
	model = Upload

#class MetaValueInline(admin.TabularInline):
#	model = MetaValue

class ModelAdmin(admin.ModelAdmin):
	model = Model
	fields = ('slug', 'title', 'description', 'metadata')
	prepopulated_fields = {"slug": ("title",)}
#	inlines = (MetaValueInline,)

class SubmissionAdmin(admin.ModelAdmin):
	model = Submission
	fields = ('owner', 'experiment', 'model', 'version', 'created', 'modified', 'notes')
	readonly_fields = ('created', 'modified')
	inlines = (UploadInline,)


admin.site.register(Model, ModelAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Upload)
