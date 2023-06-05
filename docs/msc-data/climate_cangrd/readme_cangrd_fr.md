[In English](readme_cangrd_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > CanGRD

# Données et produits des Anomalies de température et précipitation interpolées pour le Canada (CANGRD)  

CANGRD est un ensemble de données canadiennes des anomalies annuelles, saisonnières et mensuelles des températures et précipitations qui sont interpolées à partir des stations des Données Climatiques Canadiennes Ajustées et Homogénéisées (DCCAH); cet ensemble de données est utilisé pour produire le Bulletin des Tendances et Variations Climatiques (BTVC).

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles sur les services web géospatiaux GeoMet-Climat](readme_cangrd-geomet_fr.md)
* [Données disponibles sur les services web géospatiaux GeoMet-OGC-API](https://api.meteo.gc.ca/):
    * [CanGRD - Tendance annuelle historique](https://api.meteo.gc.ca/collections/climate:cangrd:historical:annual:trend)
    * [CanGRD - Tendance saisonnière historique](https://api.meteo.gc.ca/collections/climate:cangrd:historical:seasonal:trend)
    * [CanGRD - Anomalie annuelle historique](https://api.meteo.gc.ca/collections/climate:cangrd:historical:annual:anomaly)
    * [CanGRD - Anomalie saisonnière historique](https://api.meteo.gc.ca/collections/climate:cangrd:historical:seasonal:anomaly)
    * [CanGRD - Anomalie mensuelle historique](https://api.meteo.gc.ca/collections/climate:cangrd:historical:monthly:anomaly)
* [Données GeoTIFF disponibles sur le Datamart du SMC](readme_cangrd-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [CANGRD.ANO.TX_ANNUAL](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=CANGRD.ANO.TX_ANNUAL) du CanGRD provenant de GeoMet du SMC :

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CANGRD.ANO.TX_ANNUAL&format=image/png&STYLE=TEMP-ANOMALIES"/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
</div>

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

Les [métadonnées des Anomalies de température et précipitation interpolées pour le Canada sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/3d4b68a5-13bc-48bb-ad10-801128aa6604)

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_cangrd/CANGRD_Technical_Documentation_fr.pdf)
* Ces données sont aussi disponibles via le [Centre canadien des services climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/a-propos.html)

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
        js.src = "../../../js/cangrd_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cangrd.js";
    }
    head.appendChild(js);
</script>
