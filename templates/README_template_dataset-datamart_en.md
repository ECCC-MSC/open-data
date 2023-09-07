# Template for dataset pages on the MSC Datamart

This template is used for dataset pages under `/msc-data/`. Add the link to the English version, the logo and the breadcrumb trail


## *Dataset name -all the way through for NWP-* (*acronym if relevant*) data in *specify format* format
One or 2 sentences that reference the main page.

> Example for HRDLPS:

> This page describes the [High Resolution Deterministic Land Surface Prediction System (HRDLPS)](https://eccc-msc.github.io/open-data/msc-data/nwp_hrdlps/readme_hrdlps_en/) experimental data available in NetCDF format on the DD-Alpha server, the MSC Datamart data testing website.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](.../.../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples to access and use Meteorological Service of Canada's open data](.../.../usage-overview/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, you will get a list of links giving access to a file *specify the data format*.

The data is available at the address: https://dd.weather.gc.ca.../HH/hhh/ (for model data)

* where:

    * HH: UTC time of model run start [00,]
    * hhh: Forecast time [000, ]

A history of _XX_ days is available in this directory _(note: this sentence may be invalid for data only available on HPFX Collab since the retention time varies depending on the space available)_

## Technical specification of the grid - *(for NWEP only)*

If relevant, provide grid descriptions in tabular form and if necessary an image of the domain. Images should be collected on [Collaboration](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc) and only referred here via ![](address)

Example: https://eccc-msc.github.io/open-data/msc-data/nwp_wcps/readme_wcps-atm-ocean-datamart_en/#specification-technique-de-la-grille

## Nomenclature of file names 

The files follow the following nomenclature: 

`YYYYYYYYYYYYYYYYYYYYYYYYY`

where :

* ...
* ...

Example: https://eccc-msc.github.io/open-data/msc-data/nwp_wcps/readme_wcps-atm-ocean-datamart_en/#nomenclature-des-noms-de-fichiers

## Levels - *check if relevant*

Describe the list of available levels, if relevant (only applies to 3D datasets)

## File contents - *check if relevant*
 
Confirm if relevant or if the information can be found elsewhere. Describe the file content

* Describe the contents of the file in as much detail as possible (e.g., in the case of XML files, describe the headers, sections and elements).

* Where applicable, indicate if the files have been compressed and with what utility (e.g. bzip2). Indicate how to decompress them.

* When applicable, indicate whether or not the files have been encoded, in which format and in which encoding standard (e.g. UTF-8).

* If necessary, indicate the precision of the data.*

* Include a link to the format documentation if relevant (e.g. GRIB format).

## List of variables

The available variables of XXXXXX are :

* VAR_1: Definition
* VAR_2 : Definition
* ...
* ...

NOTE: A table produced via an automated script will be inserted here, coordinate with dps.client@ec.gc.ca

## Support

For questions about this data, [please contact us](https://meteo.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/) list.
