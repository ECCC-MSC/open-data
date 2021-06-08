[In English](readme_ahccd-geomet_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [DCCAH](readme_ahccd_fr.md) > DCCAH sur GeoMet du SMC

# Données du DCCAH disponibles sur GeoMet du SMC

GeoMet du SMC donne accès à plusieurs données et produits des Données climatiques canadiennes ajustées et homogénéisées (DCCAH). Les usagers peuvent développer des applications mobiles, créer des cartes interactives en-ligne, ainsi que visualiser et animer les données climatiques du SMC dans des logiciels de bureau.

## Accès aux services web géospatiaux

Les couches du DCCAH sont [disponibles sur GeoMet-Météo par le biais des standards WMS (Web Map Service) et WCS (Web Coverage Service)](../../msc-geomet/readme_fr.md).

Exemple de carte interactive présentant la couche [AHCCD.STATIONS](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=AHCCD.STATIONS) du DCCAH provenant de GeoMet du SMC :

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

## Utilisation

La page de [l'aperçu de l'utilisation](../../usage/readme_fr.md) présente l'information de base sur l'utilisation de ces services avec des logiciels de bureau, des applications mobiles, les cartes interactives en ligne ainsi que l'accès direct. Veuillez vous référer aux [tutoriels et à la documentation technique sur les services web géospatiaux GeoMet du SMC](../../msc-geomet/web-services_fr.md) pour de l'information détaillée.

### Couches disponibles

Pour savoir quelles couches DCCAH sont servies par GeoMet du SMC, consultez le [document WMS GetCapabilities](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=f).

Les logiciels SIG de bureau tels que QGIS permettent également de [naviguer dans le document WMS GetCapabilities sous la forme d'une arborescence de couches](../../usage/tutorial_WMS_QGIS_fr.md).

### Conseils d'utilisation

Récupération de la liste des derniers pas de temps disponibles :

* Les utilisateurs peuvent ajouter le paramètre `layer` à une requête WMS GetCapabilities afin de pointer à une couche spécifique et obtenir une réponse XML plus simple avec les dimensions temporelles à jour (voir les balises `<Dimension>`). Exemple : [https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=AHCCD.STATIONS](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&layer=AHCCD.STATIONS).
* Davantage d'information est disponible dans la section sur [la spécification du temps avec les services WMS](../../../msc-geomet/web-services_fr#specification-du-temps).

Styles WMS :

* En plus du style WMS par défaut, plusieurs styles WMS alternatifs avec des échelles de couleurs différentes sont disponibles. La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities.
* Par ailleurs, les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard Styled Layer Descriptor (SLD). Veuillez vous référer à la [documentation technique sur le SLD](../../../msc-geomet/web-services_fr#specification-des-styles).

Légendes :

* Les légendes sont disponibles pour tous les styles WMS. Les détails sont disponibles dans la [documentation technique des légendes WMS](../../../msc-geomet/web-services_fr#wms-getlegendgraphic).
* Exemple d'une requête pour récupérer une légende : [https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=AHCCD.STATIONS&format=image/png&STYLE=default](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=AHCCD.STATIONS&format=image/png&STYLE=default).

![La légende default pour la couche AHCCD.STATIONS](https://geo.weather.gc.ca/geomet-climate?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=AHCCD.STATIONS&format=image/png&STYLE=default)


## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://weather.gc.ca/mainmenu/contact_us_e.html).


## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) afin d'être informés des améliorations et changements aux services GeoMet du SMC.

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
