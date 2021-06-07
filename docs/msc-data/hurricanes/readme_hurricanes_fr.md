[In English](readme_hurricanes_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Ouragans

# Données et produits de prévision des ouragans

Les trajectoires d'ouragans et la zone de réaction aux ouragans sont émises par le [Centre canadien de prévision des ouragans](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-faits-ouragans/produits.html), dans le cadre des prévisions régulières lors de la saison des ouragans.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [La zone de réaction aux ouragans et les trajectoires sont disponibles sur l'API de GeoMet-Météo](readme_hurricanes_geomet_fr.md)
* [Les trajectoires sont disponibles sur le Datamart du SMC](readme_hurricanes-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

Exemple de carte interactive présentant les couches Web Map Service (WMS) de zone de réaction aux ouragans et ouragans actifs, en plus de couches d'avertissements météo (beta) et de précipitation, provenant de GeoMet du SMC :

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

Non disponible.

## Produits

* [Cartes des trajectoires d'ouragans](https://meteo.gc.ca/hurricane/track_f.html)
* [Centre canadien de prévisions des ouragans : prévisions et produits](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-faits-ouragans/produits.html)

## Documentation technique

* [Centre canadien des ouragans](https://www.ec.gc.ca/ouragans-hurricanes/)


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
        js.src = "../../../js/hurricane_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/hurricane.js";
    }
    head.appendChild(js);
</script>
