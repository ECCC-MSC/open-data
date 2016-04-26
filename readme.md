![ECCC logo](img_eccc-logo.png)

[En français](readme_fr.md)

Meteorological Service of Canada public data documentation
==========================================================

Short description: access MSC public data, free of charge, with the license 

Table of Content
----------------
1. [License](license)
    * The main requirement is to clearly acknowledge Environment and Climate Change Canada as data source

2. Metadata and data discovery
    * link to GoC Open data portal... 

3. MSC meteorological data
    * stuff here
    
4. MSC Datamart
    * Short description: MSC Datamart, weather data files available on an http server
    * AMQP: real-time data push notification and retrieval
      * Pattern matching and triggers (on part, on file, on message)
      * Working examples of retrieving MSC data with AMQP
    * dd_info
    
5. MSC GeoMet
    * PRIORITY // Short description: MSC GeoMet, Interactively accessing MSC data via geospatial web services
    * PRIORITY // Table of Layer groups (list of first level, e.g. GDPS, GIOPS, radar, AQHI, Citypage, etc) with description, formats available (e.g. WMS: styles, WFS: formats, WCS: formats) as columns... NOT ON A PER LAYER BASIS
	    - manually updated table content updates from GeoMet’s GetCapabilities [TO DO, NOT AN ITEM]
	    - full list of layers only in get capabilities?
    * PRIORITY // Services
	    - short description of WMS, WCS, WFS, SLD (copy from WOUDC)
    * Viewing data
	    - .md with what is WMS, how it can be used
	    - SLD
	    - Downloading data
		    - Vector data in WFS 
			    - link to list of WFS accessible layers 
		    - Raster data in WCS
			    - link to list of WCS accessible layers 
		    - Time series
	    - KML (Google Earth examples)
    * PRIORITY // GeoMet-Info
    
6. How to: documented examples for frequent use cases 
    * short description + disclaimer that we don't endorse any software
    * I want to download specific weather data over an area
	    - Link to layer list, give examples of requests and explain query parameters 
    * I want to interactively view the weather data
	    - On the web
	    - in ArcGIS Online
        - On your own web page
	    - in GoC OpenMaps (Federal Government only)
	    - In a desktop software, such as QGIS and Google Earth
	    - On a mobile phone
	    
7. Links
    - [CMC Product Guide](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html)
	-  Reference documentation for Canadian Meteorological Centre (CMC) products
    - [Contact us](http://weather.gc.ca/mainmenu/contact_us_e.html)
        - Contact MSC about its public data

# MOVE ELSEWHERE
ascii
graphs
static maps
produits habillés (mon ti-truc)


