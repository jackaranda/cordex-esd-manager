from django.contrib import admin
from submissions.models import Model, ModelMetaCategory, ModelMetaTerm, ModelMetaDependencies, ModelMetaValues, Submission, Upload

# Register your models here.

class UploadInline(admin.TabularInline):
	model = Upload

class ModelAdmin(admin.ModelAdmin):
	model = Model
	fields = ('slug', 'title', 'contact', 'description',)
	prepopulated_fields = {"slug": ("title",)}


class SubmissionAdmin(admin.ModelAdmin):
	model = Submission
	fields = ('owner', 'experiment', 'model', 'version', 'created', 'modified', 'notes')
	readonly_fields = ('created', 'modified')
	inlines = (UploadInline,)


admin.site.register(ModelMetaCategory)
admin.site.register(ModelMetaTerm)
admin.site.register(ModelMetaDependencies)
admin.site.register(ModelMetaValues)
admin.site.register(Model, ModelAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Upload)
