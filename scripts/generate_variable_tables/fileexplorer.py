import logging
import glob
import os
import subprocess

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

def sync_files(paths, user_at_host, src_dir, dst_dir):
    for path in paths:
        src_path = os.path.join(src_dir, path)
        dst_path = os.path.join(dst_dir, path)

        try:
            os.makedirs(dst_path, exist_ok=True)
            logger.info(f'Destination directory {dst_path} created')
        except OSError as e:
            logger.error(e)
            exit(1)
        
        subprocess.run(['rsync', '-rq', f'{user_at_host}:{src_path}', dst_path])

    return find_files(paths, dst_dir)

def delete_files(list_files):
    for file in list_files:
        if os.path.exists(file):
            os.remove(file)
            logger.info(f'File {file} was deleted')
