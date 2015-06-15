import netCDF4
import json
import sys
import os
import argparse
import numpy, numpy.ma
from datetime import datetime
import glob
import dateutil.parser as dateparser

from functions import *

sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm

parser = argparse.ArgumentParser()
parser.add_argument("source", default=None)
#parser.add_argument("target", default=None)
parser.add_argument("-c", "--config", help="configuration JSON file", default="diagnostics.json")
parser.add_argument("-s", "--statistic", help="name of diagnostic to run", default='mean')
parser.add_argument("-a", "--aggregation", help="aggregation time period (month, year)", default="monthly")
parser.add_argument("-v", "--variable", help="variable to use", default="pr")
parser.add_argument("--biases", action="store_true")

args = parser.parse_args()

if args.biases:
	print "Going to calculate biases from reference data"

if args.config:
	config = json.loads(open(args.config).read())

print config['reference']

runs = []

for experiment in config["experiments"].keys():
	print "processing ", experiment

	for name, params in config["experiments"][experiment]["statistics"].items():
		print name, params

		submitters = os.listdir(args.source)
		for submitter in submitters:
			models = os.listdir("{}/{}".format(args.source, submitter))		
			for model in models:
				for varname in params["vars"]:
#					print "{}/{}/{}/{}/{}*_day_*.nc".format(args.source, submitter, model, experiment, varname)
					source_filenames = glob.glob("{}/{}/{}/{}/{}*_day_*.nc".format(args.source, submitter, model, experiment, varname))
					startdate = config["experiments"][experiment]["startdate"]
					enddate = config["experiments"][experiment]["enddate"]
					runs.append({"name":name, "filenames":source_filenames, "varname":varname, "startdate":startdate, "enddate":enddate, "params":params})


for run in runs:
	print run
	for filename in run["filenames"]:
		
		function = eval(run["params"]["function"])
		varname = run["varname"]

		if run["params"]["args"].has_key("aggregation"):
			if run["params"]["args"]["aggregation"] == "monthly":
				monthly_aggregate = True
		else:
			monthly_aggregate = False

		ds = pycdm.open(filename)
		print ds

		variable = ds.root.variables[varname]

		# Silly hack for datasets that don't have a coordinates attribute
		variable.attributes[u'coordinates'] = u"latitude longitude"

		field = pycdm.Field(variable)

		feature_dim = field.coordinates_mapping['latitude']['map'][0]

		print variable
		print "variable shape = ", variable.shape

		time_values, results = makestats(variable, function, **run["params"]["args"])

		if monthly_aggregate:
			results = monthly_climate(results, field.time_dim)
			time_values = time_values[:12]

		print "results shape = ", results.shape

		if args.biases:

			print "opening reference dataset: ", config["reference"][varname]
			ref_ds = pycdm.open(config['reference'][varname])
			ref_variable = ref_ds.root.variables[varname]
			ref_field = pycdm.Field(ref_variable)
			print "reference shape = ", ref_variable.shape

			startdate = dateparser.parse(run["startdate"])
			enddate = dateparser.parse(run["enddate"])

			ref_time_values, ref_results = makestats(ref_variable, function, after=startdate, before=enddate, **run["params"]["args"])
	
			if monthly_aggregate:
				ref_results = monthly_climate(ref_results, ref_field.time_dim)
				ref_time_values = ref_time_values[:12]

			print "reference results shape = ", ref_results.shape	

			# We are going to need the feature ids
			ref_ids = ref_ds.root.variables['id'][:]

			for id_name in ['id', 'station_id', 'stid']:
				try:
					ids = ds.root.variables[id_name][:]
				except:
					continue
				else:
					break
			
			# NetCDF3 files may have character arrays which need to be converted
			if len(ids.shape) > 1:
				new_ids = []
				for i in range(0,ids.shape[0]):
					tmp = u''
					for j in range(0, ids.shape[1]):
						tmp += ids[i,j]
					new_ids.append(tmp.strip())
				ids = np.array(new_ids)


			# IDs should be strings
			if ids.dtype != unicode:
				ids = ids.astype(int).astype(unicode)
			#print ids

			try:
				id_map = value_map(ids, ref_ids)
			except:
				"Aborting because I can't map IDs"
				continue

			if len(results.shape) == 3:
				dims = [0,1,2]

				for d in range(0,3):
					if d == feature_dim or d == field.time_dim:
						continue
					group_dim = d
					break
				print "group dimension = ", group_dim

				s = [slice(0,None)]*3
				rs = [slice(0,None)]*2
				for i in range(0,results.shape[group_dim]):
					
					s[group_dim] = slice(i,i+1)
					rs[1] = list(id_map)
					#print s, rs
					# We may have to transpose the ref_results
					try:
						results[tuple(s)] = results[tuple(s)] - ref_results[tuple(rs)].reshape(results[tuple(s)].shape)
					except:
						results[tuple(s)] = results[tuple(s)] - ref_results[tuple(rs)].reshape(results[tuple(s)].shape).T

			else:
				rs = [slice(0,None)]*2
				rs[1] = id_map
				#print rs
				# At this point we may have to transpose the ref_results
				try:
					results[:] = results[:] - ref_results[tuple(rs)].T
				except:
					results[:] = results[:] - ref_results[tuple(rs)]

			ref_ds.ncfile.close()

		ds.root.dimensions['time'] = pycdm.Dimension('time', len(time_values))
		print "results shape = ", results.shape

		data_dimensions = variable.dimensions
		data_attributes = variable.attributes

		ds.root.variables[varname] = pycdm.Variable(varname, ds.root, dimensions=data_dimensions, attributes=data_attributes, data=results)
		print "output variable shape: ", ds.root.variables[varname].shape

		time_attributes = field.time_variable.attributes

		ds.root.variables['time'] = pycdm.Variable('time', ds.root, dimensions=[u'time'], attributes=time_attributes, data=time_values)

		if args.biases:
			output_filename = filename.replace("_day_", "_{}_bias_".format(run["name"]))
		else:
			output_filename = filename.replace("_day_", "_{}_".format(run["name"]))

		print output_filename

		try:
			pycdm.plugins.netcdf4.netCDF4Dataset.copy(ds, output_filename, include=[varname, 'elevation', 'id'])
		except:
			print "FAILED, SOMETHING WENT WRONG!"

		ds.ncfile.close()
