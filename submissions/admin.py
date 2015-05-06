from django.contrib import admin
from submissions.models import Model, Submission, Upload

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



admin.site.register(Model, ModelAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Upload)
