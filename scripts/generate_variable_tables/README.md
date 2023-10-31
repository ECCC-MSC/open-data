# Generate Weather Variable Tables

## Introduction

The script generates weather variable tables by downloading GRIB2 and NetCDF files and reading their metadata. The script creates one table in english and another in french in two seperate files. The CSV tables display the variables, their abbreviation, their level and their unit. 

## Requirements

* Python 3.8.10
* [GDAL 3.5.2](https://pypi.org/project/GDAL/)
* [bs4](https://pypi.org/project/beautifulsoup4/)
* [yaml](https://pypi.org/project/PyYAML/)

The `geomet-dev-21.cmc.ec.gc.ca` server has all the dependencies required to run the script. If you do not have a `geomet-dev-21` account, you can also create a Conda environment with the following commands. 

```sh
conda create -n env_geomet PYTHON=3.8.10
conda activate env_geomet
conda install -c conda-forge pyyaml bs4 gdal==3.5.2
```

## Configuration

The configuration file `config.yaml` allows the user to change certain settings, such as the path of the temporary directory with the `temporary` variable. In addition, the user may also change the path of the lookup tables, though it is not necessary.

* `temporary`: Path of the temporary directory
* `model_file`: Path of the lookup table for the datasets
* `variable_file`: Path of the lookup table for the variables
* `product_file`: Path of the lookup table for the products
* `level_file`: Path of the lookup table for the levels

## Execution

Before running the script, rename the value of the `temporary` variable in `config.yaml` to an existing directory in which you have permissions to read and write. 

**Note**: Avoid creating the temporary directory in your home, as you may exceed your disk quota while downloading files.

To generate variable tables for every available dataset, run this script in your terminal in the `public-doc/scripts/generate_variable_tables/` directory.

```sh
python3 main.py --directory ./tables
```

After executing the script, you must move the created files to the `public-doc/docs/assets/csv/` directory to update the MSC Open Data Documentation. 

**Note**: It is not recommended to set `public-doc/docs/assets/csv/` as the `--directory`, because the script overwrites files in the directory.

Finally, you must insert the following code block in the corresponding datamart pages located in `public-doc/docs/msc-data/` to load the tables. Make sure to rename the file in the `loadTable` function to load the correct CSV file.

```js
<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/Variables-List.csv");
</script>
```

### Notes

To generate variable tables from files in a local directory, you may use the `--path` argument to avoid needless downloads. The local files do not get deleted after the creation of the variable tables. 

**Note**: The paths from the `--path` argument and from the `datasets.yml` lookup table are concatenated during execution and the result must be a valid directory. As such, you may need to create directories and move the files around.

The `CanSIPS` path in `datasets.yml` is incomplete, because the year and the month are missing, as there are multiple possible values. As such, when the `--models` argument takes `CanSIPS`, you will be prompted to enter the year and the month as integers to complete the path.

## Maintenance

* You can add a dataset to `datasets.yml` by creating a new entry. A key can have more than one value. These values will be concatenated with an URL to download GRIB2 or NetCDF files from a server, e.g. `https://dd.alpha.meteo.gc.ca/`.
* If you receive a warning indicating that a variable has not been found, you can add it to `variable_translation.yml` or `product_translation.yml` by creating a new entry. The key must be the variable from the warning.
* If you receive a warning indicating that a level has not been found, you can add it to `readable_level.yml` by creating a new entry. The key must be the level from the warning.

## Options

* `--directory`
    * Writes output files in directory;
    * Deletes existing CSV files;
    * Default value is current directory.

* `--models` 
    * Generates variable table from dataset;
    * Can select multiple datasets at once;
    * Default value is all datasets.

* `--path`
    * Downloads files from the server;
    * Find files in local directory;
    * Appends dataset paths to the URL;
    * Default value is `http://hpfx.collab.science.gc.ca/YYYYMMDD/WXO-DD/`

* `--verbose`
    * Sets logging level to `INFO` when activated;
    * Default logging level is `WARNING`.

## Classes

### FileExplorer

* Downloads files from the server or locally
* Uses lists of paths from the dataset lookup table
* Removes temporary directory and its files

### FileParser

* Extracts metadata from GRIB2 or NetCDF files
* Transforms and translates metadata with lookup tables
* Creates CSV variable tables with processed metadata

## Lookup Tables

### datasets.yml

* Key: Dataset abbreviation
* Value: List of paths

Note: CanSIPS files are only available on the last day of the month. The CanSIPS path in the dictionary is incomplete. The format is changed to `ensemble/cansips/grib2/forecast/raw/YYYY/MM/` during execution.

### variable_translation.yml

* Key: Raw variable name
* `Variable EN`: Variable name in english
* `Variable FR`: Variable name in french
* `Abbreviation`: Variable abbreviation
* `Unit EN`: Formatted variable unit or category in english
* `Unit FR`: Formatted variable unit or category in french

Note: GRIB2 variables are followed by their unit in brackets.

Note: Unit exponents must be inside `<sup>` tags.

### product_translation.yml

* Key: Raw product name
* `Variable EN`: Product name in english
* `Variable FR`: Product name in french
* `Abbreviation`: Variable abbreviation
* `Unit EN`: Formatted variable unit or category in english
* `Unit FR`: Formatted variable unit or category in french

Note: Serves the same function as `variable_translation.yml` for probabilistic products.

Note: GRIB2 variables are followed by their unit in brackets.

Note: Unit exponents must be inside `<sup>` tags.

### readable_level.yml

* Key: Raw variable level
* `EN`: Readable variable level in english
* `FR`: Readable variable level in french

## Data Feeds

### HPFX

* Source: `http://hpfx.collab.science.gc.ca/`
* Destination: `/data/geomet/dev/$USER/tmp/`

### DD-Meteo

* Source: `https://dd.meteo.gc.ca/`
* Destination: `/data/geomet/dev/$USER/tmp/`

### DD-Alpha

* Source: `https://dd.alpha.meteo.gc.ca/`
* Destination: `/data/geomet/dev/$USER/tmp/`

## Tests

To execute all unit tests, run this script in your terminal in the `public-doc/scripts/generate_variable_tables/` directory.

```sh
python3 -m unittest tests/test_main.py tests/test_fileexplorer.py tests/test_fileparser.py -b
```

### tests/test_main.py

* Test module which tests the methods in `main.py`
* Verifies that the directory is created if it does not exist
* Verifies that the year and month are appended to the path

### tests/test_fileexplorer.py

* Test module which tests the `FileExplorer` class and its methods
* Verifies that the temporary directory is deleted if it exists

### tests/test_fileparser.py

* Test module which tests the `FileParser` class and its methods
* Verifies that metadata is parsed from GRIB2 and NetCDF files
* Verifies that variable tables are generated in english and french

### tests/mock_files/

* Directory containing GRIB2 files which are necessary to test `FileParser`
