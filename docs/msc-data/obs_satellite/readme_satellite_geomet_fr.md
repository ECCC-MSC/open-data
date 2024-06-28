[In English](readme_satellite_geomet_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [GOES Satellite](readme_satellite_fr.md) > Données satellite GOES sur GeoMet du SMC

# Données de satellites météorologiques disponibles sur GeoMet du SMC

MSC GeoMet donne accès aux couches des satellites météorologiques. Les utilisateurs peuvent créer des applications mobiles, des cartes web interactives et afficher et animer des couches de satellites météorologiques dans des logiciels de bureau.


## Accès aux services web géospatiaux

Les données GOES sont disponibles sur GeoMet-Weather via les standards [Web Map Service (WMS)](../../msc-geomet/wms_fr.md) et [Web Coverage Service (WCS)](../../msc-geomet/wcs_fr.md).

Exemple de carte web configurée pour afficher la couche d'imagerie satellite en couleur naturelle [(GOES-East_1km_NaturalColor)](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&layer=GOES-East_1km_NaturalColor) servie par MSC GeoMet :

<div id="map" style="height: 400px; position: relative">
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;cursor: pointer;"></span>
</div>

</br>

## Utilisation

La [page de l'aperçu de l'utilisation](../../usage/readme_fr.md) fournit des informations génériques sur l'utilisation des services OGC avec des logiciels de bureau, des applications mobiles, des cartes web interactives et un accès direct. Veuillez vous référer aux [tutoriels](../../usage/tutorials_fr.md) et à la [documentation technique pour les services web géospatiaux de MSC GeoMet](../../msc-geomet/readme_fr.md#standards-disponibles) pour des informations détaillées. Voir également la [page principale des données des satellites météorologiques](readme_satellite_fr.md) qui contient des liens vers des informations supplémentaires sur les couches de satellites météorologiques.

### Couches disponibles

Les couches satellites météorologiques sont mises à jour toutes les 10 minutes.

Est :

* GOES-Est visibilité de jour / Convection nuageuse de jour [1 km], ID: `GOES-East_1km_DayVis`
* GOES-Est Couleur naturelle [1 km], ID: `GOES-East_1km_NaturalColor`
* GOES-Est IR de nuit [2 km], ID: `GOES-East_2km_NightIR`
* GOES-Est Microphysique de nuit [2 km], ID: `GOES-East_2km_NightMicrophysics`
* GOES-Est Température des feux/SWIR [1 km], ID: `GOES-East_1km_FireTemperature-SWIR`
* GOES-Est Cendre [2 km], ID: `GOES-East_2km_Ash`
* GOES-Est SO2 [2 km], ID: `GOES-East_2km_SO2`
* GOES-Est Poussière [2 km], ID: `GOES-East_2km_Dust`
* GOES-Est Type de nuage de jour/Microphysique de nuit [1 km], ID: `GOES-East_1km_DayCloudType-NightMicrophysics`
* GOES-Est Visibilité de jour/IR de nuit [1 km], ID: `GOES-East_1km_DayVis-NightIR`
* GOES-Est Sandwich visible et IR/Microphysique de nuit et IR [1 km], ID: `GOES-East_1km_VisibleIRSandwich-NightMicrophysicsIR`
* GOES-Est Neige-brouillard/Microphysique de nuit [1 km], ID: `GOES-East_1km_SnowFog-NightMicrophysics`
* GOES-Est Fumée sur Canal-1 ABI/SWIR [1 km], ID: `GOES-East_1km_SmokeABIband1-SWIR`
* GOES-Est Détection de feux de jour /SWIR [1 km], ID: `GOES-East_1km_DayLandCloudFire-SWIR`

Ouest :

* GOES-Ouest visibilité de jour / Convection nuageuse de jour [1 km], ID: `GOES-West_1km_DayVis`
* GOES-Ouest Couleur naturelle [1 km], ID: `GOES-West_1km_NaturalColor`
* GOES-Ouest IR de nuit [2 km], ID: `GOES-West_2km_NightIR`
* GOES-Ouest Microphysique de nuit [2 km], ID: `GOES-West_2km_NightMicrophysics`
* GOES-Ouest Température des feux/SWIR [1 km], ID: `GOES-West_1km_FireTemperature-SWIR`
* GOES-Ouest Cendre [2 km], ID: `GOES-West_2km_Ash`
* GOES-Ouest SO2 [2 km], ID: `GOES-West_2km_SO2`
* GOES-Ouest Poussière [2 km], ID: `GOES-West_2km_Dust`
* GOES-Ouest Type de nuage de jour/Microphysique de nuit [1 km], ID: `GOES-West_1km_DayCloudType-NightMicrophysics`
* GOES-Ouest Visibilité de jour/IR de nuit [1 km], ID: `GOES-West_1km_DayVis-NightIR`
* GOES-Ouest Sandwich visible et IR/Microphysique de nuit et IR [1 km], ID: `GOES-West_1km_VisibleIRSandwich-NightMicrophysicsIR`
* GOES-Ouest Neige-brouillard/Microphysique de nuit [1 km], ID: `GOES-West_1km_SnowFog-NightMicrophysics`
* GOES-Ouest Fumée sur Canal-1 ABI/SWIR [1 km], ID: `GOES-West_1km_SmokeABIband1-SWIR`
* GOES-Ouest Détection de feux de jour /SWIR [1 km], ID: `GOES-West_1km_DayLandCloudFire-SWIR`

### Conseils d'utilisation

Récupération de la liste des derniers pas de temps disponibles :

* Les utilisateurs peuvent ajouter le paramètre `layer` à une requête WMS GetCapabilities afin de pointer vers une couche spécifique et obtenir une réponse XML plus simple avec les dimensions temporelles à jour. Exemple pour la couche de couleur naturelle du satellite de 1 km : [https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=GOES-East_1km_NaturalColor](https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=GOES-East_1km_NaturalColor)
* Les utilisateurs peuvent également avoir les dimensions temporelles les plus à jour pour toutes les couches satellite qui ont un intervalle de temps en minutes, en une seule requête, via l'utilisation du paramètre de requête `LAYERS_REFRESH_RATE=PT1M`. De plus, toutes les couches ayant un intervalle de temps en minutes feront partie de ce WMS GetCapabilities. Exemple pour la requête : [https://geo.weather.gc.ca/geomet?LAYERS_REFRESH_RATE=PT1M&SERVICE=WMS&REQUEST=GetCapabilities&lang=fr](https://geo.weather.gc.ca/geomet?LAYERS_REFRESH_RATE=PT1M&SERVICE=WMS&REQUEST=GetCapabilities&lang=fr)
* Davantage d'informations sont disponibles dans la section sur [la spécification du temps avec les services WMS](../../../msc-geomet/wms_fr#specification-du-temps)

Styles WMS :

* En plus du style WMS par défaut, plusieurs styles WMS alternatifs avec des échelles de couleurs différentes sont disponibles. La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities
* Par ailleurs, les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard Styled Layer Descriptor (SLD). Veuillez vous référer à la [documentation technique sur le SLD](../../../msc-geomet/wms_fr#specification-des-styles)

## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://weather.gc.ca/mainmenu/contact_us_f.html).


## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) afin d'être informés des améliorations et changements aux services GeoMet du SMC.

<style>
  #legend-img {
    margin: 0px;
  }
  #legend-popup {
    position: absolute;
    top: 40px;
    right: 8px;
    z-index: 2;
  }
  .legend-switch{
    top: 8px;
    right: .5em;
  }
  .ol-touch .legend-switch {
    top: 80px;
  }
  .distinguish-switch{
    top: 8px;
    right: 1em;
    width: 15rem;
    position: relative;
  }
  .ol-touch .distinguish-switch{
    top: 80px;
  }
  .distinguish-switch.ol-unselectable.ol-control button{
    width: 15rem;
  }

  .distinguish-switch::before {
    content: "Données de jour seulement"; /* Ajoute le texte que tu veux ici */
    position: absolute;
    top: 50%; /* Ajuste la position verticale si nécessaire */
    left: 50%; /* Ajuste la position horizontale si nécessaire */
    transform: translate(-50%, -50%); /* Centre le texte */
    white-space: nowrap; /* Empêche le texte de passer à la ligne */
  }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
<script>
    function isIE() {
      return window.navigator.userAgent.match(/(MSIE|Trident)/);
    }
    var head = document.getElementsByTagName('head')[0];
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (isIE())
    {
        js.src = "../../../js/satellite_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/satellite.js";
    }
    head.appendChild(js);
</script>