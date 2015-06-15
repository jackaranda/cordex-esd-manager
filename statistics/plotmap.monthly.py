import sys
import os
import numpy as np
import datetime
import glob

sys.path.append('/home/cjack/work/projects/code/pycdm2/')
import pycdm


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from matplotlib.cm import ScalarMappable
    
infilename = sys.argv[1]
varname = sys.argv[2]
cmap = sys.argv[3]
vmin = float(sys.argv[4])
vmax = float(sys.argv[5])

ds = pycdm.open(infilename)
variable = ds.root.variables[varname]
field = pycdm.Field(variable)
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
	time_dim = dims.index(field.time_dim)

else:
	dims = [0,1]
	time_dim = field.time_dim

print "new time dim = ", field.time_dim
print "data.shape = ", data.shape

#vmin = np.min(data)*1.1
#vmax = np.max(data)/1.1

#vmax = max(vmax, -1*vmin)
#vmin = min(vmin, -1*vmax)
print "value range ", vmin, vmax

# Setup the plot
fig = plt.figure(figsize=(12,8))
ax = fig.add_axes([0.0,0.0,1.0,1.0])
ax.axis('off')


for m in range(0,12):

	s = [slice(0,None)] * len(data.shape)
	s[time_dim] = slice(m,m+1)
	vals = data[tuple(s)]

	print "vals.shape = ", vals.shape

	date = realtimes[m]

	ax = fig.add_subplot(3,4,m+1)

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
	m.scatter(x,y,s=80, c=vals, marker='o', cmap=cmap, vmin=vmin, vmax=vmax, alpha=0.7)
	print date.strftime("%b")
	plt.title(date.strftime("%b"))

#for i, txt in enumerate(range(0,len(latitudes))):
    
#    ax.annotate(names[i], (x[i], y[i]), size='small')

mappable = ScalarMappable(cmap=cmap)
mappable.set_array(np.arange(vmin,vmax,0.1))
mappable.set_clim((vmin,vmax))

    
colorbar_ax = fig.add_axes([0.93, 0.05, 0.02, 0.4])
plt.colorbar(mappable, cax=colorbar_ax)
plt.tight_layout()

outfilename = "{}.monthly.png".format(os.path.splitext(infilename)[0])
plt.savefig(outfilename)
