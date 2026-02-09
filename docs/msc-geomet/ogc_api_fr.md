[In English](ogc_api_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [GeoMet du SMC](readme_fr.md) > OGC API

# OGC API
</br>
Les normes API de l'Open Geospatial Consortium (OGC) sont un ensemble de spécifications développées par l'OGC pour faciliter l'échange interopérable de données et de services géospatiaux sur le web. Ces normes sont conçues pour permettre une intégration et un partage transparents des informations géospatiales entre différents systèmes, applications et organisations. La documentation suivante présente les bases des normes OGC API - Features et OGC API - Coverages et fournit des exemples d'interrogation de GeoMet-OGC-API à l'aide de ces normes.

## Points d'accès principaux

##### <span class="badge badge-info">GET /</span> - Page d'accueil

[https://api.meteo.gc.ca](https://api.meteo.gc.ca)
</br></br>
La page d'accueil GeoMet-OGC-API avec des liens pour visualiser les collections de données, les processus et les classes de conformité mises en œuvre par l'API.

##### <span class="badge badge-info">GET /collections</span> - Toutes les collections de données
[https://api.meteo.gc.ca/collections](https://api.meteo.gc.ca/collections)

Récupère les informations décrivant l'ensemble des collections prises en charge et fournit une liste des collections avec le type de données et une brève description.

##### <span class="badge badge-info">GET collections/{collectionID}</span> - Informations spécifiques à la collection
[https://api.meteo.gc.ca/collections/hydrometric-daily-mean](https://api.meteo.gc.ca/collections/hydrometric-stations)

Récupère des informations descriptives sur une collection spécifique, soit de type entité, soit de type couverture. Par exemple, l'URL ci-dessus renvoie
la page racine de la collection d'entités Stations de surveillance hydrométrique.

##### <span class="badge badge-info">GET /openapi</span> - Documentation de l'OpenAPI

[https://api.meteo.gc.ca/openapi](https://api.meteo.gc.ca/openapi)

Les liens de la documentation de l'API fournissent une page Swagger de l'API comme outil pour les développeurs afin de fournir des exemples de capacités de demande/réponse/requête. Une représentation JSON est également fournie.

##### <span class="badge badge-info">GET /conformance</span> - Définition de la conformité de l'API
[https://api.meteo.gc.ca/conformance](https://api.meteo.gc.ca/conformance)

La page de conformité fournit une liste d'URL correspondant aux classes de conformité de l'API de l'OGC supportées par GeoMet-OGC-API.
</br>

## <strong>Paramètres de requête communs</strong>
La section suivante fournit des informations sur les paramètres de requête courants, souvent utilisés lors de l'envoi de requêtes aux types de collection Feature et Coverage. Les paramètres de requête sont transmis avec l'URL de la requête en utilisant le caractère `?` pour séparer le paramètre de requête de l'URL et le caractère `&` pour séparer plusieurs paramètres de requête.

##### <span class="badge badge-info">f</span> - Format du paramètre de requête

[https://api.meteo.gc.ca/collections/?f=json](https://api.meteo.gc.ca/collections/?f=json) avec le format `json`.

Le paramètre de requête format est utilisé pour spécifier le format de la réponse du serveur. Selon le type de collection, la valeur du paramètre de requête du format peut être l'une des suivantes : html, json. L'exemple ci-dessus renvoie la liste des collections disponibles de GeoMet-OGC-API sous forme d'objet JSON.

Pour les collections d'entités, les résultats peuvent également être renvoyés sous forme de fichier CSV via `?f=csv`

Pour les collections de couverture, le format de sortie de la couverture peut être spécifié via ce paramètre. En fonction de la collection et des formats de sortie supportés, les valeurs suivantes sont supportées : `GRIB`, `GeoTiff`, et `NetCDF` dans GeoMet-OGC-API.

##### <span class="badge badge-info">bbox</span> - Paramètre de requête pour une boîte de délimitation
[https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?bbox=-71,46,-65,49](https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?bbox=-71,46,-65,49)

Permet d'extraire des informations en fonction d'une région spécifique ou d'une boîte de délimitation. Il s'agit d'une zone rectangulaire définie par deux ensembles de coordonnées qui représentent les extensions minimale et maximale de la boîte. Les valeurs des coordonnées `bbox` doivent être comprises dans les limites de [EPSG:4326](https://epsg.io/4326). Les coordonnées spécifiées doivent être dans l'ordre suivant : `minX, minY, maxX, maxY`.

##### <span class="badge badge-info">datetime</span> - Paramètre de requête de date
[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Recherche d'informations en fonction d'une date, d'une année ou d'un intervalle de temps spécifique. Il est fortement recommandé d'utiliser des chaînes de dates conformes à la norme RFC 3339 (c'est-à-dire `YYYY-MM-DD` ou `YYYY-MM-DDTHH:MM:SSZ`). Le paramètre datetime peut être utilisé en conjonction avec le mot-clé `..` pour spécifier une période de temps. Par exemple, `datetime=2012-05-20/..` renvoie tous les éléments à partir de 2015-05-20. `datetime=../2015-11-11` renvoie tous les éléments antérieurs à 2015-11-11.
</br></br>

## OGC API - Features

La norme [OGC API - Features](https://ogcapi.ogc.org/features/) (OAFeat) fournit une liste de spécifications normalisées pour l'interrogation de données géospatiales vectorielles (points, lignes et polygones) sur le web. Vous trouverez ci-dessous des exemples de points d'extrémité de collecte de caractéristiques OGC-API, des exemples de filtrage spatial, temporel et de propriété, ainsi que des détails supplémentaires concernant la pagination.

##### <span class="badge badge-info">GET collections/{collectionID}/items</span> - Éléments de la collection

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items)

Retourne les entités spécifiques d'une collection.

L'URL ci-dessus renvoie des éléments de la collection `hydrometric-daily-mean` :
![Items de la collection](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items.png)


##### <span class="badge badge-info">GET collections/{collectionID}/items/{itemID}</span>
##### Vue d'ensemble d'une seule entité
[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items/01AA002](https://api.meteo.gc.ca/collections/hydrometric-stations/items/01AA002)

Renvoie l'élément de la collection demandée avec l'ID correspondant et fournit l'ensemble de ses propriétés.

L'URL ci-dessus renvoie l'élément avec l'ID `01AA002` de la collection `stations hydrométriques` :
![Item 01AA002](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_itemID_01AA002.png)

##### <span class="badge badge-info">GET collections/{collectionID}/items?{paramètres de requête}</span>
##### Interroger une collection d'entités

Les requêtes de collecte d'informations permettent de filtrer l'espace, le temps et les propriétés. Les paramètres de filtrage peuvent être combinés pour formuler une requête plus complexe. Le premier paramètre d'une requête doit être spécifié avec `?` et les paramètres suivants avec `&`.</br>

Vous trouverez ci-dessous quelques exemples de différents types de requêtes, allant de simples requêtes de filtrage bbox et datetime à des requêtes plus complexes composées de plusieurs paramètres de requête. Toutes les requêtes portent sur la collection de caractéristiques [hydometric-daily-mean](https://api.meteo.gc.ca/collections/hydrometric-daily-mean).


### <span class="badge badge-light">Spatial</span>

Requête par boîte englobante (minx, miny, maxx, maxxy).</br>
    </br>
[https://api.meteo.gc.ca/collections/hydrometric-stations/items?bbox=-71,46,-65,49](https://api.meteo.gc.ca/collections/hydrometric-stations/items?bbox=-71,46,-65,49)

Renvoie les éléments de la collection d'éléments qui intersectent la boîte de délimitation fournie :
![Carte avec la zone sélectionnée](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_bbox.png)

### <span class="badge badge-light">Temporel</span>

Recherche d'une valeur instantanée avec une seule date :</br>
    </br>
[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Renvoie les éléments de la collection d'éléments qui correspondent à la valeur de date fournie :
![Éléments de la collection qui correspondent à la date](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items&_1_datetime.png)

Requête pour un intervalle de temps :</br>
</br>

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31)


Renvoie les éléments de la collection d'éléments qui se situent dans la plage de dates fournie :
![Entités selon un intervall de date](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items&_intervalle_datetime.png)


Interrogez par période de temps avec le mot-clé ouvert `..` :

*  Depuis une date précise :</br>
    [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..)

    Les retours concernent les articles de la collection à partir de 2015-05-20.

*   Jusqu'à une date précise :</br>
    [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11)</br>

    Les retours portent sur des éléments de collection antérieurs au 2015-11-11.

### <span class="badge badge-light">Propriété</span>

Interrogation par une propriété de la collection d'entités :</br>

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001)

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

    Le paramètre `limit` est utilisé pour définir le nombre maximum d'entités à renvoyer dans la réponse. La taille limite de la réponse est de 10,000 entités par requête.</br>
    Dans la requête suivante, une seule entité est demandée, par exemple, pour inspecter sa géométrie et ses propriétés :
    </br></br>

    [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?limit=1](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?limit=1)

    Renvoie un seul élément de la collection :

    ![Entités avec une limite de 1](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/GET_items_limit.png)

    Les paramètres `offset` et `limit` peuvent être utilisés en tandem pour parcourir les collections d'éntités. Les exemples ci-dessous montrent comment ajuster et paginer les résultats d'une requête.

    *   Interroger et limiter aux éléments 1 à 100 :</br>
        [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100)

    *   Interroger et limiter aux éléments 101-200 :</br>
        [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&offsetx=101&limit=100](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&offset=101&limit=100)
        </br>

*   ### <span class="badge badge-light">Stratégies de pagination</span>

    La stratégie de pagination est couramment utilisée pour extraire de grandes quantités de données. Par exemple, un client peut paginer par 500 entités pour parcourir l'ensemble d'un enregistrement de station, en commençant par les 500 premiers éléments et en demandant ensuite les 500 entités suivantes, jusqu'à ce que tous les éléments soient renvoyés.</br>
    </br>
    [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=500](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=0&limit=500)

    [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=500&limit=500](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&offset=500&limit=500)</br>

    Les requêtes ci-dessus renvoient respectivement les 500 premiers éléments et les 500 éléments suivants. Le client peut alors simplement parcourir tous les éléments jusqu'à ce qu'il n'y ait plus d'enregistrements. Il s'agit alors de l'ensemble de l'enregistrement. Le point d'accès `/items` renvoie aussi un lien `next` qui peut être utilisé pour récupérer la page suivante de résultats. Le lien `next` contiendra le paramètre `offset` mis à jour pour la prochaine page de résultats.
    </br>

### <span class="badge badge-light">Filtrer la liste des propriétés d'un élément interrogé</span>

Interroger une collection d'éléments et renvoyer les caractéristiques pour lesquelles la liste des propriétés associées est limitée aux propriétés énumérées dans la valeur `properties=`. Par exemple, la requête ci-dessous retourne des propriétés reliées aux observations de pression atmosphérique, au format JSON.
</br>

[https://api.meteo.gc.ca/collections/swob-realtime/items?lang=en&offset=0&sortby=-date_tm-value&url=CYRV&properties=date_tm-value%2Cmslp%2Cmslp-uom%2Cmslp-qa&f=json](https://api.meteo.gc.ca/collections/swob-realtime/items?lang=en&offset=0&sortby=-date_tm-value&url=CYRV&properties=date_tm-value%2Cmslp%2Cmslp-uom%2Cmslp-qa&f=json)

### <span class="badge badge-light">Combinaison de paramètres de filtre</span>

Interroger toutes les données hydrométriques moyennes journalières d'une seule station entre 2001 et 2010 :</br>

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31)

### <span class="badge badge-light">Exporter au format CSV</span>

Les résultats des requêtes effectuées sur les collections d'entités peuvent être exportés au format CSV en ajoutant `&f=csv` à la requête, ou en cliquant sur l'icône `CSV` en haut à droite de la page de la collection.</br>

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?f=csv](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?f=csv)

### <span class="badge badge-light">Tri</span>

Les résultats d'une requête peuvent être triés en utilisant le paramètre `sortby`. Par défaut, l'ordre de tri est croissant. Pour un tri descendant, ajoutez le caractère `-` (moins) avant le nom de la propriété. Le tri par plusieurs propriétés est possible en fournissant une liste de propriétés séparées par des virgules au paramètre de requête `sortby`.</br>

`&sortby=PROPERTY` tri l'attribut par odre croissant</br>
`&sortby=-PROPERTY` tri l'attribut par odre décroissant.

Exemples avec la propriété `DATE`:

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=DATE]( https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=DATE) `croissant`

[https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=-DATE]( https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000&sortby=-DATE) `décroissant`
</br>

---------------------


## OGC API - Coverages

La norme [OGC API - Coverages](https://ogcapi.ogc.org/coverages/) spécifie les éléments fondamentaux de l'API pour interagir avec les couvertures (données matricielles). La communauté des données spatiales utilise le terme "couverture" pour désigner des ensembles homogènes de valeurs situées dans l'espace et dans le temps, telles que des données provenant de capteurs spatio-temporels, d'images, de simulations et de statistiques.

##### <span class="badge badge-info">GET collections/{coverageId}</span> - Page d'accueil de la collection de couvertures

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly)

Récupère les métadonnées de couverture détaillées pour la collection spécifiée. La réponse en JSON pour cette page affiche l'étendue géographique de la collection, la taille de la grille et les étendues (spatiale, temporelle et toute dimension additionnelle). La page racine de la collection présente aussi d'autres liens associés à la collection tels que le schéma de la collection (champs disponibles) et les URLs de couverture pour chaque format permis par la collection.


##### <span class="badge badge-info">GET collections/{coverageId}/schema</span> - Schéma de la couverture

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/schema](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/schema)

Récupère le schéma de la collection de couverture. Le schéma fournit une liste des champs disponibles et leurs types de données. Le schéma peut être retourné en format JSON ou HTML et peut être utilisé pour comprendre les champs disponibles des données de couverture.

##### <span class="badge badge-info">GET collections/{coverageId}/coverage</span> - Requête de couverture sans paramètres

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage)

Renvoie les données de couverture pour la collection spécifiée. La réponse inclura toutes les données disponibles de la collection, ce qui peut représenter un volume important. Il est recommandé d’utiliser des paramètres de requête pour filtrer les données retournées. Les données peuvent être retournées dans différents formats, comme [CoverageJSON](https://covjson.org/), GRIB ou NetCDF, selon la collection et les formats de sortie qu’elle prend en charge. Consultez les liens de la page racine de la collection pour connaître les formats disponibles.

##### <span class="badge badge-info">GET collections/{coverageId}/coverage?{paramètres}</span>
##### Couverture avec paramètres de requête

Les requêtes sur les collections de couvertures permettent un filtrage spatial, temporel et de l'étendue dans l'espace à n dimensions de la couverture elle-même. Le premier paramètre d'une requête doit être spécifié avec `?` et les paramètres suivants avec `&`.

### <span class="badge badge-light">Spatial</span>

Requête par boîte englobante (minx, miny, maxx, maxxy).</br>

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&bbox=-80.557251,42.561173,-75.135498,44.805224)

### <span class="badge badge-light">Temporel</span>

*   Demande d'une valeur instantanée pour une période unique si une étiquette d'axe "temps" est disponible, pour cette     couverture spécifique :</br>

    [https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1905)


*   Demande d'un intervalle de temps :</br>
    </br>
    [https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?f=json&datetime=1901/1905)

### <span class="badge badge-light">Champ du schéma</span>

Requête pour un champ spécifique du schéma avec le paramètre de requête `properties`. Par exemple, la requête ci-dessous permet de récupérer les données de couverture pour le champ nommé "sit" (épaisseur de la glace de mer).
</br>

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?properties=sit)

### <span class="badge badge-light">Dimensions supplémentaires</span>

Interrogez des dimensions supplémentaires (autres que les dimensions spatiales et temporelles, interrogées respectivement via les paramètres `bbox` et `datetime`) avec le paramètre de requête `subset`. Les dimensions supplémentaires disponibles sont répertoriées sous la clé `extent` à la racine de la collection de couverture, via la réponse JSON uniquement.
</br>

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25)](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?subset=percentile(25))

### <span class="badge badge-light">Combinaison de paramètres de filtrage</span>

Interroger la couverture avec un filtre spatial, un filtre temporel et un filtre pour un champ spécifique via le paramètre de requête `properties`.</br>
    </br>
Retourne au format json par défaut :

[https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 ](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly/coverage?bbox=-80.557251,42.561173,-75.135498,44.805224&properties=sfcWind&datetime=1901/1905 )


### <span class="badge badge-light">Exporter au format GeoTiff ou NetCDF</span>

Les requêtes pointant vers les pages des collections peuvent être exportées au format GeoTiff et au format NetCDF s'il est disponible. Consultez la racine d'une collection de couverture donnée pour identifier les formats de données de réponse disponibles. Par exemple, la racine d'une collection de couverture donnée peut être consultée pour identifier les formats de données disponibles :

[https://api.meteo.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json](https://api.meteo.gc.ca/collections/climate:cmip5:projected:annual:absolute?f=json)

Sous la clé `links`, les valeurs disponibles pour le paramètre `?f` peuvent être trouvées. Dans ce cas, les données de couverture peuvent être demandées en JSON via `?f=json` ou en NetCDF via `?f=NetCDF`.


---------------------

## OGC API - Filtrage avancé avec CQL2

L'API GeoMet-OGC prend en charge le filtrage des données à l’aide du langage de requête commun (Common Query Language, CQL2) via le paramètre de requête `?filter` dans la requête HTTP. `CQL2` est une [norme de l’OGC](https://docs.ogc.org/is/21-065r2/21-065r2.html) conçue pour prendre en charge des requêtes avancées sur les données géospatiales et effectuer le filtrage directement sur le serveur. En utilisant CQL2, les clients peuvent réduire la quantité de données retournées et ne récupérer que les données pertinentes.

CQL2 permet aux utilisateurs de construire des requêtes flexibles et précises basées sur les attributs et la géométrie des entités.</br>

* Correspondances exactes : `=` recherche les entités pour lesquelles un attribut possède une valeur exacte.</br>
* Chaînes partielles ou mots-clés : `LIKE` avec le caractère générique `%`.</br>
* Opérateurs de comparaison : `>`, `<`, `>=`, `<=` permettent de filtrer les valeurs numériques ou temporelles.</br>
* Opérateurs logiques : `AND`, `OR`, `NOT` permettent de comparer des conditions.</br>
* Prédicats spatiaux : `INTERCEPTS`, `DISJOINT` permettent de filtrer selon la géométrie.</br>

La liste complète des prédicats disponibles est accessible dans la [norme OGC CQL2](https://docs.ogc.org/is/21-065r2/21-065r2.html).

Les valeurs de type chaîne doivent être placées entre guillemets simples `''` et le chemin de la propriété (`properties.attribute`) doit correspondre exactement au nom de l'attribut défini dans le schéma de la collection (sensible à la casse).

Pour les collections GeoMet-OGC-API, la syntaxe est :
```html
https://api.meteo.gc.ca/collections/{collectionID}/items?filter=<expression CQL2>&<expression CQL2>
```
---------------------

##### <span class="badge badge-info">1. Recherche de correspondances exactes</span>


**1.1)** Filtrer tous les bulletins météorologiques de type `CA` provenant du bureau émetteur `AO`. </br>
```python
CQL2: ?filter=properties.type=CA AND properties.issuing_office=AO
```
[https://api.meteo.gc.ca/collections/bulletins-realtime/items?filter=properties.type=CA AND properties.issuing_office=AO &lang=fr](https://api.meteo.gc.ca/collections/bulletins-realtime/items?filter=properties.type=CA%20AND%20properties.issuing_office=AO&lang=fr)
</br> </br>

**1.2)** Filtrer `Climat - Observations quotidiennes` par l'attribut `LOCAL_DAY`. Ici, `LOCAL_DAY` doit être en majuscules, conformément au schéma.
```python
CQL2: ?filter=properties.LOCAL_DAY=15
```
[https://api.meteo.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_DAY=15 &lang=fr](https://api.meteo.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_DAY=15 &lang=fr)

---------------------

##### <span class="badge badge-info">2. Recherche de mots clés partiels</span>

CQL2 prend en charge la correspondance partielle de texte grâce à l'opérateur `LIKE`. Il permet de rechercher des sous-chaînes dans des attributs textuels en utilisant le caractère générique `%`, qui peut représenter zéro ou plusieurs caractères. La comparaison est insensible à la casse, mais la chaîne de recherche **doit** être saisie en <u>minuscules</u> et entre <u>guillemets simples</u>. Si la valeur de l'attribut contient plusieurs mots, le prédicat `LIKE` est appliqué à la valeur textuelle entière, comparant le motif à toute sous-chaîne présente.

**2.1)** Trouver tous les `STATION_NAME` contenant le mot-clé `LAKE`. Dans ce cas, `'%lak%'` correspond à des mots clés insensibles à la casse, tels que `Lake, lak5, SPOKIN LAKE 4E, 2LAKE9, LaK`.</br>
```
CQL2: ?filter=properties.STATION_NAME LIKE '%lak%'
```
[https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE '%lak%' &lang=fr](https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20LIKE%20%27%lak%%27&lang=fr)
</br></br>


**2.2)** Filtrer uniquement le nom spécifique de la station dont le nom est ou n'est pas (`NOT`) dans une liste donnée. Le caractère générique `%` peut également être utilisé dans la liste.</br>
```
CQL2: ?filter=properties.STATION_NAME NOT IN ('lake', 'river')
```
[https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME NOT IN ('lake', 'river') &lang=fr](https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20NOT%20IN%20(%27lake%27,%20%27river%27)&lang=fr)
</br></br>

**2.3)** Pour filtrer <u>plusieurs mots</u>, vous avez besoin de deux prédicats `LIKE` différents. Dans ce cas, spécifier 'quinsam' `AND` 'river' permet de filtrer les noms de stations contenant **à la fois** les mots-clés 'quinsam' et 'river'. L'utilisation de `OR` renverrait le nom de la station contenant soit « quinsam », soit « river », soit les deux.
```
CQL2: ?filter=properties.STATION_NAME LIKE '%quisam%' AND properties.STATION_NAME LIKE '%river%'
```
[https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE '%quinsam%' AND properties.STATION_NAME LIKE '%river%' &lang=fr](https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20LIKE%20%27%quinsam%%27%20AND%20properties.STATION_NAME%20LIKE%20%27%river%%27&lang=fr)
</br></br>

**2.4)** Extraire le nom de la station commençant par la lettre `K`. Vous pouvez placer le caractère générique `%` selon vos besoins. Ici, vous constatez que ce n'est pas forcément le premier mot du nom de la station qui correspond. Le prédicat `LIKE` compare tous les mots-clés du texte.

