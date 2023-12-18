[In English](wms_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [GeoMet du SMC](readme_fr.md) > WMS

# Web Map Service (WMS)

Les requêtes effectuées avec le [standard Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms) de l'OGC permettent principalement aux usagers to récupérer des données géospatiales en tant que cartes. Les requêtes WMS sont effectuées via Internet (HTTP) et servent principalement à récupérer une image (e.g. JPEG, PNG) issue de données géospatiales pour une région d'intérêt donnée.

Plusieurs types de requêtes WMS peuvent être spécifiés et celles-ci sont décrites ci-après:

* GetCapabilities
* GetMap
* GetFeatureInfo
* GetLegendGraphic
</br></br>


## WMS GetCapabilities

Une requête WMS GetCapabilities permet à l'usager de récupérer un document XML contenant les métadonnées décrivant le service. Ce document contient l'information associée aux types de requêtes supportées, les systèmes de coordonnées cartographiques supportés, et particulièrement important, la liste des couches (données) disponibles.

Une requête WMS GetCapabilities est composée des paramètres suivants :


| Paramètres obligatoires | Définition |
| ------------------------- | ---------- |
| SERVICE         | Le service que l'utilisateur sollicite. Dans ce cas, `wms`|
| VERSION         | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version la plus récente, soit `1.3.0`|
| REQUEST         | Le type de requête, soit `GetCapabilities`|

| Paramètres optionnels | Définition |
| ------------------------- | ---------- |
| LAYERS         | Un paramètre externe (vendor extension) permettant aux usagers de filter le document GetCapabilities pour une couche spécifique. Ceci réduit significativement la grosseur du document XML résultant|
| LANG          | Un paramètre externe (vendor extension) permettant aux usagers de choisir d'afficher en français(fr) ou en anglais(en) le document GetCapabilities. Si le paramètre n'est pas spécifié, le document GetCapabilities est retourné en anglais par défaut|

Une requête WMS GetCapabilities pour GeoMet-Météo est donc construite ainsi :


[https://geo.meteo.gc.ca/geomet/?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr](https://geo.meteo.gc.ca/geomet/?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities)

Chaque couche définie dans le document XML du WMS GetCapabilities contient l'information telle que l'identifiant de la couche et son nom, son étendue géographique, la plage temporelle ainsi que les styles disponibles.
</br></br>

## WMS GetMap

Une requête WMS GetMap permet aux usagers de récupérer une image (e.g. JPEG, PNG) d'une couche pour une région déterminée. Une requête WMS GetMap est constituée de plusieurs paramètres qui spécifie la couche désirée, son style, le système de coordonnées cartographiques, le pas de temps, en plus des propriétés additionnelles associées à l'image. Une [requête WMS GetCapabilities](#wms-getcapabilities) supporte les usagers en guidant l'utilisateur sur les valeurs possibles pour ces paramètres.

Une requête WMS GetMap est composée des paramètres suivants :

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
| TIME            | La date et l'heure associées à l'image désirée. Le format doit respecter le standard ISO8601. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WMS](#specification-du-temps)|
| DIM_REFERENCE_TIME  | Le temps de la passe du modèle (model run) à utiliser pour l'image désirée. Pour davantage d'information, vous référer à section sur [la spécification du temps dans les requêtes WMS](#specification-du-temps)|

La requête WMS GetMap suivante demande une image de la couche de température de l'air du Système global de prévision déterministe (SGPD) :


```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180
&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png
```

Et retourne :

![Température de l'air du Système global de prévision déterministe (SGPD)](https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=600&HEIGHT=301&LAYERS=GDPS.ETA_TT&FORMAT=image/png)
</br></br></br>

## WMS GetFeatureInfo

Une requête WMS GetFeatureInfo permet de récupérer les données brutes pour un lieu géographique spécifique. Une requête WMS GetFeatureInfo ressemble à une requête WMS GetMap à laquelle s'ajoute les paramètres suivants : `I`, `J` et `QUERY_LAYERS`. Ces paramètres représentent la localisation horizontale et verticale du pixel ainsi que le nom des couches à interroger.

Une requête WMS GetFeatureInfo est composée des paramètres suivants :>

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
| TIME            | La date et l'heure associées à la requête. Le format doit respecter le standard ISO8601. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WMS](#specification-du-temps)|
| DIM_REFERENCE_TIME  | Le temps de la passe du modèle (model run) à utiliser pour la requête. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WMS](#specification-du-temps)|

Une requête GetFeatureInfo pour la même image que l'exemple WMS GetMap ci-dessus :

```
https://geo.meteo.gc.ca/geomet?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&BBOX=45,-75,45.5,-74.5
&CRS=EPSG:4326&WIDTH=10&HEIGHT=10&LAYERS=GDPS.ETA_TT&INFO_FORMAT=application/json&QUERY_LAYERS=GDPS.ETA_TT&I=5&J=5
```
</br></br></br>

## WMS GetLegendGraphic

Une requête GetLegendGraphic retourne une image de la légende d'une couche pour le style demandé. La manière simple d'accéder à la légende d'un style spécifique est de consulter le document WMS GetCapabilities pour la couche en question. Tous les styles d'une couche s'y retrouvent et l'URL de la légende se retrouve dans la balise `<OnlineResource>`.

Par exemple, la couche de température de l'air du SGPD offre plusieurs styles dans le document WMS GetCapabilities. Demander la légende du style `TEMPERATURE-LINEAR` en utilisant une requête GetLegendGraphic retourne cette légende :

![Exemple GetLegendeGraphic TEMPERATURE-LINEAR](https://geo.meteo.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS.ETA_TT&format=image/png&STYLE=TEMPERATURE-LINEAR)

Une requête WMS GetLegendeGraphic est composée des paramètres suivants :

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
| STYLE           | Le style associé à la légende désirée. Si ce paramètre n'est pas spécifié, le style par défaut de la couche sera utilisé. Les styles disponibles pour une couche est spécifié dans le résultat d'une requête [WMS GetCapabilities](#wms-getcapabilities). Note: Assurez-vous de taper la forme au singulier `STYLE` de ce paramètre dans la requête `GetLegendGraphic` et non la forme au pluriel (i.e. STYLES) car la sortie sera le style par défaut de la couche au lieu de celui demandé. |
| SLD             | Indique que la légende doit être créée selon un document SLD externe. Vous référer à la section [Spécification des styles](#specification-des-styles) pour les explications détaillées|
| SLD_BODY        | Permet à l'usager d'inclure le document SLD directement dans la requête| Note: la valeur de LAYER dans la requête WMS GetMap et la valeur de se:Name (ou se%3AName lorsqu'il est encodé) dans SLD_BODY doivent être différentes pour que la requête fonctionne correctement.
| LANG          | Un paramètre externe (vendor extension) permettant aux usagers de choisir d'afficher en français(fr) ou en anglais(en) la légende. Si le paramètre n'est pas spécifié, la légende est retournée en anglais par défaut|
</br>

Un exemple de requête GetLegendGraphic pour la couche des courants océaniques (CIOPS-East_2km_SeaIceVelocity) du Système Mondial de Prévision des Glaces et des Océans (GIOPS) va comme suit :

```
https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0
&layer=OCEAN.GIOPS.2D_UU2W&format=image/png&STYLE=SEA_CURARROW_0MTO100M_SURFACE
```

Et retourne :

![Exemple des flèches des courants océaniques du GIOPS](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=OCEAN.GIOPS.2D_UU2W&format=image/png&STYLE=SEA_CURARROW_0MTO100M_SURFACE)


## Spécification du temps

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

</br>

#### <span class="badge badge-light">Différences entre les dimensions temporelles de GeoMet-Météo et GeoMet-Climat</span>

Il est important de considérer les différences dans la spécification du temps entre GeoMet-Météo et GeoMet-Climat, différences issues de la nature différente des données en cause.

Dans GeoMet-Climat, les intervalles temporels sont soit annuels (YYYY) ou mensuels (YYYY-MM) selon la couche interrogée. Une requête WMS GetCapabilities sur les services GeoMet-Climat indique aux usagers quelles sont les dimensions temporelles disponibles pour un couche spécifique.

Par exemple, la balise `<Dimension>` de la couche [Ensembles mensuels CMIP5 pour la vitesse du vent près de la surface (5e percentile)](https://geo.meteo.gc.ca/geomet-climate?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&Layer=CMIP5.SFCWIND.RCP26.ENS.ABS_PCTL5) indique :

```xml
<Dimension name="time" units="ISO8601" default="2100-12" nearestValue="0">2006-01/2100-12/P1M</Dimension>
```

Un requête WMS GetMap valide avec le paramètre `TIME` doit ainsi utiliser une valeur entre `2006-01` et `2100-12`.

</br></br>

## Spécification des styles

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
