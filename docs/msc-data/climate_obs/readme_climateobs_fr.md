[In English](readme_climateobs_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Données climatiques (normales, données quotidiennes, sommaires mensuels)

# Données et produits données climatiques (normales, données quotidiennes, sommaires mensuels)

__Normales climatiques__

Les normales et moyennes climatiques sont utilisées pour résumer ou décrire les conditions climatiques moyennes d'un endroit particulier. À la fin de chaque décennie, Environnement et changements climatiques Canada met à jour ses normales climatiques pour autant d'endroits et autant de caractéristiques climatiques que possible. Les normales, moyennes et extrêmes climatiques présentées ici sont basées sur des stations climatiques canadiennes ayant au moins 15 ans de données entre 1981 et 2010.

__Données quotidiennes__

Les observations climatiques quotidiennes proviennent de deux sources de données. Les premières sont des stations climatiques quotidiennes produisant une ou deux observations par jour de température, de précipitations. Les deuxièmes sont des stations horaires qui produisent généralement plus d'éléments météorologiques, comme le vent ou la neige au sol. Seul un sous-ensemble des stations totales est affiché en raison de limitations de taille. Les critères de sélection des stations sont énumérés ci-dessous. Les priorités d'inclusion sont les suivantes : (1) La station est actuellement opérationnelle, (2) Stations avec de longues périodes d'enregistrement, (3) Stations qui sont co-localisées avec les catégories ci-dessus et complètent la période d'enregistrement.

__Données mensuelles__

Un sommaire transcanadien des moyennes et des extrêmes pour le mois, y compris les précipitations totales, les températures maximales et minimales et les degrés-jours.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles via l'API / les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) ainsi que sur le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md):

* [Données disponibles via les services web géospatiaux GeoMet-Climat](readme_climateobs-geomet_fr.md)
* [Données CSV disponibles sur le Datamart du SMC](readme_climateobs-datamart_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. Exemple de carte interactive présentant la couche [DCS.TX.RCP85.YEAR.2081-2100_PCTL50](https://geo.weather.gc.ca/geomet-climate?service=WMS&version=1.3.0&request=GetCapabilities&lang=fr&layer=DCS.TX.RCP85.YEAR.2081-2100_PCTL50) des observations historiques provenant de GeoMet du SMC :

<div id="map" style="height: 400px;"></div>
<div id="controller" role="group" aria-label="Animation controls" style="background: #ececec; padding: 0.5rem;">
  <button id="exportmap" class="btn btn-primary btn-sm" type="button"><i class="fa fa-download" style="padding: 0rem 1rem"></i></button>
</div>

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Métadonnées

* Les [métadonnées des normales climatiques sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/746f9469-ab78-5dcc-b165-4b51e8ab8652)
* Les [métadonnées des données quotidiennes  sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/5f963c2d-d4ed-5a79-8a31-c9c582ca5098)
* Les [métadonnées des données mensuelles sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/b24efb37-11b6-5d03-ab19-5759f83db546)

## Produits 

* [Cartes des statistiques météo en temps réel](https://collaboration.cmc.ec.gc.ca/cmc/wtoftpa/www/)

## Documentation technique

* [Note technique](https://climat.meteo.gc.ca/doc/Documentation_technique.pdf)
* [Site web du Climat](http://climat.meteo.gc.ca/historical_data/search_historic_data_f.html)
* [Centre canadien des services climatiques](https://www.canada.ca/fr/environnement-changement-climatique/services/changements-climatiques/centre-canadien-services-climatiques.html)


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
        js.src = "../../../js/climateobs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/climateobs.js";
    }
    head.appendChild(js);
</script>
