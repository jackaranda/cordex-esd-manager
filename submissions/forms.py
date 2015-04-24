from django.forms import ModelForm
from submissions.models import Model
from submissions.models import Submission
from submissions.models import Upload


class SubmissionModelForm(ModelForm):

	class Meta:
		model = Model
		fields = ['title', 'description']

class SubmissionForm(ModelForm):

	class Meta:
		model = Submission
		fields = ['experiment', 'model', 'notes', 'owner']

class UploadForm(ModelForm):

	class Meta:
		model = Upload
		fields = ['submission', 'format', 'uploaded']