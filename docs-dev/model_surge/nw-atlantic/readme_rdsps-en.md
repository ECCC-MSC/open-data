----------------------------------------

ENVIRONMENT AND CLIMATE CHANGE CANADA

This README file describes data available on the Datamart of the Meteorological Service of Canada (MSC) from the Regional Deterministic storm Surge Prediction System (RDSPS) for the north-west Atlantic region.

To consult this file online, go to
http://dd.weather.gc.ca/model_surge/doc/README_RDSPS.txt

The files are produced by Environment and Climate Change Canada.
http://ec.gc.ca/

----------------------------------------


# Version of 2020-02-28

In this file:
* About
* License
* Download
* Data Wire
* Description
* Filename
* File content
* Variable list
* Contact Us


##   About  

This document explains the regional storm surge model data available on the Meteorological Service of Canada's HTTP data server under following directory:
http://dd.weather.gc.ca/model_surge/nw_atlantic/

The overarching README file of the Datamart itself can be found here:
http://dd.weather.gc.ca/about_dd_apropos.txt



##   License

For the terms of use for the RDSPS data, see the general MSC Datamart license at:
http://dd.weather.gc.ca/doc/LICENCE_GENERAL.txt


##    Download

The RDSPS files can be found at the following address:
http://dd.weather.gc.ca/model_surge

A history of 24h of forecasts is kept in this directory.


##     Data Wire  

To facilitate the retrieval of timely data on the Datamart, the Meteorological
Service of Canada (MSC) has set up a data wire for announcing file availability
on the Datamart.  This data wire uses the 'Advanced Message Queueing Protocol'
(AMQP) protocol. Not only does this enable the user to be notified of available
products as they're published, but also to receive them automatically.

The service may apply to a specific set of files (weather warnings,
observations, model data, etc.) and thus may concern only those products of
interest to the user.

The documentation about this service can be found here:
http://dd.weather.gc.ca/doc/README_AMQP.txt


##   Description

The Regional Deterministic storm Surge Prediction System (RDSPS) produces storm surge
forecasts using the DalCoast ocean model. DalCoast (Bernier and Thompson 2015) is a storm surge forecast system for the east coast of
Canada based on the depth-integrated, barotropic and linearized form of the
Princeton Ocean Model. The model is forced by the 10 meters winds and sea level pressure from the Global Deterministic
Prediction System (GDPS).

For further details consult the CMC Product guide on Collaboration:
http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/changes_e.html


##    Filename

NOTE:  ALL HOURS ARE IN UTC.

 (*TODO: implement T, Z in the name*)

File names have the form:

CMC_rdsps_domain_Variable_LevelType_level_latlond.dddxd.ddd_YYYYMMDDTHHZ_Phhh.nc

Where:

* CMC: constant string indicating that the data is from the Canadian Meteorological Centre
* rdsps: constant string indicating that the data is from the Regional Deterministic storm Surge Prediction System
* domain: constant string indicating which domain the data is from
* Variable: Variable type included in this file
* LevelType: Level type
* Level: Level value
* latlond.dddxd.ddd: constant string indicating that the projection used is lat/long at d.ddd x d.ddd degrees resolution
* YYYYMMDD: Year, month and day of the beginning of the forecast
* HH: UTC run time `[00, 06, 12, 18]`
* Phhh : P is a constant character. hhh represents the forecast hour `[000, 001, 002, ..., 240]`
* nc: constant string indicating the NetCDF format is used
* T: time date separator
* Z: time zone indicator (UTC)

Example of file name:

CMC_rdsps_nw-atlantic_etas_SFC_0_latlon0.033x0.033_20180417T12Z_P024.nc

This file originates from the Canadian Meteorological Center (CMC) and contains
the data of the Regional Deterministic storm Surge Prediction System. The data in the
file start on April 17th 2018 at 12Z (2018041712). It contains the storm surge water level (ETAS) at the surface (SFC_0) on a lat/long grid
at 0.033 degree x 0.033 degree resolution for the forecast hour 24 (P024) in
NetCDF format (.nc).


##   File Content

The data files are in NetCDF format. The NetCDF files comply with Climate and Forecast (CF) conventions to facilitate
processing and sharing.

NetCDF is a file format for the storage and transport of gridded meteorological
data, such as Numerical Weather Prediction model output. It is designed to be
self-describing, compact and portable across computer architectures.  The NetCDF standard was designed and is maintained by
the University Corporation for Atmospheric Research (UCAR).

Information about this format and software to manipulate and display NetCDF data are available here:
https://www.unidata.ucar.edu/software/netcdf/docs/index.html

Climate and Forecast Conventions:
http://cfconventions.org/


##    Variable list

The list below provides, for each variable: a short description, an alphabetical abbreviation, the levels available for the parameter, and measurement units.

|NetCDF  | Short description|                          Abbr.|  Level|  Units|
|--------|---------------|----------|----------|----------|
|etas    |Storm surge    |                            ETAS|   SFC_0|    m|


### Levels

Levels that may be applicable to a given parameter are:

* SFC: surface



##   Contact Us

If you use the data available on the Datamart, you are invited to subscribe to the Datamart's mailing list in order to be warned of any updates or changes regarding the data available. You can subscribe here:
http://lists.cmc.ec.gc.ca/mailman/listinfo/dd_info

Once subscribed, please use the following email address to contact us for any comment or question:
ec.dps-client.ec@canada.ca


