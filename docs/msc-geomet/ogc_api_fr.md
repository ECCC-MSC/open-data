[In English](ogc_api_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [GeoMet du SMC](readme_fr.md) > OGC API

# OGC API
</br>
Les normes API de l'Open Geospatial Consortium (OGC) sont un ensemble de spécifications développées par l'OGC pour faciliter l'échange interopérable de données et de services géospatiaux sur le web. Ces normes sont conçues pour permettre une intégration et un partage transparents des informations géospatiales entre différents systèmes, applications et organisations. La documentation suivante présente les bases des normes OGC API - Features et OGC API - Coverages et fournit des exemples d'interrogation de GeoMet-OGC-API à l'aide de ces normes.

## Endpoints principaux

##### <span class="badge badge-info">GET /</span> - Page d'accueil

[https://api.weather.gc.ca](https://api.weather.gc.ca/)
</br></br>
La page d'accueil GeoMet-OGC-API avec des liens pour visualiser les collections de données, les processus et les classes de conformité mises en œuvre par l'API.

##### <span class="badge badge-info">GET /collections</span> - Toutes les collections de données
[https://api.weather.gc.ca/collections](https://api.weather.gc.ca/collections)

Récupère les informations décrivant l'ensemble des collections prises en charge et fournit une liste des collections avec le type de données et une brève description.

##### <span class="badge badge-info">GET collections/{collectionID}</span> - Informations spécifiques à la collection
[https://api.weather.gc.ca/collections/hydrometric-daily-mean](https://api.weather.gc.ca/collections/hydrometric-stations)

Récupère des informations descriptives sur une collection spécifique, soit de type entité, soit de type couverture. Par exemple, l'URL ci-dessus renvoie
la page racine de la collection d'entités Stations de surveillance hydrométrique.

##### <span class="badge badge-info">GET /openapi</span> - Documentation de l'OpenAPI

[https://api.weather.gc.ca/openapi](https://api.weather.gc.ca/openapi)

Les liens de la documentation de l'API fournissent une page Swagger de l'API comme outil pour les développeurs afin de fournir des exemples de capacités de demande/réponse/requête. Une représentation JSON est également fournie.

##### <span class="badge badge-info">GET /conformance</span> - Définition de la conformité de l'API
[https://api.weather.gc.ca/conformance](https://api.weather.gc.ca/conformance)

La page de conformité fournit une liste d'URL correspondant aux classes de conformité de l'API de l'OGC supportées par GeoMet-OGC-API.
</br>

## <strong>Paramètres de requête communs</strong>
La section suivante fournit des informations sur les paramètres de requête courants, souvent utilisés lors de l'envoi de requêtes aux types de collection Feature et Coverage. Les paramètres de requête sont transmis avec l'URL de la requête en utilisant le caractère `?` pour séparer le paramètre de requête de l'URL et le caractère `&` pour séparer plusieurs paramètres de requête.

##### <span class="badge badge-info">f</span> - Format du paramètre de requête

[https://api.weather.gc.ca/collections/?f=json](https://api.weather.gc.ca/collections/?f=json) avec le format `json`.

Le paramètre de requête format est utilisé pour spécifier le format de la réponse du serveur. Selon le type de collection, la valeur du paramètre de requête du format peut être l'une des suivantes : html, json. L'exemple ci-dessus renvoie la liste des collections disponibles de GeoMet-OGC-API sous forme d'objet JSON.

Pour les collections d'entités, les résultats peuvent également être renvoyés sous forme de fichier CSV via `?f=csv`

Pour les collections de couverture, le format de sortie de la couverture peut être spécifié via ce paramètre. En fonction de la collection et des formats de sortie supportés, les valeurs suivantes sont supportées : `GRIB`, `GTiff`, et `NetCDF` dans GeoMet-OGC-API.

##### <span class="badge badge-info">bbox</span> - Paramètre de requête pour une boîte de délimitation
[https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?bbox=-71,46,-65,49](https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?bbox=-71,46,-65,49)

Permet d'extraire des informations en fonction d'une région spécifique ou d'une boîte de délimitation. Il s'agit d'une zone rectangulaire définie par deux ensembles de coordonnées qui représentent les extensions minimale et maximale de la boîte. Les valeurs des coordonnées `bbox` doivent être comprises dans les limites de [EPSG:4326](https://epsg.io/4326). Les coordonnées spécifiées doivent être dans l'ordre suivant : `minX, minY, maxX, maxY`.

##### <span class="badge badge-info">datetime</span> - Paramètre de requête de date
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Recherche d'informations en fonction d'une date, d'une année ou d'un intervalle de temps spécifique. Il est fortement recommandé d'utiliser des chaînes de dates conformes à la norme RFC 3339 (c'est-à-dire `YYYY-MM-DD` ou `YYYY-MM-DDTHH:MM:SSZ`). Le paramètre datetime peut être utilisé en conjonction avec le mot-clé `..` pour spécifier une période de temps. Par exemple, `datetime=2012-05-20/..` renvoie tous les éléments à partir de 2015-05-20. `datetime=../2015-11-11` renvoie tous les éléments antérieurs à 2015-11-11.
</br></br>

## OGC API - Features

La norme [OGC API - Features](https://ogcapi.ogc.org/features/) (OAFeat) fournit une liste de spécifications normalisées pour l'interrogation de données géospatiales vectorielles (points, lignes et polygones) sur le web. Vous trouverez ci-dessous des exemples de points d'extrémité de collecte de caractéristiques OGC-API, des exemples de filtrage spatial, temporel et de propriété, ainsi que des détails supplémentaires concernant la pagination.

##### <span class="badge badge-info">GET collections/{collectionID}/items</span> - Éléments de la collection

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items)

Retourne les entités spécifiques d'une collection.

L'URL ci-dessus renvoie des éléments de la collection `hydrometric-daily-mean` :
![Items de la collection](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items.png)


##### <span class="badge badge-info">GET collections/{collectionID}/items/{itemID}</span>
##### Vue d'ensemble d'une seule entité
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items/01AA002](https://api.weather.gc.ca/collections/hydrometric-stations/items/01AA002)

Renvoie l'élément de la collection demandée avec l'ID correspondant et fournit l'ensemble de ses propriétés.

L'URL ci-dessus renvoie l'élément avec l'ID `01AA002` de la collection `stations hydrométriques` :
![Item 01AA002](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_itemID_01AA002.png)

##### <span class="badge badge-info">GET collections/{collectionID}/items?{paramètres de requête}</span>
##### Interroger une collection d'entités

Les requêtes de collecte d'informations permettent de filtrer l'espace, le temps et les propriétés. Les paramètres de filtrage peuvent être combinés pour formuler une requête plus complexe. Le premier paramètre d'une requête doit être spécifié avec `?` et les paramètres suivants avec `&`.</br>

Vous trouverez ci-dessous quelques exemples de différents types de requêtes, allant de simples requêtes de filtrage bbox et datetime à des requêtes plus complexes composées de plusieurs paramètres de requête. Toutes les requêtes portent sur la collection de caractéristiques [hydometric-daily-mean](https://api.weather.gc.ca/collections/hydrometric-daily-mean).


### <span class="badge badge-light">Spatial</span>

Requête par boîte englobante (minx, miny, maxx, maxxy).</br>
    </br>
[https://api.weather.gc.ca/collections/hydrometric-stations/items?bbox=-71,46,-65,49](https://api.weather.gc.ca/collections/hydrometric-stations/items?bbox=-71,46,-65,49)

Renvoie les éléments de la collection d'éléments qui intersectent la boîte de délimitation fournie :
![Carte avec la zone sélectionnée](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_bbox.png)

### <span class="badge badge-light">Temporel</span>

Recherche d'une valeur instantanée avec une seule date :</br>
    </br>
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Renvoie les éléments de la collection d'éléments qui correspondent à la valeur de date fournie :
![Éléments de la collection qui correspondent à la date](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items&_1_datetime.png)

Requête pour un intervalle de temps :</br>
</br>
[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31)


Renvoie les éléments de la collection d'éléments qui se situent dans la plage de dates fournie :
![Entités selon un intervall de date](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items&_intervalle_datetime.png)


Interrogez par période de temps avec le mot-clé ouvert `..` :

*  Depuis une date précise :</br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..)

    Les retours concernent les articles de la collection à partir de 2015-05-20.

*   Jusqu'à une date précise :</br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11)</br>

    Les retours portent sur des éléments de collection antérieurs au 2015-11-11.

### <span class="badge badge-light">Propriété</span>

Interrogation par une propriété de la collection d'entités :</br>

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001)

Retourne les éléments de la collection d'éléments qui ont `STATION_NUMBER = 10CD001`.
![Entités selon le numéro de station](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_stationNumber.png)


### <span class="badge badge-light">Pagination</span>

*   #### <span class="badge badge-light">Offset</span>
    Le paramètre `offset`  peut être utilisé pour spécifier l'enregistrement à partir duquel les caractéristiques sont extraites. La valeur par défaut est `0` (première caractéristique)</br>
    </br>
*   #### <span class="badge badge-light">Nombre total d'entités</span>
    Le paramètre `resulttype=hits` est utilisé pour retourner le nombre d'entités trouvés dans une collection, sans retourner aucune entité de la collection. Le nombre de entitéss se trouve dans la clé `numberMatched` de la réponse.

    [https://api.meteo.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits](https://api.meteo.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits)

    ![Json de numbermatched](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/numberMatched.png)

*   #### <span class="badge badge-light">Limite</span>

    Le paramètre `limit` est utilisé pour définir le nombre maximum d'entités à renvoyer dans la réponse. La taille de la réponse par défaut est de 500 entités.</br>
    Dans la requête suivante, une seule entité est demandée, par exemple, pour inspecter sa géométrie et ses propriétés :
    </br></br>

    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?limit=1](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?limit=1)

    Renvoie un seul élément de la collection :

    ![Entités avec une limite de 1](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_limit.png)

    Les paramètres `offset` et `limit` peuvent être utilisés en tandem pour parcourir les collections d'éntités. Les exemples ci-dessous montrent comment ajuster et paginer les résultats d'une requête.

    *   Interroger et limiter aux éléments 1 à 100 :</br>
        [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100)

    *   Interroger et limiter aux éléments 101-200 :</br>
        [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&offsetx=101&limit=100](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&offset=101&limit=100)
        </br>

*   ### <span class="badge badge-light">Stratégies de pagination</span>

    La stratégie de pagination est couramment utilisée pour extraire de grandes quantités de données. Par exemple, un client peut paginer par 1000 entités pour parcourir l'ensemble d'un enregistrement de station, en commençant par les 1000 premiers éléments et en demandant ensuite les 1000 entités suivantes, jusqu'à ce que tous les éléments soient renvoyés.</br>
    </br>
    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=1000](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=1000)

    [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=1000&limit=1000)</br>

    Les requêtes ci-dessus renvoient respectivement les 1000 premiers éléments et les 1000 éléments suivants.
    Le client peut alors simplement parcourir tous les éléments jusqu'à ce qu'il n'y ait plus d'enregistrements. Il s'agit alors de l'ensemble de l'enregistrement.
    </br>

### <span class="badge badge-light">Combinaison de paramètres de filtre</span>

Interroger toutes les données hydrométriques moyennes journalières d'une seule station entre 2001 et 2010 :</br>

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31)

### <span class="badge badge-light">Exporter au format CSV</span>

Les résultats des requêtes effectuées sur les collections d'entités peuvent être exportés au format CSV en ajoutant `&f=csv` à la requête, ou en cliquant sur l'icône `CSV` en haut à droite de la page de la collection.</br>

[https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=csv](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=csv)

### <span class="badge badge-light">Tri</span>

Les résultats d'une requête peuvent être triés en utilisant le paramètre `sortby`. Par défaut, l'ordre de tri est croissant. Pour un tri descendant, ajoutez le caractère `-` (moins) avant le nom de la propriété. Le tri par plusieurs propriétés est possible en fournissant une liste de propriétés séparées par des virgules au paramètre de requête `sortby`.</br>

`&sortby=PROPERTY` tri l'attribut par odre croissant</br>
`&sortby=-PROPERTY` tri l'attribut par odre décroissant.

Exemples avec la propriété `DATE`:

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=DATE]( https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=DATE) `croissant`

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=-DATE]( https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=-DATE) `décroissant`
</br>

## OGC API - Coverages

La norme [OGC API - Coverages](https://ogcapi.ogc.org/coverages/) spécifie les éléments fondamentaux de l'API pour interagir avec les couvertures (données matricielles). La communauté des données spatiales utilise le terme "couverture" pour désigner des ensembles homogènes de valeurs situées dans l'espace et dans le temps, telles que des données provenant de capteurs spatio-temporels, d'images, de simulations et de statistiques.

##### <span class="badge badge-info">GET collections/{coverageId}</span> - Page d'accueil de la collection de couvertures

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly)

Récupère les métadonnées de couverture détaillées pour la collection spécifiée. Cette page affiche l'étendue géographique des collections, les formes de sortie prises en charge et les liens connexes.

##### <span class="badge badge-info">GET collections/{coverageId}/coverage</span> - Requête de couverture sans paramètres

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage)

Récupère les données de couverture et les informations descriptives connexes (ensemble de plages, ensemble de domaines, type de plage, métadonnées). Elle est comparable à une réponse WCS GetCoverage. Par défaut, la réponse est renvoyée au format JSON. L'URL ci-dessus renvoie l'ensemble des données de couverture pour le champ de couverture par défaut "tas" (température de surface).

##### <span class="badge badge-info">GET collections/{coverageId}/coverage/rangetype</span> - Type d'étendue de la couverture

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/rangetype?](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/rangetype?)

