# Document Generation script

This script generates the markdown and text documentation based on a
general markdown. while generating this documentation, it take the
public-data-documentation-src and convert it into a txt documentation.
After, it adds data tables for msc-data.

To Convert the script in txt format, it find all markdown links
(example : [MY LINK](path to the link) ) and replace,remove or modify
those link based on what types of links they are.

To add the tables to the documentation,the script  search for all valid
ID (format = $ID$) and then replace them with a table related to the id.


Requirement
------------------------------------------------------------------------
* python 2.7
* ruamel.yaml (installed automatically in the setup.sh)


Workflow
------------------------------------------------------------------------

### 1. edit the public-data-documentation-src
* you can add any files to the public-data-documentation-src. However
  all the markdown files must have the .md extension at the end

* it is not recommended to add squared bracket ( [] ) into the files
  if it is not a link it might remove it in some weird cases

* For msc-data you can add an identifier (example : $ID$) so it replaces
  it by a data tables related to the identifier.
  <br><br>
   The valid Identifiers are:

    *  README_\<LANGUAGE\>.md :
    *  \<DATASETID\>_\<LANGUAGE\>.md

        * WHERE :

            \<LANGUAGE\> = EN OR FR <br><br>
            \<DATASETID\> = ID of a specific dataset

    NOTE: to know the id go to the geomet.yml and look at the
    for a "Forecast_model". The Id is all the string left to the first
    "_".

### 2. Run the program

#### Installation:
run in a terminal in the scripts directory :

    $ /bin/bash/ script/setup.sh`

#### Execution:
run in a terminal in the scripts directory :

    $ /bin/bash script/generate_documentation.sh <geomet_yaml>

where geomet_yaml is the current yaml for geomet
you can also edit the generate_documentation.sh to change
base DD url path for the txt version


### 3. Push the modification

run these commands in a terminal this assumes that you have a fork
and that you have pulled a local fork of the dps and that the version
is in sync with his upstreamed master

    $ git add .
    $ git commit -m "message related to the commit"
    $ git push

then add your account name  and your related github password.

To finish ask for a merge request with the upstream master.
IF you can have access to the master you do not have ask for a merge
request