```
CQL2: ?filter=properties.STATION_NAME LIKE 'k%'
```
[https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE 'k%' &lang=fr](https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME%20LIKE%20%27k%%27&lang=fr)
![CQL Wildcard debut](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Like_Wildcard_Debut_fr.png)
</br>

**2.5)** Extraire le nom de la station se terminant par la lettre `T`. Vous pouvez placer le caractère générique `%` selon les besoins. Ici, vous constatez que ce n’est pas nécessairement le dernier mot du nom de la station qui correspond. Le prédicat `LIKE` compare tous les mots clés du texte.
```
CQL2: ?filter=properties.STATION_NAME LIKE '%t'
```
[https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME LIKE '%t' &lang=fr](https://api.meteo.gc.ca/collections/climate-normals/items?filter=properties.STATION_NAME+LIKE+%27%25t%27&limit=10&offset=0&lang=fr)
![CQL Wildcard fin](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Like_Wildcard_Fin_fr.png)
</br>


**2.6)** Recherche de bulletins météorologiques par identifiant. Il n'est pas possible d'effectuer une recherche manuelle par `id` sur l'interface. Les utilisateurs peuvent utiliser des filtres CQL2 et s'appuyer sur la documentation de la [nomenclature des noms de fichiers des bulletins](https://eccc-msc.github.io/open-data/msc-data/bulletins/readme_bulletins-datamart_fr/#nomenclature-des-repertoires-et-noms-de-fichiers).</br>
```
CQL2 : ?filter=properties.identifier LIKE '%WWCN70%'
```
[https://api.meteo.gc.ca/collections/bulletins-realtime/items/?filter=properties.identifier LIKE '%wwcn70%' &lang=fr](https://api.meteo.gc.ca/collections/bulletins-realtime/items/?filter=properties.identifier%20LIKE%20%27%wwcn70%%27&lang=fr)
</br></br>

**2.7)** Recherche de bulletins avec un mot-clé partiel `CYOY` dans l'URL.
```
CQL2: ?filter=properties.type=SA AND properties.issuer_code=CWAO AND properties.url LIKE '%cyoy%'
```
[https://api.meteo.gc.ca/collections/bulletins-realtime/items?filter=properties.type=SA AND properties.issuer_code=CWAO AND properties.url LIKE '%cyoy%' &lang=fr](https://api.meteo.gc.ca/collections/bulletins-realtime/items?filter=properties.type=SA%20AND%20properties.issuer_code=CWAO%20AND%20properties.url%20LIKE%20%27%cyoy%%27&lang=fr) </br>

`?q=` correspond à la fonctionnalité de recherche en texte intégral de l'API OGC de MSC GeoMet. La requête équivalente est :

```html
https://api.meteo.gc.ca/collections/bulletins-realtime/items?type=SA&issuer_code=CWAO&q=*CYOY*
```
</br>

**2.8)** Recherche de bulletins par type et code d'émetteur.
```python
CQL2: ?filter=((properties.type=SA OR properties.type=SP) AND (properties.issuer_code=CWAO OR properties.issuer_code=CYOY))
```
[https://api.meteo.gc.ca/collections/bulletins-realtime/items/?filter=((properties.type=SA OR properties.type=SP) AND (properties.issuer_code=CWAO OR properties.issuer_code=CYOY)&lang=fr)](https://api.meteo.gc.ca/collections/bulletins-realtime/items/?filter=((properties.type=SA%20OR%20properties.type=SP)%20AND%20(properties.issuer_code=CWAO%20OR%20properties.issuer_code=CYOY))&lang=fr)
</br></br>

---------------------

##### <span class="badge badge-info">3. Recherche d'opérateurs de comparaison</span>

CQL2 prend en charge les comparaisons numériques à l'aide d'opérateurs.

**3.1)** Filtrer les valeurs de températures `TEMP` de moins de 10 °C.
```python
CQL2: ?filter=properties.TEMP< 10
```
[https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.TEMP < 10 &lang=fr](https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.TEMP%20%3C10&lang=fr)
</br></br>

**3.2)** Filtrer les prévisions de la cote air santé (CAS) classées à faible risque (1 à 3).
```python
CQL2: ?filter=properties.aqhi<=3
```
[https://api.meteo.gc.ca/collections/aqhi-forecasts-realtime/items?filter=properties.aqhi<=3 &lang=fr](https://api.meteo.gc.ca/collections/aqhi-forecasts-realtime/items?filter=properties.aqhi%3C=3&lang=fr)
</br></br>

**3.3)** Filtrer les observations CAS inférieures à 2 situées dans une zone géographique spécifiée (Nouvelle-Écosse).
```python
CQL2: ?bbox=-70,42,-60,45&filter=properties.aqhi<2
```
[https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?bbox=-70,42,-60,45&filter=properties.aqhi<2 &lang=fr](https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?bbox=-70,42,-60,45&filter=properties.aqhi%3C2&lang=fr)

