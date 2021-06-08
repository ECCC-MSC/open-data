[In English](readme_radar_geomet_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Radar](readme_radar_fr.md) > Données radar sur GeoMet du SMC

# Données radar météo disponibles sur GeoMet du SMC

GeoMet du SMC donne accès à plusieurs couches de la populaire composite radar météo nord-américaine. Les usagers peuvent développer des applications mobiles, créer des cartes interactives en-ligne, ainsi que visualiser et animer les données du SMC dans des logiciels de bureau.


## Accès aux services web géospatiaux

Les couches radar météo sont [disponibles sur GeoMet-Météo par le biais du standard Web Map Service (WMS)](../../msc-geomet/readme_fr.md).

Exemple de carte interactive présentant des couches WMS de la composite radar météo provenant de GeoMet du SMC :

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="play" class="btn btn-primary btn-sm" type="button"><i class="fa fa-play" style="padding: 0rem 1rem"></i></button>
  <button id="pause" class="btn btn-primary btn-sm" type="button"><i class="fa fa-pause" style="padding: 0rem 1rem"></i></button>
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
  <span id="info" style="padding-left: 0.5rem;"></span>
</div>
Les couches de la composite radar météo nord-américaine de GeoMet du SMC peuvent être vues en action dans MétéoCAN, [l'application mobile officielle d'ECCC](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/meteocan.html).


## Utilisation

La page de [l'aperçu de l'utilisation](../../usage/readme_fr.md) présente l'information de base sur l'utilisation de ces services avec des logiciels de bureau, des applications mobiles, les cartes interactives en ligne ainsi que l'accès direct. Veuillez vous référer aux [tutoriels et à la documentation technique sur les services web géospatiaux GeoMet du SMC](../../msc-geomet/readme_fr.md) pour de l'information détaillée. Voir également la [page d'accueil des données radar météo](readme_radar_fr.md) qui pointe vers de l'information additionnelle sur les radars météo.

### Couches disponibles

Les couches radar météo sont mises à jour toutes les 10 minutes. Les 3 dernières heures de données sont disponibles sur GeoMet du SMC.

Composite radar météo nord-américaine à 1 km :

* Taux de précipitation radar (Pluie) (1 km) [mm/hr], ID: `RADAR_1KM_RRAI`
* Taux de précipitation radar (Neige) (1 km) [cm/hr], ID: `RADAR_1KM_RSNO`
* Couches de la couverture radar dynamique correspondantes :
    * Couverture pour la pluie, ID: `RADAR_COVERAGE_RRAI`. ID pour le style WMS inversé : `RADAR_COVERAGE_RRAI.INV`
    * Couverture pour la neige, ID: `RADAR_COVERAGE_RSNO`. ID pour le style WMS inversé: `RADAR_COVERAGE_RSNO.INV`

### Conseils d'utilisation

Récupération de la liste des derniers pas de temps disponibles :

* Les utilisateurs peuvent ajouter le paramètre `layer` à une requête WMS GetCapabilities afin de pointer à une couche spécifique et obtenir une réponse XML plus simple avec les dimensions temporelles à jour. Exemple pour la nouvelle couche de neige radar à 1km : [https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO](https://geo.weather.gc.ca/geomet?lang=fr&service=WMS&version=1.3.0&request=GetCapabilities&layer=RADAR_1KM_RSNO)
* Davantage d'informations sont disponibles dans la section sur [la spécification du temps avec les services WMS](../../../msc-geomet/web-services_fr#specification-du-temps)

Styles WMS :

* En plus du style WMS par défaut, plusieurs styles WMS alternatifs avec des échelles de couleurs différentes sont disponibles. La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities
* Par ailleurs, les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard Styled Layer Descriptor (SLD). Veuillez vous référer à la [documentation technique sur le SLD](../../../msc-geomet/web-services_fr#specification-des-styles)

Légendes :

* Les légendes sont disponibles pour tous les styles WMS. Les détails sont disponibles dans la [documentation technique des légendes WMS](../../../msc-geomet/web-services_fr#wms-getlegendgraphic)
* Exemple d'une requête pour récupérer une légende : `https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=RADARURPPRECIPR14-LINEAR`

![La légende WMS RADARURPPRECIPR14-LINEAR](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=RADAR_1KM_RRAI&format=image/png&STYLE=RADARURPPRECIPR14-LINEAR)


## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) afin d'être informés des améliorations et changements aux services GeoMet du SMC.


<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.css" integrity="sha256-rQq4Fxpq3LlPQ8yP11i6Z2lAo82b6ACDgd35CKyNEBw=" crossorigin="anonymous" />
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/openlayers/4.6.5/ol.js" integrity="sha256-77IKwU93jwIX7zmgEBfYGHcmeO0Fx2MoWB/ooh9QkBA=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
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