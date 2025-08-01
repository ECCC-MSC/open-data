[In English](readme_geps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SGPE

# Données et Produits du Système global de prévision d'ensemble (SGPE)

Le Système global de prévision d'ensemble (SGPE) procède à des calculs physiques afin de produire des prévisions probabilistes d'éléments de l'atmosphère du jour présent jusqu'à 16 jours dans le futur (jusqu'à 39 jours les lundis et jeudis à 00 UTC pour le calcul des anomalies de prévision). Le SGPE génère différentes prévisions (scénarios) pour estimer les incertitudes des prévisions causées par le comportement non-linéaire (chaotique) de l'atmosphère. Les prévisions probabilistes sont basées sur un ensemble de 20 scénarios qui diffèrent par leurs conditions initiales, leurs paramètres physiques qui sont aléatoirement perturbés par la méthode de Perturbation des Paramètres Stochastiques (SPP) ainsi que des perturbations stochastiques (énergie cinétique). Un membre de contrôle qui n'est pas perturbé est également disponible. Les éléments de l'atmosphère incluent notamment la température, les précipitations, le couvert nuageux, la vitesse et direction des vents, l'humidité et autres. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique est globale. Les données sont disponibles sur une quinzaine de niveaux verticaux sur une grille latitude-longitude uniforme globale avec une résolution horizontale de 0.5 degré (environ 39km). Les prévisions sont exécutées deux fois par jour.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md)  :

* [Données disponibles via l'API / les services web géospatiaux GeoMet-Météo](readme_geps-geomet_fr.md)
* [Données GRIB2 disponibles sur le Datamart du SMC](readme_geps-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche `GEPS.DIAG.12_PRMM.ERGE10` du SGPE provenant de GeoMet du SMC :



<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" style="display: flex; max-width: 85px;" src="https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GEPS.DIAG.12_PRMM.ERGE10&format=image/png&STYLE=REPS_PROB-LINEAR"/>
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

### Métadonnées de découverte

À venir.

## Documentation technique

* [Version actuelle du système global de prévision d'ensemble](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_geps_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_GEPS_fr.svg)
* [Fiche d'information associée au dernier cycle d'innovation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_geps_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système global de prévision d'ensemble (SGPE) est disponible [ici](changelog_geps_fr.md).

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
        js.src = "../../../js/geps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/geps.js";
    }
    head.appendChild(js);
</script>
