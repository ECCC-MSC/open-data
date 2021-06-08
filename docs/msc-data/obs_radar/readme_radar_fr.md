[In English](readme_radar_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Observations radar

# Données et produits des observations radar

Cette page décrit les données et produits des radars canadiens du réseau de 31 sites d’Environnement et Changement climatique Canada qui se concentre dans les régions les plus peuplées du Canada, offrant ainsi une couverture à plus de 95 % des Canadiennes et des Canadiens. La fonction principale du réseau est la détection avancée des précipitations, des orages et des phénomènes météorologiques à grande retombée qui se développent, tout comme de suivre le parcours des précipitations. 

## Accès

### Comment accéder aux données

Les données radar sont disponibles via l'API et les services web GeoMet du SMC ainsi qu'en tant qu'images statiques GIF sur le serveur de données Datamart du SMC :

* [Couches disponibles pour la composite radar nord-américaine via les services web géospatiaux GeoMet-Météo](readme_radar_geomet_fr.md)
* [Imagerie radar en format GIF disponible sur le Datamart du SMC](readme_radarimage-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Ci-après est un exemple de carte interactive configurée pour présenter des couches WMS de la composite radar météo servies par GeoMet du SMC.

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

Non disponibles pour le moment.

## Documentation technique

* [A propos des radars](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/a-propos.html)
* [Remplacement du réseau canadien de radars météorologiques](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/modernisation-reseau.html)
* [Interruption et maintenance du service radar](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/interruption-maintenance-service.html)

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
        js.src = "../../../js/radar_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/radar.js";
    }
    head.appendChild(js);
</script>