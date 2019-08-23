#!/usr/bin/env python

import numpy as np
import sys
from astropy.io import fits
import numpy as np

infits = sys.argv[1]
hdu = fits.open(infits)
rms = np.nanstd(hdu[0].data, axis=1)
hdu[0].data = rms
hdu.writeto(infits.replace(".fits", "_rms.fits"))
