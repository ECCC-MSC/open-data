[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > GeoMet du SMC


# GeoMet du SMC

Les services GeoMet du SMC rendent publiquement accessibles les données du Service météorologique du Canada (SMC) et d'Environnement et Changement climatique Canada (ECCC) via des services web interopérables et des interfaces de programme (API). Par le biais de standards ouverts, ces services donnent rapidement et gratuitement accès à des milliers de jeux de données et produits météorologiques qui peuvent être intégrés dans les applications spécifiques de l'usager et leurs systèmes d'aide à la décision. Les usagers peuvent développer des applications mobiles, créer des cartes interactives en-ligne, ainsi que de visualiser et animer les données du SMC dans des logiciels de bureau. Les services GeoMet du SMC rendent également possible le découpage de données et la reprojection à la volée, tout autant que la conversion de formats et la visualisation personnalisée de couches de données.


## Accès

L'accès aux services GeoMet du SMC est anonyme et gratuit. Ces services doivent être accédés via un logiciel qui supporte les services web géospatiaux.


### GeoMet-Météo

GeoMet-Météo donne accès aux données météorologique, hydriques et environnementales du Service météorologique du Canada (SMC) par le biais de services web interopérables. Ce service donne accès aux données telles que les alertes météorologiques, les prévisions publiques, les observations ainsi que les données de modèles de prévision numérique du temps.

Capacités de ce service :
* L'URL WMS de GeoMet-Météo : https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities
* L'URL WCS de GeoMet-Météo : https://geo.weather.gc.ca/geomet?lang=fr&service=WCS&version=2.0.1&request=GetCapabilities

### GeoMet-Climat

GeoMet-Climat donne accès aux données d'Environnement et Changement climatique Canada (ECCC) via des services web interopérables. Ce service donne accès aux données climatiques historiques tels que les données climatiques quotidiennes, les sommaires climatiques mensuels et les normales climatiques pour les stations climatiques à travers le pays. GeoMet-Climat est une source de données pour le [Centre Canadien des Services Climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques.html).

Capacités de ce service :
* L'URL WMS de GeoMet-Climat : https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr
* L'URL WCS de GeoMet-Climat : https://geo.weather.gc.ca/geomet-climate?service=WCS&version=2.0.1&request=GetCapabilities&lang=fr

Le code source de GeoMet-Climat et de l'Outil d'extraction de données climatiques est publiquement disponible sur GitHub :
* https://github.com/ECCC-CCCS/geomet-climate
* https://github.com/ECCC-CCCS/climate-data-extraction-tool

### GeoMet-OGC-Features

GeoMet-OGC-Features donne accès aux données d'Environnement et Changement climatique Canada (ECCC) et du Service météorologique du Canada (SMC)par le biais du standard émergeant [OGC-API-Features (WFS 3) de l'Open Geospatial Consortium (OGC)](https://github.com/opengeospatial/WFS_FES). Ce service donne présentement accès aux données hydrométriques et climatiques.

Capacités de ce service :
* L'URL WFS 3 de GeoMet-OGC-Features : https://geo.weather.gc.ca/geomet/features/?f=html

### GeoMet-Beta

GeoMet-Beta donne accès à des données expérimentales et autres données non-opérationnelles. Ce service n'est pas supporté opérationellement.

Capacités de ce service :
* L'URL WMS de GeoMet-Beta : https://geo.weather.gc.ca/geomet-beta?lang=fr&service=WMS&version=1.3.0request=GetCapabilities
* L'URL WCS de GeoMet-Beta : https://geo.weather.gc.ca/geomet-beta?lang=fr&service=WCS&version=2.0.1request=GetCapabilities


## Utilisation

La documentation au sujet de l'utilisation de ces services et des exemples sont disponibles aux endroits suivants :
* La [page de survol de l'utilisation des données](../usage-overview/readme_fr.md)
* La [page d'information technique sur les services web géospatiaux](web-services_fr.md)


## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) afin d'être informés des améliorations et changements aux services GeoMet du SMC.


## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://www.meteo.gc.ca/mainmenu/contact_us_f.html).