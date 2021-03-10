# usage: $ python grib_data_frame.py <grib-file-path>
import numpy as np
from IPython import embed as shell
import pygrib
import sklearn
import sys

f = pygrib.open(sys.argv[1])

all_gribs = [a for a in f]

outer = all_gribs[0].latlons()[0].shape[0]
inner = all_gribs[0].latlons()[0].shape[1]

lats = np.array(all_gribs[0].latlons()[0].reshape(outer*inner))
lons = np.array(all_gribs[0].latlons()[1].reshape(outer*inner))

surf_pres = np.array(all_gribs[401].values.reshape(1, outer*inner)[0])
surf_temp = np.array(all_gribs[403].values.reshape(1, outer*inner)[0])

shell()
