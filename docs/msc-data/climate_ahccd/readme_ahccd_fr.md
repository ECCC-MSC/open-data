[In English](readme_ahccd_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > DCCAH

# Données et produits des Données Climatiques Canadiennes Ajustées et Homogénéisées (DCCAH) 

Les données se composent de moyennes mensuelles, saisonnières et annuelles de température de l’air de surface quotidienne maximale, minimale et moyenne homogénéisée pour plus que 330 emplacements au Canada; de totaux mensuels, saisonniers et annuels de chute de pluie, de neige et de précipitation totale quotidienne ajustée pour plus que 460 emplacements; moyennes homogénéisées mensuelles, saisonnières et annuelles de la vitesse du vent horaire pour plus de 110 emplacements; moyennes mensuelles, saisonnières et annuelles de pression horaire au niveau de la station et au niveau de la mer ajustée pour plus que 630 emplacements. Les données sont fournies pour la période complète d’observation. Veuillez consulter les documents ci-dessous pour obtenir de l’information sur les procédures utilisées pour l’homogénéisation et les ajustements. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles via les services web géospatiaux GeoMet-Climat](readme_ahccd-geomet_fr.md)
* [Données GeoJSON disponibles sur le Datamart du SMC](readme_ahccd-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [AHCCD.STATIONS](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=AHCCD.STATIONS) du DCCAH provenant de GeoMet du SMC :

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>
### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

Les [métadonnées des Données Climatiques Canadiennes Ajustées et Homogénéisées sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/9c4ebc00-3ea4-4fe0-8bf2-66cfe1cddd1d)

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_ahccd/AHCCD_Technical_Documentation_fr.pdf)
* Ces données sont aussi disponibles via le [Centre canadien des services climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques/a-propos.html)


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
        js.src = "../../../js/ahccd_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/ahccd.js";
    }
    head.appendChild(js);
</script>
