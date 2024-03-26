[In English](readme_lightning-geomet_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Densité de foudre](readme_lightning_fr.md) > Densité de foudre sur GeoMet du SMC

# Données des densité de foudre disponibles sur GeoMet du SMC

GeoMet du SMC donne accès à la couche des données de foudre. Les usagers peuvent développer des applications mobiles, créer des cartes interactives en-ligne, ainsi que visualiser et animer les données du SMC dans des logiciels de bureau.

## Accès aux services web géospatiaux

La couche des alertes météo est [disponible sur GeoMet-Météo par le biais du standard WMS (Web Map Service)](../../msc-geomet/wms_fr.md).

## Utilisation

La page de [l'aperçu de l'utilisation](../../usage/readme_fr.md) présente l'information de base sur l'utilisation de ces services avec des logiciels de bureau, des applications mobiles, les cartes interactives en ligne ainsi que l'accès direct. Veuillez vous référer aux [tutoriels](../../usage/tutorials_fr.md) et à [la documentation technique sur les services web géospatiaux GeoMet du SMC](../../msc-geomet/readme_fr.md#standards-disponibles) pour de l'information détaillée. Voir également la [page d'accueil des données de densité de foudre](readme_lightning_fr.md) qui pointe vers de l'information additionnelle sur les données de densité de foudre.

### Couches disponibles

Il y a une seule couche principale de densité de foudre la surveillance de la foudre dans la majeure partie du Canada.

### Conseils d'utilisation

Styles WMS :

* La liste des styles WMS est fournie dans la réponse d'une requête WMS GetCapabilities ([exemple d'une requête WMS GetCapabilites](https://geo.weather.gc.ca/geomet?service=WMS&version=1.3.0&lang=fr&request=GetCapabilities&layer=Lightning_2.5km_Density))
* Les utilisateurs peuvent visualiser les couches avec leurs propres styles en utilisant le standard Styled Layer Descriptor (SLD), veuillez vous référer à la [documentation technique sur le SLD](../../../msc-geomet/wms_fr#specification-des-styles).

Légendes :

* Les légendes sont disponibles pour tous les styles WMS. Les détails sont disponibles dans la [documentation technique des légendes WMS](../../../msc-geomet/wms_fr#wms-getlegendgraphic).
* Exemple d'une requête pour récupérer une légende : `https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Lightning_2.5km_Density&format=image/png&STYLE=Lightning`

![La légende WMS ALERTES](https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=Lightning_2.5km_Density&format=image/png&STYLE=Lightning)

## Support

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Liste d'information

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) afin d'être informés des améliorations et changements aux services GeoMet du SMC.


<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
