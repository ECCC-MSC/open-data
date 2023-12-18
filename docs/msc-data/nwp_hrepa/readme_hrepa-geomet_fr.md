
[In English](readme_hrepa-geomet_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [AHREP](readme_hrepa_fr.md) > AHREP sur GeoMet du SMC

# Données de l'Analyse à Haute Résolution Ensembliste de Précipitation (AHREP) sur GeoMet du SMC

GeoMet du SMC donne accès à plusieurs couches de Système global de l'Analyse à Haute Résolution Ensembliste de Précipitation (AHREP). Les usagers peuvent développer des applications mobiles, créer des cartes interactives en ligne, ainsi que visualiser et animer les données du SMC dans des logiciels de bureau.

## Accès aux services web géospatiaux

Les couches du AHREP sont disponibles sur [GeoMet-Météo par le biais des standards WMS (Web Map Service) et WCS (Web Coverage Service).](../../msc-geomet/readme_fr.md#standards-disponibles)

Exemple de carte interactive présentant la couche Precip-Accum06h-Pct25 du AHREP provenant de GeoMet du SMC :

<div id="map" style="height: 400px; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" src="https://geo.weather.gc.ca/geomet?lang=fr&version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=GEPS.DIAG.12_PRMM.ERGE10&format=image/png&STYLE=REPS_PROB-LINEAR"/>
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


## Utilisation

La page de [l'aperçu de l'utilisation](../../usage/readme_fr.md) présente l'information de base sur l'utilisation de ces services avec des logiciels de bureau, des applications mobiles, les cartes interactives en ligne ainsi que l'accès direct. Veuillez vous référer aux [tutoriels](../../usage/tutorials_fr.md) et à [la documentation technique sur les services web géospatiaux GeoMet du SMC](../../msc-geomet/readme_fr.md#standards-disponibles) pour de l'information détaillée.

### Couches disponibles

Pour avoir la liste des couches AHREP qui sont servies par GeoMet du SMC, consultez le [document WMS GetCapabilities](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&request=GetCapabilities&lang=f).

Quatre couches sont disponibles pour AHREP:

* pr [mm]: Accumulation de précipitation sur une période de 6 heures pour les 25 membres de l'ensemble (disponible dans les fichiers contenant la sous-chaîne Precip-Accum06h dans le nom du fichier), le premier membre correspond au membre contrôle (sans perturbations)
* cfia [sans unité]: Indice de confiance de l'analyse, seulement pour le membre controle de l'ensemble (disponible dans les fichiers contenant la sous-chaîne Precip-Accum06h dans le nom du fichier)
* q025 [mm]: 25ème percentile de l'ensemble des analyses de cumuls 6 heures de précipitation (disponible dans les fichiers contenant la sous-chaîne Precip-Accum06h-Pct25 dans le nom du fichier)
* q075[mm]: 75ème percentile de l'ensemble des analyses de cumuls 6 heures de précipitation (disponible dans les fichiers contenant la sous-chaîne Precip-Accum06h-Pct75 dans le nom du fichier)

Les logiciels SIG de bureau tels que QGIS permettent également de [naviguer dans le document WMS GetCapabilities sous la forme d'une arborescence de couches](../../usage/tutorial_WMS_QGIS_fr.md).


### Conseils d'utilisation

Récupération de la liste des derniers pas de temps disponibles :

* Les utilisateurs peuvent ajouter le paramètre `layer` à une requête WMS GetCapabilities afin de pointer à une couche spécifique et obtenir une réponse XML plus simple avec les dimensions temporelles à jour (voir les balises `<Dimension>`).
    - Exemple pour la couche 20220214T06Z_MSC_HREPA_Precip-Accum06h-Pct25_Sfc_RLatLon0.0225.nc - 25eme percentile de précipitations issue de l'ensemble à 25 membres [mm] : https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=20220214T06Z_MSC_HREPA_Precip-Accum06h-Pct25_Sfc_RLatLon0.0225.nc
* Davantage d'information est disponible dans la section sur [la spécification du temps avec les services WMS](../../../msc-geomet/wms_fr#specification-du-temps).

Styles WMS :

* En plus du style WMS par défaut, plusieurs styles WMS alternatifs avec des échelles de couleurs différentes sont disponibles. La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities
* Par ailleurs, les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard *Styled Layer Descriptor* (SLD). Veuillez vous référer à la [documentation technique sur le SLD](../../../msc-geomet/wms_fr#specification-des-styles).

Légendes :

* Les légendes sont disponibles pour tous les styles WMS. Les détails sont disponibles dans la [documentation technique des légendes WMS](../../../msc-geomet/wms_fr#wms-getlegendgraphic).
* Exemple d'une requête pour récupérer une légende : 


## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) afin d'être informés des améliorations et changements aux services GeoMet du SMC.

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
        js.src = "../../../js/geps_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/geps.js";
    }
    head.appendChild(js);
</script>