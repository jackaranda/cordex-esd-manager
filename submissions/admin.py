from django.contrib import admin
from submissions.models import Model, ModelMeta, Submission, SubmissionMeta, Upload

# Register your models here.

class UploadInline(admin.TabularInline):
	model = Upload

class ModelMetaInline(admin.TabularInline):
	model = ModelMeta

class ModelAdmin(admin.ModelAdmin):
	model = Model
	fields = ('slug', 'title', 'description')
	prepopulated_fields = {"slug": ("title",)}
	inlines = (ModelMetaInline,)

class SubmissionMetaInline(admin.TabularInline):
	model = SubmissionMeta

class SubmissionAdmin(admin.ModelAdmin):
	model = Submission
	fields = ('owner', 'experiment', 'model', 'version', 'created', 'modified', 'notes')
	readonly_fields = ('created', 'modified')
	inlines = (SubmissionMetaInline, UploadInline,)


admin.site.register(Model, ModelAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Upload)
