[En français](readme_riops_S111-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

## S-111 Dynamic Hydrographic Products(DHP) in HDF5 format using RIOPS(Regional Ice Ocean Prediction System) surface currents data. 

The S-111 Dynamic Hydrographic Products(DHP) for oceanographic models currents is an open standard [ HDF5 ](https://www.hdfgroup.org/solutions/hdf5/) format with a specification provided by the [ International Hydrographic Organisation(IHO) ](https://iho.int). Each S-111 data file is a 1x1 degrees regular bounding box tiled subset of RIOPS surface currents data. The S-111 tiled files are using the EPSG:4326 as its GIS Common Reference System(CRS) to define all its geographical coordinates locations.

The data coding format 3 (Ungeorectified gridded data or point set data at one or more times) of the [ IHO S-111 format specification ](http://registry.iho.int/beta/productspec/view.do?idx=168&product_ID=S-111&statusS=5&domainS=ALL&category=product_ID&searchValue=) is used because it allows to directly use RIOPS data, which itself use a a polar stereographic grid, without any interpolation.

S-111 currents are expressed as a Speed(in knots) and a Direction(navigatioal angle) using the HDF5 H5T_COMPOUND data type.

## Data location

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable HDF5 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URL:

* [https://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/{HH}/](https://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/)

* __HH__: RIOPS model synoptic run start hour, in UTC [00, 06, 12, 18].

## Files name nomenclature

NOTE: ALL HOURS ARE IN UTC.

The S-111 DHP tiled files have the following nomenclature:

CMC_riops_111CA002{nnnn}N{wwwww}W_{YYYYYMMDD}T{hh}Z.h

* __nnnn__: Tag of the decimal degrees latitude(Northern Hemisphere) of the South-West corner of the 1x1 degree tiles bounding boxes used.
* __wwwww__: Tag of the decimal degrees longitude(Western Hemisphere) of the South-West corner of the 1x1 degree tiles bounding boxes used.
* __YYYYYMMDD__: RIOPS model synoptic run start date, in UTC.
* __hh__: RIOPS model synoptic run start hour, in UTC [00, 06, 12, 18].

Example of a S-111 DHP tiled file name:

CMC_riops_111CA0024200N06900W_20200128T12Z.h

This file originates from the Canadian Meteorological Center (CMC) and contains RIOPS surface currents that were packaged as a 1x1 degree S-111 DHP tile which have its South-West corner located at latitude 42.00 and longitude -69.00. The RIOPS surface currents were produced on January 28 2020 at 12UTC 

## 1x1 degree tiles for Scotian shelf
![PNG Scotian shelf L2 tiles](NovaScotiaLL2Tiles.png)

