What's missing in this page:
* The Table of Content
* The mouseover tooltip for MSC: "Service météorologique du Canada"
* The mouseover tooltip for WMS: "Web Map Service", in the section: FAQ / Can I display layers' legends...
* The FAQ section has its subsections folded by default







#  Services web géospatiaux

GeoMet du SMC donne accès aux données du Service météorologique du Canada (SMC) d'Environnement et Changement climatique Canada, notamment les données brutes de modèles de prévision numérique du temps et de la mosaïque des radars météo, par le biais de standards de l'Open Geospatial Consortium (OGC). Les couches météorologiques sont dynamiquement servies par le biais du [standard Web Map Service (WMS)](http://www.opengeospatial.org/standards/wms) afin de permettre aux utilisateurs d'afficher les données météorologiques dans leurs propres outils, sur des cartes interactives en ligne et dans les applications mobiles.


## Utilisateurs ciblés

Ce service vise les utilisateurs spécialisés et les développeurs ayant une connaissance de la météorologie et des technologies de l'information géospatiale. Les utilisateurs peuvent visualiser et traiter les données météorologiques à l'aide d'outils géospatiaux communs ; intégrer les couches météorologiques avec d'autres données dans leurs propres plateformes, ou ; afficher les couches météorologiques sur des cartes intéractives en ligne ou sur des appareils mobiles.


## Comment utiliser le service

### Web Map Service

GeoMet du SMC sert les couches météorologiques à de multiples pas de temps par le biais du [standard Web Map Service (WMS)](http://www.opengeospatial.org/standards/wms) accompagné des métadonnées associées fournies selon le standard ISO 19115.

Les services web GeoMet du SMC sont accessibles sur :<br>
WMS: http://geo.weather.gc.ca/geomet/?lang=fr&service=WMS&request=GetCapabilities<br>
WCS: http://geo.weather.gc.ca/geomet/?lang=fr&service=WCS&request=GetCapabilities<br>
WFS: http://geo.weather.gc.ca/geomet/?lang=fr&service=WFS&request=GetCapabilities

### Modifications au services GeoMet

Le SMC se doit d'être flexible dans sa manière de fournir ses données spécialisées aux usagers intéressés. Pour ce faire, nous devons être en mesure de faire des mises à jour et des changements à nos formats ou nos données mêmes en temps opportun, c'est-à-dire avec les avancements continus de la technologie et des standards. Le SMC ne s'engage nullement à utiliser un format ou standard particulier pour une période de temps prolongé. Le SMC n'a aucune obligation d'aviser les usagers à l'avance de changements sur le serveur, mais fera tous les efforts pour le faire lorsque possible, en informant les usagers inscrits à notre liste de distribution. Muni de cette information, il est de la responsabilité des usagers de s'assurer qu'ils s'adaptent aux modifications des formats, le moment d'émission, le type de données, etc. Afin de vous abonner à notre liste d'usagers GeoMet-Information, allez à : [liste de distribution GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info).


### Licence

Les conditions d'utilisation et les obligations d'attribution envers Environnement Canada sont définies dans le [texte de licence d'utilisation](http://dd.weatheroffice.gc.ca/doc/LICENCE_GENERAL.txt).



## Foire aux questions


### Comment puis-je utiliser ces données ?

Les couches météorologiques de GeoMet peuvent être accédées par le biais du standard Web Map Service (WMS).

* Les couches accédées par le biais du standard WMS peuvent être utilisées pour bâtir des cartes interactives en ligne et des applications mobiles à l'aide d'outils tels que OpenLayers et Leaflet.
* Les couches accédées par le biais du standard WMS peuvent être affichées par une multitude de logiciels, tel des logiciels propriétaires comme ArcGIS d'Esri et des logiciels libres tels que QGIS.

Il est anticipé que les couches météorologiques de GeoMet rejoindront les consommateurs à travers le développement d'applications par des tiers.


### Quels sont les bénéfices d'utiliser les services web GeoMet ?

Les services web GeoMet vous offrent :

* La capacité d'intégrer, de combiner et d'incorporer des couches météorologiques aux données et outils de votre propre organisation.
* Vous pouvez construire des cartes interactives en ligne avec peu d'efforts.
* Aucun téléchargement de fichiers n'est requis pour afficher les couches météorologiques.
* La capacité de visualiser les données pour votre zone d'intérêt sans la nécessité de télécharger ou charger des données à l'extérieur de votre zone d'intérêt.
* Les données sont toujours à jour.
* Capacité de visualiser de multiples couches ou champs de données simultanément.


### Puis-je utiliser les services GeoMet dans des produits commerciaux ?

Oui. Vous devez spécifier que les données proviennent d'Environnement et Changement climatique Canada, veuillez-vous référer aux [détails dans la licence d'utilisation](http://dd.weatheroffice.gc.ca/doc/LICENCE_GENERAL.txt).


### Puis-je afficher la légende des couches ?

Oui. L'accès aux légendes est spécifié par la requête GetCapabilities du standard WMS.


### Dois-je être connecté à Internet pour utiliser GeoMet ?

Oui. Les couches météorologiques de GeoMet du SMC sont servies à la volée et requirent une connection Internet.