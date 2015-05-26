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
print field.time_slices(start=[{'day':1, 'hour':12}])