![CQL Nouvelle-Ecosse CAS](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_NouvelleEcosse_CAS_fr.png)

---------------------

##### <span class="badge badge-info">4. Recherche avec opérateur logique</span>

CQL2 prend en charge le filtrage par plage grâce à l'opérateur `BETWEEN`. Cet opérateur inclut les deux valeurs limites. L'utilisation de `BETWEEN` est équivalente à `>=` et `<=`, mais améliore la lisibilité.
```
Syntaxe : [`NOT`] <attribute> BETWEEN <limite_inférieure> AND <limite_supérieure>
```

**4.1)** Filtrer les éléments selon la température `TEMP` comprise entre 10 °C et 12,5 °C. Pour les valeurs numériques (number), les guillemets ne sont pas nécessaires.
```python
CQL2: ?filter=properties.TEMP BETWEEN 10 AND 12.5
```
[https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.TEMP BETWEEN 10 AND 12.5 &lang=fr](https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.TEMP%20BETWEEN%2010%20AND%2015&lang=fr)
</br></br>

**4.2)** Filtrer les vents de direction nord-nord-est (NNE 23°) à nord-est (NE 45°) et de vitesse supérieure à 25 km/h.
```python
CQL2: ?filter=properties.WIND_DIRECTION BETWEEN 23 AND 45 AND properties.WIND_SPEED >= 25
```
[https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.WIND_DIRECTION BETWEEN 23 AND 45 AND properties.WIND_SPEED >= 25 &lang=fr](https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.WIND_DIRECTION%20BETWEEN%2023%20AND%2045%20AND%20properties.WIND_SPEED%20%3E=%2025&lang=fr)
</br></br>


