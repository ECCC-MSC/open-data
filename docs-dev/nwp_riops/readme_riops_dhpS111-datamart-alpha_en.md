[En français](readme_riops_dhpS111-datamart-alpha_fr.md)

![ECCC logo](../../docs/img_eccc-logo.png)

# S-111 Dynamic Hydrographic Products(DHP) in HDF5 file format using the Regional Ice Ocean Prediction System (RIOPS) surface currents data. 

This S-111 Dynamic Hydrographic Products(DHP) tiled dataset use the surface currents of the RIOPS oceanographic model. The S-111 tiled data use an open standard [HDF5](https://www.hdfgroup.org/solutions/hdf5/) file format with a specification provided by the [International Hydrographic Organisation(IHO)](https://iho.int). All maritime navigation stakeholders that are interested by the RIOPS surface oceanic currents of the canadian coastal waters can use this [EPSG:4326](https://epsg.io/4326) georeferenced S-111 tiled dataset.

# Data location

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../docs/msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../docs/usage/readme_en.md) is also available.

The data is also available using the basic HTTP protocol and resides in a directory that is plainly accessible by a web browser at the following URL:

* [http://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/{HH}/](http://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/)

* __HH__: Model run start, in UTC [00, 06, 12, 18]

Note that the S-111 data is updated four times a day following the end of each daily RIOPS operational model synoptic runs.

# Files name nomenclature

NOTE: ALL HOURS ARE IN UTC.

The S-111 DHP tiled files have the following nomenclature:

CMC_riops_111CA002{nnnn}N{wwwww}W_{YYYYYMMDD}T{HH}Z.h5

* __nnnn__: Four numeric characters tag to represent the decimal degrees latitude(Northern Hemisphere) of the South-West corner of each 1x1 degree tiles bounding box of the dataset.
* __wwwww__: Five numeric characters tag to represent the decimal degrees longitude(Western Hemisphere) of the South-West corner of each 1x1 degree tiles bounding box of the dataset.
* __YYYYYMMDD__: Year, month and day of the beginning of the forecast.
* __T__: Time delimiter according to ISO8601 norms.
* __HH__: Model synoptic run start hour, in UTC [00, 06, 12, 18].
* __Z__: Time zone (UTC hour).
* __h5__: Official HDF5 file format extension.

Example of a S-111 DHP tiled file name:

CMC_riops_111CA0024200N06900W_20200129T18Z.h5

This file originates from the Canadian Meteorological Center (CMC) and contains RIOPS surface currents for the canadian coastal waters that were packaged as a 1x1 degree S-111 DHP tile which have its South-West corner located at latitude 42.00N and longitude 69.00W. The S-111 tiled files were produced by post-processing of RIOPS data results coming from its synoptic forecast run issued on January 29 2020 at 18UTC. 

# List of variables 

* __"Speed"__ : Wind speed (in knots) for each RIOPS data grid point
* __"Direction"__ : Wind direction (navigation angle 0°-360°) for each RIOPS data grid point

Both variables are regrouped in a [HDF5 H5T_COMPOUND type](https://bitbucket.hdfgroup.org/pages/HDFFV/hdf5doc/master/browse/html/cpplus_RM/class_h5_1_1_comp_type.html) for each RIOPS data grid point.

There is also a comprehensive metadata content in each S-111 tiled data file (for more information on the S-111 metadata, see the official [International Hydrographic Organisation(IHO) specification](http://registry.iho.int/beta/productspec/view.do?idx=168&product_ID=S-111&statusS=5&domainS=ALL&category=product_ID&searchValue=)).

# Files data structure

* The S-111 tiled files are using the [EPSG:4326](https://epsg.io/4326) as its GIS [CRS](https://docs.qgis.org/2.8/en/docs/gentle_gis_introduction/coordinate_reference_systems.html) to define all its geographical coordinates locations.

* Each file is a 1x1 degrees regular bounding box tiled subset of RIOPS surface currents data.

* The usage of the [EPSG:4326](https://epsg.io/4326) CRS and the data coding format 3 (Ungeorectified gridded data or point set data at one or more times) of the IHO S-111 format specification allows the direct usage, without any interpolation, of RIOPS data which itself use a north-polar stereographic projection with 5km resolution at the standard parallel 60° N.

* Each S-111 tiled data files have 55 timestamped data structures(HDF5 GROUP) called __"timePoint"__ of surface currents data objects. Each S-111 contains the 49 timestamps of the RIOPS synoptic forecast run results used for the tiled file names and the first 6 timestamps are taken from the previous RIOPS synoptic forecast run to have a data cushion in the past.

# Examples of canadian coastal waters tiled domains available

## 1x1 degree tiles bounding boxes for the Bay of Fundy, Scotian shelf and Northumberland Strait.

![PNG Scotian shelf L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/ScotianShelfL2_tiles.png)

## 1x1 degree tiles bounding boxes for the Gulf of St. Lawrence

![PNG GStl L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/GSTLL2Tiles.png)

## 1x1 degree tiles bounding boxes for the West-Coast (Vancouver)

![PNG West-Coast L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/WCoastL2Tiles.png)

## 1x1 degree tiles bounding boxes for the West-Coast (Queen Charlotte Islands)

![PNG GStl L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/WCoastNL2Tiles.png)
