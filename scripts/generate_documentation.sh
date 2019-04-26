#!/bin/bash
# =================================================================
#
# Copyright (c) 2017 Government of Canada
#
# =================================================================

if [ "$#" -lt 1 ]; then
    YAML_URL='https://gccode.ssc-spc.gc.ca/ec-msc/geomet/raw/master/etc/geomet.yml'
else
    YAML_URL=$1/raw/master/etc/geomet.yml
fi

YAML='geomet.yml'
DOC_SRC='../public-data-documentation-src'
DOC_TXT='../public-data-documentation-txt'
DOC_MD='../public-data-documentation-md'
DD_BASEPATH='http://dd.weather.gc.ca/doc/'

echo -e '\nPUBLIC DATA DOCUMENTATION GENERATION SCRIPT \n '

echo -e '\t1/5: Getting The yaml file from: ' ${YAML_URL}
if [ -f ${YAML} ]; then
    rm  ${YAML}
fi
wget ${YAML_URL} --quiet


echo -e "\t2/5: Converting markdown into a txt format"
python markdown_to_txt/markdown_to_txt.py ${DOC_SRC} ${DOC_TXT} ${DD_BASEPATH}

if [ "$(ls -A ${DOC_MD})" ]; then
     rm -r ${DOC_MD}/*
fi
cp -r ${DOC_SRC}/* ${DOC_MD}

source python-package/bin/activate

echo -e "\t3/5: Adding tables into markdown documentation"
python generate-geomet-data-tables/main.py ${YAML} ${DOC_MD} ${DOC_MD} default

echo -e "\t4/5: Adding tables into txt documentation"
python generate-geomet-data-tables/main.py ${YAML} ${DOC_TXT} ${DOC_TXT} raw

echo -e "\t5/5: Cleaning up\n"

if [ -f ${YAML} ]; then
    rm  ${YAML}
fi
deactivate

echo  "Done"
