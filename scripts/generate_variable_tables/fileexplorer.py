import logging
import glob
import os

# Module logger
logger = logging.getLogger(__name__)

def find_files(paths, directory):
    '''
    Find GRIB2 or NetCDF files in a local directory.

    Parameters:
        paths ([str]): Incomplete model paths
        directory (str): Local directory path
    Returns:
        files ([str]): File paths
    '''
    files = []
    for path in paths:
        dir_path = os.path.join(directory, path)
        pattern_grib2 = os.path.join(dir_path, '**', '*.grib2')
        pattern_nc = os.path.join(dir_path, '**', '*.nc')
        try:
            for file in glob.glob(pattern_grib2, recursive=True):
                files.append(file)
            for file in glob.glob(pattern_nc, recursive=True):
                files.append(file)
        except OSError as e:
            logger.error(e)
        
    count = len(files)
    logger.info(f'Number of files found: {count}')

    return files
