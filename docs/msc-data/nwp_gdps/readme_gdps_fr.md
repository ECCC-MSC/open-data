[In English](readme_gdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SGPD


# Données et produits du Système global de prévision déterministe

Le Système global de prévision déterministe (SPGD) procède à des calculs physiques afin de produire des prévisions déterministes d'éléments de l'atmosphère du jour présent jusqu'à 10 jours dans le futur. Les éléments de l'atmosphère incluent notamment la température, les précipitations, la couverture nuageuse, la vitesse et direction des vents et l'humidité. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique est mondiale. La résolution spatiale horizontale des données est de 15 km. Les données sont offertes pour 33 niveaux verticaux. Les prévisions sont exécutées deux fois par jour.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) et le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_gdps-geomet_fr.md)
* [Données GRIB2 de prévision disponibles sur le Datamart du SMC](readme_gdps-datamart_fr.md)
* [Données GeoJSON statistiquement post-traitées sur le Datamart du SMC](readme_gdps-statpostproc-datamart_fr.md)
* [Données expérimentales GRIB2 d'éléments du temps sur grille disponibles sur DD-Alpha, le site Web d'essai de données du Datamart du SMC](readme_gdps-datamart-alpha_fr.md) 
* [Données NetCDF d'analyse de glace globale sur le Datamart du SMC](readme_gdps-ice-anal-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche `GDPS.DIAG_NW_PT1H` du SGPD provenant de GeoMet du SMC :

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GDPS.DIAG_NW_PT1H&format=image/png&STYLE=SIGPRECIPITATIONTYPE-FR"/>
  </div>
</div>
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

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

* Les [métadonnées du Système global de prévision déterministe sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/c041e79a-914a-5a4e-a485-9cbc506195df).
* Les [métadonnées de la Prévision du système global de prévision déterministe statistiquement post-traité par UMOS sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/7c1070fd-af7d-40fe-9e78-49d2962f0bbc).

## Produits

Liste et liens vers les produits disponibles pour ce jeu de données :

### Cartes de prévision

* [Cartes 4 panneaux classiques](https://meteo.gc.ca/model_forecast/global_f.html)

### Cartes d'analyses

* [Température de la surface de la mer](https://meteo.gc.ca/data/analysis/351_100.gif)
* [Étendue de la glace de mer](https://meteo.gc.ca/data/analysis/350_100.gif)
* [Épaisseur de la neige au sol](https://meteo.gc.ca/data/analysis/352_100.gif)
* [Ozone stratosphérique](https://woudc.org/data/products/?lang=fr)

## Documentation technique

* [Version actuelle du Système global de prévision déterministe](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GDPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_gdps_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_GDPS_fr.svg)

## Registre des changements 

La chronologie des changements apportés au Système global de prévision déterministe (SPGD) est disponible [dans le registre des changements](changelog_gdps_fr.md).

<style>
  #legend-img {
    margin: 0px;
    height:300px;
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
        js.src = "../../../js/gdps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/gdps.js";
    }
    head.appendChild(js);
</script>
