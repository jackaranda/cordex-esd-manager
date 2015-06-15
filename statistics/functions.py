import numpy as np
import numpy.ma as ma
import scipy.stats as stats

import sys
sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm

def value_map(source, target):
	"""
	Returns a list of indices that map source items to target items
	"""
	return np.array([list(target).index(val) for val in list(source)])

def time_subset(field, start=None, end=None):

	realtimes = field.realtimes

	data_slice = [slice(None)]*len(field.variables[0].shape)

	if type(realtimes) == np.ndarray:

		if start == None or start < realtimes[0]:
			start = realtimes[0]

		if end == None or end > realtimes[-1]:
			end = realtimes[-1]

		time_select = np.where(np.logical_and(realtimes >= start,realtimes <= end))[0]
		#print time_select

		data_slice[field.time_dim] = slice(time_select[0], time_select[-1])
		data_slice = tuple(data_slice)
	
	return data_slice

def makestats(variable, function, aggregation=None, after=None, before=None, mask_below=None, mask_above=None):

	field = pycdm.Field(variable)
	times = field.times
	realtimes = field.realtimes

	print "from ", after, " to ", before

	print "aggregation = ", aggregation
	if aggregation == 'monthly':
		time_slices = field.time_slices(start=[{'day':1, 'hour':12}], after=after, before=before)
	elif aggregation == 'annual':
		time_slices = field.time_slices(start=[{'day':1, 'month':1, 'hour':12}], length='1 year', after=after, before=before)
	else:
		time_slices = [slice(0,len(realtimes))]

	time_values = np.array([field.times[s.stop-1] for s in time_slices])

	results_shape = list(variable.shape)
	results_shape[field.time_dim] = len(time_slices)
	results_shape = tuple(results_shape)
	results = np.ndarray(results_shape, dtype=variable[:].dtype)
	print results_shape

	print 'time dimension = ', field.time_dim
	source_slices = [slice(None)]*len(results_shape)
	target_slices = [slice(None)]*len(results_shape)

	for i in range(0, len(time_slices)):
#		print i, realtimes[time_slices[i].start], realtimes[time_slices[i].stop-1]
		target_slices[field.time_dim] = slice(i,i+1)
		source_slices[field.time_dim] = time_slices[i]
		target_shape = results[tuple(target_slices)].shape

		source = variable[tuple(source_slices)]
		source = np.ma.masked_array(source)
		if mask_below:
			source = np.ma.masked_less(source, mask_below)
		if mask_above:
			source = np.ma.masked_greater(source, mask_above)

		#print source
		#print source.shape, target_shape
		tmp = np.reshape(function(source, axis=field.time_dim), target_shape)

		results[tuple(target_slices)] = tmp

	return time_values, results

def monthly_climate(data, time_dim):

	shape = list(data.shape)
	source_slice = [slice(0,None)]*len(data.shape)
	result_slice = [slice(0,None)]*len(data.shape)

	result_shape = shape
	result_shape[time_dim] = 12

	result = np.empty(tuple(result_shape))

	for m in range(0,12):
		source_slice[time_dim] = slice(m, None, 12)
		result_slice[time_dim] = slice(m, m+1)
		print "monthly_climate source shape ", data[tuple(source_slice)].shape
		result[tuple(result_slice)] = np.mean(data[tuple(source_slice)], axis=time_dim).reshape(result[tuple(result_slice)].shape)

	return result


def r50p(data, axis=None):
	data = np.ma.masked_array(data)
	data = np.ma.masked_less(data, 0.2)
	return np.nanpercentile(data.filled(np.nan), 50, axis=axis)

def t5p(data, axis=None):
	data = np.ma.masked_array(data)
	return np.nanpercentile(data.filled(np.nan), 5, axis=axis)

def r95p(data, axis=None):
	data = np.ma.masked_array(data)
	data = np.ma.masked_less(data, 0.2)
	return np.nanpercentile(data.filled(np.nan), 95, axis=axis)

def t95p(data, axis=None):
	data = np.ma.masked_array(data)
	return np.nanpercentile(data.filled(np.nan), 95, axis=axis)

def r99p(data, axis=None):
	data = np.ma.masked_array(data)
	data = np.ma.masked_less(data, 0.2)
	return np.nanpercentile(data.filled(np.nan), 99, axis=axis)

def t99p(data, axis=None):
	data = np.ma.masked_array(data)
	return np.nanpercentile(data.filled(np.nan), 99, axis=axis)
def wetdays(data, axis=None):
	data = np.ma.masked_array(data)
	data = data.filled(-99.0)
	data = np.ma.masked_less(data, 0.2)
	return np.ma.count(data, axis=axis)
