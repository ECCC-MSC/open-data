#!/usr/bin/python
import argparse
import logging
import os
import re
import sys
from datetime import datetime, timedelta
from urllib import error, request

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
temporary = '/data/geomet/dev/afsuxad/tmp/'

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
        "--url",
        default=url,
        type=str,
        help=f"Server URL to download GRIB2 and NetCDF files from (default: {url}).")

    class Show(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            width = 98
            print('=' * width)
            print(f'SHOWING ALL AVAILABLE DATASETS')
            print('=' * width)
            # Headers
            h = '|{:^20}|{:^75}|'
            print(h.format('dataset', 'path'))
            print('=' * width)
            # Data
            for key in model_LUT:
                for path in model_LUT[key]:
                    print(h.format( key, path ))
                    print('-' * width)
            print('DONE PRINTING ALL DATASETS, EXITING')
            parser.exit() # exit parser and program, ignore other arguments

    parser.add_argument(
        '--show',
        nargs=0,
        action=Show,
        help='Print all datasets and their paths. Note: All other options will be ignored.')
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print info messages to standard output.')

    args = parser.parse_args(input)

    # Logging configuration
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    # Validate input URL
    try:
        request.urlopen(args.url)
    except error.URLError as e:
        logging.error(e)
        exit(1)

    # Handle output directory
    if not os.path.exists(args.directory):
        if args.directory:
            logging.info(f'Creating temporary directory: {args.directory}')
            os.makedirs(args.directory)

    return args

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

    # Append year and month to CanSIPS URL
    if 'CanSIPS' in args.models:
        pattern = re.search('\d{8}', args.url)
        if not pattern is None:
            date = datetime.strptime(pattern.group(), "%Y%m%d")
            new_date = date.replace(day=1) + timedelta(days=31)
            cansips = model_LUT['CanSIPS'][0]
            model_LUT['CanSIPS'][0] = os.path.join(cansips, new_date.strftime('%Y/%m/'))

    explorer = FileExplorer(args.url, temporary)
    parser = FileParser(variable_LUT, product_LUT, level_LUT)

    for model in args.models:
        # Download files
        files = explorer.download_files(model_LUT[model])        
        # Parse metadata for all files and print tables
        parser.parse_metadata(files, args.directory, model)

    # Remove temporary directory
    explorer.remove_files()

if __name__ == '__main__':
    main()
