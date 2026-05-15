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

Les données météorologiques en format IWXXM sont disponibles à l'adresse:

* [https://dd.meteo.gc.ca/today/aviation/iwxxm/{product}/{code_issuer}/{HH}](https://dd.meteo.gc.ca/today/aviation/iwxxm)

Avec:

* __product__ : Produit météorologique (voir la liste ci-dessous)
* __code_issuer__ : Code de l'aérodrome qui rapporte l'observation
* __HH__ : Heure d'émission des données (UTC)


| Produit à l'aviation | Type de bulletin         | En-tête du fichier           |
|------------------|-----------------------|----------------------|
| vaa              | Avis de cendres volcaniques (VAA) | A_LUCN                |
| qvaci            | Analyse quantitative des cendres volcaniques (QVA) | A déterminer         |
| taf              | Prévision d’aérodrome  (TAF) | A_LTCN                |
| metar            | Rapport météorologique régulier d'aérodrome (METAR) | A_LACN               |
| speci            | Rapport météorologique spécial d'aérodrome (SPECI) | A_LPCN              |
| airmet           | AIRman's METeorological Information (AIRMET) | A_LWCN / A_LWNT               |
| sigmet           | SIGnificant METeorological Information (SIGMET) | A_LSCN-A / A_LYCN / A_LVCN             |

Le Canada utilise la version 3.0.0 des schémas IWXXM de l'OMM, disponibles à l'adresse suivante : [https://schemas.wmo.int/iwxxm/](https://schemas.wmo.int/iwxxm/)

Le Canada utilise également des schémas d'extension afin de fournir des éléments météorologiques supplémentaires ou pour répondre aux exigences nationales. Les schémas d'extension canadiens sont disponibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/today/aviation/iwxxm/schema/](https://dd.meteo.gc.ca/today/aviation/iwxxm/schema)

Certains éléments météorologiques utilisés dans les bulletins à l'aviation ont des définitions spécifiques pour le Canada. Ces éléments et leurs définitions sont disponibles à l'adresse suivante :

* [https://dd.meteo.gc.ca/today/aviation/iwxxm/code-ca/](https://dd.meteo.gc.ca/today/aviation/iwxxm/code-ca)

Une documentation détaillée est disponible à cette adresse :

* [https://dd.meteo.gc.ca/today/aviation/iwxxm/doc/](https://dd.meteo.gc.ca/today/aviation/iwxxm/doc)

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

Davantage d'information concernant la [nomenclature des bulletins](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/aviation/iwxxm/TAC_Bulletins_IWXXM_Files_2A_fr.pdf) est disponible.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
