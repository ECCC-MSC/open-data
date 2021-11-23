[En français](readme_fr.md)

![ECCC logo](img_eccc-logo.png)

# Meteorological Service of Canada Open Data User Documentation

The Meteorological Service of Canada makes weather, climate, water and environmental data available to private sector, academics, and the general public.

## Available open data

The **[available open data from the Meteorological Service of Canada](msc-data/readme_en.md)** provides up-to-date information on past, present and future weather, water, climate and environmental conditions over Canada and the world. The main categories of data available are:

* Weather alerts, current conditions and public forecasts
* Weather, water and environmental observations and forecast data
* Climate data

## Data access

Access to open data available on the MSC Datamart and MSC GeoMet services is anonymous and free of charge. The available open data services are:

* **[MSC GeoMet](msc-geomet/readme_en.md)**
    * API to access raw data and products
    * Visualize and animate weather data
    * Integrate data in web maps, mobile apps and desktop software
    * Geospatial web services to clip, reproject, convert format and more
* **[MSC Datamart](msc-datamart/readme_en.md)**
    * Raw data and products available on a web accessible server
    * Real-time push notifications and data retrieval service
* **[Cost-recovered services](cost-recovered/readme_en.md)**
    * Archived data retrieval
    * Dedicated data feeds with 24/7 support

## Usage and tutorials

Overview, examples and tutorials to access and use Meteorological Service of Canada's open data.

* **[Usage overview](usage/readme_en.md)**

**Tutorials**:

* **Access and use data in the QGIS desktop software**:
    * [Add, query and animate WMS layers](usage/tutorial_WMS_QGIS_en.md)
    * [Add and query OGC API Features layers](usage/tutorial_OAFeat_QGIS_en.md)
    * [Add raw data](usage/tutorial_raw-data_QGIS_en.md)
* **[Create interactive web maps with OpenLayers and Leaflet](usage/tutorial_web-maps_en.md)**:
    * Add layers
    * Display popup dialog boxes
    * Animate temporal layers
* **[Create interactive web graphs and tables](usage/tutorial_graphs-tables_en.md)** :
    * Prepare and send requests
    * Create an interactive graph
    * Display a table with forecast data

**Use cases**:

* [Arthur: profits based on the probability of precipitation](../usage/use-case_arthur/use-case_arthur_en/):
    * **Access and use the MSC GeoMet data API directly from a Python script**, specifically the OGC Web Map Service (WMS) standard to create data tables and graphs
* [Cathy: tracking water levels at hydrometric stations](../usage/use-case_oafeat/use-case_oafeat-script_en/):
    * **Access and use the MSC GeoMet data API directly from a Python script**, specifically the OGC API - Features (OAFeat) standard to create time series and interactive maps

**Technical documentation**:

* **[API / geospatial web services technical documentation](msc-geomet/web-services_en.md)**
* **[Use GDAL from the command line](../usage/tutorial_gdal/tutorial_gdal_en/)**

## Data discovery and metadata

### Canadian Open Government Portal

The Meteorological Service of Canada's [metadata is available on the Canadian Open Government portal](https://open.canada.ca/en/open-data), enabling users to search open data that is relevant to Canadians, learn how to work with datasets, and see what people have done with open data across the country.

### WMO Information System (WIS)

The [WMO Information System (WIS)](https://community.wmo.int/activity-areas/wis/wis-overview) enables discovery of authoritative meteorological and hydrological data and supports the collection of data and its exchange between World Meteorological Organization (WMO) Centres and their users. The "WIS Catalogue" describes the data and products available across WMO. Data and products are registered with the WIS by submitting a metadata record to the WIS Catalogue that describes the content, structure and access mechanisms for the associated data or product.

MSC is a WIS Data Collection or Production Centre (DCPC), and provides a Discovery, Access and Retrieval (DAR) service available at [https://api.weather.gc.ca/wis/catalogue/csw](https://api.weather.gc.ca/wis/catalogue/csw).  The DAR supports a number of search interfaces including OGC Catalogue Services for the Web (CSW), Search/Retrieval via URL (SRU), and the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) standard.

## Events

Series of events organized around MSC open data:

* [MSC open data forum - July 8, 2019](events/2019-07_open-data-forum_en.md)
* [METEOHACK hackathon - July 8-11, 2019](events/2019-07_hackathon-METEOHACK_en.md)

## Licence

The End-use Licence determines the conditions for using the data and information. The main requirement is to clearly acknowledge Environment and Climate Change Canada as the data source, [please refer to the Licence for details](licence/readme_en.md).

## Frequently Asked Questions

The most frequently asked questions about MSC's open data are collected in a [FAQ](faq/readme_en.md). If you cannot find the answer to your question, please contact us.

## Your opinion matters to us

In order for the Meteorological Service of Canada open data user documentation to meet your needs, please let us know what you think by answering this short [questionnaire](https://eccc.sondage-survey.ca/f/s.aspx?s=35b3c882-2af9-488f-ad98-9112d2892b8f).

## Contact us

User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).

