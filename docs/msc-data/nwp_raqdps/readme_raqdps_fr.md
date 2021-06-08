[In English](readme_raqdps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SRPDQA

# Données et Produits du Système régional de prévision déterministe de la qualité de l'air 

Le Système régional de prévision déterministe de la qualité de l'air (SRPDQA) procède à des calculs physiques et chimiques afin de produire des prévisions déterministes de la concentration d'espèces chimiques d'intérêt pour la qualité de l'air. Ces constituants chimiques incluent les gaz O3, SO2, NO et NO2, s'ajoutant aux particules fines PM2.5 (diamètre de 2.5 micromètres ou moins) et aux particules grossières (diamètre de 10 micromètres ou moins). Les prévisions sont disponibles pour le présent jusqu'à 72 heures dans le futur. La couverture géographique est le domaine nord américain. Les données sont disponibles à une résolution spatiale horizontale de 10 km. Le système comporte 84 niveaux verticaux et les données sont disponibles seulement au niveau de la surface. Les prévisions sont exécutées deux fois par jour. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les API / services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_raqdps-geomet_fr.md)
* [Données GRIB2 disponibles sur le Datamart du SMC](readme_raqdps-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche `RAQDPS.EATM_PM2.5` du SRPDQA provenant de GeoMet du SMC :
<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="play" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-pause" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <span id="info" style="padding-left: 0.5rem;"></span>
</div>

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

À venir.

## Produits

* [Cartes des prévisions à 48h](https://meteo.gc.ca/aqfm/index_f.html) pour l'ozone troposphérique près de la surface et aux altitudes de 50 mètres et de 500 mètres ainsi que pour les PM2.5 et les PM10 près de la surface sont disponibles ci-dessous. 
* [Cartes à 4 panneaux](https://meteo.gc.ca/aqfm/index_f.html) permettent de voir simultanément les prévisions pour les PM2.5, les PM10 et l'ozone près de la surface et pour l'ozone à 500 mètres.

## Documentation technique

* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdps_f.pdf) 

## Registre des changements 

La chronologie des changements apportés aux systèmes opérationnels est disponible [dans le registre des changements](changelog_raqdps_fr.md).

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.css" integrity="sha256-rQq4Fxpq3LlPQ8yP11i6Z2lAo82b6ACDgd35CKyNEBw=" crossorigin="anonymous" />
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.js" integrity="sha256-77IKwU93jwIX7zmgEBfYGHcmeO0Fx2MoWB/ooh9QkBA=" crossorigin="anonymous"></script>
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
        js.src = "../../../js/raqdps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/raqdps.js";
    }
    head.appendChild(js);
</script>
