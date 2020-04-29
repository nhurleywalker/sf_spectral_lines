# sf_spectral_lines
Sripts for source-finding and measuring statistics on spectral line cubes.

 - aegean.sh: Master script to run the source-finding to search for noise
 - rms.py: generate an RMS map using the spectral axis
 - zero.py: generate a zero-background map with the same shape as the RMS map
 - calc.py: calculate Gaussian statistical expectations for various sigma levels
 - hist.py: plot a histogram of pixel values for a particular dataset
 - make_scaled_rms.py: scale the RMS map to match the local RMS of your particular slice (OBSOLETE WITH THE NEW CONTINUUM SUBTRACTION CODE)
 - make_tcat.sh: make a concatenation script for stils to run (tcat.sh) to join all the source-finding results together