**4.3)** Filtrer les éléments entre deux dates et heures. Les valeurs de date et d'heure doivent être placées entre guillemets simples, car elles sont définies comme `string` dans les interrogeables de la collection.
```
CQL2: ?filter=properties.LOCAL_DATE BETWEEN '2023-11-28 14:00:00' AND '2024-11-28 14:00:00'
```
[https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.LOCAL_DATE BETWEEN '2023-11-28 14:00:00' AND '2024-11-28 14:00:00' &lang=fr](https://api.meteo.gc.ca/collections/climate-hourly/items?limit=100&filter=properties.LOCAL_DATE+BETWEEN+%272023-11-28+14%3A00%3A00%27+AND+%272024-11-28+14%3A00%3A00%27&lang=fr)

![CQL Climat Horaire](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Schema_ClimatHoraire_fr.png)
</br>


**4.4)** Recherche des observations de la cote air santé présentant un risque modéré uniquement (`BETWEEN 4 AND 6`) dans une `BBOX`.
```
CQL2: ?filter=BBOX(geometry, -140, 50, -85, 63) AND properties.aqhi BETWEEN 4 AND 6
CQL2: ?filter=BBOX(geometry, -140, 50, -85, 63) AND properties.aqhi>=7 (risque élevé)
```
[https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?filter=BBOX(geometry, -140, 50, -85, 63) AND properties.aqhi BETWEEN 4 AND 6 &lang=fr](https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?filter=BBOX(geometry,%20-140,%2050,%20-85,%2063)%20AND%20properties.aqhi%20BETWEEN%204%20AND%206&lang=fr)
</br>

