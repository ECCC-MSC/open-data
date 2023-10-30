#!/usr/bin/python
import argparse
import logging
import os
import re
import sys
from datetime import datetime, timedelta

import yaml

from fileexplorer import FileExplorer
from fileparser import FileParser

# Datasets lookup table
model_file = './datasets.yml'
# Variable translation lookup table
variable_file = './variable_translation.yml'
product_file = './product_translation.yml'
# Readable level lookup table
level_file = './readable_level.yml'

# Temporary directory
temporary = f'/fs/project/eccc/cmod/cmoa/edouards/public-doc/variable_tables/work'
# Root logger
logging.basicConfig()
logger = logging.getLogger()

def read_args(input, model_LUT):
    """
    Parse and validate input arguments.
        
        Parameters:
            input ([str]): Input arguments
            model_LUT (dict): Datasets with their paths
        Returns:
            args (Namespace): Parsed arguments
    """
    # Formated date
    time = datetime.now() - timedelta(1)
    yesterday = time.strftime("%Y%m%d")
    
    # Default arguments
    url = f"http://hpfx.collab.science.gc.ca/{yesterday}/WXO-DD/"
    models = list(model_LUT.keys())

    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--directory",
        default=".",
        type=str,
        help="Output directory (default: current directory). Caution: Existing files will be overwritten. ")
    parser.add_argument(
        "--models",
        nargs="*",
        choices=models,
        default=models,
        metavar="MODELS",
        type=str,
        help=f"GRIB2 or NetCDF datasets (default: all datasets).")
    parser.add_argument(
        "--path",
        default=url,
        type=str,
        help=f"Server URL or local directory (default: {url}).")
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print info messages to standard output.')

    args = parser.parse_args(input)

    # Logging configuration
    if args.verbose:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    # Create output directory
    try:
        os.makedirs(args.directory, exist_ok=True)
        logger.info(f'Temporary directory {args.directory} created')
    except OSError as e:
        logger.error(e)
        exit(1)

    return args

def append_date(path, cansips):
    '''
    Append year and month to CanSIPS path.

        Parameters:
            path (str): URL with date to extract
            cansips (str): CanSIPS path without year and month
        Returns:
            cansips (str): CanSIPS path with year and month
    '''
    # Search for date in url
    pattern = re.search('\d{8}', path)
    if pattern is None:
        return cansips
    
    try:
        # Create datetime from pattern
        date = datetime.strptime(pattern.group(), "%Y%m%d")
    except ValueError as e:
        logger.error(e)
        return cansips
    
    # Jump to next month
    new_date = date.replace(day=1) + timedelta(days=31)
    # Convert date to YYYY/MM format
    return os.path.join(cansips, new_date.strftime('%Y/%m/'))

def main():
    # Load datasets lookup table
    with open(model_file, 'r') as file:
        model_LUT = yaml.safe_load(file)
    # Load variable translation lookup table
    with open(variable_file, 'r') as file:
        variable_LUT = yaml.safe_load(file)
    # Load product translation lookup table
    with open(product_file, 'r') as file:
        product_LUT = yaml.safe_load(file)
    # Load readable level lookup table
    with open(level_file, 'r') as file:
        level_LUT = yaml.safe_load(file)

    # Get input arguments
    args = read_args(sys.argv[1:], model_LUT)

    explorer = FileExplorer(temporary)
    parser = FileParser(variable_LUT, product_LUT, level_LUT)

    # Append year and month to CanSIPS URL
    if 'CanSIPS' in args.models:
        model_LUT['CanSIPS'][0] = append_date(args.path, model_LUT['CanSIPS'][0])

    for model in args.models:
        if os.path.isdir(args.path):
            files = explorer.find_files(model_LUT[model], args.path)
        else:
            files = explorer.download_files(model_LUT[model], args.path)
        # Parse metadata for all files and print tables
        parser.parse_metadata(files, args.directory, model)

    # Remove temporary directory
    explorer.remove_files()

if __name__ == '__main__':
    main()
