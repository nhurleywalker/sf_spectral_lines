#!/usr/bin/env python

from astropy.io import fits
import numpy as np
import sys

print "make_scaled_rms.py <input cube file> <slice number> <spectral rms file>"

infits = sys.argv[1]
inslice = sys.argv[2]

hdu = fits.open(infits)
subset = hdu[0].data[:, int(inslice)-1, 1000:1250, 1000:1250]
rms = np.nanstd(subset)

hdu_spec = fits.open(sys.argv[3])
subset_spec = hdu_spec[0].data[:, 1000:1250, 1000:1250]
rms_spec = np.nanmean(subset_spec)

ratio = rms / rms_spec

hdu_spec[0].data *= ratio

with open('ratios.txt', 'a') as the_file:
    the_file.write("{0} {1}\n".format(inslice,ratio))

hdu_spec.writeto(infits.replace(".fits", "_"+inslice+"_rms.fits"))
