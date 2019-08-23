#!/bin/bash

echo "stilts tcat \\" > tcat.sh

for file in *comp.fits
do
    infiles="$infiles $file"
done

echo "in='$infiles' \\" >> tcat.sh

echo "out=concat.fits" >> tcat.sh
