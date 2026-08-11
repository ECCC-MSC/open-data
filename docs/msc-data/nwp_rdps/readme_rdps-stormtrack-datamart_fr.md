[In English](readme_rdps-stormtrack-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_fr.md) > Trajectoires de tempêtes issues du SRPD sur le Datamart du SMC

# Données de trajectoires de tempêtes générées à partir du Système régional de prévision déterministe

Le produit de trajectoire de tempêtes est un système automatisé qui détecte, identifie, suit et caractérise les systèmes dépressionnaires à partir des sorties des modèles numériques de prévision météorologique (déterministe et ensembliste) ou des réanalyses.  Il permet de produire des cartes, des animations décrivant l'évolution des cyclones extratropicaux et tropicaux pendant toute leur durée de vie.

Une fois déterminés à chaque échéance du modèle, les centres des tempêtes sont reliés entre eux grâce à la méthode développée par [Mark R. Sinclair](https://journals.ametsoc.org/view/journals/wefo/12/3/1520-0434_1997_012_0595_oiocat_2_0_co_2.xml), qui recherche le meilleur prolongement possible d'une trajectoire en tenant compte notamment de la position précédente, de la vitesse de déplacement, de la direction du mouvement et de la continuité temporelle. Seuls les systèmes ayant une durée de vie d'au moins 24 heures sont conservés comme tempêtes valides.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont accessibles à l’adresse suivante : 

* [https://dd.meteo.gc.ca/today/model_rdps/storm-tracks/{HH}/](https://dd.meteo.gc.ca/today/model_rdps/storm-tracks)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18] 

## Spécifications techniques

Chaque tempête est représentée par une ligne reliant les positions successives du centre. Pour chaque position sont affichés :

* La date et l'heure (UTC) 
* La position du centre 
* La pression minimale ou la vorticité maximale
* Un symbole dont la taille représente l'intensité 
* Des marqueurs indiquant les positions à 00 UTC

_Documenter les 2 types de fichiers (StormTracks et TropicalCycloneTracks) et leur contenu_

## Nomenclature des noms de fichiers 

Les __fichiers de prévision__ ont la nomenclature suivante :

* `{YYYYMMDD}T{HH}Z_MSC_RDPS-StormTracks_{Var}_{LVLTYPE}-{LVL}_PT{hhh}H.json`
* `{YYYYMMDD}T{HH}Z_MSC_RDPS-TropicalCycloneTracks_PT{hhh}H_Pressure_MSL_PT{000...hhh}H.json`

Les __fichiers d'analyse__ ont la nomenclature suivante:

* `{YYYYMMDD}T{HH}Z_MSC_RDPS-Analysis-StormTracks_{Var}_{LVLTYPE}_PT{hhh}H.json`
* `{YYYYMMDD}T{HH}Z_MSC_RDPS-Analysis-TropicalCycloneTracks_PT{hhh}H_Pressure_MSL_PT{000...hhh}H.json`

où :

* __YYYYMMDD__ : Année, mois et jour de la passe du modèle
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDPS-StormTracks__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de tempêtes générées à partir du Système régional de prévision déterministe (RDPS en anglais)
* __RDPS-Analysis-StormTracks__ : Chaîne de caractères constante indiquant des analyses de trajectoires de tempêtes générées à partir du Système régional de prévision déterministe (RDPS en anglais)
* __RDPS-TropicalCycloneTracks__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de centres de tempêtes générées à partir du Système régional de prévision déterministe (RDPS en anglais)
* __RDPS-Analysis-TropicalCycloneTracks__ : Chaîne de caractères constante indiquant des analyses de trajectoires de centres de tempêtes générées à partir du Système régional de prévision déterministe (RDPS en anglais)
* __Var__ : Variables contenues dans le fichier ["GeopotentialHeight" pour l'altitude géopotentielle (gpm), "Pressure" pour la pression (mb)]
* __LVLTYPE__ : Type de niveau vertical ["IsbL" pour le niveau idobarique (__Isobaric Level__), "MSL" pour le niveau moyen de la mer (__Mean Sea Level__)]
* __LVL__ : Valeur du niveau vertical [0500 pour 500mb, 1000 pour 100mb]. Ce paramètre est absent pour le niveau moyen de la mer
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente ... _à compléter_
* __PT{000...hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente ... _à compléter_
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemples de noms de fichiers: 

* 20251016T12Z_MSC_RDPS-StormTracks_GeopotentialHeight_IsbL-0500_PT048H.json
* 20251012T12Z_MSC_RDPS-Analysis-TropicalCycloneTracks-PT048H_Pressure_MSL_PT024H.json : analyse générée à 20251014T12Z (20251012T12Z +  PT048H) correspondant à la prévision de 20251013T12Z (20251012T12Z +  PT024H).

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
