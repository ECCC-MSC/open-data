[In English](readme_rdaqa_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > ARDQA

# Données et Produits de l'Analyse régionale déterministe de la qualité de l'air 

L’Analyse régionale déterministe de qualité de l’air (ARDQA) est une analyse objective des polluants de surface qui combine les prévisions numériques du Système régional de prévision déterministe de la qualité de l’air (SRPDQA) avec les observations horaires des différents réseaux de surveillance en Amérique du Nord incluant les réseaux de mesure canadiens opérés par les provinces, territoires et certaines villes en plus des différents réseaux américains dans le contexte du programme AIRNow administré par US/EPA (US Environmental Protection Agency). L'analyse ARDQA fournit la meilleure description des conditions courantes de la qualité de l’air et est utilisée pour informer le public, les météorologistes des différents bureaux de prévision d’Environnement et Changement climatique Canada, Santé Canada et d’autres usagers, sur la distribution des polluants atmosphériques près du sol et sur la performance des modèles de prévision.

Chaque heure, un produit préliminaire est disponible environ une heure après le temps de mesure des observations alors que des produits final et Firework sont disponibles environ deux heures après le temps de mesure. Les produits préliminaires et final contiennent l’analyse des constituants chimiques O3, SO2, NO, NO2, PM2.5 (particules fines de diamètre 2.5 micromètres ou moins) et PM10 (particules grossières de diamètre 10 micromètres ou moins), alors que le produit Firework contient l’analyse de PM2.5 et PM10.

## Accès

### Comment accéder aux données

Ces données sont disponibles sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les [services web GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données GRIB2 disponibles sur le Datamart du SMC](readme_rdaqa-datamart_fr.md)
* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_rdaqa-geomet_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [RDAQA_10km_PM10](https://geo.meteo.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=RDAQA_10km_PM10) du ARDQA provenant de GeoMet du SMC :



<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" style="display: flex; max-width: 85px;" src="https://geo.meteo.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RDAQA_10km_PM10&format=image/png&STYLE="/>
  </div>
</div>
</div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;cursor: pointer;"></span>
</div>



### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées de découverte

Les [métadonnées de l'Analyse régionale déterministe de la qualité de l'air sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/1f11ed9f-b13d-497b-853a-997b991195a1)


## Documentation technique

* [Version actuelle du Système régional de prévision déterministe de la qualité de l'air](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDAQA_f.pdf) 
* [Note technique](http://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdaqa_f.pdf)
* [Diagramme de dépendances](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwep-dependency-diagrams/system_RDAQA_FW_fr.svg) 
* [Fiche d'information associée au dernier cycle d'innovation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/fact_sheets/factsheet_rdaqa_f.pdf)

## Registre des changements 

La chronologie des changements apportés aux systèmes opérationnels est disponible [dans le registre des changements](changelog_rdaqa_fr.md).



<style>
  #legend-img {
    margin: 0px;
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
        js.src = "../../../js/rdaqa_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/rdaqa.js";
    }
    head.appendChild(js);
</script>