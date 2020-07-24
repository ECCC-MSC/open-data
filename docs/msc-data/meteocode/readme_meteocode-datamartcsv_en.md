[En français](readme_meteocode-datamartcsv_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Public Data](../readme_en.md) > [Meteocode forecast](readme_meteocode_en.md) > Meteocode forecast data in CSV on MSC Datamart

# Meteocode forecast data in CSV format

This document describes the content of the [meteocode data](readme_meteocode_en.md) in CSV format.

The files for meteocode terrestrial data in CSV format are created from the CMML files using the [XSLT](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/meteocode/cmml2csv.xsl) technology. The CSV files does not contain more information than the CMML files, they are only in a different format. Moreover, each CMML files contains many regions while each CSV file contains only one region.

## Data address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTP protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a CSV file.

The files are available at the following address :

* [https://dd.weather.gc.ca/meteocode/mtm/csv/](https://dd.weather.gc.ca/meteocode/mtm/csv/)
* [https://dd.weather.gc.ca/meteocode/mtm/csv/](https://dd.weather.gc.ca/meteocode/ont/csv/)
* [https://dd.weather.gc.ca/meteocode/pnr/csv/](https://dd.weather.gc.ca/meteocode/pnr/csv/)
* [https://dd.weather.gc.ca/meteocode/pyr/csv/](https://dd.weather.gc.ca/meteocode/pyr/csv/)
* [https://dd.weather.gc.ca/meteocode/que/csv/](https://dd.weather.gc.ca/meteocode/que/csv/)

An history of 24 hours is kept in these directories.

## File name nomenclature 

NOTE: ALL HOURS ARE IN UTC.

The filenames of the meteocode CSV files have the following nomenclature :

YYYY-MM-DDTHH-MM-SSZ_FPAANN_rRRRR_BB.csv

where :

* **YYYY-MM-DDTHH-MM-SSZ** : Time of emission for the forecast. Date is in ISO 8601 format. 
* **P** : Constant string meaning "Forecast Public".
* **ANN** : See the section 'Filename' in the CMML README at [https://dd.weather.gc.ca/meteocode/doc/cmml/README_CMML.txt](https://dd.weather.gc.ca/meteocode/doc/cmml/README_CMML.txt)
* **r** : Constant string indicating the beginning of the region code.
* **RRRR** : Alphanumerical code indicating the region of the public forecast. Can be of an arbitrary length (ex: 3pe, 10zf, 71.14). The complete list of forecast region and their associated code can be found at the end of this file in the section "Region's code and name".
* **BB** : String indicating the weather elements. Can be one of the following values: TA (Air Temperature), TD (Dew Point), PA (Precipitation accumulation), POP (Probability Of Precipitation), WS (Wind Speed and Direction), WG (Wind Gust), CC (Cloud Cover).

**Note**:

The [region's code and name correspondence](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/meteocode/table_region_code_name.xlsx) is available.

The codes are separated by the forecast offices because the same code can be used by more than one region, as:

    bulletin code, region code, French name, English name

## File content

* For each forecast region, 7 files are created. The content of each file is described below.
* The ''-9999.00'' value is for a missing or an invalid data for air temperature or dew point.
* If no wind gust is available for the forecast valid time in the CMML files, then the associated CSV file contains no data for this specific date.
* All dates are in ISO 8601 format.

__1. Air Temperature (TA)__

This file contains the air temperature.

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The 2 other values describe the content of each column :
    * Forecast valid time.
    * Air temperature in degree Celsius.

__2. Dew Point (TD)__

This file contains dew point temperature.

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The 2 other values describe the content of each column :
    * Forecast valid time.
    * Dew point in degree Celsius.

__3. Precipitation Accumulation (PA)__

This file contains the precipitation accumulation and type.

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The other values describe the content of each column :
    * Starting time of accumulation period.
    * Ending time of accumulation period.
    * Value of lower cumulative precipitation amount in mm.
    * Value of upper cumulative precipitation amount in mm.
    * Lower limit value of precipitation amount in mm.
    * Upper limit value of precipitation amount in mm.
    * Precipitation type. Can be amongst the following values :
        * Rain
        * Snow
        * Ice pellet
        * Freezing rain

__4. Probability of precipitation (POP)__

This file contains the probability of precipitation in percent.

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The other values describe the content of each column :
    * Starting time of period for this probability of precipitation.
    * Ending time of period for this probability of precipitation.
    * Probability of precipitation, in percent.

__5. Wind (WS)__

This file contains the values of wind speed and direction.

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The other values describe the content of each column :
    * Starting time of period.
    * Ending time of period.
    * Lower value of wind speed, in km/h.
    * Higher value of wind speed, in km/h.
    * String for wind direction. Can be one of these values :
        * east
        * nil
        * north
        * northeast
        * northwest
        * west
        * easterly
        * northerly
        * northeasterly
        * northwesterly
        * westerly
        * southerly
        * southeasterly
        * southwesterly
        * south
        * southeast
        * southwest
        * variable 

__6. Wind Gust (WG)__

This file contains the values of wind gust.

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The other values describe the content of each column :
    * Starting time of period.
    * Ending time of period.
    * Lower value of wind gust, in km/h.
    * Higher value of wind gust, in km/h.

__7. Cloud Cover (CC)__

The first line of these files contains the parameters:

where :

* **Region_en** : English name of the forecast region.
* **Region_fr** : French name of the forecast region.
* **CMML** : Constant string.
* **cmml_filename.xml** : Name of the CMML file from which this CSV file originates.
* The other values describe the content of each column :
    * Valid time for this cloud cover.
    * Cloud cover value, decimal.

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
