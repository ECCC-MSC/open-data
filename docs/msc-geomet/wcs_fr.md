[In English](wcs_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [GeoMet du SMC](readme_fr.md) > WCS

# Web Coverage Service (WCS)

Les requêtes de type [OGC Web Coverage Service](https://www.opengeospatial.org/standards/wcs) permettent aux usagers de télécharger les données géospatiales brutes pour une région d'intérêt spécifique. Les requêtes WCS sont effectuée via l'Internet et offrent davantage de flexibilité lorsque comparées au téléchargement de fichiers bruts. Le service WCS rend possible plusieurs types de requêtes, qui sont décrites en détail ci-dessous.


Notez que seule la version WCS 2.0.1 est présentement supportée par les services web GeoMet du SMC. Nous invitons les usagers à utiliser cette version du standard. Il est aussi à noter que QGIS et ArcGIS ne supportent pas le WCS 2.0.1.

Plusieurs types de requêtes WCS peuvent être spécifiés et celles-ci sont décrites ci-après:

* GetCapabilities
* DescribeCoverage
* GetCoverage
* GetLegendGraphic
</br></br>

## WCS GetCapabilities

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

</br></br>

## WCS DescribeCoverage

Une requête WCS DescribeCoverage permet à l'usager de récupérer davantage d'information qu'un WCS GetCapabilities pour une couche en particulier. L'information provenant d'une requête WCS DescribeCoverage inclut l'étendue géographique des données, les couches et les formats disponibles.

Une requête WCS DescribeCoverage est construite ainsi :

| Paramètres obligatoires   | Définition |
| ------------------------- | ---------- |
| SERVICE      | Le service que l'utilisateur sollicite. Dans ce cas, `wcs`|
| VERSION      | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version supportée, soit `2.0.1`|
| REQUEST      | Le type de requête, soit `DescribeCoverage`|
| COVERAGEID   | Un paramètre permettant aux usagers de spécifier la couche désirée. La liste des couches disponibles est récupérée par le biais d'une requête  [WCS GetCapabilities](#wcs-getcapabilities)|

Une requête WCS DescribeCoverage pour la couche GDPS.ETA_TT de GeoMet-Météo est construite comme suit :

[https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT](https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=DescribeCoverage&COVERAGEID=GDPS.ETA_TT)

</br></br>

## WCS GetCoverage

Une requête WCS GetCoverage est utilisée afin de récupérer les données brutes d'une couche en particulier. L'aspect pratique de ces requêtes est qu'elles permettent de récupérer un sous-domaine spatial dans la projection cartographique spécifiée ainsi que de récupérer les données dans un format de données et une résolution spatiale différente que les données d'origine.

Une requête WCS GetCoverage est composée des paramètres suivants :

| Paramètres obligatoires   | Définition |
| ------------------------- | ---------- |
| SERVICE      | Le service que l'utilisateur sollicite. Dans ce cas, `wcs`|
| VERSION      | La version du service que l'utilisateur sollicite. Nous recommendons l'utilisation de la version supportée, soit `image/jpeg`|
| REQUEST      | Le type de requête, soit `GetCoverage`|
| COVERAGEID   | Un paramètre permettant aux usagers de spécifier la couche désirée. La liste des couches disponibles est récupérée par le biais d'une requête  [wcs getcapabilities](#wcs-getcapabilities)|
| FORMAT       | Le format de données désiré pour les données brutes. Les valeurs possibles pour ce paramètre sont : `image/tiff` (GeoTIFF) ou `image/netcdf` (NetCDF)|


| Paramètres optionnels        | Définition |
| ------------------------- | ---------- |
|SUBSETTINGCRS     | Le système de coordonnées cartographiques (CRS) utilisé dans la requête de récupération des données brutes|
|OUTPUTCRS         | Le système de coordonnées cartographiques (CRS) des données brutes téléchargées. Ce paramètre peut être différent de `SUBSETTINGCRS`. Note: L'utilisation de ce paramètre est **fortement recommandée** pour garantir la précision des réponses `WCS GetCoverage`.|
|SUBSET=axis()     | L'étendue géographique des données demandées, par axe. Les sous-paramètres supportées sont : `x`, `xaxis`, `x-axis`, `x_axis`, `long`, `long_axis`, `long-axis`, `lon`, `lon_axis`, `lon-axis`, `y`, `axis`, `y-axis`, `y_axis`, `lat`, `lat_axis` et `lat-axis`. Les coordonnées doivent utiliser les mêmes unités que SUBSETTINGCRS. L'étendue géographique demandée doit couvrir au moins une partie de l'étendue géographique de la donnée demandée|
|RESOLUTION=axis() | La résolution spatiale pour chaque axe (pixel/unité) pour la donnée demandée. Si aucune valeur n'est spécifiée, la résolution spatiale de la donnée récupérée pourrait être différente de la donnée d'origine, il est donc recommandé de spécifier la resolution voulue dans la requête. Notez que les paramètres `RESOLUTION` et `SIZE` sont mutuellement exclusifs pour un axe et ne doivent pas être utilisés en même temps pour le même axe d'une requête|
|SIZE=axis()       | Le nombre de pixels voulus pour un axe donné. Si aucune valeur n'est spécifiée, la grosseur de pixel de la donnée récupérée pourrait être différente de la donnée d'origine, il est donc recommandé de spécifier le nombre de pixels voulus dans la requête. Notez que les paramètres `RESOLUTION` et `SIZE` sont mutuellement exclusifs pour un axe et ne doivent pas être utilisés en même temps pour le même axe d'une requête|
|INTERPOLATION     | La méthode d'interpolation utilisée si une mise à l'échelle est nécessaire. Les trois méthodes suivantes sont disponibles : `NEAREST`, `BILINEAR` et `AVERAGE`. Si aucune n'est spécifiée, la méthode par défaut est `NEAREST`|
|RANGESUBSET       | Ce paramètre permet à l'usager de spécifier une bande de la donnée matricielle à récupérer. Le nom ou le numéro de la bande doit être utilisé|
|TIME              | La date et temps associés à la donnée demandée. Le format doit respecter le standard ISO8601. Pour davantage de détails au sujet de la composante temporelle, se référer à la section [Spécification du temps dans les requêtes WCS](#specification-du-temps)|
|DIM_REFERENCE_TIME| Le temps de la passe de modèle (model run), lorsque disponible, à récupérer par le biais de la requête. Le format doit respecter le standard ISO8601. Pour davantage d'information, vous référer à la section sur [la spécification du temps dans les requêtes WCS](#specification-du-temps)|

Une requête WCS GetCoverage pour la couche GDPS.ETA_TT de GeoMet-Météo est construite comme suit :

[https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&
SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&
RESOLUTION=y(0.24)&FORMAT=image/tiff](https://geo.meteo.gc.ca/geomet?SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID=GDPS.ETA_TT&SUBSETTINGCRS=EPSG:4326&SUBSET=x(-120,-85)&SUBSET=y(48,66)&RESOLUTION=x(0.24)&RESOLUTION=y(0.24)&FORMAT=image/tiff)

</br></br>

## Spécification du temps

Compte tenu de l'importance des dimensions temporelles des données météorologiques, il est important de connaître comment GeoMet du SMC traite les paramètres temporels dans les requêtes. Par défaut, si aucun paramètre `TIME` ou `DIM_REFERENCE_TIME` n'est spécifié dans une requête, GeoMet du SMC va utiliser le pas de temps ainsi que la passe de modèle les plus proches.

Un utilisateur désirant effectuer une requête pour un moment spécifique pour les requêtes WCS GetCoverage doit utiliser les paramètres `TIME` et/ou `DIM_REFERENCE_TIME`. La date et le moment doit être envoyé dans le format du standard ISO8601 et les temps sont toujours en UTC (Coordinate Universal Time).

</br>

#### <span class="badge badge-light">GeoMet-Climat</span>
</br>

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
</br>

#### <span class="badge badge-light">GeoMet-Météo</span>

Pour les requêtes temporelles WCS avec GeoMet-Météo, veuillez vous référer à section sur [la spécification du temps dans les requêtes WMS](../WMS_fr/#specification-du-temps) puisque l'utilisation des paramètres `TIME` et `DIM_REFERENCE_TIME` demeure la même.

Les dimensions temporelles pour les requêtes WCS sur GeoMet-Météo ne sont pas fournies par les requêtes WCS GetCapabilities ou WCS DesbcribeCoverage. Les dimensions temporelles de ce service WCS ne sont accessibles que dans une requête WMS GetCapabilities.
</br></br>

## Exemple d'utilisation

Le service WCS de GeoMet-Climat et GeoMet-Météo peut être accédé avec [l'Outil d'extraction de données climatiques](https://changements-climatiques.canada.ca/donnees-climatiques/) du [Centre canadien des services climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques.html).

Les utilisateurs peuvent choisir une variable métérologique ou climatique, une région d'intérêt, l'information temporelle ainsi que de spécifier le format de récupération des données pour obtenir les données brutes correspondantes.
</br></br>