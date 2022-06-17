[In English](web-services_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [GeoMet du SMC](readme_fr.md) > Documentation technique

# Table des matières
- [Web Map Service (WMS)](#web-map-service-wms)
    * [WMS GetCapabilities](#wms-getcapabilities)
    * [WMS GetMap](#wms-getmap)
    * [WMS GetFeatureInfo](#wms-getfeatureinfo)
    * [WMS GetLegendGraphic](#wms-getlegendgraphic)
    * [Spécification du temps](#specification-du-temps)
    * [Spécification des styles](#specification-des-styles)
- [Web Coverage Service (WCS)](#web-coverage-service-wcs)
    * [WCS GetCapabilities](#wcs-getcapabilities)
    * [WCS DescribeCoverage](#wcs-describecoverage)
    * [WCS GetCoverage](#wcs-getcoverage)
    * [Spécification du temps](#wcs-specification-du-temps)
    * [Exemple d'utilisation](#exemple-dutilisation)
- [OGC API - Features (WFS 3)](#ogc-api-features)

# Services web géospatiaux

Les services web sont des protocoles élaborés pour supporter des interactions machine-à-machine sur un réseau et sont typiquement utilisés via un accès programmatique et les outils et applications associées dans un environnement informatique de type client/serveur.

Les services web GeoMet du SMC implémentent les standards ouverts ratifiés par [l'Open Geospatial Consortium (OGC)](https://www.opengeospatial.org/) et [l'International Organization for Standardization (ISO)](https://www.isotc211.org/) qui rendent possible l'interopérabilité et ainsi simplifient la découverte, l'accès, la visualisation et l'intégration de données. Les standards de l'OGC et ISO jouent un rôle important pour [l'interopérabilité au sein de l'Organisation étéorologique mondiale (OMM)](https://www.wmo.int/pages/prog/www/WIS/documents/MOAWMO_OGC.pdf) et le [WMO Information System](https://www.wmo.int/pages/prog/www/WIS/). Ces standards sont supportés par de nombreux logiciels libres et logiciels commerciaux.

Les services web de l'OGC suivant sont supportés par GeoMet du SMC :

* Web Map Service (WMS)
* Web Coverage Service (WCS)
* OGC API - Features (OAFeat)
* OGC API - Coverages (OACov)


## Web Map Service (WMS)

Les requêtes effectuées avec le [standard Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms) de l'OGC permettent principalement aux usagers to récupérer des données géospatiales en tant que cartes. Les requêtes WMS sont effectuées via Internet (HTTP) et servent principalement à récupérer une image (e.g. JPEG, PNG) issue de données géospatiales pour une région d'intérêt donnée.

Plusieurs types de requêtes WMS peuvent être spécifiés et celles-ci sont décrites ci-après.

### WMS GetCapabilities

Une requête WMS GetCapabilities permet à l'usager de récupérer un document XML contenant les métadonnées décrivant le service. Ce document contient l'information associée aux types de requêtes supportées, les systèmes de coordonnées cartographiques supportés, et particulièrement important, la liste des couches (données) disponibles.

Une requête WMS GetCapabilities est composée des paramètres suivants :



| Paramètres obligatoires | Définition |
| ------------------------- | ---------- |
| SERVICE         | Le service que l'utilisateur sollicite. Dans ce cas, `wms`|
| VERSION         | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version la plus récente, soit `1.3.0`|
| REQUEST         | Le type de requête, soit `GetCapabilities`|

| Paramètres optionnels | Définition |
| ------------------------- | ---------- |
| LAYER         | Un paramètre externe (vendor extension) permettant aux usagers de filter le document GetCapabilities pour une couche spécifique. Ceci réduit significativement la grosseur du document XML résultant|
| LANG          | Un paramètre externe (vendor extension) permettant aux usagers de choisir d'afficher en français(fr) ou en anglais(en) le document GetCapabilities. Si le paramètre n'est pas spécifié, le document GetCapabilities est retourné en anglais par défaut|

Une requête WMS GetCapabilities pour GeoMet-Météo est donc construite ainsi :

[https://geo.meteo.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr](https://geo.meteo.gc.ca/geomet/?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities)

Chaque couche définie dans le document XML du WMS GetCapabilities contient l'information telle que l'identifiant de la couche et son nom, son étendue géographique, la plage temporelle ainsi que les styles disponibles.

### WMS GetMap

Une requête WMS GetMap permet aux usagers de récupérer une image (e.g. JPEG, PNG) d'une couche pour une région déterminée. Une requête WMS GetMap est constituée de plusieurs paramètres qui spécifie la couche désirée, son style, le système de coordonnées cartographiques, le pas de temps, en plus des propriétés additionnelles associées à l'image. Une [requête WMS GetCapabilities](#getcapabilities) supporte les usagers en guidant l'utilisateur sur les valeurs possibles pour ces paramètres.


| Paramètres obligatoires | Définition |
| ------------------------- | ---------- |
| SERVICE         | Le service que l'utilisateur sollicite. Dans ce cas présent, `wms`|
| VERSION         | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version la plus récente, soit `1.3.0`|
| REQUEST         | Le type de requête, soit `GetMap`|
| LAYERS          | L'identifiant des couches à être affichées sur l'image. L'identifiant des couches est spécifié dans le résultat d'une requête [WMS GetCapabilities](#wms-getcapabilities). GeoMet du SMC supporte présentement seulement une seule valeur pour le paramètre GetMap LAYERS. Ceci sera amélioré dans une version à venir afin de supporter les couches multiples du standard WMS 1.3.0.|
| STYLES          | Le style à utiliser pour l'affichage de la couche. Si ce paramètre n'est pas spécifié, le style par défaut de la couche sera utilisé. 
| CRS (version 1.3.0) ou SRS (version 1.1.0) | Le système de coordonnées cartographiques (CRS) à utiliser pour créer l'image. **Attention, le nom de ce paramètre diffère selon la version du service WMS utilisé**|
| BBOX            | L'étendue géographique associée à l'image désirée. Les coordonnées doivent utiliser les unités du CRS/SRS. Si la requête est effectuée en WMS 1.3.0 *et avec la projection EPSG:4326*, l'ordre des coordonnées est `minY,minX,maxY,maxX`. En WMS 1.3.0, l'ordre des axes dépend de la projection. Si la requête est effectuée en WMS 1.1.1, l'ordre des coordonnées est `minX,minY,maxX,maxY`|
| FORMAT          | Le format de données pour l'image désirée. Les valeurs possibles pour ce paramètre sont : `image/jpeg` ou `image/png`. Le format PNG supporte la transparence, alors que le format JPEG est plus léger|
| HEIGHT          | La hauteur en pixels de l'image retournée|
| WIDTH           | La largeur en pixels de l'image retournée|

| Paramètres optionnels | Définition |
| ------------------------- | ---------- |
| TIME            | La date et l'heure associées à l'image désirée. Le format doit respecter le standard ISO8601. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WMS](#spécification-du-temps)|
| DIM_REFERENCE_TIME  | Le temps de la passe du modèle (model run) à utiliser pour l'image désirée. Pour davantage d'information, vous référer à section sur [la spécification du temps dans les requêtes WMS](#spécification-du-temps)|

La requête WMS GetMap suivante demande une image de la couche de température de l'air du Système global de prévision déterministe (SGPD) :

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```

Et retourne :

![Température de l'air du Système global de prévision déterministe (SGPD)](https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png) 

### WMS GetFeatureInfo

Une requête WMS GetFeatureInfo permet de récupérer les données brutes pour un lieu géographique spécifique. Une requête WMS GetFeatureInfo ressemble à une requête WMS GetMap à laquelle s'ajoute les paramètres suivants : `I`, `J` et `QUERY_LAYERS`. Ces paramètres représentent la localisation horizontale et verticale du pixel ainsi que le nom des couches à interroger.


| Paramètres obligatoires | Définition |
| ------------------------- | ---------- |
| SERVICE         | Le service que l'utilisateur sollicite. Dans ce cas, `wms`|
| VERSION         | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version la plus récente, soit `1.3.0`|
| REQUEST         | Le type de requête, soit `GetFeatureInfo`|
| LAYERS          | L'identifiant de la couche à interroger. L'identifiant de la couche est spécifié dans le résultat d'une requête [WMS GetCapabilities](#wms-getcapabilities)|
| CRS (version 1.3.0) ou SRS (WMS version 1.1.0) | Le système de coordonnées cartographiques (CRS) à utiliser pour la requête. **Attention, le nom de ce paramètre diffère selon la version du service WMS utilisé** |
| BBOX            | L'étendue géographique associée à l'image désirée. Les coordonnées doivent utiliser les unités du CRS/SRS. Si la requête est effectuée en WMS 1.3.0 *et avec la projection EPSG:4326*, l'ordre des coordonnées est `minY,minX,maxY,maxX`. En WMS 1.3.0, l'ordre des axes dépend de la projection. Si la requête est effectuée en WMS 1.1.1, l'ordre des coordonnées est `minX,minY,maxX,maxY`|
| FORMAT          | Le format de données pour l'image désirée. Les valeurs possibles pour ce paramètre sont : `image/jpeg` ou `image/png`. Le format PNG supporte la transparence, alors que le format JPEG est plus léger|
| HEIGHT          | La hauteur en pixels de l'image associée|
| WIDTH           | La largeur en pixels de l'image associée|
| I (WMS version 1.3.0) ou X (WMS version 1.1.0) | La coordonnée horizontale du pixel à interroger|
| J (WMS version 1.3.0) ou Y (WMS version 1.1.0)  | La coordonnée verticale du pixel à interroger|
| QUERY_LAYERS    | L'identifiant de la couche à interroger|

| Paramètres optionnels      | Définition |
| ------------------------- | ---------- |
| INFO_FORMAT     | Le format des données retournées par la requête. Les valeurs acceptées pour ce paramètres sont : `text/plain` (valeur par défaut), `application/json` ou `application/vnd.ogc.gml`|
| FEATURE_COUNT   | Le nombre d'entités retourné par la requête|
| TIME            | La date et l'heure associées à la requête. Le format doit respecter le standard ISO8601. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WMS](#spécification-du-temps)|
| DIM_REFERENCE_TIME  | Le temps de la passe du modèle (model run) à utiliser pour la requête. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WMS](#spécification-du-temps)|

Une requête GetFeatureInfo pour la même image que l'exemple WMS GetMap ci-dessus :

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&BBOX=45,-75,45.5,-74.5
&CRS=EPSG:4326&WIDTH=10&HEIGHT=10&LAYERS=GDPS.ETA_TT&INFO_FORMAT=application/json&QUERY_LAYERS=GDPS.ETA_TT&I=5&J=5
```

### WMS GetLegendGraphic

Une requête GetLegendGraphic retourne une image de la légende d'une couche pour le style demandé. La manière simple d'accéder à la légende d'un style spécifique est de consulter le document WMS GetCapabilities pour la couche en question. Tous les styles d'une couche s'y retrouvent et l'URL de la légende se retrouve dans la balise `<OnlineResource>`.

Par exemple, la couche de température de l'air du SGPD offre plusieurs styles dans le document WMS GetCapabilities. Demander la légende du style `TEMPERATURE-LINEAR` en utilisant une requête GetLegendGraphic retourne cette légende :

![Exemple GetLegendeGraphic TEMPERATURE-LINEAR](https://geo.meteo.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS.ETA_TT&format=image/png&STYLE=TEMPERATURE-LINEAR)



| Paramètres obligatoires | Définition |
| ------------------------- | ---------- |
| SERVICE         | Le service que l'utilisateur sollicite. Dans ce cas, `wms`|
| VERSION         | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version la plus récente, soit `1.3.0`|
| REQUEST         | Le type de requête, soit `GetLegendGraphic`|
| LAYER           | L'identifiant de la couche à interroger. L'identifiant des couches est spécifié dans le résultat d'une requête [WMS GetCapabilities](#wms-getcapabilities)|
| FORMAT          | Le format de données pour la légende désirée. Les valeurs possibles pour ce paramètre sont : `image/jpeg` ou `image/png`|
| SLD_VERSION     | La version du document SLD. Nous recommendons d'utiliser la version `1.1.0`|

| Paramètres optionnels  | Définition |
| ------------------------- | ---------- |
| STYLE           | Le style associé à la légende désirée. Si ce paramètre n'est pas spécifié, le style par défaut de la couche sera utilisé. Les styles disponibles pour une couche est spécifié dans le résultat d'une requête [WMS GetCapabilities](#wms-getcapabilities). Note: Assurez-vous de taper la forme au singulier de ce paramètre dans la requête `GetLegendGraphic` et non la forme au pluriel (i.e. `STYLES`) car la sortie sera le style par défaut de la couche au lieu de celui demandé. |
| SLD             | Indique que la légende doit être créée selon un document SLD externe. Vous référer à la section [Spécification des styles](#spécification-des-styles) pour les explications détaillées|
| SLD_BODY        | Permet à l'usager d'inclure le document SLD directement dans la requête| Note: la valeur de LAYER dans la requête WMS GetMap et la valeur de se:Name (ou se%3AName lorsqu'il est encodé) dans SLD_BODY doivent être différentes pour que la requête fonctionne correctement.
| LANG          | Un paramètre externe (vendor extension) permettant aux usagers de choisir d'afficher en français(fr) ou en anglais(en) le légende. Si le paramètre n'est pas spécifié, la légende est retournée en anglais par défaut|

Un exemple de requête GetLegendGraphic pour la couche de vent (GDWPS.UU.1h) du Système Global de Prévision Déterministe de Vague (SGPDV) va comme suit :

```
https://geo.meteo.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0
&layer=GDWPS.UU.1h&format=image/png&STYLE=WINDARROW
```

Et retourne :

![Exemple des flèches de vent du SGPDV](https://geo.meteo.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDWPS.UU.1h&format=image/png&STYLE=WINDARROW)


### Spécification du temps

Compte tenu de l'importance des dimensions temporelles des données météorologiques, il est important de connaître comment GeoMet du SMC traite les paramètres temporels dans les requêtes. Par défaut, si aucun paramètre `TIME` ou `DIM_REFERENCE_TIME` n'est spécifié dans une requête, GeoMet du SMC va utiliser le pas de temps ainsi que la passe de modèle les plus proches.

Un utilisateur désirant effectuer une requête pour un moment spécifique pour les requêtes WMS GetMap et WMS GetFeatureInfo doit utiliser les paramètres `TIME` et/ou `DIM_REFERENCE_TIME`. La date et le moment doit être envoyé dans le format du standard ISO8601 et les temps sont toujours en UTC (Coordinate Universal Time).

Afin de générer une requête pour un pas de temps spécifique ou une passe de modèle, l'utilisateur doit premièrement valider quels sont les intervalles de temps valides. Cette information est disponible dans la balise `<Dimension>` disponible dans le document WMS GetCapabilities.

Par exemple, les dimensions temporelles pour la couche de température de l'air (GDPS.ETA_TT) du Système global de prévision déterministe (SGPD) ressemble à :

```xml
<Dimension name="time" units="ISO8601" default="2019-06-12T15:00:00Z" 
nearestValue="0">2019-06-12T00:00:00Z/2019-06-22T00:00:00Z/PT3H</Dimension>

<Dimension name="reference_time" units="ISO8601" default="2019-06-12T00:00:00Z" 
multipleValues="1" nearestValue="0">2019-06-11T00:00:00Z/2019-06-12T00:00:00Z/PT12H</Dimension>
```

La première balise `<Dimension>` représente l'intervalle de temps disponible pour cette couche. La valeur associée à `default` indique la valeur considérée si le paramètre `TIME` n'est pas spécifié dans la requête. La valeur de la balise, soit `2019-06-12T00:00:00Z/2019-06-22T00:00:00Z/PT3H` dans l'exemple, indique à l'usager quelles sont les valeurs temporelles valides. Au moment où la requête WMS GetCapabilities a fourni cette réponse, les usagers étaient en mesure de récupérer des cartes (WMS GetMap) ou la donnée brute à un point (WMS GetFeatureInfo) pour n'importe quel moment entre 2019-06-12T00:00:00Z et 2019-06-22T00:00:00Z à un intervalle de 3 heures (PT3H).

La seconde balise `<Dimension>` représente les passes de modèles (model runs) disponibles pour la couche. La valeur indiqué à `default` est celle de la passe de modèle disponible la plus récente. La valeur de la balise, soit `2019-06-11T00:00:00Z/2019-06-12T00:00:00Z/PT12H` dans cet exemple indique les passes de `2019-06-11T00:00:00Z` à `2019-06-12T00:00:00Z` à tous les 12 heures (PT12H) sont valides.

Avec cette information, un usager est en mesure d'effectuer une requête WMS GetMap pour la température de l'air du SGPD pour 12:00:00 UTC le 21 juin 2019 pour la passe de modèle la plus récente 2019-06-12T00:00:00Z. La requête serait celle-ci :

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
&TIME=2019-06-21T12:00:00Z&DIM_REFERENCE_TIME=2019-06-12T00:00:00Z
```

Notez que les requêtes avec des plages de temps ou des valeurs temporelles multiples ne sont pas actuellement prises en charge dans GeoMet pour les paramètres `TIME` ou `DIM_REFERENCE_TIME`. Seules les requêtes de temps ponctuelles sont supportées.

#### Différences entre les dimensions temporelles de GeoMet-Météo et GeoMet-Climat

Il est important de considérer les différences dans la spécification du temps entre GeoMet-Météo et GeoMet-Climat, différences issues de la nature différente des données en cause.

Dans GeoMet-Climat, les intervalles temporels sont soit annuels (YYYY) ou mensuels (YYYY-MM) selon la couche interrogée. Une requête WMS GetCapabilities sur les services GeoMet-Climat indique aux usagers quelles sont les dimensions temporelles disponibles pour un couche spécifique.

Par exemple, la balise `<Dimension>` de la couche [Ensembles mensuels CMIP5 pour la vitesse du vent près de la surface (5e percentile)](https://geo.meteo.gc.ca/geomet-climate?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&Layer=CMIP5.SFCWIND.RCP26.ENS.ABS_PCTL5) indique :

```xml
<Dimension name="time" units="ISO8601" default="2100-12" nearestValue="0">2006-01/2100-12/P1M</Dimension>
```

Un requête WMS GetMap valide avec le paramètre `TIME` doit ainsi utiliser une valeur entre `2006-01` et `2100-12`.


### Spécification des styles

La représentation graphique de l'information et des données peut avoir un impact significatif sur la manière que les données sont interprétées par les usagers. GeoMet du SMC offre fréquemment plusieurs représentations graphiques possibles pour une même couche. L'usager doit identifier le style à utiliser qui est le plus approprié pour le cas d'utilisation.

L'utilisateur utilise le paramètre `STYLE` dans les requêtes WMS GetMap et WMS GetFeatureInfo afin de spécifier la représentation graphique désirée. Les styles disponibles pour une couche sont énumérés dans le document WMS GetCapabilities.

Voici deux exemples de requêtes WMS GetMap pour la couche de quantité de précipitation (RDPA.24F_PR) de l'Analyse régional déterministe de précipitation (ARDP) avec des paramètres `STYLE` différents.

Couche RDPA.24F_PR avec le style CAPA24-LINEAR :

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR
&STYLES=CAPA24-LINEAR&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png
```

![Couche RDPA.24F_PR avec le style CAPA24-LINEAR](https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR&STYLES=CAPA24-LINEAR&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png)

Couche RDPA.24F_PR avec le style RDPA-WXO :

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR
&STYLES=RDPA-WXO&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png
```

![Couche RDPA.24F_PR avec le style RDPA-WXO](https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=RDPA.24F_PR&STYLES=RDPA-WXO&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=600&HEIGHT=400&FORMAT=image/png)

Les utilisateurs peuvent également spécifier leurs propres styles en fournissant par le biais du standard [OGC Styled Layer Descriptor (SLD)](https://www.opengeospatial.org/standards/sld), soit en pointant vers un document SLD externe avec le paramètre `SLD` soit en spécifiant le contenu SLD directement dans le paramètre `SLD_BODY`. Notez que le contenu de `SLD_BODY` doit être entièrement encodé tel un URL HTTP. Aussi, pour `SLD_BODY`, la valeur du paramètre LAYER dans la requête WMS GetMap et la valeur de se:Name (ou se%3AName lorsqu'il est encodé) dans `SLD_BODY` doivent être différentes pour que la requête fonctionne correctement.

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=GDPS.ETA_NT
&STYLES=&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=1800&HEIGHT=1200&FORMAT=image/png
&SLD_BODY=%22%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%20%3C
StyledLayerDescriptor%20version%3D%221.0.0%22%20xmlns%3D%22http%3A%2F%2Fwww.opengis.net
%2Fsld%22%20xmlns%3Aogc%3D%22http%3A%2F%2Fwww.opengis.net%2Fogc%22%20xmlns%3Axlink%3D%22
http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F
2001%2FXMLSchema-instance%22%20xsi%3AschemaLocation%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld
%20http%3A%2F%2Fschemas.opengis.net%2Fsld%2F1.0.0%2FStyledLayerDescriptor.xsd%22%3E%20%3C
NamedLayer%3E%20%3Cse%3AName%3EGDPS.ETA_NT%3C%2Fse%3AName%3E%20%3CUserStyle%3E%20%3CTitle
%3ETEST%3C%2FTitle%3E%20%3Cse%3AFeatureTypeStyle%3E%20%3Cse%3ARule%3E%20%3Cse%3A
RasterSymbolizer%3E%20%3Cse%3AOpacity%3E1.0%3C%2Fse%3AOpacity%3E%20%3CColorMap%3E%20%3C
ColorMapEntry%20color%3D%22%238cff66%22%20quantity%3D%220%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%23ffff00%22%20quantity%3D%2225%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%23b38600%22%20quantity%3D%2250%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%23cc0000%22%20quantity%3D%2275%22%2F%3E%20%3C
ColorMapEntry%20color%3D%22%234d0000%22%20quantity%3D%22100%22%2F%3E%20%3C%2FColorMap%3E
%20%3C%2Fse%3ARasterSymbolizer%3E%20%3C%2Fse%3ARule%3E%20%3C%2Fse%3AFeatureTypeStyle%3E
%20%3C%2FUserStyle%3E%20%3C%2FNamedLayer%3E%20%3C%2FStyledLayerDescriptor%3E%0A
```

![Couche du SGPD avec un style SLD provenant de l'usager](https://geo.weather.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=GDPS.ETA_NT&STYLES=&CRS=EPSG:4326&BBOX=35,-150,85,-45&WIDTH=1800&HEIGHT=1200&FORMAT=image/png&SLD_BODY=%22%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%20%3CStyledLayerDescriptor%20version%3D%221.0.0%22%20xmlns%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld%22%20xmlns%3Aogc%3D%22http%3A%2F%2Fwww.opengis.net%2Fogc%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema-instance%22%20xsi%3AschemaLocation%3D%22http%3A%2F%2Fwww.opengis.net%2Fsld%20http%3A%2F%2Fschemas.opengis.net%2Fsld%2F1.0.0%2FStyledLayerDescriptor.xsd%22%3E%20%3CNamedLayer%3E%20%3Cse%3AName%3EGDPS.ETA_NT%3C%2Fse%3AName%3E%20%3CUserStyle%3E%20%3CTitle%3ETEST%3C%2FTitle%3E%20%3Cse%3AFeatureTypeStyle%3E%20%3Cse%3ARule%3E%20%3Cse%3ARasterSymbolizer%3E%20%3Cse%3AOpacity%3E1.0%3C%2Fse%3AOpacity%3E%20%3CColorMap%3E%20%3CColorMapEntry%20color%3D%22%238cff66%22%20quantity%3D%220%22%2F%3E%20%3CColorMapEntry%20color%3D%22%23ffff00%22%20quantity%3D%2225%22%2F%3E%20%3CColorMapEntry%20color%3D%22%23b38600%22%20quantity%3D%2250%22%2F%3E%20%3CColorMapEntry%20color%3D%22%23cc0000%22%20quantity%3D%2275%22%2F%3E%20%3CColorMapEntry%20color%3D%22%234d0000%22%20quantity%3D%22100%22%2F%3E%20%3C%2FColorMap%3E%20%3C%2Fse%3ARasterSymbolizer%3E%20%3C%2Fse%3ARule%3E%20%3C%2Fse%3AFeatureTypeStyle%3E%20%3C%2FUserStyle%3E%20%3C%2FNamedLayer%3E%20%3C%2FStyledLayerDescriptor%3E%0A)


## Web Coverage Service (WCS)

Les requêtes de type [OGC Web Coverage Service](https://www.opengeospatial.org/standards/wcs) permettent aux usagers de télécharger les données géospatiales brutes pour une région d'intérêt spécifique. Les requêtes WCS sont effectuée via l'Internet et offrent davantage de flexibilité lorsque comparées au téléchargement de fichiers bruts. Le service WCS rend possible plusieurs types de requêtes, qui sont décrites en détail ci-dessous.


Notez que seule la version WCS 2.0.1 est présentement supportée par les services web GeoMet du SMC. Nous invitons les usagers à utiliser cette version du standard. Il est aussi à noter que QGIS et ArcGIS ne supportent pas le WCS 2.0.1.

 
### WCS GetCapabilities

Une requête WCS GetCapabilities permet à l'usager de récupérer un document XML contenant les métadonnées décrivant le service. Ce document contient l'information sur le type de requêtes et les systèmes de coordonnées cartographiques supportées, ainsi que les couches pour lesquelles les données brutes sont disponibles.

Une requête WCS GetCapabilities est composée des paramètres suivants :

| Paramètres obligatoires   | Définition |
| ------------------------- | ---------- |
| SERVICE      | Le service que l'utilisateur sollicite. Dans ce cas, `wcs`|
| VERSION      | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version supportée, soit `2.0.1`|
| REQUEST      | Le type de requête, soit `GetCapabilities`|

| Paramètre optionnel | Définition |
| ------------------------- | ---------- |
| COVERAGEID                | Un paramètre externe (vendor extension) permettant aux usagers de filter le document GetCapabilities pour une couche spécifique. Ceci réduit significativement la grosseur du document XML résultant|
| LANG          | Un paramètre externe (vendor extension) permettant aux usagers de choisir d'afficher en français(fr) ou en anglais(en) le document GetCapabilities. Si le paramètre n'est pas spécifié, le document GetCapabilities est retourné en anglais par défaut|

Une requête WCS GetCapabilities peut ainsi être construite de cette manière :

[https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities](https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCapabilities)

Le document GetCapabilities résultant contiendra l'information sur le nom du service, l'étendue géographique des données, les couches et les formats disponibles.

### WCS DescribeCoverage

Une requête WCS DescribeCoverage permet à l'usager de récupérer davantage d'information qu'un WCS GetCapabilities pour une couche en particulier. L'information provenant d'une requête WCS DescribeCoverage inclut l'étendue géographique des données, les couches et les formats disponibles.

| Paramètres obligatoires   | Définition |
| ------------------------- | ---------- |
| SERVICE      | Le service que l'utilisateur sollicite. Dans ce cas, `wcs`|
| VERSION      | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version supportée, soit `2.0.1`|
| REQUEST      | Le type de requête, soit `DescribeCoverage`|
| COVERAGEID   | Un paramètre permettant aux usagers de spécifier la couche désirée. La liste des couches disponibles est récupérée par le biais d'une requête  [WCS GetCapabilities](#wcsgetcap)|

Une requête WCS DescribeCoverage pour la couche GDPS.ETA_TT de GeoMet-Météo est construite comme suit :

[https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT](https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT)

### WCS GetCoverage

Une requête WCS GetCoverage est utilisée afin de récupérer les données brutes d'une couche en particulier. L'aspect pratique de ces requêtes est qu'elles permette de récupérer un sous-domaine spatial dans la projection cartographique spécifiée ainsi que de récupérer les données dans un format de données et une résolution spatiale différente que les données d'origine.

| Paramètres obligatoires   | Définition |
| ------------------------- | ---------- |
| SERVICE      | Le service que l'utilisateur sollicite. Dans ce cas, `wcs`|
| VERSION      | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version supportée, soit `2.0.1`|
| REQUEST      | Le type de requête, soit `GetCoverage`|
| COVERAGEID   | Un paramètre permettant aux usagers de spécifier la couche désirée. La liste des couches disponibles est récupérée par le biais d'une requête  [WCS GetCapabilities](#wcs-getcapabilities)|
| FORMAT       | Le format de données désiré pour les données brutes. Les valeurs possibles pour ce paramètre sont : `image/tiff` (GeoTIFF) ou `image/netcdf` (NetCDF)|


| Paramètres optionnels        | Définition |
| ------------------------- | ---------- |
|SUBSETTINGCRS     | Le système de coordonnées cartographiques (CRS) utilisé dans la requête de récupération des données brutes|
|OUTPUTCRS         | Le système de coordonnées cartographiques (CRS) des données brutes téléchargées. Ce paramètre peut être différent de `SUBSETTINGCRS`. Note: L'utilisation de ce paramètre est **fortement recommandée** pour garantir la précision des réponses `WCS GetCoverage`.|
|SUBSET=axis()     | L'étendue géographique des données demandées, par axe. Les sous-paramètres supportées sont : `x`, `xaxis`, `x-axis`, `x_axis`, `long`, `long_axis`, `long-axis`, `lon`, `lon_axis`, `lon-axis`, `y`, `yaxis`, `y-axis`, `y_axis`, `lat`, `lat_axis` et `lat-axis`. Les coordonnées doivent utiliser les mêmes unités que SUBSETTINGCRS. L'étendue géographique demandée doit couvrir au moins une partie de l'étendue géographique de la donnée demandée|
|RESOLUTION=axis() | La résolution spatiale pour chaque axe (pixel/unité) pour la donnée demandée. Si aucune valeur n'est spécifiée, la résolution spatiale de la donnée récupérée pourrait être différente de la donnée d'origine, il est donc recommandé de spécifier la resolution voulue dans la requête. Notez que les paramètres `RESOLUTION` et `SIZE` sont mutuellement exclusifs pour un axe et ne doivent pas être utilisés en même temps pour le même axe d'une requête|
|SIZE=axis()       | Le nombre de pixels voulus pour un axe donné. Si aucune valeur n'est spécifiée, la grosseur de pixel de la donnée récupérée pourrait être différente de la donnée d'origine, il est donc recommandé de spécifier le nombre de pixels voulus dans la requête. Notez que les paramètres `RESOLUTION` et `SIZE` sont mutuellement exclusifs pour un axe et ne doivent pas être utilisés en même temps pour le même axe d'une requête|
|INTERPOLATION     | La méthode d'interpolation utilisée si une mise à l'échelle est nécessaire. Les trois méthodes suivantes sont disponibles : `NEAREST`, `BILINEAR` et `AVERAGE`. Si aucune n'est spécifiée, la méthode par défaut est `NEAREST`|
|RANGESUBSET       | Ce paramètre permet à l'usager de spécifier une bande de la donnée matricielle à récupérer. Le nom ou le numéro de la band doit être utilisé|
|TIME              | La date et temps associés à la donnée demandée. Le format doit respecter le standard ISO8601. Pour davantage de détails au sujet de la composante temporelle, se référer à la section [Spécification du temps dans les requêtes WCS](#wcs-specification-du-temps)|
|DIM_REFERENCE_TIME| Le temps de la passe de modèle (model run), lorsque disponible, à récupérer par le biais de la requête. Le format doit respecter le standard ISO8601. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WCS](#wcs-specification-du-temps)|

Une requête WCS GetCoverage pour la couche GDPS.ETA_TT de GeoMet-Météo est construite comme suit :

[https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff](https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff)

### <a name="wcs-specification-du-temps"></a>Spécification du temps

Compte tenu de l'importance des dimensions temporelles des données météorologiques, il est important de connaître comment GeoMet du SMC traite les paramètres temporels dans les requêtes. Par défaut, si aucun paramètre `TIME` ou `DIM_REFERENCE_TIME` n'est spécifié dans une requête, GeoMet du SMC va utiliser le pas de temps ainsi que la passe de modèle les plus proches.

Un utilisateur désirant effectuer une requête pour un moment spécifique pour les requêtes WCS GetCoverage doit utiliser les paramètres `TIME` et/ou `DIM_REFERENCE_TIME`. La date et le moment doit être envoyé dans le format du standard ISO8601 et les temps sont toujours en UTC (Coordinate Universal Time).

#### GeoMet-Climat

Le service WCS de GeoMet-Climat ne supporte pas les requêtes avec les paramètres `TIME` ou `DIM_REFERENCE_TIME`. À la place, l'information temporelle des requêtes WCS sur GeoMet-Climat utilise des bandes différentes, chaque bande correspondant à un pas de temps spécifique. Les usagers doivent utiliser le paramètre `RANGESUBSET` pour accéder au pas de temps désiré.

La liste des différentes bandes disponibles peut être récupérée par une requête WCS `DescribeCoverage`. Voici un exemple pour la couche DCS.TM.RCP26.YEAR.ANO_PCTL50 de GeoMet-Climat :

```
https://geo.meteo.gc.ca/geomet-climate?SERVICE=WCS&VERSION=2.0.1
&REQUEST=DescribeCoverage&COVERAGEID=DCS.TM.RCP26.YEAR.ANO_PCTL50
```

```xml
...
<swe:field name="B2006">
    <swe:Quantity>
        <swe:nilValues/>
        <swe:uom code="W.m-2.Sr-1"/>
        <swe:constraint>
            <swe:AllowedValues>
                <swe:interval>-3.4028e+38 3.4028e+38</swe:interval>
                <swe:significantFigures>12</swe:significantFigures>
            </swe:AllowedValues>
        </swe:constraint>
    </swe:Quantity>
</swe:field>
<swe:field name="B2007">
    <swe:Quantity>
        <swe:nilValues/>
        <swe:uom code="W.m-2.Sr-1"/>
        <swe:constraint>
            <swe:AllowedValues>
                <swe:interval>-3.4028e+38 3.4028e+38</swe:interval>
                <swe:significantFigures>12</swe:significantFigures>
            </swe:AllowedValues>
        </swe:constraint>
    </swe:Quantity>
</swe:field>
<swe:field name="B2008">
...
```

Dans cet exemple, la valeur `field` indique à l'usager le nom des bandes disponibles. Pour GeoMet-Climat, les bandes utilisent toujours la nomenclature suivante : `B` suivi de l'intervalle ISO8601 correspondant, soit `YYYY` pour un intervalle annuel et `YYYY-MM` pour un intervalle mensuel.

Pour GeoMet-Climat, les usagers pour demander un pas de temps unique ou une plage temporelle :

* Pas de temps unique : `RANGESUBSET=B2015`
* Plage temporelle : `RANGESUBSET=B2015:B2019`

Notez que la limite pour une seule requête WCS GetCoverage est de 256 bandes à la fois.

#### GeoMet-Météo

Pour les requêtes temporelles WCS avec GeoMet-Météo, veuillez vous référer à section sur [la spécification du temps dans les requêtes WMS](#spécification-du-temps) puisque l'utilisation des paramètres `TIME` et `DIM_REFERENCE_TIME` demeure la même.

Les dimensions temporelles pour les requêtes WCS sur GeoMet-Météo ne sont pas fournies par les requêtes WCS GetCapabilities ou WCS DesbcribeCoverage. Les dimensions temporelles de ce service WCS ne sont accessibles que dans une requête WMS GetCapabilities.

### Exemple d'utilisation

Le service WCS de GeoMet-Climat et GeoMet-Météo peut être accédé avec [l'Outil d'extraction de données climatiques](https://changements-climatiques.canada.ca/donnees-climatiques/) du [Centre canadien des services climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques.html).

Les utilisateurs peuvent choisir une variable métérologique ou climatique, une région d'intérêt, l'information temporelle ainsi que de spécifier le format de récupération des données pour obtenir les données brutes correspondantes.


## OGC API - Features

Le standard [OGC API - Features](https://ogcapi.ogc.org/features/) (OAFeat) fournit une liste de spécifications standardisées permettant d'interroger des données géospatiales sur le Web. Le service fonctionne via HTTPS et les requêtes sont effectuées via des requêtes HTTPS GET. Aucune authentification HTTPS n'est requise.

### Points de service

* [https://api.meteo.gc.ca/](https://api.meteo.gc.ca/)

### Documentation OpenAPI 3.0

* [https://api.meteo.gc.ca/openapi](https://api.meteo.gc.ca/openapi)

### Collections d'entités

Répertorier toutes les collections d’entités disponibles :

* [https://api.meteo.gc.ca/collections](https://api.meteo.gc.ca/collections)

La réponse fournit une liste de collections de fonctionnalités avec leurs métadonnées associées (titre, description, liens, étendue, CRS).

### Collection d'entités

Répertorier une seule collection d'entités :

* [https://api.meteo.gc.ca/collections/hydrometric-stations](https://api.meteo.gc.ca/collections/hydrometric-stations)

### Inspection du schéma de collection d'entités

Émettre une requête renvoyant une seule entité pour inspecter sa géométrie et ses propriétés :

* [https://geo.meteo.gc.ca/collections/hydrometric-daily-mean/items?limit=1](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?limit=1)

### Requête

Les requêtes sur les collections d'entités permettent un filtrage spatial, temporel et sur des propriétés. Les paramètres de filtre peuvent être combinés pour formuler une recherche exclusive ('et'). Le premier paramètre d'une requête doit être spécifiée avec `?` et les paramètres subséquents avec `&`.

Les exemples suivants utilisent la collection [hydrométrique de moyennes quotidiennes](https://api.meteo.gc.ca/collections/hydrometric-daily-mean).

Requête par défaut, pas de filtres :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items)

#### Spatial

Requête par zone de sélection (minx, miny, maxx, maxy) :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?bbox=-140,43.2,-65,67](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?bbox=-140,43.2,-65,67)

#### Temporel

Requête pour une valeur instantanée :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30)

Requête pour un intervalle de temps :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?datetime=1972-10-30/2010-07-31)

Requête pour un intervalle de temps le mot clé de borne ouverte `..` : 

* Depuis un moment spécifique : [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=2012-05-20/..)
* Jusqu'à un moment spécifique : [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?f=json&STATION_NUMBER=07DA006&datetime=../2015-11-11)


#### Propriété

Requête par une propriété de collection d'entités :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001)

#### Pagination

##### Startindex

Le paramètre `startindex` peut être utilisé pour spécifier l’enregistrement à partir duquel extraire les entités. La valeur par défaut est 0 (première entité).

##### Nombre total d'enregistrements

Le paramètre `resulttype=hits` est utilisé pour obtenir le nombre d'entités d'une collection, sans que les entités soient retournées. Le nombre d'enregistrements est indiqué à la valeur `numberMatched` de la réponse.

* Exemple : [https://api.meteo.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits](https://api.meteo.gc.ca/collections/ltce-stations/items?f=json&resulttype=hits)

##### Limite

Le paramètre `limit` permet de définir le nombre maximal d'enregistrements à retourner. La taille de réponse par défaut est de 500 entités.

##### Parcourir les résultats

Les paramètres `startindex` et `limit` peuvent être utilisés en tandem pour parcourir les collections d’entités. Les exemples ci-dessous montrent comment ajuster et parcourir les résultats d'une requête.

Requête et limite aux entités 1-2 :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=2](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=2)

Requête et limite aux entités 1 à 100 :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&limit=100)

Requête et limite aux entités 101-200 :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&startindex=101&limit=100](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&startindex=101&limit=100)

##### Stratégies de pagination

La stratégie de pagination est couramment utilisée pour améliorer les performances lors du retour d'extractions de données volumineuses. Par exemple, un client peut faire défiler par 1 000 entités pour parcourir un enregistrement de station complet :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=0&limit=1000](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=0&limit=1000)
* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=01AP004&startindex=1000&limit=1000)

Le client peut alors simplement parcourir tous les éléments jusqu'à ce qu'il n'y ait plus d'enregistrements. Cela constituerait le dossier complet.

 
#### Combinaison de paramètres de filtre

Interroger toutes les moyennes quotidiennes d'une station entre 2001 et 2010 :

* [https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31](https://api.meteo.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=10CD001&datetime=2001-01-01/2010-12-31)

#### Exporter au format CSV

Toute requête peut être exportée au format CSV en ajoutant `f=csv` à la demande.

#### Tri

Toute requête peut être triée utilisant le paramètre `sortby`. L'ordre de tri est croissant par défaut et ajoutez le signe `-` avant le nom de l'attribut pour un tri décroissant. Le tri en fonction de plusieurs attributs est pris en charge en fournissant une liste séparée par des virgules au paramètre `sortby`. Exemples :

* `&sortby=PROPERTY` tri croissant de l'attribut
* `&sortby=-PROPERTY` tri décroissant de l'attribut

### Accès par identifiant

Récupérer une seule caractéristique par un identifiant :

* [https://api.weather.gc.ca/collections/hydrometric-daily-mean/items/11AC016.1926-06-12](https://api.weather.gc.ca/collections/hydrometric-daily-mean/items/11AC016.1926-06-12)