---------------------

##### <span class="badge badge-info">5. Recherches spatiales</span>

Les recherches spatiales permettent aux utilisateurs de personnaliser leurs requêtes en fonction de leur localisation géographique.

**5.1)** Trouver les entités qui intersectent un polygone. Renvoie toutes les entités qui touchent, traversent, se trouvent à l'intérieur ou chevauchent un polygone. Un polygone à `x` côtés possède nécessairement `x+1` points, car le dernier point est la répétition du premier pour fermer le polygone. Indiquez d'abord la longitude, puis la latitude. </br>
```python
CQL2: ?filter=INTERSECTS(geometry, POLYGON((lon_1 lat_1,lon_2 lat_2,lon_3 lat_3,lon_4 lat_4,lon_1 lat_1)))
CQL2: ?filter=INTERSECTS(geometry, POLYGON((-56 47,-55 47,-55 48,-56 48,-56 47)))
```
[https://api.meteo.gc.ca/collections/swob-stations/items?filter=INTERSECTS(geometry, POLYGON((-56 47,-55 47,-55 48,-56 48,-56 47)))&lang=fr](https://api.meteo.gc.ca/collections/swob-stations/items?filter=INTERSECTS(geometry,%20POLYGON((-56%2047,-55%2047,-55%2048,-56%2048,-56%2047)))&lang=fr) → Renvoie toutes les stations SWOB intersectant le polygone d'une largeur de 1 degré (longitude ouest-est) et d'une hauteur de 1 degré (latitude nord-sud).</br>
</br></br>

**5.2)** Recherche les entités avec `DISJOINT`. Renvoie toutes les entités situées à l'extérieur d'un polygone et qui n'intersectent pas la géométrie. C'est l'inverse de `INTERSECTS`.
```python
CQL2: ?filter=DISJOINT(geometry, POLYGON((lon_1 lat_1,lon_2 lat_2,lon_3 lat_3,lon_4 lat_4,lon_1 lat_1)))
CQL2: ?filter=DISJOINT(geometry, POLYGON((-80 42,-50 42,-50 60,-80 60,-80 42)))
```
[https://api.meteo.gc.ca/collections/swob-stations/items?filter=DISJOINT(geometry, POLYGON((-80 42,-50 42,-50 60,-80 60,-80 42)))&lang=fr](https://api.meteo.gc.ca/collections/swob-stations/items?filter=DISJOINT(geometry,%20POLYGON((-80%2042,-50%2042,-50%2060,-80%2060,-80%2042)))&lang=fr)
→ Renvoie toutes les stations SWOB qui **n'intersectent pas** le polygone de 30 degrés de longitude et 18 degrés de latitude dans l'est du Canada.</br>

![CQL SWOB Station](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_SWOB_Station_fr.png)

---------------------

##### <span class="badge badge-info">Exemples de filtrage multi-paramètres</span>


**6.1)** Filtrage des observations quotidiennes du climat pour une station météorologique de Lanaudière, durant les mois d'été chauds et humides, pour une station dont :</br>

