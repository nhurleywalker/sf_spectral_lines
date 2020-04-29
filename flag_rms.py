#!/usr/bin/env python

import numpy as np
import sys
from astropy.io import fits
import numpy as np
import argparse

def find_flags(data):
# Use the box around Puppis to decide what gets flagged
    layers = []
    for s in np.arange(0, data.shape[1]):
        layers.append(np.nanstd(data[:,s,1450:1750,1450:1750]))
    layers = np.array(layers)
    ind = np.where(layers > 1.2*good)
    return ind

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group1 = parser.add_argument_group("Input/output files")
    group1.add_argument("--subbed", dest='subbed', type=str, default=None,
                        help="Name of the continuum-subtracted cube from which to calculate the flags")
    group1.add_argument("--continuum", dest='continuum', type=str, default=None,
                        help="Name of the unsubtracted cube to which to apply flags")
    options = parser.parse_args()

    if options.subbed is None or options.continuum is None:
        parser.print_help()
        sys.exit()

    hdu = fits.open(options.subbed)
    cont = fits.open(options.continuum)
    # Find a typical RMS level in this image
    good = np.nanmean(np.nanstd(hdu[0].data[:,:,1000:1300,1000:1300], axis=1))
    # Find flags
    ind = find_flags(hdu[0].data)
    # Apply
    hdu[0].data[:,ind,:,:] = np.nan*np.ones((hdu[0].data.shape[0],1,hdu[0].data.shape[2],hdu[0].data.shape[3]))
    cont[0].data[:,ind,:,:] = np.nan*np.ones((hdu[0].data.shape[0],1,hdu[0].data.shape[2],hdu[0].data.shape[3]))

    # Repeat
    good = np.nanmean(np.nanstd(hdu[0].data[:,:,1000:1300,1000:1300], axis=1))
    ind = find_flags(hdu[0].data)
    hdu[0].data[:,ind,:,:] = np.nan*np.ones((hdu[0].data.shape[0],1,hdu[0].data.shape[2],hdu[0].data.shape[3]))
    cont[0].data[:,ind,:,:] = np.nan*np.ones((hdu[0].data.shape[0],1,hdu[0].data.shape[2],hdu[0].data.shape[3]))

    # Repeat
    good = np.nanmean(np.nanstd(hdu[0].data[:,:,1000:1300,1000:1300], axis=1))
    ind = find_flags(hdu[0].data)

    # Final apply
    cont[0].data[:,ind,:,:] = np.nan*np.ones((hdu[0].data.shape[0],1,hdu[0].data.shape[2],hdu[0].data.shape[3]))
    cont[0].data = cont[0].data.astype("float32")

    # Export
    cont.writeto(options.continuum.replace(".fits", "_flagged.fits"), overwrite=True)
