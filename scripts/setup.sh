#!/bin/bash
# =================================================================
#
# Copyright (c) 2017 Government of Canada
#
# =================================================================

PYTHON=python-package

virtualenv -p python3 ${PYTHON}

source ${PYTHON}/bin/activate

pip install ruamel.yaml

deactivate