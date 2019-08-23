#!/usr/bin/env python

# Zero a fitsfile

import sys
import numpy as np

# fits files
try:
    import astropy.io.fits as fits
except ImportError:
    import pyfits as fits

file1=sys.argv[1]
output=sys.argv[2]

print "Blanking "+file1

hdu1=fits.open(file1)
hdu1[0].data = np.zeros(hdu1[0].data.shape)
hdu1.writeto(output,clobber=True)
