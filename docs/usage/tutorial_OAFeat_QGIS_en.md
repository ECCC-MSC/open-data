[En français](tutorial_OAFeat_QGIS_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > OGC API - Features layers in QGIS

# Tutorial: using OGC API - Features data in QGIS

Adding OGC API - Features data in the [free and open source QGIS desktop software](https://qgis.org):

1. In the menu bar, choose: <b>Layer - Add Layer - Add WFS Layer: </b> <br> <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_ajouter-wfs_en.png" width=60%> 
2. Add a new connection
    * Click on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-new_en.png" width=7%> to add a new connection
    * Choose a name for the service and write it in the `Name` box
    * Enter the URL of the geospatial web service: [https://geo.weather.gc.ca/geomet/features](https://geo.weather.gc.ca/geomet/features) in the `URL` box
    * In the `Option WFS` box at the `Version` line, select <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-ogc-api-features.png" width=15%> 
    * Click on `OK`
3. Click on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-connexion_en.png" width=7%> for a list of available layers
4. Build a query (optional step)
    * Click on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-construire-requete_en.png" width=7%> to build a query and filter the data to be displayed
    * Building a query using the `Fields`, `Values` and `Operators` panels
    * Validate the query by clicking on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-test_en.png" width=5%>
    * Click on `OK` 
5. Click on <img src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_button-add_en.png" width=5%> to display the layer

Please refer to the [OGC API - Features](../msc-geomet/web-services_en/#ogc-api-features) section for more details on this standard.

Animated example of OGC API - Features layer in QGIS:

![Adding OGC API - Features data](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/images_QGIS/qgis_ogc-api-features-add-filters_en.gif)
