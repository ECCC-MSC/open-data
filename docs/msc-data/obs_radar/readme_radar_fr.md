[In English](readme_radar_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Données et produits radar

# Données et produits des observations radar

Cette page décrit les données et produits des radars canadiens du réseau de 32 sites d’Environnement et Changement climatique Canada qui se concentre dans les régions les plus peuplées du Canada, offrant ainsi une couverture à plus de 95 % des Canadiennes et des Canadiens. La fonction principale du réseau est la détection avancée des précipitations, des orages et des phénomènes météorologiques à grande retombée qui se développent, tout comme de suivre le parcours des précipitations. 

## Accès

### Comment accéder aux données

Les données radar sont disponibles via l'API et les services web GeoMet du SMC ainsi que sur le serveur de données Datamart du SMC :

* [Couches de radar disponibles via les services web géospatiaux GeoMet-Météo](readme_radar_geomet_fr.md):
    * Composite radar nord-américaine
    * Type de précipitation à la surface du radar nord-américain [expérimental]
    * Extrapolation radar nord-américaine [expérimental]
* [Imagerie radar en format GIF disponible sur le Datamart du SMC](readme_radarimage-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Ci-après est un exemple de carte interactive configurée pour présenter des couches WMS de la composite et de l'extrapolation radar météo servies par GeoMet du SMC.

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src=""/>
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

* Les [métadonnées de Composite radar nord-américaine (1 km) sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/37aecae5-7783-4274-b595-df02aa003ac3).
* Les [métadonnées de Couverture dynamique de la composite radar sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/6b02c778-8eaa-46f5-8786-ae80b0ea0f72).
* Les [métadonnées de Radars météorologiques - Accumulation sur 24 heures sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/ce9e475b-3e3b-4b15-9ac4-165549366b09).
* Les [métadonnées de Radars météorologiques - CAPPI sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/aae10768-0c0c-4670-807e-8e893680887e).
* Les [métadonnées de Radars météorologiques - EQPDP sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/6059da1d-e1da-4f2b-a420-b5c2a130eeaa).
* Les [métadonnées de Radars météorologiques - PRECIP-ET sont accessibles sur le portail du gouvernement ouvert](https://open.canada.ca/data/fr/dataset/d76c0f4e-af27-4f9c-b0b0-0eba5aca1d3b).

## Documentation technique

* [A propos des radars](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/a-propos.html)
* [Modernisation du réseau canadien de radars météorologiques](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/modernisation-reseau.html)
* [Interruption et maintenance du service radar](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/interruption-maintenance-service.html)
* Guide des produits radar  --  __à venir__ 

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
    right: 2.25em;
    width: 10rem;
  }
  .ol-touch .distinguish-switch{
    top: 80px;
  }
  .distinguish-switch.ol-unselectable.ol-control button{
    width: 10rem;
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
        js.src = "../../../js/radar_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/radar.js";
    }
    head.appendChild(js);
</script>
