[En français](readme_lightning-geomet_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [Lightning](readme_lightning_en.md) > Lightning on MSC GeoMet

# Real time lightning data available on MSC GeoMet

MSC GeoMet provides access to the lightning layer. Users can build mobile apps, create interactive web maps, and display and animate MSC data in desktop software.

## Access to the geospatial web services

The lightning layer is [available on GeoMet-Weather via the Web Map Service (WMS) standard](../../msc-geomet/wms_en.md).

## Usage

The [usage overview page](../../usage/readme_en.md) provides generic information on using these services with desktop software, mobile apps, interactive web maps and direct access. Please refer to the [tutorials](../../usage/tutorials_en.md) and [technical documentation for MSC GeoMet geospatial web services](../../msc-geomet/readme_en.md#available-ogc-standards) for detailed information. See also the [main lightning data page](readme_lightning_en.md) which links to additional information on weather alerts.

### Available layers

There is a single main lightning density layer monitoring lightning across most of Canada.

### Usage tips

Retrieving the list of latest layer timesteps available:

* Users can use the `layer` query parameter in WMS GetCapabilities requests to point to a specific layer and retrieve a smaller XML payload with up-to-date temporal dimensions. Example for the lightning density layer: [https://geo.weather.gc.ca/geomet?&service=WMS&version=1.3.0&request=GetCapabilities&layer=Lightning_2.5km_Density](https://geo.weather.gc.ca/geomet?&service=WMS&version=1.3.0&request=GetCapabilities&layer=Lightning_2.5km_Density)
* Users can also get the most up-to-date time dimensions for all layers that have a time interval in minutes, including lightning density, in a single query, via the use of the `LAYERS_REFRESH_RATE=PT1M` query parameter. In addition, all layers with a time interval in minutes will be included in this GetCapabilities. Example for the query: [https://geo.weather.gc.ca/geomet?LAYERS_REFRESH_RATE=PT1M&SERVICE=WMS&REQUEST=GetCapabilities](https://geo.weather.gc.ca/geomet?LAYERS_REFRESH_RATE=PT1M&SERVICE=WMS&REQUEST=GetCapabilities)
* Additional information is available in the [handling time with WMS section](../../../msc-geomet/wms_en#handling-time)

WMS styles:

* The list of available WMS styles is provided in the WMS GetCapabilities response ([example of a WMS GetCapabilities request](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=Lightning_2.5km_Density))
* Furthermore, users can request layers with their own custom styles with the Styled Layer Descriptor (SLD) standard, please refer to the [SLD technical documentation](../../../msc-geomet/wms_en#handling-styles).

Legends:

* Legends are available for every WMS style. Details are provided in [the WMS legend technical documentation](../../../msc-geomet/wms_en#wms-getlegendgraphic).
* Legend retrieval request example: `https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Lightning_2.5km_Density&format=image/png&STYLE=Lightning`

![The Lightning WMS legend](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Lightning_2.5km_Density&format=image/png&STYLE=Lightning)

## Support

The MSC GeoMet services are operational 24/7. User support is provided on a best-effort basis during normal business hours. If you have any questions about these services, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcement mailing list

We encourage users to subscribe to the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement mailing list to be informed of enhancements and changes to the MSC GeoMet services.



<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
