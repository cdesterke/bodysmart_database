#!/bin/bash

grep -E DATE MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > DATE 
grep -E NAME MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > NAME
grep -E SEXE MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > SEXE
grep -E WEIGHT_KG MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > WEIGHT_KG
grep -E SIZE_CM MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > SIZE_CM
grep -E AGE_YEARS MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > AGE_YEARS
grep -E BODY_MASS_INDEX MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > BODY_MASS_INDEX
grep -E BODY_SURFACE_MOSTELLER_M2 MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > BODY_SURFACE_MOSTELLER_M2
grep -E IDEAL_WEIGHT_LORENTZ_KG MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > IDEAL_WEIGHT_LORENTZ_KG
grep -E IDEAL_WEIGHT_DEVINE_KG MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > IDEAL_WEIGHT_DEVINE_KG
grep -E IDEAL_WEIGHT_PECK_KG MY_BODY_DATA.txt | awk -F "\t" '{print $2}' > IDEAL_WEIGHT_PECK_KG

paste DATE NAME SEXE WEIGHT_KG SIZE_CM AGE_YEARS BODY_MASS_INDEX BODY_SURFACE_MOSTELLER_M2 IDEAL_WEIGHT_LORENTZ_KG IDEAL_WEIGHT_DEVINE_KG IDEAL_WEIGHT_PECK_KG | awk -F "\t" '{print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6"\t"$7"\t"$8"\t"$9"\t"$10"\t"$11}'> table.tsv

echo  "DATE \tNAME \tSEXE \tWEIGHT_KG \tSIZE_CM \tAGE_YEARS \tBODY_MASS_INDEX \tBODY_SURFACE_MOSTELLER_M2 \tIDEAL_WEIGHT_LORENTZ_KG \tIDEAL_WEIGHT_DEVINE_KG \tIDEAL_WEIGHT_PECK_KG"  > headers.tsv

cat headers.tsv table.tsv > my_body_table.tsv

rm DATE
rm NAME
rm SEXE
rm WEIGHT_KG
rm SIZE_CM
rm AGE_YEARS
rm BODY_MASS_INDEX
rm BODY_SURFACE_MOSTELLER_M2
rm IDEAL_WEIGHT_LORENTZ_KG
rm IDEAL_WEIGHT_DEVINE_KG
rm IDEAL_WEIGHT_PECK_KG




