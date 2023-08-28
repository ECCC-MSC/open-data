import logging
import multiprocessing
import os
import re
import shutil
from urllib import error, request

import bs4

cpus = 8
logger = logging.getLogger(__name__)

class FileExplorer:
    def __init__(self, website, temporary):
        self.website = website
        self.temporary = temporary

    def download_files(self, paths):
        '''
        Download GRIB2 or NetCDF files.

            Parameters:
                paths ([str]): Model paths
            Returns:
                files ([str]): Downloaded file paths
    '''
        files = list()
        for path in paths:
            url = os.path.join(self.website, path) 
            directory = os.path.join(self.temporary, path)

            # Create directory if it does not exist
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Open the URL and parse the page
            try:
                logger.info(f'Downloading files from: {url}')
                page = request.urlopen(url)
                soup = bs4.BeautifulSoup(page, "html.parser")
                links = soup.findAll('a', attrs={'href': re.compile("^(.*grib2|.*nc)$")})
    
                arguments = list()
                for link in links:
                    file_url = os.path.join(url, link.get('href'))
                    filename = os.path.join(directory, link.get('href'))
                    arguments.append((file_url, filename))

                # Download the files locally
                with multiprocessing.Pool(cpus) as pool:
                    results = pool.starmap(request.urlretrieve, arguments)
                files += [tuple[0] for tuple in results]
            except error.URLError as e:
                logger.error(e)

        # Print number of files found
        logger.info(f'Number of files found: {len(files)}')
        return files

    def remove_files(self):
        # Remove temporary files
        if os.path.isdir(self.temporary):
            logger.info(f'Removing temporary directory: {self.temporary}')
            shutil.rmtree(self.temporary)