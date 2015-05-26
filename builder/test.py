import sys
import os
import psycopg2
import zipfile
from shutil import rmtree



sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm
print pycdm.Dataset.__subclasses__()

#source = '/home/cjack/work/projects/research/cordex/statistical/experiment1/uploads//mathieu.vrac/analog/tier-1/uploaded/tmp'
source = '/home/cjack/work/projects/research/cordex/statistical/experiment1/uploads/maria.laura.bettolli/analogue-method-uba/tier-1/uploaded/tmp/'
#source = '/home/cjack/work/projects/research/cordex/statistical/experiment1/uploads//mathieu.vrac/swg/tier-1/uploaded/tmp3/'

ds = pycdm.open(source)
pycdm.plugins.netcdf4.netCDF4Dataset.copy(ds, 'test2.nc')