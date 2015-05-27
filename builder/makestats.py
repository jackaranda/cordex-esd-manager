import netCDF4
import json
import sys
import argparse
import numpy, numpy.ma

from functions import *

sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm

parser = argparse.ArgumentParser()
parser.add_argument("source", default=None)
#parser.add_argument("target", default=None)
parser.add_argument("-c", "--config", help="configuration JSON file", default="diagnostics.json")
parser.add_argument("-s", "--statistic", help="name of diagnostic to run", default=None)
parser.add_argument("-a", "--aggregation", help="aggregation time period (month, year)", default="month")
parser.add_argument("-v", "--variable", help="variable to use", default="pr")

args = parser.parse_args()

if args.config:
	config = json.loads(open(args.config).read())

if args.source:
	single = True
else:
	single = False

if single:
	ds = pycdm.open(args.source)

print ds

variable = ds.root.variables[args.variable]
print variable

field = pycdm.Field(variable)
print field.coordinates_mapping

times = field.times
realtimes = field.realtimes

if args.aggregation == 'month':
	time_slices = field.time_slices(start=[{'day':1, 'hour':0}])
if args.aggregation == 'year':
	time_slices = field.time_slices(start=[{'day':1, 'month':1, 'hour':0}], length='1 year')

print len(time_slices)

time_values = numpy.array([field.times[s.stop-1] for s in time_slices])

results_shape = list(variable.shape)
results_shape[field.time_dim] = len(time_slices)
results_shape = tuple(results_shape)
results = numpy.ndarray(results_shape, dtype=variable[:].dtype)
print results_shape

print 'time dimension = ', field.time_dim
source_slices = [slice(None)]*len(results_shape)
target_slices = [slice(None)]*len(results_shape)

stats_function = np.ma.sum

for i in range(0, len(time_slices)):

	target_slices[field.time_dim] = slice(i,i+1)
	source_slices[field.time_dim] = time_slices[i]

	results[tuple(target_slices)] = stats_function(field.variables[0][tuple(source_slices)], axis=field.time_dim)

ds.root.dimensions['time'] = pycdm.Dimension('time', len(time_slices))

data_dimensions = variable.dimensions
data_attributes = variable.attributes
ds.root.variables[args.variable] = pycdm.Variable(args.variable, ds.root, dimensions=data_dimensions, attributes=data_attributes, data=results)

time_attributes = field.time_variable.attributes
ds.root.variables['time'] = pycdm.Variable('time', ds.root, dimensions=[u'time'], attributes=time_attributes, data=time_values)

pycdm.plugins.netcdf4.netCDF4Dataset.copy(ds, 'test_stats.nc', include=[args.variable, 'elevation', 'id'])

