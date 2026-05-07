[In English](readme_aviation-iwxxm-datamart_en.md)

![ECCC logo](../../../img_eccc-logo.png)

[TdM](../../../readme_fr.md) > [Données du SMC](../../readme_fr.md) > [Données météorologiques à l'aviation](readme_aviation-iwxxm_fr.md) > Données météorologiques à l'aviation en format IWXXM sur le Datamart du SMC

# Données météorologiques à l'aviation en format IWXXM

Cette page décrit les bulletins spécialisés à l'aviation distribués dans le [format IWXXM](https://community.wmo.int/iwxxm), un modèle d'échange d'informations météorologiques de l'OACI) introduit en novembre 2013 par l'amendement 76 de l'Annexe 3 de l'OACI, permettant aux États d'échanger leurs données OPMET (_Expert Group on Operational Meteorology_) non seulement sous forme de TAC (code alphanumérique traditionnel) mais aussi en langage de balisage extensible (XML) et plus précisément en langage de balisage géographique (GML).

L'échange d'information IWXXM est devenu une recommandation par le biais de l'amendement 77 à l'Annexe 3 de l'OACI depuis novembre 2016 et une norme depuis novembre 2020, comme indiqué dans l'amendement 78 à l'Annexe 3 de l'OACI.

Cette page décrit à la fois les [données météorologiques à l'aviation en format IWXXM](readme_aviation-iwxxm_fr.md) disponibles sur le Datamart du SMC mais aussi le schéma utilisé pour encoder les données spécifiques au Canada.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les données météorologiques en format IWXXM, ainsi que le schéma associé aux [spécificités des données canadiennes](https://dd.meteo.gc.ca/today/aviation/iwxxm/code-ca/) se trouvent respectivement:

* [https://dd.meteo.gc.ca/today/aviation/iwxxm/{product}/{code_issuer}/{HH}](https://dd.meteo.gc.ca/today/aviation/iwxxm)
* [https://dd.meteo.gc.ca/today/aviation/iwxxm/schema](https://dd.meteo.gc.ca/today/aviation/iwxxm/schema)

Avec:

* __product__ : Produit météorologique (voir la liste ci-dessous)
* __code_issuer__ : Code international des bureaux émetteurs (voir la liste ci-dessous)
* __HH__ : Heure d'émission des données

#### Description des produits

* __vaa__ :
* __qvaci__ :
* __taf__ :
* __metar__ :
* __speci__ :
* __airmet__ :
* __sigmet__ :

#### Liste des bureau émetteurs

| Code        |  Non du bureau émetteur   |  Ville               | Code de fuseau horaire  |
|-------------|---------------------------|----------------------|-------------------------|
| cwao | Centre météorologique canadien | Montréal     | EST5EDT         |
|      |                                |              |                 |
|      |                                |              |                 |

... _A compléter via https://eccc-msc.github.io/open-data/msc-data/alerts/readme_alerts-datamart_fr/#notes ??_


## Nomenclature des noms de fichiers 

Les noms de fichiers suivent la nomenclature ci-dessous :

`A_{TTAAiiCCCCYYGGggBBB}_C_{CCC}_{YYYYMMddhhmmss}.xml`

où :

* __A__ : Chaine de caractères constante permanente
* __TTAAiiCCCCYYGGgg__ : Entête actuelle de l’OMM avec le groupe date et heure
* __HHmm__ : Heure et minute à laquelle les données sont émises
* __BBB__ : Chaine de caractères optionnelle
* __C__ : Chaine de caractères constante permanente
* __CCC__ : Identificateur de l’élément `TTAAiiCCCC` qui est répété
* __YYYYMMddhhmmss__ : Groupe date et heure
* __xml__ : Extension du fichier (format XML)

Exemple :

* A_LTCN33CWAO102300RRA_C_CWAO_20260210230000.xml

Notes:

* Les données sont générées X fois par jour (??) et sont valides pour les 24 prochaines heures (??). Plus spécifiquement, les données sont valides de ??
* _Infos sur les fichiers textes du code canadien: https://dd.meteo.gc.ca/today/aviation/iwxxm/code-ca ???_


## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
