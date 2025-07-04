[In English](readme_citypageweather_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Prévisions météorologiques par ville

# Données et produits des prévisions météorologiques officielles par ville

Cette page décrit les données et produits des prévisions météorologiques par ville qui sont crées pour certaines villes des provinces et des territoires canadiens et distribuées sur le site d'Environnement et Changement climatique Canada : 

[http://www.meteo.gc.ca/](http://www.meteo.gc.ca/)

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données XML disponibles sur le Datamart du SMC](readme_citypageweather-datamart_fr.md) 
* [Données disponibles via les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md) - *Conditions courantes seulement*

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

Exemple de carte interactive présentant la couche `CURRENT_CONDITIONS` provenant de GeoMet du SMC :
<div id="map" style="height: 400px; margin-bottom: 1rem; position: relative"></div>
<div id="popup" class="ol-popup">
    <a href="#" id="popup-closer" class="ol-popup-closer"></a>
    <div id="popup-content"></div>
    <div id="nav" style="margin-top: 0.5rem">
        <div id="nav-btns">
            <button id="left-btn" class="btn btn-outline-primary btn-sm">
              <i class="fa fa-arrow-left" aria-hidden="true"></i>
            </button>
            <span style="width: 20px; height: auto; display:inline-block;"></span>
            <button type="button" id="right-btn" class="btn btn-outline-primary btn-sm">
              <i class="fa fa-arrow-right" aria-hidden="true"></i>
            </button>
        </div>
        <div style="margin-top: 0.25rem; font-size: 0.8rem;">
          <p id="nav-text" style="margin-bottom: 0rem;"></p>
        </div>
    </div>
</div>


### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées de découverte

Les [métadonnées des prévisions météorologiques par ville sont disponibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/1f864766-7f7f-4be7-8292-295065c65c78)

## Documentation technique

Le [Guide des prévisions météorologiques](https://www.canada.ca/fr/environnement-changement-climatique/services/types-previsions-meteorologiques-utilisation/publiques/guide.html) fournit des renseignements sur les bulletins de prévisions: heure de publication, période couverte, régions, terminologie relative à la période de prévision, renseignements fournis et révision des prévisions.

<style>
    .ol-popup {
      position: absolute;
      background-color: white;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
      padding: 15px;
      border-radius: 10px;
      border: 1px solid #cccccc;
      bottom: 12px;
      left: -50px;
      min-width: 300px;
      font-size: 0.8rem;
      line-height: 0.9rem;
    }

    .ol-popup:after,
    .ol-popup:before {
      top: 100%;
      border: solid transparent;
      content: " ";
      height: 0;
      width: 0;
      position: absolute;
      pointer-events: none;
    }

    .ol-popup:after {
      border-top-color: white;
      border-width: 10px;
      left: 48px;
      margin-left: -10px;
    }

    .ol-popup:before {
      border-top-color: #cccccc;
      border-width: 11px;
      left: 48px;
      margin-left: -11px;
    }

    .ol-popup-closer {
      text-decoration: none;
      position: absolute;
      top: 5px;
      right: 8px;
    }

    .ol-popup-closer:after {
      content: "✖";
      color: #A9A9A9;
    }

    .arrow {
      border: solid #2fa4e7;
      border-width: 0 3px 3px 0;
      display: inline-block;
      padding: 3px;
    }

    .right {
      transform: rotate(-45deg);
      -webkit-transform: rotate(-45deg);
    }

    .left {
      transform: rotate(135deg);
      -webkit-transform: rotate(135deg);
    }

    .city-descrip {
      overflow: auto;
      max-height: 5rem;
    }

</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdn.jsdelivr.net/npm/luxon@3.0.1/build/global/luxon.min.js" integrity="sha256-uQ0RrcqAQ8NxzNqZH11eXx3qFLAgwEgSQN1V0N1+UlM=" crossorigin="anonymous"></script>
<script src="../../../js/citypageweather_fr.js" type="text/javascript"></script>