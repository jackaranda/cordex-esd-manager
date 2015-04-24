from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	institution = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=100, blank=True, null=True)

	complete = models.BooleanField(default=False)
	activated = models.BooleanField(default=False)

	def __unicode__(self):
		return '{} {}'.format(self.user.first_name, self.user.last_name)

	


