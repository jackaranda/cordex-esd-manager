import sys
import os
import psycopg2
import zipfile
from shutil import rmtree

from functions import value_map



sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm
print pycdm.Dataset.__subclasses__()

sys.path.append('/home/cjack/work/projects/code/cordex-esd-manager/cordex_esd_manager/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cordex_esd_manager.settings")

import django
django.setup()

from experiments.models import Experiment
from submissions.models import Submission, Upload, Model


UPLOAD_ROOT = '/home/cjack/work/projects/research/cordex/statistical/experiment1/uploads/'
force_rebuild = False

for e in Experiment.objects.all():
	print e.meta.slug, e.slug

	reference_ds = pycdm.open('/home/cjack/work/data/observed/station/claris/station/pr.nc')

	for submission in Submission.objects.filter(experiment=e):
		print "\t{}".format(submission)

		for upload in submission.uploads.all():
			print "\t\t{}".format(upload)

			filename = UPLOAD_ROOT + "/" + upload.uploaded.name

			# Check the file is there
			if not os.path.exists(filename):
				continue

			target = "{}.nc".format(os.path.splitext(filename)[0])
			print "\t\t\tWriting to {}".format(target)
			
			rebuild = False
			try:
				source_timestamp = os.stat(fileanme).st_mtime
				target_timestamp = os.stat(target).st_mtime
				if source_timestamp > target_timestamp:
					rebuild = True
			except:
				rebuild = True

			if force_rebuild:
				rebuild = True

			if rebuild:

				# See if its a zipfile
				if upload.uploaded.name[-3:] == 'zip':
					
					zfile = zipfile.ZipFile(filename, 'r')
					source = "{}/tmp".format(os.path.split(filename)[0])
					print "unzipping {} into {}".format(filename, source)
					zfile.extractall(source)
					zfile.close()
					#rmtree(source)

				else:
					source = filename

				ds = pycdm.open(source)

				# Copy metadata from reference dataset
			 	feature_map = value_map(ds.root.variables['id'][:], reference_ds.root.variables['id'][:])

			 	latitudes = reference_ds.root.variables['latitude'][:][feature_map]
			 	longitudes = reference_ds.root.variables['longitude'][:][feature_map]
			 	elevations = reference_ds.root.variables['elevations'][:][feature_map]

			 	ds.root.variables['latitude'][:] = latitudes
			 	ds.root.variables['longitude'][:] = longitudes
			 	ds.root.variables['elevation'][:] = elevations

				pycdm.plugins.netcdf4.netCDF4Dataset.copy(ds, target)

				# Clean up zip extraction
				#if upload.uploaded.name[-3:] == 'zip':
				#	rmtree(source)



		
#		target_names = {}

#		for variable in e.variables.filter(experimentvariables__category='output'):
#			for period in e.timeperiods.filter(experimenttimeperiods__category='validation'):
#				begin = period.begin.strftime("%Y%m%d")
#				end = period.end.strftime("%Y%m%d")

#				target_names[variable.short_name] = "{}_{}-{}_{}_v{}_day_{}_{}.nc".format(variable.short_name, e.meta.slug, e.slug, s.model.slug, s.version, begin, end)
	
	
#		print target_names

#ds = pycdm.open(EXPERIMENT_ROOT)
#print ds
#print ds.root.dimensions

#pycdm.plugins.netcdf4.netCDF4Dataset.copy(ds, 'test2.nc')


