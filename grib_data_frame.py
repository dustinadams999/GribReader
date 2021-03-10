import numpy as np
from IPython import embed as shell
import pygrib
import sys

f = pygrib.open(sys.argv[1])
shell()

all_gribs = [a for a in f]

