[En français](tutorial_WMS_QGIS_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > WMS layers in QGIS 

# Tutorial: display, interact and animate WMS layers in QGIS

Usage examples of [MSC GeoMet](../msc-geomet/readme_en.md) geospatial web services in the [free and open source QGIS desktop software](https://qgis.org):

* [Adding WMS layers in QGIS](#adding-wms-layers-in-qgis)
* [Possible interactions with WMS layers in QGIS](#possible-interactions-with-wms-layers-in-qgis)
* [Manipulating the time component of the WMS layers](#manipulating-the-time-component-of-the-wms-layers)

## Adding WMS layers in QGIS

The use of WMS (Web Map Service) layers makes it easy to add geospatial data to a QGIS project without having to download and create the layer styles yourself.

In the following example, the air temperature layer of the MSC Global Deterministic Prediction System (GDPS) is displayed from [MSC GeoMet](../msc-geomet/readme_en.md):

1. Open the QGIS browser panel
    * Right-click in the toolbar
    * Check <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_panneau-explorateur_en.png" width="20%">
2. Add a WMS service 
    * In the browser panel, right-click on `WMS/WMTS`: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_wms-nouvelle-connection_en.png" width="20%">
    * Choose a name for the service and write it in the `Name` box
    * Enter the URL of the geospatial web service: [https://geo.weather.gc.ca/geomet?&service=WMS&version=1.3.0&request=GetCapabilities](https://geo.weather.gc.ca/geomet?&service=WMS&version=1.3.0&request=GetCapabilities) in the `URL` box
    * Click on `OK`
3. Add a WMS layer to the project
    * Return to the browser panel under `WMS/WMTS` and navigate through the tree structure to reach the desired layer

Animated example of the procedure:

![Adding WMS layers in QGIS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_add-wms_en.gif)

## Possible interactions with WMS layers in QGIS

Here are the basic manipulations of a WMS layer:

* To move around the map: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-pan.png">
* To zoom in on a location on the map: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-zoom-in.png">
* To zoom out of a location on the map: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-zoom-out.png">
* To make a "GetFeatureInfo" and get the raw value of a pixel or a geospatial feature of a WMS layer: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-getfeatureinfo.png">

Animated example of these manipulations:

![Examples of interactions with WMS layers](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_wms-pan-zoom-gfi_en.gif)

## Manipulating the time component of the WMS layers 

Manipulation example of the temporal dimension of a WMS layer:

1. Add a WMS layer with at least one time dimension using the browser panel (refer to the section [adding WMS layers in QGIS](#adding-wms-layers-in-qgis))
2. After adding a WMS layer, double-click on the small clock next to the layer name in the layer panel: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-temporal.png">
3. Make sure that the temporal properties of the layer are recognized
    * "Temporal" must be checked
    * "Specify time range" must be selected
    * Make sure that "Start date" and "End date" correspond to the time values of the layer in the "GetCapabilities"
    * Close the layer properties window
4. Open the time control panel in the toolbar: click on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-temporal.png">
    * Update the time values by clicking on: <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-temporal-refresh.png" width="5%">
    * Adjust the time step according to the interval of the time dimension of the WMS layer. This information is available in the "GetCapabilities" of the layer
    * Use the animation tools to manipulate or animate the WMS layer

Animated example of WMS layer temporal manipulation:

![Manipulating the time component of WMS layers](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_wms-temporal_en.gif)
