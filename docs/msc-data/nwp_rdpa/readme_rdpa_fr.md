[In English](readme_rdpa_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > ARDP

# Données et produits de l'Analyse régionale déterministe de précipitation

L'Analyse régionale déterministe de précipitation (ARPD) produit une estimation optimale de la quantité de précipitation qui est survenue au cours de périodes passées récentes de 6h ou 24h. Cet estimé intègre des relevés provenant de capteurs de précipitation, de radar météo, d'imagerie satellitaire et de modèles de prévision numérique du temps. La couverture géographique est l'Amérique du Nord (Canada, États-Unis et le Mexique). Les données sont disponibles à une résolution spatiale horizontale de 10 km. Les données ne sont disponibles qu'au niveau de la surface. Les données d'analyse sont rendues disponibles quatre fois par jour pour les intervalles de 6h et deux fois par jour pour l'intervalle de 24h. Un estimé préliminaire est disponible environ 1h après la fin de la période d'accumulation, et révisé 7h plus tard afin d'assimiler les pluviomètres dont les données furent disponibles tardivement.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) et les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données courantes et d'archives disponibles sur les services web géospatiaux GeoMet-Météo](readme_rdpa-geomet_fr.md)
* [Données courantes et d'archives disponibles sur les services web géospatiaux GeoMet-OGC-API](https://api.meteo.gc.ca/) :
    * [ARPD - Accumulation de 24 heures](https://api.meteo.gc.ca/collections/weather:rdpa:10km:24f)
    * [ARPD - Accumulation de 6 heures](https://api.meteo.gc.ca/collections/weather:rdpa:10km:6f)
    * [ARPD - Accumulation de 24 heures (préliminaire)](https://api.meteo.gc.ca/collections/weather:rdpa:10km:24p)
    * [ARPD - Accumulation de 6 heures (préliminaire)](https://api.meteo.gc.ca/collections/weather:rdpa:10km:6p)
    * [ARPD - Accumulation de 24 heures à 15 km](https://api.meteo.gc.ca/collections/weather:rdpa:15km:24f)
    * [ARPD - Accumulation de 6 heures à 15 km](https://api.meteo.gc.ca/collections/weather:rdpa:15km:6f)
* [Données courantes GRIB2 disponibles sur le Datamart du SMC](readme_rdpa-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive configurée pour afficher la quantité de précipitations [mm] au cours des dernières 24h en utilisant une couche WMS de l'Analyse régionale déterministe de précipitation (ARDP) provenant de GeoMet du SMC :

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="fast-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-backward" style="padding: 0rem 1rem"></i></button>
  <button id="step-backward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-backward" style="padding: 0rem 1rem"></i></button>
  <button id="play-pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="step-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-step-forward" style="padding: 0rem 1rem"></i></button>
  <button id="fast-forward" class="btn btn-primary btn-sm" type="button"><i class="fa fa-fast-forward" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <a id="image-download" download="msc-geomet_web-map_export.png"></a>
  <span id="info" style="padding-left: 0.5rem;"></span>
</div>


### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées

Les [métadonnées de l'Analyse régionale déterministe de précipitation sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/fdd3446a-dc20-5bad-9755-0855e3ec9b19).

## Produits

Liste et liens vers les produits disponibles pour ce jeu de données :

### Cartes d'analyse

Des [cartes d'analyses](https://meteo.gc.ca/analysis/index_f.html#APCP) de cumuls 6 heures valides aux heures synoptiques (00, 06, 12 et 18 UTC) et une analyse 24 heures valide à 12 UTC sont disponibles pour l'ouest et l'est du Canada ainsi que pour le pays en entier.

## Documentation technique

* [Version actuelle de l'Analyse régionale déterministe de précipitation](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDPA_f.pdf)
* [Note technique](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/technote_capa_rdpa_f.pdf)

## Registre des changements

La chronologie des changements apportés à l'Analyse régionale déterministe de précipitation (ARPD) est disponible [ici](changelog_rdpa_fr.md).

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
        js.src = "../../../js/rdpa_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/rdpa.js";
    }
    head.appendChild(js);
</script>
