[In English](readme_cmip5_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > CMIP5

# Données et produits de scénarios climatiques, basés sur un ensemble de projections de modèles climatiques globaux de la phase 5 du projet d’intercomparaison de modèles couplés (CMIP5) 

Des ensembles multimodèles de sorties de modèles et de changements projetés sur grille sont disponibles pour les simulations historiques et trois scénarios d'émissions, RCP2.6, RCP4.5 et RCP8.5, à une résolution de de 1x1 degré. Les changements projetés sont exprimés sous forme d'anomalies par rapport à la période de référence 1986-2005. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles sur les services web géospatiaux GeoMet-Climat](readme_cmip5-geomet_fr.md)
* [Données disponibles sur les services web géospatiaux GeoMet-OGC-API](https://api.meteo.gc.ca/) :
    * [CMIP5 - Annuelle projetée](https://api.meteo.gc.ca/collections/climate:cmip5:projected:annual:absolute)
    * [CMIP5 - Saisonnière projetée](https://api.meteo.gc.ca/collections/climate:cmip5:projected:seasonal:absolute)
    * [CMIP5 - Mensuelle projetée](https://api.meteo.gc.ca/collections/climate:cmip5:projected:monthly:absolute)
    * [CMIP5 - Anomalie annuelle projetée](https://api.meteo.gc.ca/collections/climate:cmip5:projected:annual:anomaly)
    * [CMIP5 - Anomalie saisonnière projetée](https://api.meteo.gc.ca/collections/climate:cmip5:projected:seasonal:anomaly)
    * [CMIP5 - Anomalie mensuelle projetée](https://api.meteo.gc.ca/collections/climate:cmip5:projected:monthly:anomaly)
    * [CMIP5 - Anomalie annuelle projetée pour une moyenne de 20 ans](https://api.meteo.gc.ca/collections/climate:cmip5:projected:annual:P20Y-Avg)
    * [CMIP5 - Anomalie saisonnière projetée pour une moyenne de 20 ans](https://api.meteo.gc.ca/collections/climate:cmip5:projected:seasonal:P20Y-Avg)
    * [CMIP5 - Annuelle historique](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:absolute)
    * [CMIP5 - Saisonnière historique](https://api.meteo.gc.ca/collections/climate:cmip5:historical:seasonal:absolute)
    * [CMIP5 - Mensuelle historique](https://api.meteo.gc.ca/collections/climate:cmip5:historical:monthly:absolute)
    * [CMIP5 - Anomalie annuelle historique](https://api.meteo.gc.ca/collections/climate:cmip5:historical:annual:anomaly)
    * [CMIP5 - Anomalie saisonnière historique](https://api.meteo.gc.ca/collections/climate:cmip5:historical:seasonal:anomaly)
    * [CMIP5 - Anomalie mensuelle historique](https://api.meteo.gc.ca/collections/climate:cmip5:historical:monthly:anomaly)
* [Données NetCDF disponibles sur le Datamart du SMC](readme_cmip5-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [CMIP5.TT.HISTO.SUMMER.ABS_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50) du CMIP5 provenant de GeoMet du SMC :

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP5.TT.HISTO.SUMMER.ABS_PCTL50&format=image/png&STYLE=TEMP-ABSOLUTE"/>
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

### Métadonnées de découverte

* Les [métadonnées des changements de température projetés basés sur les ensembles multimodèles CMIP5 sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/1e86f4f7-da88-403e-bd44-92065c0fd568)
* Les [métadonnées des changements de précipitation projetés basés sur les ensembles multimodèles CMIP5 sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/eddd6eaf-34d7-4452-a994-3d928115a68b)
* Les [métadonnées des changements projetés dans l’épaisseur de la couche de neige basés sur les ensembles multimodèles CMIP5 sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/0933f0dc-3625-4583-828a-86d032e4b737)
* Les [métadonnées des changements dans l’épaisseur de la glace de mer basés sur les ensembles multimodèles CMIP5 sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/b6a68b05-58f3-4d71-89d8-25b5a5277796)
* Les [métadonnées des changements dans la concentration de glace de mer basés sur les ensembles multimodèles CMIP5 sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/78f9e3e0-3a12-4321-99dd-eed047c31e5e)
* Les [métadonnées des changements projetés de la vitesse du vent de surface basés sur les ensembles multimodèles CMIP5 sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/e0c71149-db7a-4700-acfd-1c8f9d778354)

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_cmip5/CMIP5_Technical_Documentation_fr.pdf)
* [Informations sur les profils représentatifs d’évolution de concentration](http://scenarios-climatiques.canada.ca/index.php?page=scen-rcp)
* [Introduction aux scénarios climatiques](http://scenarios-climatiques.canada.ca/index.php?page=cmip5-intro)
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
        js.src = "../../../js/cmip5_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cmip5.js";
    }
    head.appendChild(js);
</script>
