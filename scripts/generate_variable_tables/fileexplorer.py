import logging
import multiprocessing
import os
import re
import shutil
from urllib import error, request

import bs4

# Number of cpus
cpus = 8
# Module logger
logger = logging.getLogger(__name__)

class FileExplorer:
    def __init__(self, temporary):
        self.temporary = os.path.join(temporary, str(os.getpid()))

    def find_files(self, paths, directory):
        '''
        Find GRIB2 or NetCDF files in a local directory.

        Parameters:
                paths ([str]): Incomplete model paths
                directory (str): Local directory path
            Returns:
                files ([str]): File paths
        '''
        files = list()
        for path in paths:
            dir_path = os.path.join(directory, path)
            try:
                for file in os.listdir(dir_path):
                    if file.endswith(('.grib2', '.nc')):
                        files.append(os.path.join(dir_path, file))
            except OSError as e:
                logger.error(e)

        return files

    def download_files(self, paths, website):
        '''
        Download GRIB2 or NetCDF files.

            Parameters:
                paths ([str]): Incomplete model paths
                website (str): Server URL (HPFX, DD-Alpha)
            Returns:
                files ([str]): Downloaded file paths
    '''
        files = list()
        for path in paths:
            directory = os.path.join(self.temporary, path)
            url = os.path.join(website, path)

            # Create directory if it does not exist
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Open the URL and parse the page
            try:
                page = request.urlopen(url)
                soup = bs4.BeautifulSoup(page, "html.parser")
                links = soup.findAll('a', attrs={'href': re.compile("^(.*grib2|.*nc)$")})

                # Create list of tuples with urls and paths
                arguments = [(os.path.join(url, link.get('href')), os.path.join(directory, link.get('href'))) for link in links]

                # Download the files locally
                with multiprocessing.Pool(cpus) as pool:
                    results = pool.starmap(request.urlretrieve, arguments)
                logger.info(f'Downloaded {len(results)} files from {url}')
                files += [tuple[0] for tuple in results]
            except error.URLError as e:
                logger.error(e)

        return files

    def remove_files(self):
        # Remove temporary files
        if os.path.isdir(self.temporary):
            shutil.rmtree(self.temporary)
            logger.info(f'Temporary directory {self.temporary} removed')
