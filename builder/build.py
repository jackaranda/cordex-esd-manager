import sys
import os
import psycopg2
import zipfile
from shutil import rmtree
import numpy as np

from functions import value_map


sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm
print pycdm.Dataset.__subclasses__()

#sys.path.append('/servers/cordex_manager_env/cordex-esd-manager')
sys.path.append('/home/cjack/work/projects/code/cordex-esd-manager/cordex_esd_manager/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cordex_esd_manager.settings")

import django
django.setup()

from experiments.models import Experiment
from submissions.models import Submission, Upload, Model

#UPLOAD_ROOT = '/servers/cordex_manager_env/uploads'
UPLOAD_ROOT = '/home/cjack/work/projects/code/cordex-esd-manager/uploads'
force_rebuild = False

for e in Experiment.objects.all():
	print e.meta.slug, e.slug
    
	reference_ds = pycdm.open('/home/cjack/work/data/observed/station/claris/station/pr.nc')
	reference_ids = reference_ds.root.variables['id'][:]

	for submission in Submission.objects.filter(experiment=e):
		print "\t{}".format(submission)

		for upload in submission.uploads.all():
			print "\t\t{}".format(upload)

			filename = UPLOAD_ROOT + "/" + upload.uploaded.name

			# Check the file is there
			if not os.path.exists(filename):
				continue

			target = "{}.build.nc".format(os.path.splitext(filename)[0])
			print "\t\t\tWriting to {}".format(target)
			
			rebuild = False
			try:
				source_timestamp = os.stat(filename).st_mtime
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

					# Clean up any previous unzipping
					try:
						rmtree(source)
					except:
						pass

					zfile.extractall(source)
					zfile.close()

				else:
					source = filename

				try:
					ds = pycdm.open(source)
				except:
					print "Failed to open the source dataset!!!!"
					continue

				# Copy metadata from reference dataset
				print "source variables = ", ds.root.variables
				#print pycdm.Field(ds.root.variables['pr']).coordinates_mapping
			 	
				# This is ugly, but we have to try a few possible names for station ID
				features_mapped = False
				features_id_names = ['id', 'station_id', 'stid']

				for name in features_id_names:
					print "looking for ", name
					if ds.root.variables.has_key(name):
						source_ids = ds.root.variables[name][:]
						features_mapped = True

				print "source_ids = ", source_ids

				if not features_mapped:
					print "Failed to map features!!!!"
					continue

				print "reference_ids = ", reference_ids
				feature_map = np.array([list(reference_ids).index(val) for val in list(source_ids)])

				#print "Mapped features"
				#feature_map = range(0,81)
				# Get reference lat/lon and elevations
			 	latitudes = reference_ds.root.variables['latitude'][:][feature_map]
			 	longitudes = reference_ds.root.variables['longitude'][:][feature_map]
			 	elevations = reference_ds.root.variables['elevation'][:][feature_map]
			 	#latitudes = reference_ds.root.variables['latitude'][:]
			 	#longitudes = reference_ds.root.variables['longitude'][:]
			 	#elevations = reference_ds.root.variables['elevation'][:]

			 	# Create or overide dataset lat/lon elevations
			 	if ds.root.variables.has_key('latitude'):
				 	ds.root.variables['latitude'][:] = latitudes
				else:
					ds.root.variables['latitude'] = pycdm.Variable('latitude', ds.root, data=latitudes, dimensions=['feature'], attributes={'units':'degrees north'})

			 	if ds.root.variables.has_key('longitude'):
				 	ds.root.variables['longitude'][:] = longitudes
				else:
					ds.root.variables['longitude'] = pycdm.Variable('longitude', ds.root, data=longitudes, dimensions=['feature'], attributes={'units':'degrees east'})

			 	if ds.root.variables.has_key('elevation'):
				 	ds.root.variables['elevation'][:] = elevations
				else:
					ds.root.variables['elevation'] = pycdm.Variable('elevation', ds.root, data=elevations, dimensions=['feature'], attributes={'units':'m'})

				print "Going to try to write out netCDF file"
				try:
					pycdm.plugins.netcdf4.netCDF4Dataset.copy(ds, target)
				except:
					print sys.exc_info()
					print "Something went very wrong!!!!"
					continue

			# Open the netcdf file and write out each variable to separate netcdf files
			target_names = {}
			for variable in e.variables.filter(experimentvariables__category='output'):
				for period in e.timeperiods.filter(experimenttimeperiods__category='validation'):
					begin = period.begin.strftime("%Y%m%d")
					end = period.end.strftime("%Y%m%d")
					target_names[variable.short_name] = "{}_{}-{}_{}_v{}_day_{}_{}.nc".format(variable.short_name, e.meta.slug, e.slug, s.model.slug, s.version, begin, end)
		
			print target_names
