[In English](readme_alerts_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > Alertes

# Données et produits d'avertissements météorologiques dans le format du Protocole d'Alerte Commun (PAC)

Environnement et Changement climatique Canada publie des alertes météo lorsque le temps est menaçant pour informer les personnes se trouvant dans les zones touchées afin qu'elles puissent prendre des mesures pour se protéger et protéger leurs biens. Le type d'alerte utilisé dépend de la gravité et du moment de l'événement. Ce qui inclut : les avertissements, les veilles, les avis et les bulletins. Les avertissements sont habituellement émis entre 6 et 24 heures à l'avance, même si certains phénomènes violents (par exemple les orages et les tornades) peuvent se produire rapidement, avec un avis de moins d'une demi-heure. 

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les services du serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) et les services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) :

* [Données XML disponibles sur le Datamart du SMC](readme_alerts-datamart_fr.md) 
* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_alerts-geomet_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

Exemple de carte interactive présentant la couche `ALERTS` provenant de GeoMet du SMC :
<div id="map" style="height: 400px; margin-bottom: 1rem; position: relative">
  <div id="legend-popup">
  <div id="legend-popup-content">
    <img id="legend-img" style="display: flex; max-width: 150px;" src="https://geo.weather.gc.ca/geomet?version=1.3.0&service=WMS&request=GetLegendGraphic&sld_version=1.1.0&layer=ALERTS&format=image/png&STYLE=ALERTES&lang=fr"/>
  </div>
</div>
</div>
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

* Les [métadonnées des Alertes météo sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/79550951-6b17-49a6-9028-8ae1c21274cf).

## Documentation technique

* [Version actuelle du système national d'alertes au public](https://www.securitepublique.gc.ca/cnt/mrgnc-mngmnt/mrgnc-prprdnss/npas/clf-lng-20-fr.aspx)
* [Critères d'alertes météo publiques](https://www.canada.ca/fr/environnement-changement-climatique/services/types-previsions-meteorologiques-utilisation/publiques/criteres-alertes-meteo.html) 

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

    .alert-descrip {
      overflow: auto;
      max-height: 5rem;
    }
    
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
<script src="https://cdn.jsdelivr.net/npm/luxon@3.0.1/build/global/luxon.min.js" integrity="sha256-uQ0RrcqAQ8NxzNqZH11eXx3qFLAgwEgSQN1V0N1+UlM=" crossorigin="anonymous"></script>
<script src="../../../js/alerts_fr.js" type="text/javascript"></script>