[En français](readme_hydrometric-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Hydrometric data](readme_hydrometric_en.md) > Hydrometric data on MSC Datamart

# Hydrometric data in CSV format

This page describes the [real time hydrometric](readme_hydrometric_en.md) data available in CSV format.

# Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable CSV file.

The data is available at the following address:

* [https://dd.weather.gc.ca/hydrometric/csv/{PROVTERR}/{FREQUENCY}/](https://dd.weather.gc.ca/hydrometric/csv)

where:

* __PROVTERR__ : 2-letter code for the province or territory. The code is one of the 13 following values:
    * AB (Alberta)
    * BC (British Columbia)
    * MB (Manitoba)
    * NB (New Brunswick)
    * NL (Newfoundland and Labrador)
    * NS (Nova Scotia)
    * NT (Northwest Territories)
    * NU (Nunavut)
    * ON (Ontario)
    * PE (Prince Edward Island)
    * QC (Quebec)
    * SK (Saskatchewan)
    * YT (Yukon)

* __FREQUENCY__ : Frequency of update, "hourly" or "daily".

A 30-day history is kept in this directory.

## File name nomenclature 

Each real-time hydrometric data file has a static filename which follows this naming convention:

[PROVTERR]_[ID]_[FREQUENCY]_hydrometric.csv 

where:

* __PROVTERR__ : 2-letter code for the province or territory

* __ID__ : station identifier

* __FREQUENCY__ : frequency of update, "hourly" or "daily"

Example: 

"AB_05AA004_hourly_hydrometric.csv" means the hydrometric observations updated hourly for the station "05AA004" in Alberta (AB) in CSV format.

__Province File__

A file containing all stations in a province is also provided for convenience.
It has a static filename which follows this naming convention:

[PROVTERR]_[FREQUENCY]_hydrometric.csv 

where:

* __PROVTERR__ : 2-letter code for the province or territory

* __FREQUENCY__ : frequency of update, "hourly" or "daily"

Example:

"ON_daily_hydrometric.csv" means the hydrometric observations updated daily for all stations in Ontario (ON) in CSV format.

## Data description

### Data File

The real-time hydrometric data is provided in a CSV format for the distribution 
by Environment and Climate Change Canada.

The files updated on an hourly basis contain the last 2 complete days of data 
plus the current incomplete day. The files updated on a daily basis contain the 
last 30 complete days of data plus the current incomplete day.

The first line is a bilingual header, followed by data records. Below are the 
English column descriptors:

 ID,Date,Water Level (m),Grade,Symbol,QA/QC,Discharge (cms),Grade,Symbol,QA/QC

where :

*  __ID__ : Station identifier. The first two digits indicate the major drainage 
basin in which the station is located. The next two characters indicate 
the sub-basin and sub-sub-basin. The last three digits indicate the 
specific station within the sub-sub-basin.

* __Date__ : Data timestamp in ISO 8601 format, Local Standard Time (LST).

* __Water Level (m)__ : Water level in meters.

* __Grade__ : Future use.

* __Symbol__ : Future use.

* __QA/QC__ : Quality assurance/quality control flag for the water level 
         (1 = preliminary, 2 = reviewed, 3 = checked, 4 = approved).

* __Discharge (cms)__ : Discharge in cubic meters per second.

* __Grade__ : Future use.

* __Symbol__ : Future use.

* __QA/QC__ : Quality assurance/quality control flag for the discharge.

Please note that the timestamps of the data are always in LST at that 
particular station. The timestamps of the data records show the offset from 
UTC.

### Station List File

A list of the [real-time hydrometric stations](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_hydrometric/hydrometric_StationList.geojson) in GeoJSON format is available.

The first line is a bilingual header, followed by station metadata. Below are the English column descriptors:

ID,Name,Latitude,Longitude,Prov/Terr,Timezone

where :

*  __ID__ : Station identifier.

* __Name__ : Name of the station. The name is in English or French depending on the 
        location of the station.

* __Latitude__ : Latitude in decimal format.

* __Longitude__ : Longitude in decimal format.

* __Prov/Terr__ : 2-letter code for the province or territory.

* __Timezone__ : LST offset from UTC.

## Support

If you have any questions about these data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
