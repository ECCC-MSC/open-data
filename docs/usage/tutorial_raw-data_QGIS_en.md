[En français](tutorial_raw-data_QGIS_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > Raw data file in QGIS

# Tutorial: adding raw geospatial file in QGIS

[QGIS](https://qgis.org) is a Geographic Information System (GIS) software that allows the visualization and manipulation of vector (Shapefile, GeoJSON, GeoPackage, etc) or raster (GRIB2, GeoTIFF, NetCDF, etc) geospatial data. To add a raw geospatial file in QGIS:

1. In the menu bar, choose: <b>Layer - Add Layer - Add vector / raster layer</b><br> <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-layer_en.png" width=60%>
2. Navigate to the geospatial file to be added
3. Click on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-add_en.png" width=5%> to display the layer

Animated example of adding a geospatial file in QGIS:

![Adding raw geospatial file](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-raw-file_en.gif)

It is possible to directly add geospatial files from the [MSC Datamart](../msc-datamart/readme_en.md) in QGIS by dragging and dropping a file into the QGIS map interface:

1. Go to the [MSC Datamart website](https://dd.weather.gc.ca) and navigate to the file to be added
2. Drag and drop the file into the QGIS map interface

The following are examples of geospatial file formats available on the MSC Datamart that can be directly added to QGIS:

* Raster data:
    * GRIB2 (.grib2)
    * NetCDF (.nc)
    * GeoTIFF (.tif)
* Vector data:
    * GeoJSON (.geojson)
    * Shapefile (.shp): note that to add a Shapefile in QGIS, you also need to have downloaded the other extensions: .prj, .dbf and .shx and make sure that these files are in the same directory

The same approach also works for adding raw data retrieved from the WCS and OGC API - Features web services available on [MSC GeoMet](../msc-geomet/readme_en.md).

Animated example of adding the MSC Datamart geospatial file to QGIS via Firefox:

![Adding a geospatial file from Datamart](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-raw-file-from-dd_en.gif)
