[In English](readme_raqdps-fw_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SRPDQA-FW

# Données et Produits du Système régional de prévision déterministe de la qualité de l'air FireWork

La fumée des feux de forêt et de broussailles peut constituer une source importante de pollution de l’air pour les Canadiens. Les particules fines présentes dans la fumée peuvent représenter un risque grave pour la santé, en particulier pour les enfants, les personnes âgées et les gens souffrant de maladies cardiaques ou pulmonaires. Comme la fumée peut être transportée par le vent sur des milliers de kilomètres, des endroits éloignés peuvent être presque aussi durement touchés que les régions près de l’incendie. Afin d’aider les Canadiens à mieux se préparer, des cartes de prévisions sur la fumée des feux de forêt sont accessibles par le biais du système FireWork du gouvernement du Canada. FireWork est un système de prévision de la qualité de l’air indiquant comment la fumée des feux de forêt devrait traverser l’Amérique du Nord pendant les 72 prochaines heures.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) et sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_raqdps-fw-geomet_fr.md)
* [Données GRIB2 disponibles sur le Datamart du SMC](readme_raqdps-fw-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche `RAQDPS-FW.EATM_PM2.5-DIFF` du SRPDQA-FW provenant de GeoMet du SMC :

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

* [Cartes des prévisions quotidiennes sur la fumée](https://meteo.gc.ca/firework/index_f.html)

## Documentation technique

* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_raqdpsfw_f.pdf) 

## Registre des changements 

La chronologie des changements apportés aux systèmes opérationnels est disponible [le registre des changements](changelog_raqdps-fw_fr.md).

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
        js.src = "../../../js/raqdps-fw_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/raqdps-fw.js";
    }
    head.appendChild(js);
</script>
