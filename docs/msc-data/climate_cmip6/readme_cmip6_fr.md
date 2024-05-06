[In English](readme_cmip6_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > CMIP6

# Données et produits de scénarios climatiques, basés sur un ensemble de projections de modèles climatiques globaux de la phase 6 du projet d’intercomparaison de modèles couplés (CMIP6) 

Des ensembles multimodèles pour une série de variables basées sur les projections des modèles climatiques mondiaux (MCM) de la phase 6 du Projet d’intercomparaison des modèles couplés (CMIP6) sont disponibles pour 1850 à 2100 sur une grille mondiale commune de 1 x 1 degré.

Les projections climatiques varient entre les MCM en raison des différences dans la représentation et l’approximation des systèmes et des processus terrestres, ainsi que de la variabilité naturelle et de l’incertitude concernant les futurs facteurs climatiques. Ainsi, aucun modèle climatique n’est meilleur que les autres. À la place, l’utilisation des résultats d’un ensemble de modèles (p. ex. en utilisant la moyenne) constitue une pratique exemplaire puisqu’un ensemble tient compte de l’incertitude dans les projections des modèles et offre des projections climatiques plus fiables.

Le site Données et scénarios climatiques canadiens (DSCC) offre quatre types de produits basés sur les ensembles multimodèles du CMIP6 : des ensembles de données et des graphiques de séries chronologiques, des cartes et des ensembles de données connexes, des ensembles de données tabulaires et des ensembles de données maillées à l’échelle mondiale. Des ensembles mensuels, saisonniers et annuels sont disponibles pour un maximum de six profils socioéconomiques partagés (SSP) [SSP1 1.9, SSP1 2.6, SSP2 4.5, SSP3 7.0, SSP4 6.0 et SSP5 8. 5], quatre périodes futures (court terme [2021-2040], moyen terme [2041-2060 et 2061-2080], fin du siècle [2081-2100]) et un maximum de cinq percentiles (5e, 25e, 50e [médiane], 75e et 95e) de la distribution de l’ensemble du CMIP6.

Le nombre de modèles dans chaque ensemble diffère selon la disponibilité des modèles pour chaque SSP et variable; consultez la liste des modèles pour plus de détails sur les modèles inclus dans chaque ensemble. La majorité des produits indiquent les changements prévus sous forme d’anomalies selon une période de référence historique (1995 à 2014). Les produits fournis comprennent des ensembles de données et des graphiques à l’échelle mondiale, nationale, provinciale et territoriale. Pour de plus amples renseignements sur les ensembles multimodèles du CMIP6, veuillez consulter la documentation technique.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles sur les services web géospatiaux GeoMet-Climat](readme_cmip6-geomet_fr.md)
* [Données NetCDF disponibles sur le Datamart du SMC](readme_cmip6-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [CMIP6-SSP585_AirTempAnomaly-Pct50_2081-2100_P0Y](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=CMIP6-SSP585_AirTempAnomaly-Pct50_2081-2100_P0Y) du CMIP6 provenant de GeoMet du SMC :

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet-climate?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=CMIP6-SSP585_AirTempAnomaly-Pct50_2081-2100_P0Y&format=image/png&STYLE=TEMP-ANOMALIES"/>
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
### Métadonnées

* La [métadonnée sur les ensembles multimodèles CMIP6 est accessible sur le portail du gouvernement ouvert](https://catalogue.ec.gc.ca/geonetwork/srv/fre/catalog.search#/metadata/7e7337b7-d36c-4486-a8df-16609a6b99bd)

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_cmip6/CMIP6_Technical_Documentation_fr.pdf)
* [Informations sur les profils représentatifs d’évolution de concentration](http://scenarios-climatiques.canada.ca/index.php?page=scen-rcp)
* [Introduction aux scénarios climatiques](http://scenarios-climatiques.canada.ca/index.php?page=cmip6-scenarios)
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
        js.src = "../../../js/cmip6_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/cmip6.js";
    }
    head.appendChild(js);
</script>
