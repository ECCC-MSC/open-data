#!/usr/bin/python
import argparse
import logging
import os

import yaml

from fileexplorer import find_files, sync_files, delete_files
from fileparser import parse_metadata

# Root directory of script
root_dir = os.path.dirname(os.path.realpath(__file__))

# Lookup tables files
model_file = os.path.join(root_dir, 'lookup_tables/datasets.yml')
variable_file = os.path.join(root_dir, 'lookup_tables/variable_translation.yml')
product_file = os.path.join(root_dir, 'lookup_tables/product_translation.yml')
level_file = os.path.join(root_dir, 'lookup_tables/readable_level.yml')

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
    
    # Default arguments
    directory = os.path.join(os.getcwd(), 'variable_tables')
    path = f'/data/geomet/feeds/hpfx/'
    models = list(model_LUT.keys())
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--directory', default=directory, help='Output directory (default: current directory). Caution: Existing files will be overwritten')
    parser.add_argument('--models', nargs='*', choices=models, default=models, metavar='MODELS', help=f'GRIB2 or NetCDF datasets (default: all datasets)')
    parser.add_argument('--path', default=path, help=f'Directory path on current machine or remote host (default: {path})')
    parser.add_argument('--user_at_host', help='Copy files from host with user. Ignore to read files on current machine')
    parser.add_argument('--verbose', action='store_true', help='Print info messages to standard output')

    args = parser.parse_args()

    # Logging configuration
    if args.verbose:
        # Add module name, function name and line number
        log_level = logging.DEBUG
        log_format = '(%(levelname)s) (%(asctime)s) (%(name)s %(module)s:%(funcName)s:L%(lineno)d) ::: %(message)s'
    else:
        log_level = logging.INFO
        log_format = '(%(levelname)s) (%(asctime)s) (%(name)s) ::: %(message)s'
    logging.basicConfig(level=log_level, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

    # Create the root logger
    logger = logging.getLogger()

    # Check if path exists on current machine
    if not args.user_at_host:
        if not os.path.isdir(args.path):
            parser.error(f'Directory {args.path} does not exist')

    # Create output directory
    try:
        os.makedirs(args.directory, exist_ok=True)
        logger.info(f'Output directory {args.directory} created')
    except OSError as e:
        parser.error(e)

    for model in args.models:
        logger.info(f'Generating csv file for {model}')
        if args.user_at_host:
            files = sync_files(model_LUT[model], args.user_at_host, args.path, args.directory)
        else:
            files = find_files(model_LUT[model], args.path)
        # Parse metadata for all files and print tables
        parse_metadata(files, args.directory, model, variable_LUT, product_LUT, level_LUT)
        # Delete temporary files 
        if args.user_at_host:
            logger.info(f'Deleting files for {model}')
            delete_files(files)

if __name__ == '__main__':
    main()
