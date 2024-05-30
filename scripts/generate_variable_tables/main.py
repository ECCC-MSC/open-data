#!/usr/bin/python
import argparse
import logging
import os

import yaml

from fileexplorer import find_files
from fileparser import parse_metadata

# Configuration file
config_file = 'config.yaml'

def main():
    # Load configurations
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    # Load datasets lookup table
    with open(config['model_file'], 'r') as file:
        model_LUT = yaml.safe_load(file)
    # Load variable translation lookup table
    with open(config['variable_file'], 'r') as file:
        variable_LUT = yaml.safe_load(file)
    # Load product translation lookup table
    with open(config['product_file'], 'r') as file:
        product_LUT = yaml.safe_load(file)
    # Load readable level lookup table
    with open(config['level_file'], 'r') as file:
        level_LUT = yaml.safe_load(file)
    
    # Default arguments
    path = f'/data/geomet/feeds/hpfx/'
    models = list(model_LUT.keys())

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--directory', default='.', help='Output directory (default: current directory). Caution: Existing files will be overwritten')
    parser.add_argument('--models', nargs='*', choices=models, default=models, metavar='MODELS', help=f'GRIB2 or NetCDF datasets (default: all datasets)')
    parser.add_argument('--path', default=path, help=f'Local directory path (default: {path})')
    parser.add_argument('--verbose', action='store_true', help='Print info messages to standard output')

    args = parser.parse_args()

    # Logging configuration
    if args.verbose:
        # Add module name, function name and line number
        logging.basicConfig(level=logging.INFO, format='(%(levelname)s) (%(asctime)s) (%(name)s %(module)s:%(funcName)s:L%(lineno)d) ::: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    else:
        logging.basicConfig(level=logging.WARNING, format='(%(levelname)s) (%(asctime)s) (%(name)s) ::: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # Create the root logger
    logger = logging.getLogger()

    # Check if path exists
    if not os.path.isdir(args.path):
        parser.error(f'Directory {path} does not exist')

    # Create output directory
    try:
        os.makedirs(args.directory, exist_ok=True)
        logger.info(f'Output directory {args.directory} created')
    except OSError as e:
        parser.error(e)

    for model in args.models:
        logger.info(f'Generating csv file for {model}')
        files = find_files(model_LUT[model], args.path)
        # Parse metadata for all files and print tables
        parse_metadata(files, args.directory, model, variable_LUT, product_LUT, level_LUT)

if __name__ == '__main__':
    main()
