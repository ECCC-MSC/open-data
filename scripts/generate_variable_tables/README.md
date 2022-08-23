# Generate Weather Variable Tables

## Introduction

The script generates weather variable tables by downloading GRIB2 and NetCDF files and reading their metadata. The script creates one table in english and another in french in two seperate files. The CSV tables display the variables, their abbreviation, their level and their unit. 

## Options

* `--directory`
    * Writes output files in directory;
    * Deletes existing CSV files;
    * Default value is current directory.

* `--models` 
    * Generates variable table from dataset;
    * Can select multiple datasets at once;
    * Default value is all datasets.

* `--url`
    * Downloads files from the server;
    * Appends dataset paths to the URL;
    * Default value is http://hpfx.collab.science.gc.ca/YYYYMMDD/WXO-DD/

* `--show`
    * Prints all datasets to output when turned on;
    * Displays every path for each dataset;
    * Ignores every option and exits after printing.

* `--verbose`
    * Prints info level messages to output when selected.

## Classes

### FileExplorer

* Downloads files from the server in a temporary directory
* Uses lists of paths from the dataset lookup table
* Removes temporary directory and its files

### FileParser

* Extracts metadata from GRIB2 or NetCDF files
* Transforms and translates metadata with lookup tables
* Creates CSV variable tables with processed metadata

## Lookup Tables

### datasets.yml

* Key: Dataset abbreviation
* Value: List of HPFX paths

Note: CanSIPS files are only available on the last day of the month. CanSIPS URL in table is incomplete. The format is changed to `ensemble/cansips/grib2/forecast/raw/YYYY/MM/` during execution.

### variable_translation.yml

* Key: Raw variable name
* `Variable EN`: Variable name in english
* `Variable FR`: Variable name in french
* `Abbreviation`: Variable abbreviation
* `Unit`: Formatted variable unit

Note: GRIB2 variables are followed by their unit in brackets.

Note: Unit exponents must be inside `<sup>` tags.

### product_translation.yml

* Key: Raw product name
* `Variable EN`: Product name in english
* `Variable FR`: Product name in french
* `Abbreviation`: Variable abbreviation
* `Unit`: Formatted variable unit

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
* Destination: `/data/geomet/dev/afsuxad/tmp/`

### DD-Alpha

* Source: `https://dd.alpha.meteo.gc.ca/`
* Destination: `/data/geomet/dev/afsuxad/tmp/`

## Tests

```sh
python3 -m unittest tests/test_readargs.py tests/test_fileparser.py
```

### tests/test_readargs.py

* Test module which tests the `read_args` method in `main.py`
* Verifies that default values are handled correctly in the method
* Verifies that an incorrect URL terminates the script

### tests/test_fileparser.py

* Test module which tests the `FileParser` class and its methods
* Verifies that metadata is correctly parsed from GRIB2 and NetCDF files
* Verifies that variable tables are correctly generated in english and french

### tests/mock_files/

* Directory containing GRIB2 files which are necessary to test `FileParser`