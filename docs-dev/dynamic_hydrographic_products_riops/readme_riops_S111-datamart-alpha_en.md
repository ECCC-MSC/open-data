[En français](readme_riops_S111-datamart-alpha_fr.md)

![ECCC logo](../../docs/img_eccc-logo.png)

# S-111 Dynamic Hydrographic Products(DHP) in HDF5 file format using RIOPS(Regional Ice Ocean Prediction System) surface currents data. 

This S-111 Dynamic Hydrographic Products(DHP) tiled dataset use the surface currents of the operational ECCC RIOPS oceanographic model. The S-111 tiled data use an open standard [HDF5](https://www.hdfgroup.org/solutions/hdf5/) file format with a specification provided by the [International Hydrographic Organisation(IHO)](https://iho.int). All maritime navigation stakeholders that are interested by the RIOPS surface oceanic currents of the canadian coastal waters can use this [EPSG:4326](https://epsg.io/4326) georeferenced S-111 tiled dataset.

# List of variables used for the S-111 currents.

* 1). __"Speed"__(in knots) for each RIOPS data grid point
* 2). __"Direction"__(navigation angle 0°-360°) for each RIOPS data grid point

Both variables are regrouped in a [HDF5 H5T_COMPOUND type](https://bitbucket.hdfgroup.org/pages/HDFFV/hdf5doc/master/browse/html/cpplus_RM/class_h5_1_1_comp_type.html) for each RIOPS data grid point (which can then be considered as an object, see item __S-111 surface currents objects__ below for more details)

There is also a comprehensive metadata content in each S-111 tiled data file (for more information on the S-111 metadata, see the official [International Hydrographic Organisation(IHO)](https://iho.int) specification).

# S-111 Data location

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible by a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable HDF5 file. In practice, we recommend writing your own script to automate the downloading of the desired data (using wget or equivalent). If you are unsure of how to proceed, you might like to take a look at our brief wget usage guide.

The data can be accessed at the following URL:

* [https://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/{HH}/](https://dd.alpha.weather.gc.ca/model_riops/dynamic_hydrographic_products/hdf5/)

* __HH__: Model synoptic run start hour, in UTC [00, 06, 12, 18].https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/WCoastL2Tiles.png

Note that the S-111 data is updated four times a day following the end of each daily RIOPS operational model synoptic runs.

# S-111 Files datamart name nomenclature

NOTE: ALL HOURS ARE IN UTC.

The S-111 DHP tiled files have the following nomenclature:

CMC_riops_111CA002{nnnn}N{wwwww}W_{YYYYYMMDD}T{hh}Z.h5

* __nnnn__: Four characters tag of the decimal degrees latitude(Northern Hemisphere) of the South-West corner of the 1x1 degree tiles bounding boxes used.
* __wwwww__: Five characters Tag of the decimal degrees longitude(Western Hemisphere) of the South-West corner of the 1x1 degree tiles bounding boxes used.
* __YYYYYMMDD__: RIOPS model synoptic run start date, in UTC.
* __T__: ISO8601 standard date-time separator.
* __hh__: Model synoptic run start hour, in UTC [00, 06, 12, 18].
* __Z__: UTC(a.k.a ZULU) tag.
* __.h5__: Official HDF5 file format extension.
 
Example of a S-111 DHP tiled file name:

CMC_riops_111CA0024200N06900W_20200129T18Z.h

This file originates from the Canadian Meteorological Center (CMC) and contains RIOPS surface currents for the canadian coastal waters that were packaged as a 1x1 degree S-111 DHP tile which have its South-West corner located at latitude 42.00N and longitude -69.00W. The S-111 tiled files were produced by post-processing of RIOPS data results coming from its synoptic forecast run issued on January 29 2020 at 18UTC. 

# S-111 tiled files data structure

## Common Reference System(CRS)

The S-111 tiled files are using the [EPSG:4326](https://epsg.io/4326) as its GIS [CRS](https://docs.qgis.org/2.8/en/docs/gentle_gis_introduction/coordinate_reference_systems.html) to define all its geographical coordinates locations.

## Tiles extents
Each S-111 data file is a 1x1 degrees regular bounding box tiled subset of RIOPS surface currents data.

## Tiles grid mapping 
The usage of the [EPSG:4326](https://epsg.io/4326) CRS and the data coding format 3 (Ungeorectified gridded data or point set data at one or more times) of the IHO S-111 format specification allows the direct usage, without any interpolation, of RIOPS data which itself use a north-polar stereographic projection with 5km resolution at the standard parallel 60° N.

## S-111 timestamped GROUP data structures
Each S-111 tiled data files have 55 timestamped data structures(HDF5 GROUP) called __"timePoint"__ of surface currents data objects(see item surface currents objects below). Each S-111 contains the 49 timestamps of the RIOPS synoptic forecast run results used for the tiled file names and the first 6 timestamps are taken from the previous RIOPS synoptic forecast run to have a data cushion in the past.

Example of timestamped data structures for a S-111 tiled file(ex. CMC_riops_111CA0024200N06900W_20200129T18Z.h5) having RIOPS surface currents data produced by the synoptic forecast run issued on January 29 2020 at 18UTC

*  __GROUP "Group_001" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T120000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_002" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T130000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_003" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T140000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_004" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T150000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_005" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T160000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_006" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T170000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_007" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T180000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_008" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T190000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  ...
*  __GROUP "Group_054" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200129T470000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__
*  __GROUP "Group_055" { ATTRIBUTE "timePoint" { DATATYPE  H5T_STRING ... } DATASPACE SCALAR DATA { (0): "20200131T480000Z" } } DATASET "values" { DATATYPE  H5T_COMPOUND { ... } } }__


## S-111 surface currents objects
Each RIOPS surface currents grid point data is represented by a __"Speed"__(in knots) and a __"Direction"__(navigation angle 0°-360°) data object using the [HDF5 H5T_COMPOUND type](https://bitbucket.hdfgroup.org/pages/HDFFV/hdf5doc/master/browse/html/cpplus_RM/class_h5_1_1_comp_type.html).

Example of one surface currents data objects structure for one S-111 tiled file(Here a tile with 452 surface currents data objects) for one timestamped GROUP data stucture:

* __DATATYPE H5T_COMPOUND { H5T_IEEE_F32LE "Direction";  H5T_IEEE_F32LE "Speed"; } DATASPACE  SIMPLE { (452,1)/(452,1) } DATA { (0,0): { 168.927, 0.123022 }, ... (227,0): {248.724, 0.0136034 } }__

The number of such surface currents data objects is variable for each tile. 

## S-111 surface currents objects coordinates data structure.

The S-111 surface currents objects coordinates data are also using the [HDF5 H5T_COMPOUND type](https://bitbucket.hdfgroup.org/pages/HDFFV/hdf5doc/master/browse/html/cpplus_RM/class_h5_1_1_comp_type.html).

Example of of one S-111 surface currents objects coordinates data structure for one tiled file having 452 RIOPS surface currents data objects

* __GROUP "Positioning" {DATASET "geometryValues" {DATATYPE H5T_COMPOUND {H5T_IEEE_F32LE "longitude"; H5T_IEEE_F32LE "latitude";} DATASPACE SIMPLE {(452,1)/(452,1)} DATA {(0,0):{-68.0052, 42.37}, ... (451,0):{-68.9981,42.0176}__

# Examples of canadian coastal waters tiled domains available

## 1x1 degree tiles bounding boxes for the Bay of Fundy, Scotian shelf and Northumberland Strait.

![PNG Scotian shelf L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/ScotianShelfL2_tiles.png)

## 1x1 degree tiles bounding boxes for the West-Coast

![PNG West-Coast L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/WCoastL2Tiles.png)

## 1x1 degree tiles bounding boxes for the Gulf of St. Lawrence

![PNG GStl L2 tiles](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_riops/dynamic_hydrographic_products/GSTLL2Tiles.png)
