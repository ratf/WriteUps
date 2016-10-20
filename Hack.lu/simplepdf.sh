#!/bin/bash

# Extract the attachment of the first pdf file
# https://cthulhu.fluxfingers.net/static/chals/simplepdf_f8004a3ad0acde31c40267b9856e63fc.pdf
# get the pdf10000.pdf and use the script.

for ((i=10000; i >=0; i--))
do
    pdfdetach -saveall pdf$i.pdf
    echo $i
done
