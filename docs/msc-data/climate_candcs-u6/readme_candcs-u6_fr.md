[In English](readme_dcs_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > CanDCS-U6

# Données et produits des résultats statistiquement réduits à  l'échelle pour des modèles climatiques du CMIP6

La Division de la recherche climatique (DRC) d’ECCC et le Pacific Climate Impacts Consortium (PCIC) ont déjà produit des scénarios mis à l’échelle statistique et fondés sur des simulations de modèles climatiques qui faisaient partie de la phase 5 du Projet d’intercomparaison de modèles couplés (CMIP5) en 2015. Ces scénarios sont largement utilisés et sont mentionnés dans le Rapport sur le climat changeant du Canada. ECCC et le PCIC ont mis à jour les scénarios à échelle réduite fondés sur la CMIP5 en ajoutant deux nouveaux ensembles de scénarios à échelle réduite fondés sur la prochaine génération de projections climatiques de la phase 6 du Projet d’intercomparaison de modèles couplés (CMIP6). Les projections climatiques du CMIP6 sont fondées à la fois sur des modèles climatiques mondiaux actualisés et sur de nouveaux scénarios d’émissions appelés « trajectoires socioéconomiques partagées » (SSP, pour « Shared Socioeconomic Pathways »).Des ensembles de données mis à l’échelle statistique ont été produits à l’aide de 26 MCM du CMIP6 selon trois scénarios d’émissions différents (c.-à-d. SSP1-2.6, SSP2-4.5 et SSP5-8.5). Le premier de ces ensembles a été produit au moyen des mêmes méthode de réduction d’échelle (BCCAQv2) et données cibles de réduction (NRCANmet) que les scénarios à échelle réduite fondés sur la CMIP5.Les changements projetés sont exprimés sous forme d’anomalies par rapport à la période de référence de 1995 à 2014. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md).


### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.


## Documentation technique

* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_candcs-u6/CMIP6_DCS_Tech_Docs_FR.pdf)
* [Réduction d'échelle statistique](http://scenarios-climatiques.canada.ca/index.php?page=downscaling)


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
        js.src = "../../../js/dcs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/dcs.js";
    }
    head.appendChild(js);
</script>
