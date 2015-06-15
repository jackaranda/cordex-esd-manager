python plotmap.models.py --vrange -1 1  --colors RdBu_r -v tasmax -s monmean_bias  ../results/
python plotmap.models.py --vrange -1 1  --colors RdBu_r -v tasmax -s tn95p_bias  ../results/
python plotmap.models.py --vrange -1 1  --colors RdBu_r -v tasmin -s monmean_bias  ../results/
python plotmap.models.py --vrange -20 20  --colors RdBu -v pr -s montotal_bias  ../results/
python plotmap.models.py --vrange -4 4  --colors RdBu -v pr -s wetdays_bias  ../results/
python plotmap.models.py --vrange -6 6  --colors RdBu -v pr -s r50p_bias  ../results/
python plotmap.models.py --vrange -6 6  --colors RdBu -v pr -s r95p_bias  ../results/
python plotmap.models.py --vrange -6 6  --colors RdBu -v pr -s r99p_bias  ../results/

