[In English](readme_dcs_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Résultats statistiquement réduits à  l'échelle

# Données et produits des résultats statistiquement réduits à  l'échelle pour des modèles climatiques du CMIP5

Des scénarios climatiques à réduction d’échelle statistique des changements projetés pour les températures et les précipitations, par rapport à la période de référence de 1986 à 2005, sont donnés selon trois scénarios d’émissions, RCP2.6, RCP4.5 et RCP8.5,  à une résolution de 10 km. Les données avec réduction d’échelle statistique s’appuient sur les projections du modèle climatique mondial issues de la phase 5 du projet d’intercomparaison de modèles couplés (CMIP5). La médiane des changements projetés de l’ensemble multimodèles à réduction d’échelle statistique est illustrée.  

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles via les services web géospatiaux GeoMet-Climat](readme_dcs-geomet_fr.md)
* [Données NetCDF disponibles sur le Datamart du SMC](readme_dcs-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [DCS.PR.RCP26.YEAR.2021-2040_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=DCS.PR.RCP26.YEAR.2021-2040_PCTL50) des résultats statistiquement réduits à l'échelle provenant de GeoMet du SMC :

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

* Les [métadonnées des scénarios à échelle statistiquement réduite des changements projetés des températures moyennes sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/958b8357-3690-414d-8bec-d65951041636)
* Les [métadonnées des Scénarios à échelle statistiquement réduite des changements projetés des températures maximales sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/57fee0af-40ec-4aad-89da-6c0d39a6424d)
* Les [métadonnées des Scénarios à échelle statistiquement réduite des changements projetés des températures minimales sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/3156e7bf-6f11-46f7-b70a-51b6d4e3835b)
* Les [métadonnées des Scénarios à échelle statistiquement réduite des changements projetés dans les précipitations  sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/286dd106-b507-472a-9a26-f72dceffb475)
* [Scénarios climatiques mis à l’échelle de manière statistique](https://changements-climatiques.canada.ca/donnees-climatiques/#/donnees-echelle-reduite)

## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_dcs/DCS_Technical_Documentation_fr.pdf)
* [Réduction d'échelle statistique](http://scenarios-climatiques.canada.ca/index.php?page=downscaling)
* [Introduction aux scénarios climatiques](http://scenarios-climatiques.canada.ca/index.php?page=cmip5-intro)
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
        js.src = "../../../js/dcs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/dcs.js";
    }
    head.appendChild(js);
</script>
