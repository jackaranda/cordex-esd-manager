import sys
import numpy as np
import datetime
import glob
import argparse
import json
import os
import glob

sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from matplotlib.cm import ScalarMappable
    
parser = argparse.ArgumentParser()
parser.add_argument("source")
parser.add_argument("-c", "--config", default="diagnostics.json")
parser.add_argument("--vrange", nargs=2, type=float)
parser.add_argument("--colors", default="RdBu")
parser.add_argument("-v", "--varname", default="pr")
parser.add_argument("-s", "--statistic", default="montotal_bias")
parser.add_argument("-r", "--reference", default="reference")
parser.add_argument("-m", "--month", type=int)

args = parser.parse_args()
print args.month

config = json.loads(open(args.config).read())
varname = args.varname
statname = args.statistic
print statname

filenames = []
names = []
for experiment in config["experiments"].keys():
	print "processing ", experiment
	filenames = []
	names = []

	submitters = os.listdir(args.source)
	for submitter in submitters:
		models = os.listdir("{}/{}".format(args.source, submitter))		
		for model in models:
			print "{}/{}/{}/{}/{}*_{}_*.nc".format(args.source, submitter, model, experiment, varname, statname)
			tmp = glob.glob("{}/{}/{}/{}/{}*_{}_[0-9]*.nc".format(args.source, submitter, model, experiment, varname, statname))
			names.append("{} {}".format(submitter, model))
			if len(tmp) == 1:
				filenames.append(tmp[0])
			else:
				filenames.append(None)


	print "{} files found".format(len(filenames))


	vmax = -1e10
	vmin = 1e10
	fields = []
	goodnames = []
	index = 0
	for infilename in filenames:

		print infilename, varname
		
		try:
			ds = pycdm.open(infilename)
			variable = ds.root.variables[varname]
			field = pycdm.Field(variable)

			vmax = max(vmax, np.ma.max(field.variables[0][:]))
			vmin = min(vmin, np.ma.min(field.variables[0][:]))
		except:
			#fields.append(None)
			index += 1
			pass
		else:
			fields.append(field)
			goodnames.append(names[index])
			index += 1

	vmin = -20
	vmax = 20

	if args.vrange:
		vmin, vmax = args.vrange[0], args.vrange[1]

	print "value range = ", vmin, vmax

	# Setup the plot
	fig = plt.figure(figsize=(10,8))
	ax = fig.add_axes([0.0,0.0,1.0,1.0])
	ax.axis('off')

	index = 1
	for field in fields:

		print goodnames[index-1], field

		if field == None:
			index += 1
			continue

		variable = field.variables[0]
		realtimes = field.realtimes
		features = field.features
		data = variable[:]

		latitudes = field.latitudes
		longitudes = field.longitudes

		latmin = latitudes.min() - 2
		latmax = latitudes.max() + 2
		lonmin = longitudes.min() - 2
		lonmax = longitudes.max() + 2

		feature_dim = field.coordinates_mapping['latitude']['map'][0]
		print "time dim = ", field.time_dim
		print "feature_dim = ", feature_dim
		print "variable shape = ", variable.shape

		# Use the median of ensemble data
		if len(variable.shape) == 3:
			dims = [0,1,2]

			for d in range(0,3):
				if d == feature_dim or d == field.time_dim:
					continue
				group_dim = d
				break
			print "group dimension = ", group_dim
			data = np.median(data, axis=dims.index(group_dim))
			del dims[group_dim]
			print dims
			time_dim = dims.index(field.time_dim)
		else:
			dims = [0,1]
			time_dim = field.time_dim

		print "new time dim = ", time_dim
		print "data.shape = ", data.shape

		s = [slice(0,None)] * len(data.shape)

		if args.month:
			print "only month", args.month
			s[time_dim] = slice(args.month-1,args.month)
			vals = data[tuple(s)]
		else:
			print "mean of all months"
			vals = np.mean(data, axis=time_dim)

		print "vals.shape = ", vals.shape

		ax = fig.add_subplot(3,4,index)
		m = Basemap(projection='merc',llcrnrlat=latmin,urcrnrlat=latmax,\
		            llcrnrlon=lonmin,urcrnrlon=lonmax,lat_ts=25,resolution='h')
			
		x, y = m(longitudes, latitudes)

		#m.drawmapboundary(fill_color='#c0c0ff')
		m.drawcoastlines(linewidth=1.0, color='#101010')
		m.drawcountries(linewidth=0.1, color='#404040')

		m.drawparallels(np.arange(-90.,120.,15.))
		m.drawmeridians(np.arange(0.,420.,15.))

		#m.fillcontinents(color='#c0c0c0',lake_color='#8080ff', zorder=0)
		print vals
		m.scatter(x,y,s=80, c=vals, marker='o', cmap=args.colors, vmin=vmin, vmax=vmax, alpha=0.7)
		
		plt.title(goodnames[index-1], size='xx-small')
		index += 1

	#for i, txt in enumerate(range(0,len(latitudes))):
	    
	#    ax.annotate(names[i], (x[i], y[i]), size='small')

	mappable = ScalarMappable(cmap=args.colors)
	mappable.set_array(np.arange(vmin,vmax,0.1))
	mappable.set_clim((vmin,vmax))
	    
	colorbar_ax = fig.add_axes([0.93, 0.05, 0.02, 0.4])
	plt.colorbar(mappable, cax=colorbar_ax)
	plt.tight_layout()

	outfilename = "../plots/{}_{}_{}_allmodels_map.png".format(experiment, varname, statname)
	plt.savefig(outfilename)
