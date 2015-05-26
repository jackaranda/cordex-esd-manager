
import netCDF4
import json
import sys
import argparse

from functions import *

sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="configuration JSON file", default="diagnostics.json")
parser.add_argument("-d", "--diagnostic", help="name of diagnostic to run", default=None)
parser.add_argument("-s", "--sample", help="filename of sample dataset", default=None)
parser.add_argument("-v", "--variable", help="variable to use", default="pr")
parser.add_argument("-r", "--reference", help="filename of reference dataset", default=None)

args = parser.parse_args()

if args.config:
	config = json.loads(open(args.config).read())

if args.diagnostic:
	single = True
else:
	single = False

if args.reference:
	reference_path = args.reference
else:
	reference_path = config['reference']

if args.sample:
	sample_path = args.sample
else:
	sample_path = config['sample']


reference_ds = pycdm.open(reference_path)
reference_variable = reference_ds.root.variables[args.variable]
reference_field = pycdm.Field(reference_variable)
print reference_field.featuretype
print reference_field.shape

sample_ds = pycdm.open(sample_path)
#sample_variable = sample_ds.root.variables[args.variable]
sample_variable = sample_ds.root.variables['pr']
sample_field = pycdm.Field(sample_variable)
print sample_field.featuretype
print sample_field.shape

# If we have a point series we need to do some work to make sure the two arrays are compatible
feature_map = None
if reference_field.featuretype == "PointSeries" and sample_field.featuretype == "PointSeries":
	sample_ids = sample_ds.root.variables['id'][:]
	reference_ids = reference_ds.root.variables['id'][:]
	feature_map = value_map(sample_ids, reference_ids)
	print type(feature_map)

# Figure out the reference time slice
reference_times = reference_field.realtimes
sample_times = sample_field.realtimes
start = np.argwhere(reference_times >= sample_times[0])[0,0]
end = np.argwhere(reference_times <= sample_times[-1])[-1,0]+1

#print reference_variable[:]
#print sample_variable[:]
if type(feature_map) == np.ndarray:
	reference_variable = reference_variable[:][:,feature_map]

reference = reference_variable[:]
sample = sample_variable[:]



#print bias_mean(sample, reference)



