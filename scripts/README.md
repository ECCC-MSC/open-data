# Documentation Generation Script

This script generates the [Markdown](../public-data-documentation-md) and [text](../public-data-documentation-txt) publication-ready versions of the documentation based on a
[source Markdown](../public-data-documentation-src).


# What the script does

The script does the following:
* Create GeoMet tables of layers in Markdown and raw text
 * The script finds all valid IDs (format: $ID$) and then replaces them with the corresponding table
* For raw text output:
 * Inline images references become text links to image files, except for the ECCC logo references which are entirely removed
 * Removes breadcrumbs
 * Removes the landing readme.md with the language toggle as well as the notice of authoritative version
 * Change relative URLs to absolute paths URLs


# Requirements

* Python 2.7 with pip and virtualenv installed
* [ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml) (automatically installed)


# Using the script

## 1. Edit the public-data-documentation-src
* You can add any file from the public-data-documentation-src folder. However all the Markdown files must end with the .md extension
* It is not recommended to add square brackets ( [ ] ) into the files: if it is not a link the script might remove it in some unexpected cases
* For the msc-data folder, you can add an identifier (example: $ID$) so it replaces it by the corresponding data table

  The valid Identifiers are:
    *  README_\<LANGUAGE\>.md :
    *  \<DATASETID\>_\<LANGUAGE\>.md
        * WHERE :
            \<LANGUAGE\> = EN OR FR <br><br>
            \<DATASETID\> = ID of a specific dataset

    NOTE: to know the ID go to the geomet.yml and look at the
    for a "Forecast_model". The ID is all the string left to the first
    "_".

## 2. Run the script

### Installation:

Run in a terminal in the public-data-documentation/scripts/ directory:

    $ /bin/bash setup.sh

You can ignore the numerous warning messages provided the installation completes with the `Cleaning up...` line.

### Execution:

Run in a terminal in the public-data-documentation/scripts/ directory:

    $ /bin/bash generate_documentation.sh

Optionally, one can specify the GeoMet Git repos by running:

    $ /bin/bash generate_documentation.sh <geomet_git_repo>

where `geomet_git_repo` is the URL where GeoMet's code is currently. The script leverages the geomet.yml file from GeoMet's code in order to automatically generate the tables of available layers. The default `geomet_git_repo` value is: http://gitlab.ssc.etg.gc.ca/ec-msc/geomet/

NOTE: before running the script, you can also modify the base MSC Datamart URL for the documentation basepath in the
`generate_documentation.sh` file. This value is used for absolute paths in the text version of the documentation.

## 3. Validate and push the modifications

Once you're ready [go back to step 5 of the update workflow](../README.md#update-workflow) to validate the updated outputs and push the modification to the servers.