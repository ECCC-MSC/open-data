[In English](readme_metnotes_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > MetNotes

# Données MetNotes

Les MetNotes sont des polygones de format libre, géo- et temporellement référencés, émis par le SMC, qui sont complémentaires aux systèmes de diffusion actuels basés sur la localisation. Le texte concis d'une MetNote (semblable à un Tweet) est conforme à la communication d'aujourd'hui où les gens recherchent des informations en un coup d'œil. Les météorologues émettront une MetNote pour ajouter des renseignements contextuels et/ou d'impact afin de compléter les prévisions publiques valables pour une zone spécifique et un intervalle de temps spécifique.

Ces notes sont également disponibles sur l'application mobile [MétéoCAN](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/meteocan.html)

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](../../msc-geomet/readme_fr.md)
* [Données GeoJSON disponibles sur HPFX, le serveur alternatif Datamart du SMC](readme_metnotes-datamart_fr.md) 

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible. 

Exemple de carte interactive présentant la couche `METNOTES` provenant de GeoMet du SMC :
<div id="map" style="height: 400px; margin-bottom: 1rem;"></div>
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

### Métadonnées

Les [métadonnées de MetNotes sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/5fc7ab98-afa1-427b-87b6-658565cca575).

## Documentation technique

[FAQ](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/meteocan/metnotes.html)

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
</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdn.jsdelivr.net/npm/luxon@3.0.1/build/global/luxon.min.js" integrity="sha256-uQ0RrcqAQ8NxzNqZH11eXx3qFLAgwEgSQN1V0N1+UlM=" crossorigin="anonymous"></script>
<script src="../../../js/metnotes_fr.js" type="text/javascript"></script>