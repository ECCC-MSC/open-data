[En français](readme_fr.md)

![ECCC logo](img_eccc-logo.png)

Meteorological Service of Canada public data documentation
==========================================================

Short description: access MSC public data, free of charge

Table of Content
----------------
1. [License](license)
    * The main requirement is to clearly acknowledge Environment and Climate Change Canada as data source

2. [Metadata and data discovery](metadata)
    * link to GoC Open data portal... 

3. [MSC meteorological data](msc-data)
    * stuff from wxo here, such as GRIB and model description,  - LOW PRIORITY
    
4. [MSC Datamart](msc-datamart)
    * Short description: MSC Datamart, weather data files available on an http server
    * AMQP: real-time data push notification and retrieval
    * dd_info
    
5. [MSC GeoMet](msc-geomet)
    * Short description: MSC GeoMet, Interactively accessing MSC data via geospatial web services
    * Table of Layer groups (list of first level, e.g. GDPS, GIOPS, radar, AQHI, Citypage, etc) with description, formats available (e.g. WMS: styles, WFS: formats, WCS: formats) as columns... NOT ON A PER LAYER BASIS
		* manually updated table content updates from GeoMet’s GetCapabilities [TO DO, NOT AN ITEM]
		* full list of layers only in get capabilities?
		* add layers by model, layers by type; e.g. wind layers = global, regional, maximum gust, probabilities, and so on
    * Services
		* Short description of WMS, WCS, WFS, SLD (copy from WOUDC)
		* Link to layer list, give examples of requests and explain query parameters 
    * GeoMet-Info
    
6. [How to: documented examples for frequent use cases](how-to)
    * Short description + disclaimer that we don't endorse any software
    * Viewing data
	    * Static
		* Static maps over an area (habillées ou non)
		* Time series
	    * I want to interactively view the weather data
		* On the web
		* in ArcGIS Online
		* KML (Google Earth examples)
		* On your own web page
			* in GoC OpenMaps (Federal Government only)
			* In a desktop software, such as QGIS and Google Earth
			* On a mobile phone
    * Downloading data
        * AMQP
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

8. Links
    * [CMC Product Guide](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html)
		- Reference documentation for Canadian Meteorological Centre (CMC) products
    * [Contact us](http://weather.gc.ca/mainmenu/contact_us_e.html)
		- Contact MSC about its public data