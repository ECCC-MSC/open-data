[En français](readme_fr.md)

![ECCC logo](img_eccc-logo.png)

# Meteorological Service of Canada public data documentation

Short description: access MSC public data, free of charge, acknowledge the source

## Table of Content

1. [License](license)
    * The main requirement is to clearly acknowledge Environment and Climate Change Canada as data source

2. [Data discovery and metadata](metadata)
    * Access to Goc Open data portal for discovery and MSC's metadata

3. [MSC meteorological data](msc-data)
    * Change log
    * Content of the [CMC Product Guide](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html)
    * Weather alerts
    * Weather observations
      * Weather radar
      * Observations at stations
    * Numerical Weather Prediction
      * How it works
        * Weather variables, MR, FH, FHI, extent
      * Deterministic
        * GDPS
        * ...
      * Probabilistic
        * GEPS
        * ...
    * Other datasets
      * Forecast polygons
      * Weatheradio
      * ...
4. Data access
    * Generic description: anonymous, free of charge, acknowledge the source
    * [MSC Datamart](msc-datamart)
        * Short description: MSC Datamart, weather data files available on an http server
        * Access
          * Per dataset:
            * Nomenclature
            * Data formats
          * AMQP: real-time data push notification and retrieval
        * Support
        * dd_info

    * [MSC GeoMet](msc-geomet)
        * Short description: MSC GeoMet, Interactively accessing MSC data via geospatial web services
        * Geospatial web services
    		  * Short description of WMS, WCS, WFS, SLD (copy from WOUDC)
        * Available data
    		  * Link to layer list, give examples of requests and explain query parameters
          * Table of Layer groups (list of first level, e.g. GDPS, GIOPS, radar, AQHI, Citypage, etc) with description, formats available (e.g. WMS: styles, WFS: formats, WCS: formats) as columns...
        * Support
        * GeoMet-Info

6. [How to: documented examples for frequent use cases](how-to)
    * Short description + disclaimer that we don't endorse any software
    * Viewing data
	    * Static
		* Static maps over an area (habillées ou non)
		* Time series
	    * I want to interactively view the weather data
      * in ArcGIS Online
		* On the web
		* On your own web page
			* in GoC OpenMaps (Federal Government only)
			* In a desktop software, such as QGIS and Google Earth
			* On a mobile phone
    * Downloading data
        * AMQP, wget
			* Pattern matching and triggers (on part, on file, on message)
			* Working examples of retrieving MSC data with AMQP
        * Vector data in WFS
		      * link to list of WFS accessible layers
		* Raster data in WCS
		  * link to list of WCS accessible layers
		* Time series
		* ASCII

7. [FAQ](faq)
    * Access to archived data
    * Access to other dataset
        * Lightning data

8. [Contact us](http://weather.gc.ca/mainmenu/contact_us_e.html)