* L'identifiant climatique est 7014160 (station de L'Assomption) ;</br>
* La température moyenne est comprise entre 18 °C et 28 °C ;</br>
* Les précipitations totales sont comprises entre 5 et 40 mm ;</br>
* L'année locale est comprise entre 2010 et 2020 ;</br>
* Le mois local est compris entre juin et septembre (JJAS).</br>
```
CQL2: ?filter=CLIMATE_IDENTIFIER = '7014160' AND properties.MEAN_TEMPERATURE BETWEEN 18 AND 28 AND properties.TOTAL_PRECIPITATION ENTRE 5 AND 40 AND properties.LOCAL_YEAR ENTRE 2010 AND 2020 AND properties.LOCAL_MONTH ENTRE 6 AND 9
```
[https://api.meteo.gc.ca/collections/climate-daily/items?filter=CLIMATE_IDENTIFIER = '7014160' AND properties.MEAN_TEMPERATURE BETWEEN 18 AND 28 AND properties.TOTAL_PRECIPITATION BETWEEN 5 AND 40 AND properties.LOCAL_YEAR BETWEEN 2010 AND 2020 AND properties.LOCAL_MONTH BETWEEN 6 AND 9 &lang=fr](https://api.meteo.gc.ca/collections/climate-daily/items?filter=properties.CLIMATE_IDENTIFIER=%277014160%27%20AND%20properties.MEAN_TEMPERATURE%20BETWEEN%2018%20AND%2028%20AND%20properties.TOTAL_PRECIPITATION%20BETWEEN%205%20AND%2040%20AND%20properties.LOCAL_YEAR%20BETWEEN%202010%20AND%202020%20AND%20properties.LOCAL_MONTH%20BETWEEN%206%20AND%209&lang=fr)

![CQL Station Assomption](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Items_StationAssomption_fr.png)
</br>


**6.2)** Trouvez toutes les observations de la cote air santé (CAS) à l'intérieur d'un polygone autour de Calgary pour aujourd'hui, où la valeur de la CAS est supérieure à 4 (risque modéré).
```python
CQL2: ?filter=INTERSECTS(geometry,POLYGON((-114.2 50.9, -113.8 50.9, -113.8 51.2, -114.2 51.2, -114.2 50.9))) AND properties.aqhi>4
```
[https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?filter=INTERSECTS(geometry,POLYGON((-114.2 50.9, -113.8 50.9, -113.8 51.2, -114.2 51.2, -114.2 50.9))) AND properties.aqhi>4 &lang=fr](https://api.meteo.gc.ca/collections/aqhi-observations-realtime/items?filter=INTERSECTS(geometry,POLYGON((-114.2%2050.9,%20-113.8%2050.9,%20-113.8%2051.2,%20-114.2%2051.2,%20-114.2%2050.9)))%20AND%20properties.aqhi%3E4%20&lang=fr)

![CQL Intersects Calgary](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_Intersects_Calgary_fr.png)
</br>

**6.3)** Récupérer les stations météorologiques répondant à toutes les conditions suivantes :</br>

