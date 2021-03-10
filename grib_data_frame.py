# usage: $ python grib_data_frame.py <grib-file-path>
import numpy as np
from IPython import embed as shell
import pygrib
import sys

f = pygrib.open(sys.argv[1])

all_gribs = [a for a in f]

lats = np.array(all_gribs[0].latlons()[0])[0]
lons = np.array(all_gribs[0].latlons()[1])[0]

surf_pres = all_gribs[401].values.reshape(1, all_gribs[401].values.shape[0]*all_gribs[401].values.shape[1])[0]
surf_temp = all_gribs[403].values.reshape(1, all_gribs[401].values.shape[0]*all_gribs[401].values.shape[1])[0]

shell()
