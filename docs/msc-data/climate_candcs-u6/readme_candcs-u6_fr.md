[In English](readme_candcs-u6_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > CanDCS-U6

# Données et produits de scénarios climatiques mis à l’échelle statistique des modèles climatiques mondiaux du CMIP6 (CanDCS-U6) 

La Division de la recherche climatique (DRC) d’Environnement et Changement climatique Canada (ECCC) et le Pacific Climate Impacts Consortium (PCIC) ont déjà produit des scénarios mis à l’échelle statistique et fondés sur des simulations de modèles climatiques qui faisaient partie de la phase 5 du Projet d’intercomparaison de modèles couplés (CMIP5) en 2015. ECCC et le PCIC ont mis à jour les scénarios à échelle réduite fondés sur la CMIP5 en ajoutant deux nouveaux ensembles de scénarios à échelle réduite fondés sur la prochaine génération de projections climatiques de la phase 6 du Projet d’intercomparaison de modèles couplés (CMIP6). Les scénarios appelés scénarios climatiques canadiens à échelle réduite – méthode univariée de la CMIP6 (CanDCS-U6) (« Canadian Downscaled Climate Scenarios–Univariate method from CMIP6 ») et scénarios climatiques canadiens à échelle réduite – méthode multivariée de la CMIP6 (CanDCS-M6) (« Canadian Downscaled Climate Scenarios–Multivariate method from CMIP6 »).

Les projections climatiques du CMIP6 sont fondées à la fois sur des modèles climatiques mondiaux actualisés et sur de nouveaux scénarios d’émissions appelés « trajectoires socioéconomiques partagées » (SSP, pour « Shared Socioeconomic Pathways »). Des ensembles de données mis à l’échelle statistique ont été produits à l’aide de 26 modèle climatique mondial (MCM) du CMIP6 selon trois scénarios d’émissions différents (c.-à-d. SSP1-2.6, SSP2-4.5 et SSP5-8.5). La procédure de correction des biais et analogues construits avec cartographie des quantiles, version 2 (BCCAQv2) a été utilisée pour l’ensemble CanDCS-U6, tandis que la méthode multivariée de correction des biais à N dimensions (MBCn) a été utilisée pour l’ensemble CanDCS-M6. L’ensemble CanDCS-U6 a été produit au moyen des mêmes données cibles de réduction (NRCANmet) que les scénarios à échelle réduite fondés sur la CMIP5, tandis l’ensemble CanDCS-M6 utilise un nouvel ensemble cible (mêlant les ensembles ANUSPLIN et PNWNAmet).

Les résultats des modèles individuels mis à l’échelle statistique peuvent être téléchargés. Les indices climatiques mis à échelle de manière statistique réduite sont disponibles partout au Canada à une résolution spatiale de grille de 10 km pour la période antérieure 1950 2014 et la période 2015 2100 suivant chacun des trois scénarios d’émissions.

Remarque : les changements projetés par les produits mis à l’échelle sur le plan statistique ne sont pas nécessairement plus crédibles que ceux des résultats du modèle climatique sous-jacent. Souvent, surtout pour les indices fondés sur des seuils absolus, l’écart des projections fondées sur des données mises à l’échelle est plus faible en raison de l’élimination des biais du modèle. Or ce n’est pas le cas pour tous les indices. La mise à l’échelle de la résolution du MCM pour qu’elle soit haute, ce qui est nécessaire pour l’évaluation des répercussions, augmente le niveau de détail spatial et de variabilité temporelle pour mieux correspondre aux observations. Étant donné que ces ajustements dépendent du MCM, les indices qui en résultent pourraient avoir un écart plus grand lorsqu’ils sont calculés à partir de données mises à l’échelle comparativement à ceux qui sont directement calculés à partir des résultats du MCM. Dans ce dernier cas, ce n’est pas la procédure de mise à l’échelle qui rend la projection plus incertaine, il s’agit plutôt d’une plus grande variabilité associée à une échelle spatiale plus haute.

Les ensembles de données de modèles individuels et tous les produits dérivés connexes sont assujettis aux conditions d'utilisation (https://pcmdi.llnl.gov/CMIP6/TermsOfUse/TermsOfUse6-1.html) de l'organisation source.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles sur les services web géospatiaux GeoMet-Climat](readme_candcs-u6-geomet_fr.md)
* [Données NetCDF disponibles sur le Datamart du SMC](readme_candcs-u6-datamart_fr.md)

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

* La [métadonnée des scénarios climatiques mis à l’échelle statistique des modèles climatiques mondiaux du CMIP6 est accessible sur le portail du gouvernement ouvert](https://catalogue.ec.gc.ca/geonetwork/srv/fre/catalog.search#/metadata/f73d6939-912a-4add-a291-c233fc5d1946)

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_candcsu6/CanDCS-U6_Technical_Documentation_fr.pdf)
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