* Situées à l’intérieur d’un polygone spécifié (région de l’Ouest canadien) avec `INTERSECTS`;</br>
* Possède une station contenant le mot-clé « LAKE » avec `LIKE`;</br>
* Enregistrer une température minimale comprise entre -20 et -10 °C;</br>
* Enregistrer des rafales de vitesse maximale supérieures à 20 km/h.</br>
```python
CQL2: ?filter=INTERSECTS(geometry,POLYGON((-140 48,-95 48,-95 60,-140 60,-140 48))) AND properties.STATION_NAME LIKE '%lake%' AND properties.MIN_TEMPERATURE BETWEEN -20 AND -10 AND properties.SPEED_MAX_GUST >= 20
```
[https://api.meteo.gc.ca/collections/climate-daily/items?filter=INTERSECTS(geometry,POLYGON((-140 48,-95 48,-95 60,-140 60,-140 48))) AND properties.STATION_NAME LIKE '%lake%' AND properties.MIN_TEMPERATURE BETWEEN -20 AND -10 AND properties.SPEED_MAX_GUST >= 20 &lang=fr](https://api.meteo.gc.ca/collections/climate-daily/items?filter=INTERSECTS(geometry,POLYGON((-140%2048,-95%2048,-95%2060,-140%2060,-140%2048)))%20AND%20properties.STATION_NAME%20LIKE%20%27%lake%%27%20AND%20properties.MIN_TEMPERATURE%20BETWEEN%20-20%20AND%20-10%20AND%20properties.SPEED_MAX_GUST%20%3E=%2020&lang=fr)
 </br></br>


**6.4a)** Identifier les régions à risque élevé d'incendies de forêt (conditions sèches, chaudes et venteuses) pour la saison des feux de forêt de 2025.</br>