Renvoie le type de plage de la couverture, c'est-à-dire la sémantique des valeurs de données (leurs composants et le type de données). La réponse relative au type d'intervalle renvoie une liste de champs qui peuvent être interrogés par rapport à la couverture. Par exemple, la requête ci-dessous renvoie le type d'intervalle pour la collection CMIP5 Historical annual anomaly.
![RangeType](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/COV_rangeType.png)

##### <span class="badge badge-info">GET collections/{coverageId}/coverage/domainset</span>
##### Ensemble de domaines de couverture

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/domainset](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage/domainset)

Renvoie le domaine de la couverture (l'espace détaillé à n dimensions couvert par les données). Les domaines comprennent les étiquettes d'axe disponibles, l'étendue de la couverture, la taille des pixels et la résolution.

![Domainset](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/COV_domainset.png)

##### <span class="badge badge-info">GET collections/{coverageId}/coverage?{paramètres}</span>
##### Couverture avec paramètres de requête

Les requêtes sur les collections de couvertures permettent un filtrage spatial, temporel et de l'étendue dans l'espace à n dimensions (axes de l'ensemble de domaines) de la couverture elle-même. Le premier paramètre d'une requête doit être spécifié avec `?` et les paramètres suivants avec `&`.

### <span class="badge badge-light">Spatial</span>

Requête par boîte englobante (minx, miny, maxx, maxxy).</br>

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224) ou
[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224&f=NetCDF](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224&f=NetCDF)

### <span class="badge badge-light">Temporel</span>

*   Demande d'une valeur instantanée pour une période unique si une étiquette d'axe "temps" est disponible, pour cette     couverture spécifique :</br>

    [https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905)


*   Demande d'un intervalle de temps :</br>
    </br>
    [https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905)

### <span class="badge badge-light">Rangetype</span>

Requête pour un champ de type plage spécifique avec le paramètre de requête `properties`. Par exemple, la requête ci-dessous permet de récupérer les données de couverture pour le champ de type plage nommé "sit" (épaisseur de la glace de mer).
</br>

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit)

### <span class="badge badge-light">Dimension de l'ensemble du domaine</span>

Interrogation par une dimension spécifiée dans l'ensemble de domaines avec le paramètre d'interrogation `subset`.
</br>

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25)](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25))

### <span class="badge badge-light">Combinaison de paramètres de filtrage</span>

Interroger la couverture avec un filtre spatial et temporel, pour un champ de typerange spécifique via le paramètre de requête `properties`.</br>
    </br>
Retourne au format json par défaut :

[https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 ](https://api.weather.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 )


### <span class="badge badge-light">Exporter au format GTiff ou NetCDF</span>

Les requêtes pointant vers les pages des collections peuvent être exportées au format GTiff et au format NetCDF s'il est disponible. Consultez la racine d'une collection de couverture donnée pour identifier les formats de données de réponse disponibles. Par exemple, la racine d'une collection de couverture donnée peut être consultée pour identifier les formats de données disponibles :

[https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json](https://api.weather.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json)

Sous la clé `links`, les valeurs disponibles pour le paramètre `?f` peuvent être trouvées. Dans ce cas, les données de couverture peuvent être demandées en JSON via `?f=json` ou en NetCDF via `?f=NetCDF`.