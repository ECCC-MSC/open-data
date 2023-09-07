[In English](readme_climateobs-geomet_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données climatiques (normales, données quotidiennes, sommaires mensuels)](readme_climateobs_fr.md) > Données climatiques (normales, données quotidiennes, sommaires mensuels) sur GeoMet du SMC

# Données des observations historiques disponibles sur GeoMet du SMC

GeoMet du SMC donne accès à plusieurs produits et données climatiques (normales, données quotidiennes, sommaires mensuels). Les usagers peuvent développer des applications mobiles, créer des cartes interactives en-ligne, ainsi que visualiser et animer les données climatiques du SMC dans des logiciels de bureau.

## Accès aux services web géospatiaux

Les couches des observations historiques sont [disponibles sur GeoMet-Météo par le biais des standards WMS (Web Map Service) et WCS (Web Coverage Service)](../../msc-geomet/readme_fr.md).

Exemple de carte interactive présentant la couche [DCS.TX.RCP85.YEAR.2081-2100_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50) des observations historiques provenant de GeoMet du SMC :

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50&format=image/png&STYLE=TEMP-ANOMALIES"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
</div>

## Utilisation

La page de [l'aperçu de l'utilisation](../../usage/readme_fr.md) présente l'information de base sur l'utilisation de ces services avec des logiciels de bureau, des applications mobiles, les cartes interactives en ligne ainsi que l'accès direct. Veuillez vous référer aux [tutoriels et à la documentation technique sur les services web géospatiaux GeoMet du SMC](../../msc-geomet/web-services_fr.md) pour de l'information détaillée.

### Couches disponibles

Pour savoir quelles couches des observations historiques sont servies par GeoMet du SMC, consultez le [document WMS GetCapabilities](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=f).

Les logiciels SIG de bureau tels que QGIS permettent également de [naviguer dans le document WMS GetCapabilities sous la forme d'une arborescence de couches](../../usage/tutorial_WMS_QGIS_fr.md).

### Conseils d'utilisation

Récupération de la liste des derniers pas de temps disponibles :

* Les utilisateurs peuvent ajouter le paramètre `layer` à une requête WMS GetCapabilities afin de pointer à une couche spécifique et obtenir une réponse XML plus simple avec les dimensions temporelles à jour (voir les balises `<Dimension>`). Exemple : [https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50).
* Davantage d'information est disponible dans la section sur [la spécification du temps avec les services WMS](../../../msc-geomet/web-services_fr#specification-du-temps).

Styles WMS :

* En plus du style WMS par défaut, plusieurs styles WMS alternatifs avec des échelles de couleurs différentes sont disponibles. La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities.
* Par ailleurs, les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard Styled Layer Descriptor (SLD). Veuillez vous référer à la [documentation technique sur le SLD](../../../msc-geomet/web-services_fr#specification-des-styles).

Légendes :

* Les légendes sont disponibles pour tous les styles WMS. Les détails sont disponibles dans la [documentation technique des légendes WMS](../../../msc-geomet/web-services_fr#wms-getlegendgraphic).
* Exemple d'une requête pour récupérer une légende : [https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50&format=image/png&STYLE=TEMP-ANOMALIES](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50&format=image/png&STYLE=TEMP-ANOMALIES).

![La légende TEMP-ANOMALIES pour la couche DCS.TX.RCP85.YEAR.2081-2100_PCTL50](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50&format=image/png&STYLE=TEMP-ANOMALIES)


## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info.comm.collab.science.gc.ca/) afin d'être informés des améliorations et changements aux services GeoMet du SMC.

<style>
  #legend-img {
    margin: 0px;
    height:280px;
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
        js.src = "../../../js/climateobs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/climateobs.js";
    }
    head.appendChild(js);
</script>
