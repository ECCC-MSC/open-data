# Documentation Generation Script

This script generates the [markdown](../public-data-documentation-md) and [text](../public-data-documentation-txt) documentation based on a
[source markdown](../public-data-documentation-src). While generating this documentation, it take the public-data-documentation-src and convert it into a txt documentation.
After, it adds data tables for msc-data.

To convert the content to the txt format, it finds all markdown links
(example: \[MY LINK\](path to the link) ) and replaces, removes or modify
those links based on what types of links they are.

To add the tables to the documentation, the script searches for all valid
IDs (format = $ID$) and then replaces them with a table related to the ID.


## What the script do

The script does the following:
* Create GeoMet tables of layers in Markdown and raw text
* For raw text output:
 * Removes images
 * Removes breadcrumbs
 * Removes the notice of authoritative version
 * Change relative URLs to absolute paths

## Requirements

* Python 2.7 with pip and virtualenv installed
* [ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml) (installed by setup.sh)


## Workflow

### 1. edit the public-data-documentation-src
* You can add any file from the public-data-documentation-src folder. However
  all the markdown files must have the .md extension at the end

* It is not recommended to add squared bracket ( [ ] ) into the files
  if it is not a link since the script might remove it in some weird cases

* For msc-data, you can add an identifier (example : $ID$) so it replaces
  it by a data tables related to the identifier.

  The valid Identifiers are:
    *  README_\<LANGUAGE\>.md :
    *  \<DATASETID\>_\<LANGUAGE\>.md
        * WHERE :
            \<LANGUAGE\> = EN OR FR <br><br>
            \<DATASETID\> = ID of a specific dataset

    NOTE: to know the ID go to the geomet.yml and look at the
    for a "Forecast_model". The ID is all the string left to the first
    "_".

### 2. Run the script

#### Installation:

Run in a terminal in the scripts directory:

    $ /bin/bash scripts/setup.sh

#### Execution:

Run in a terminal in the scripts directory:

    $ /bin/bash scripts/generate_documentation.sh <geomet_yaml>

where geomet_yaml is the current yaml for geomet
you can also edit the generate_documentation.sh to change
base DD url path for the txt version


### 3. Push the modification

Run these commands in a terminal. This assumes that you have a fork
and that you have pulled a local fork of the dps repos and that the version
is in sync with his upstreamed master.

    $ git add .
    $ git commit -m "message related to the commit"
    $ git push

then add your account name and your related GCcode password.

To complete the process, create a merge request with the upstream master.
If you can have access to the master you do not have ask for a merge
request.