* Durant la saison des feux de forêt de 2025 (avril à octobre) :</br>
* Températures élevées (`>=` 30°C) ;</br>
* Faible humidité relative (`<=` 30%) ;</br>
* Vents forts (vitesse `>=` 30 km/h).</br>
```python
Climat - Observations horaires
CQL2: ?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_HOUR=12 AND properties.LOCAL_MONTH BETWEEN 4 AND 10 AND properties.TEMP >=30 AND properties.RELATIVE_HUMIDITY <=30 AND properties.WIND_SPEED >= 30
```
[https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_HOUR=12 AND properties.LOCAL_MONTH BETWEEN 5 AND 8 AND properties.TEMP >=30 AND properties.RELATIVE_HUMIDITY <=30 AND properties.WIND_SPEED >= 30 &lang=fr](https://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.LOCAL_YEAR=2025%20AND%20properties.LOCAL_HOUR=12%20AND%20properties.LOCAL_MONTH%20BETWEEN%205%20AND%208%20AND%20properties.TEMP%20%3E=30%20AND%20properties.RELATIVE_HUMIDITY%20%3C=30%20AND%20properties.WIND_SPEED%20%3E=%2030%20&lang=fr)
</br></br>


**6.4b)** En utilisant les mêmes conditions que pour les observations horaires, nous ajoutons maintenant la quantité totale de précipitations sur 24 heures (issue de `Climat - Observations quotidiennes`) pour tenir compte de la sécheresse. Les précipitations totales sur 24 heures sont inférieures à une valeur arbitraire de 3 mm.
```python
Climat - Observations quotidiennes
CQL2: ?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_MONTH BETWEEN 4 AND 10 AND properties.MAX_TEMPERATURE>=30 AND properties.MIN_REL_HUMIDITY<=30 AND properties.SPEED_MAX_GUST>30 AND properties.TOTAL_PRECIPITATION<=3
```
[https://api.meteo.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_YEAR=2025 AND properties.LOCAL_MONTH BETWEEN 5 AND 8 AND properties.MAX_TEMPERATURE>=30 AND properties.MIN_REL_HUMIDITY<=30 AND properties.SPEED_MAX_GUST>30 AND properties.TOTAL_PRECIPITATION<=3 &lang=fr](https://api.meteo.gc.ca/collections/climate-daily/items?filter=properties.LOCAL_YEAR=2025%20AND%20properties.LOCAL_MONTH%20BETWEEN%205%20AND%208%20AND%20properties.MAX_TEMPERATURE%3E=30%20AND%20properties.MIN_REL_HUMIDITY%3C=30%20AND%20properties.SPEED_MAX_GUST%3E30%20AND%20properties.TOTAL_PRECIPITATION%3C=3%20&lang=fr)

![CQL URL Feu Foret](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_URL_FeuDeForet_fr.png)
![CQL Feu Foret](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-geomet/cql/CQL_FeuDeForet_fr.png)

---------------------
##### <span class="badge badge-info">Commande Curl et Python</span>


Il a été démontré qu'il est possible d'effectuer une requête HTTP avec des filtres CQL2 directement dans la barre de recherche du moteur de recherche. Il est également possible de récupérer les données via la commande `curl` dans le terminal. Pour enregistrer le résultat de la requête, utilisez l'option `-o`.

* Utilisation de curl avec l'URL complète encodée.

```
curl [url_encodée] [option]
curl hhttps://api.meteo.gc.ca/collections/climate-hourly/items?filter=properties.WIND_DIRECTION%20BETWEEN%2023%20AND%2045%20AND%20properties.WIND_SPEED%20%3E=%2025%20&lang=fr -o /chemin/vers/fichier_de_sortie.json
```
* Encodage direct de l'URL avec les options de requête GET `--data-urlencode` et `-G`. Il est possible d'ajouter plusieurs paramètres `--data-urlencode` (équivalent à `&`).

```javascript
curl -G [basepath] --data-urlencode [CQL2 EXPRESSION]
curl -G "https://api.meteo.gc.ca/collections/climate-hourly/items?" --data-urlencode "filter=properties.WIND_DIRECTION BETWEEN 23 AND 45 AND properties.WIND_SPEED >=25" --data-urlencode "lang=fr"
```

**Requêtes avec Python** <br>
Pour interpréter les filtres CQL2 et effectuer des requêtes HTTP, installez les modules Python `pygeofilter` et `requests`.

```bash
pip3 install pygeofilter requests
```
```python
import requests
import json
from pygeofilter.parsers.ecql import parse

# Point de terminaison de l'API GeoMet-OGC.
api_url = "https://api.meteo.gc.ca/collections/climate-daily/items"

# Filtres CQL2.
cql_filter = (
    "properties.LOCAL_YEAR = 2025 AND "
    "properties.LOCAL_MONTH BETWEEN 6 AND 9 AND "
    "properties.MAX_TEMPERATURE >= 30"

)
# Valider les filtres CQL2 avant la requête API.
try:
    parse(cql_filter)
except Exception as e:
    raise ValueError(f"Filtre CQL2 invalide : {e}")

params = {
    "filter": cql_filter,
    "lang": "fr",
    "limit": 100
}
# Envoie une requête GET à l'API et encode l'URL.
response = requests.get(api_url, params=params)
print(f"L'URL encodée est : {response.url}")

# Formate le JSON dans le fichier de sortie.
data = response.json()
climate_output_file = "climat_joursAuDessusDe30deg_JJAS_2025.json"
with open(climate_output_file, "w") as fh:
    json.dump(data, fh)
```