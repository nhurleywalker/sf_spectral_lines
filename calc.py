#!/usr/bin/env python

import numpy as np
import sys
from scipy.special import erf
from scipy.stats import norm
import matplotlib.pyplot as plt

def phi(x):
   return 0.5 * (1 + erf(x / np.sqrt(2)))

def A(x):
   return 0.5 * erf(x / np.sqrt(2))

ncubes = 1 # Number of cubes we're searching
nx = 2500 # size of image x-dimension
ny = 2500 # size of image y-dimension
nc = 100 # number of channels in a cube
pflag = 0.01 # proportion of flagged channels
pix2deg = 0.0065 # size of a pixel in degrees
bmaj = 0.0345583 # beam major axis (typical) in deg
bmin = 0.0277333 # beam minor axis (typical) in deg

#nx = 1200 # size of image x-dimension
#ny = 1200 # size of image y-dimension

# Simulated dataset
#nx = 10000 # size of image x-dimension
#ny = 10000 # size of image y-dimension
#nc = 100
#pflag = 0.99
#pix2deg = 0.02
#bmaj = 0.07
#bmin = 0.07

bvol = bmaj*bmin*np.pi / (pix2deg * pix2deg * 4 * np.log(2))

nsamps = ncubes * nx * ny * nc * (1 - pflag) / bvol # number of "independent" data samples

minsigma=5.0
maxsigma=10.0

print("We are searching {0:3.0f} million quasi-independent samples".format(nsamps * 1.e-6))
print("By chance, between {0:3.2f} and {1:3.2f} sigma, we would expect to see {2:3.2f} false positive detections and {2:3.2f} false negative detections.".format(minsigma, maxsigma, nsamps* (A(maxsigma) - A(minsigma))))

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = norm.stats(moments='mvsk')
x = np.linspace(norm.ppf(0.68), norm.ppf(1-1e-10), 15000)
ax.semilogy(x, nsamps*norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')
ax.set_ylabel("probability density function")
ax.set_xlabel("sigma")
ax.axvline(x = minsigma, color='blue')
ax.axvline(x = maxsigma, color='blue')
fig.savefig('dist.png')
