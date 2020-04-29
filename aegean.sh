#!/bin/bash

file=Vela_I_1932_Subtracted.fits

../rms.py $file

zero.py ${file%.fits}_rms.fits ${file%.fits}_bkg.fits

for i in {01..99}
do
    echo ${file} ${i}
    python ./make_scaled_rms.py ${file} ${i} ${file%.fits}_rms.fits
    aegean --cores=6 --negative --slice=${i} --seedclip=4.5 --floodclip=3.5 --table=${file%.fits}_${i}.fits --background ${file%.fits}_bkg.fits --noise ${file%.fits}_${i}_rms.fits ${file}
    if [[ -e ${file%.fits}_${i}_comp.fits ]]
    then
        n=`fitshdr ${file%.fits}_${i}_comp.fits | grep NAXIS2 | awk '{print $3}'`
    else
        n=0
    fi
    echo "$i $n" >> detections.txt
done

../make_tcat.sh
chmod +x tcat.sh
./tcat.sh


