[In English](readme_geps_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > SGPE

# Données et Produits du Système global de prévision d'ensemble (SGPE)

Le Système global de prévision d'ensemble (SGPE) procède à des calculs physiques afin de produire des prévisions probabilistes d'éléments de l'atmosphère du jour présent jusqu'à 16 jours dans le futur (jusqu'à 32 jours les jeudis à 00 UTC). Le SGPE génère différentes prévisions (scénarios) pour estimer les incertitudes des prévisions causées par le comportement non-linéaire (chaotique) de l'atmosphère. Les prévisions probabilistes sont basées sur un ensemble de 20 scénarios qui diffèrent par leurs conditions initiales, leur choix des paramétrages physiques ainsi que par des perturbations stochastiques (tendances physiques et énergie cinétique). Un membre de contrôle qui n'est pas perturbé est également fournit. Les éléments de l'atmosphère incluent notamment la température, les précipitations, le couvert nuageux, la vitesse et direction des vents et l'humidité. Ce produit contient les résultats numériques bruts de ces calculs. La couverture géographique est globale. La résolution horizontale du système est de 0.35 degré (environ 39 km à l'équateur), le système compte 45 niveaux pour les prévisions et 81 niveaux pour les analyses. Les prévisions sont exécutées deux fois par jour.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md)  :

* [Données disponibles via l'API / les services web géospatiaux GeoMet-Météo](readme_geps-geomet_fr.md)
* [Données GRIB2 disponibles sur le Datamart du SMC](readme_geps-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche `GEPS.DIAG.12_PRMM.ERGE10` du SGPE provenant de GeoMet du SMC :

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

## Documentation technique

* [Version actuelle du système global de prévision d'ensemble](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_GEPS_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_geps_f.pdf)

## Registre des changements 

La chronologie des changements apportés au Système global de prévision d'ensemble (SGPE) est disponible [dans le registre des changements](changelog_geps_fr.md).

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
        js.src = "../../../js/geps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/geps.js";
    }
    head.appendChild(js);
</script>
