import numpy as np
import sys
from astropy.io import fits
from scipy.stats import norm
from matplotlib import pyplot as plt

hdu = fits.open("Vela_I_1290_Subtracted.fits")
subset = hdu[0].data[:,:,1150:2265,785:1978]
minx = np.nanmin(subset)
maxx = np.nanmax(subset)
flat = np.ndarray.flatten(subset)
std = np.nanstd(flat)
print std
bins = np.arange(-0.28, 0.28, 0.01)
mu = 0
sigma = std
x1 = -0.28
x2 = 0.28
fig = plt.figure()
ax = fig.add_subplot(111)
n, bins, patches = ax.hist(flat, bins, facecolor="blue", alpha=0.5)
ratio = max(n)/norm.pdf(0, 0, std)
y = ratio*norm.pdf(bins, mu, sigma)
ax.plot(bins, y, lw=2)
ax.axvline(-std, c="red", ls="--", lw=2)
ax.axvline(std, c="red", ls="--", lw=2)
ax.axvline(-5*std, c="red", ls="-.", lw=2)
ax.axvline(5*std, c="red", ls="-.", lw=2)
fig.savefig("pixel_hist_for_const_noise_region.png")
ax.set_yscale("log")
fig.savefig("pixel_hist_for_const_noise_region_log.png")
