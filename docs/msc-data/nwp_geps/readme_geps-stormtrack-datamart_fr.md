[In English](readme_geps-stormtrack-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SGPE](readme_geps_fr.md) > Trajectoires de tempêtes issues du SGPE sur le Datamart du SMC

# Données de trajectoires de tempêtes générées à partir du Système global de prévision d'ensemble

Le produit de trajectoire de tempêtes est un système automatisé qui détecte, identifie, suit et caractérise les systèmes dépressionnaires à partir des sorties des modèles numériques de prévision météorologique (déterministe et ensembliste) ou des réanalyses.  Il permet de produire des cartes, des animations décrivant l'évolution des cyclones extratropicaux et tropicaux pendant toute leur durée de vie.

Une fois déterminés à chaque échéance du modèle, les centres des tempêtes sont reliés entre eux grâce à la méthode développée par [Mark R. Sinclair](https://journals.ametsoc.org/view/journals/wefo/12/3/1520-0434_1997_012_0595_oiocat_2_0_co_2.xml), qui recherche le meilleur prolongement possible d'une trajectoire en tenant compte notamment de la position précédente, de la vitesse de déplacement, de la direction du mouvement et de la continuité temporelle. Seuls les systèmes ayant une durée de vie d'au moins 24 heures sont conservés comme tempêtes valides.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont accessibles à l’adresse suivante : 

* [https://dd.meteo.gc.ca/today/model_geps/storm-tracks/{HH}/](https://dd.meteo.gc.ca/today/model_geps/storm-tracks)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12] 

## Spécifications techniques

Les informations suivantes sont disponibles pour chaque centre de tempête:

* Un marqueur indiquant la position du centre
* Une ligne reliant les positions successives du centre
* La position du centre
* La date et l'heure (UTC)
* La durée de la tempête
* Les valeurs de pression, de tourbillon, et de circulation
* Pour les cyclones tropicaux uniquement: les valeurs de baroclinicité de bas niveaux (600-900 mb), de structure du vent thermique de bas niveaux (600-900 mb) et hauts niveaux (300-600 mb), de maximum de tourbillon à 850 mb, de maximum d'épaisseur 250-850 mb, et de maximum de vent de surface

#### Cyclones extra-tropicaux

Les cyclones extra-tropicaux sont suivis soit par leurs valeurs minimales de pression au niveau moyen de la mer (PNMM) ou par leurs valeurs maximales de tourbillon du vent gradient, à 500 et 1000 mb.

Pour le suivi basé sur le tourbillon, les cyclones (i.e. les maximums de tourbillon) doivent dépasser une certaine valeur seuil (à 1000 mb: +0,75x10-5 s-1, à 500 mb: +1,5x10-5 s-1). En premier lieu, le tourbillon est filtré avec un filtre de Cressman ayant un rayon de filtrage de 800 km afin de supprimer les détails (réels et fictifs) de petite échelle et ne conserver que la composante synoptique.

Pour le suivi basé sur la pression au niveau moyen de la mer (PNMM), les centres de basse pression sont déterminés en utilisant des champs de PNMM filtrés avec un filtre de Cressman ayant un rayon de filtrage de 300 km. Toutefois, les valeurs centrales de basse pression représentent la pression de la PNMM brute (i.e. non filtrée) à la position des centres identifiés dans les champs de PNMM filtrées.

Dans tous les cas, pour être considérés, les cyclones doivent perdurer au moins 24h.

#### Cyclones tropicaux

Le suivi des cyclones tropicaux utilise le même processus que le suivi des cyclones extra-tropicaux en pression. Afin d'identifier les cyclones de nature tropicale, 4 variables additionnelles sont prises en compte:

* Le tourbillon relatif à 850 mb filtré avec un filtre de Cressman ayant un rayon de filtrage de 300 km
* Les épaisseurs entre les niveaux 250 et 850 mb
* Le vent à 10 m
* La baroclinicité de bas niveaux (noté B) mesurée en terme d'asymétrie du champ des épaisseurs entre 600 et 900 mb. La définition de B adoptée suit celle proposée par [Sinclair, M. R., 1997](https://journals.ametsoc.org/view/journals/wefo/12/3/1520-0434_1997_012_0595_oiocat_2_0_co_2.xml).

Pour être considéré comme un cyclone tropical, un centre de basse pression doit rencontrer les 4 critères suivants:

* Posséder un maximum de tourbillon à 850 mb supérieur à 2,5x10-5 s-1 dans un rayon de 150 km
* Posséder un maximum d'épaisseur 250-850 mb upérieur à 935 dam dans un rayon de 150 km (indicateur d'un centre chaud profond et vertical)
* Être accompagné d'un vent de surface (10 m) supérieur à 22 noeuds dans un rayon de 225 km
* Evoluer dans un environnement barotrope ou de faible baroclinicité, défini ici par une valeur de B inférieure à 25 m.

Une trajectoire est initiée uniquement lorsque tous les critères précédents sont rencontrés.  Lorsqu'un cyclone tropical ne satisfait plus l'ensemble de ces quatre critères, il est classifié comme étant post-tropical. Il prend alors soit l'étiquette "Extra-Tropical" s'il évolue dans un environnement barocline (B > 25 m) ou l'étiquette "Remnant" s'il demeure dans un environnement barotrope. 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

* Cyclone tropicaux: `{YYYYMMDD}T{HH}Z_MSC_GEPS-StormTracks_TropicalCyclone_PT{hhh}H.json`
* Cyclones extra-tropicaux:
    * `{YYYYMMDD}T{HH}Z_MSC_GEPS-StormTracks_GradientWindVorticity-IsbL-0500_PT{hhh}H.json`
    * `{YYYYMMDD}T{HH}Z_MSC_GEPS-StormTracks_GradientWindVorticity-IsbL-1000_PT{hhh}H.json`
    * `{YYYYMMDD}T{HH}Z_MSC_GEPS-StormTracks_Pressure-MSL_PT{hhh}H.json`

où :

* __YYYYMMDD__ : Année, mois et jour de la passe du modèle
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GEPS-StormTracks__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de tempêtes générées à partir du Système global de prévision d'ensemble (GEPS en anglais)
* __TropicalCyclone__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de cyclones tropicaux
* __GradientWindVorticity-IsbL-0500__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de tempêtes détectées par leur tourbillon de vent gradient à 500 mb
* __GradientWindVorticity-IsbL-1000__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de tempêtes détectées par leur tourbillon de vent gradient à 1000 mb
* __Pressure-MSL__ : Chaîne de caractères constante indiquant des prévisions de trajectoires de tempêtes détectées par leur pression au niveau moyen de la mer
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l'heure à laquelle la trajectoire est prévue 
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemples de noms de fichiers: 

* 20251016T12Z_MSC_GEPS-StormTracks_TropicalCyclone_PT048H.json
* 20251015T12Z_MSC_GEPS-StormTracks_GradientWindVorticity-IsbL-0500_PT024H.json

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
