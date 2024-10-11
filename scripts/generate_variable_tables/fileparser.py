import logging
import os

from osgeo import gdal

# Module logger
logger = logging.getLogger(__name__)

def generate_row(language, variable_name, level_key, variable_LUT, level_LUT):
    '''
        Create a formatted table row from metadata.
        Translate metadata to english or french with lookup tables.
        Parameters:
            language (str): "EN" for english or "FR" for french
            variable_name (str): Variable name
            level_key (str): Variable level
            variable_LUT (dict): Variables lookup table
            level_LUT (dict): Levels lookup table
        Returns:
            row (str): Formatted table row   
    '''
    var_keys = [key for key in variable_LUT if key.lower() in variable_name.lower()]
    # Convert variable with lookup table
    if var_keys:
        var_key = ""
        for key in var_keys:
            if len(key) > len(var_key):
                var_key = key
        variable = variable_LUT[var_key]['Variable'][language]
        abbreviation = variable_LUT[var_key]['Abbreviation']
        unit = variable_LUT[var_key]['Unit'][language]
    else:
        logger.warning(f'Variable {variable_name} not found')
        variable = variable_name
        abbreviation = 'unknown'
        unit = 'unknown'
    # Convert level with lookup table
    if level_key in level_LUT:
        level = level_LUT[level_key][language]
    elif level_key is None:
        level = 'Surface'
    else:
        logger.warning(f'Level {level_key} not found')
        level = level_key
    # Return formatted row
    return f'{variable},{abbreviation},{level},{unit}'

def write_variable_table(data, filename, header):
    '''
    Write GRIB2 or NetCDF variable table into file.

        Parameters:
            data ([str]): Table rows
            filename (str): File path
            header (str): Table header
    '''
    # Remove duplicate lines in the list
    data = list(dict.fromkeys(data))
    # Sort list by variable name
    data.sort()
    # Delete existing file
    if os.path.exists(filename):
        os.remove(filename)
        logger.info(f'File {filename} removed')
    # Open the file
    out = open(filename, 'w')
    # Write the header and variables
    out.write(f'{header}\n')
    for line in data:
        out.write(f'{line}\n')
    # Close the files
    out.close()
    logger.info(f'File {filename} created')

def parse_metadata(files, directory, model, variable_LUT, product_LUT, level_LUT):
    '''
    Open GRIB2 or NetCDF files and read their metadata.
    Generate tables in english and french from metadata.
        
    Parameters:
        files ([str]): GRIB2 or NetCDF files.
        directory (str): Directory in which files will be written
        model (str): Dataset name used for file name
        variable_LUT (dict): Variables lookup table
        products_LUT (dict): Products lookup table
        level_LUT (dict): Levels lookup table
    '''
    # GDAL configuration options
    gdal.SetConfigOption('GRIB_NORMALIZE_UNITS', 'NO')
    
    data_en = []
    data_fr = []
    prod_data_en = []
    prod_data_fr = []
    # Get metadata for all files
    for file in files:
        try:
            # Open the file to get the dataset
            dataset = gdal.Open(file)
            for i in range(1, dataset.RasterCount + 1):
                # Get the dataset metadata
                if file.endswith('.grib2'):
                    name = dataset.GetRasterBand(i).GetMetadataItem('GRIB_COMMENT')
                    level = dataset.GetRasterBand(i).GetMetadataItem('GRIB_SHORT_NAME')
                elif file.endswith('.nc'):
                    name = dataset.GetRasterBand(i).GetMetadataItem('long_name')
                    level = dataset.GetRasterBand(i).GetMetadataItem('NETCDF_DIM_depth')
                # Insert metadata in variable or product lists
                prod_keys = [key for key in product_LUT if key.lower() in name.lower()]
                if prod_keys:
                    prod_data_en.append(generate_row('EN', name, level, product_LUT, level_LUT))
                    prod_data_fr.append(generate_row('FR', name, level, product_LUT, level_LUT))
                else:
                    data_en.append(generate_row('EN', name, level, variable_LUT, level_LUT))
                    data_fr.append(generate_row('FR', name, level, variable_LUT, level_LUT))
            # Close the dataset
            dataset = None
        except Exception as e:
            logger.error(e)
    
    header_en = 'Variable,Abbreviation,Level,Unit/Value'
    header_fr = 'Variable,Abréviation,Niveau,Unité/Valeur'
    if data_en and data_fr:
        # Write to english variable table file
        write_variable_table(data_en, os.path.join(directory, model + '_Variables-List_en.csv'), header_en)
        # Write to french variable table file
        write_variable_table(data_fr, os.path.join(directory, model + '_Variables-List_fr.csv'), header_fr)
    if prod_data_en and prod_data_fr:
        # Write to english product table file
        write_variable_table(prod_data_en, os.path.join(directory, model + '-Products_Variables-List_en.csv'), header_en)
        # Write to french product table file
        write_variable_table(prod_data_fr, os.path.join(directory, model + '-Products_Variables-List_fr.csv'), header_fr)
