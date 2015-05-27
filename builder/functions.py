import numpy as np
import numpy.ma as ma
import scipy.stats as stats


def value_map(source, target):
	"""
	Returns a list of indices that map source items to target items
	"""
	print "value map ", source, target
	return np.array(arange(0,len(source)))
	#return np.array([list(target).index(val) for val in list(source)])


def bias_mean(sample, reference, tdim=0):
	return ma.mean(sample, axis=tdim) - ma.mean(reference, axis=tdim)