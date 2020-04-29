#!/bin/bash

file=Vela_I_910_Cotninuum_flagged_subtracted.fits

../sf_spectral_lines/rms.py $file

../sf_spectral_lines/zero.py ${file%.fits}_rms.fits ${file%.fits}_bkg.fits

for i in {01..99}
do
    if [[ ! -e ${file%.fits}_${i}_comp.fits ]]
    then
        aegean --cores=6 --negative --slice=${i} --seedclip=7 --floodclip=4 --table=${file%.fits}_${i}.fits --background ${file%.fits}_bkg.fits --noise ${file%.fits}_rms.fits ${file}
        if [[ -e ${file%.fits}_${i}_comp.fits ]]
        then
            n=`fitshdr ${file%.fits}_${i}_comp.fits | grep NAXIS2 | awk '{print $3}'`
        else
            n=0
        fi
        echo "$i $n" >> detections.txt
    fi
done

../sf_spectral_lines/make_tcat.sh
chmod +x tcat.sh
./tcat.sh
