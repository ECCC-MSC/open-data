#!/bin/bash
# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2017 Government of Canada
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# =================================================================

if [ "$#" -lt 1 ]; then
    YAML_URL='http://gitlab.ssc.etg.gc.ca/ec-msc/geomet/raw/master/etc/geomet.yml'
else
    YAML_URL=$1/raw/master/etc/geomet.yml
fi

YAML='geomet.yml'
DOC_SRC='../public-data-documentation-src'
DOC_TXT='../public-data-documentation-txt'
DOC_MD='../public-data-documentation-md'
DD_BASEPATH='http://dd.weather.gc.ca/doc/'

echo -e '\nPUBLIC DATA DOCUMENTATION GENERATION SCRIPT \n '

echo -e '\t1/5 : Getting The yaml file from : ' ${YAML_URL}
if [ -f ${YAML} ]; then
    rm  ${YAML}
fi
wget ${YAML_URL} --quiet


echo -e "\t2/5 : Converting markdown into a txt format"
python markdown_to_txt/markdown_to_txt.py ${DOC_SRC} ${DOC_TXT} ${DD_BASEPATH}

if [ "$(ls -A ${DOC_MD})" ]; then
     rm -r ${DOC_MD}/*
fi
cp -r ${DOC_SRC}/* ${DOC_MD}

source python-package/bin/activate

echo -e "\t3/5 : Adding tables into markdown documentation"
python generate-geomet-data-tables/main.py ${YAML} ${DOC_MD} ${DOC_MD} default

echo -e "\t4/5 : Adding tables into txt documentation"
python generate-geomet-data-tables/main.py ${YAML} ${DOC_TXT} ${DOC_TXT} raw

echo -e "\t5/5 : Cleaning up"

if [ -f ${YAML} ]; then
    rm  ${YAML}
fi
deactivate

echo  "Done"


