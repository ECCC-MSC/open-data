[In English](readme_hrdpa-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [AHRDP](readme_hrdpa_fr.md) > AHRDP sur le Datamart du SMC

# Données GRIB2 de l'Analyse à haute résolution déterministe de précipitation (AHRDP)

Cette page décrit les données de l'[Analyse à haute résolution déterministe de précipitation](./readme_hrdpa-datamart_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/analysis/precip/hrdpa/grib2/polar_stereographic/{HH}](https://dd.meteo.gc.ca/analysis/precip/hrdpa/grib2/polar_stereographic)

où :

* __polar_stereographic__ :  Projection de la grille
* __HH__ :  Période d'accumulation en heures: 06 or 24 

Un historique de 30 jours est conservé dans ce répertoire.

## Spécification technique de la grille

![image de la spécification technique de la grille AHRDP](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_hrdpa/grille_hrdpa.png)

Valeurs données aux paramètres de la grille polaire stéréographique à haute résolution.

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2500 |
| nj | 1222 | 
| résolution à 60° N | 2.5 km |
| coordonnées du premier point de grille | 42.2504° N ; 131.0928° W | 
| orientation de la grille (par rapport à l’axe des j) | -115,0° | 

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_HRDPA_APCP-TotalPrecipAmount-HHMMcutoff_SFC_0_ps2.5km_YYYYMMDDHH_000.grib2

où :

* __CMC__ : Les données sont produites par le Centre Météorologique Canadien (Chaîne constante)
* __HRDPA__ : Analyse à Haute Résolution Déterministe de Précipitation (Chaîne constante)
* __APCP__ : Analyse de Précipitation (Chaîne constante)
* __AccumTotalePrecipPeriode__ : La quantité de précipitation totale sur une période de temps définie en nombre d'heures (006 ou 024)
* __HHMMcutoff__ : Le temps de coupure des observations en nombre d'heures et minutes après l'heure de validité. (0100cutoff ou 0700cutoff)
* __SFC_0__ : Le type de niveau est Surface et son type de valeur est 0 (Chaîne constante)
* __ps2.5km__: Le type de projection est polaire-stéréographique à une résolution de 2.5 km (Chaîne constante)
* __YYYYMMDDHH__: Heure de validité de l'analyse en UTC. YYYY=Année, MM=Mois, DD=Jour, HH=Heure (ex: 2018020912)
* __000__: Le temps de projection en nombre d'heures. Toujours 000 pour une analyse (Chaîne constante)

Exemple :

CMC_HRDPA_APCP-006-0100cutoff_SFC_0_ps2.5km_2018020912_000.grib2

Ce fichier provient du Centre Météorologique Canadien (CMC) et contient des données de l'Analyse à Haute Résolution Déterministe de Précipitation (HRDPA). C'est une analyse de précipitation (APCP) sur des cumuls de 6 heures (006) dont la période de cumul débute à 2018020906 et se termine à 2018020912. Elle est considérée préliminaire parce que la collecte des observations s'est faite jusqu'à 2018020913, soit 1 heure après l'heure de validité (0100cutoff). Les données sont sur une grille stéréographique polaire à une résolution de 2.5 km (ps2.5km). L'heure de validité de l'analyse est 2018020912_000 où le suffixe _000 signifie que le temps de projection dans le future est nulle, ce qui est toujours le cas pour une analyse. Les données de ce fichier sont encodées en format GRIB2 (.grib2).

À noter qu'une deuxième variable est également incluse dans ce fichier, soit l'indice de confiance de l'analyse (CFIA).

## Liste des variables

* __APCP__ : Analyse de la quantité totale de précipitation (mm)
* __CFIA__ : Indice de Confiance de l'Analyse. Plage de valeurs de 0 à 1 (sans unité)

## À propos du masque No-Data

Un masque pour mieux représenter les zones où les données ne sont pas disponibles, appelées aussi "No-Data" a été ajouté dans notre procédure d’encodage GRIB2. Ce masque vise uniquement quelques points de grille non-valides (données non-disponibles), toujours les mêmes et qui se situent en périphérie du domaine. Notons que ces points masqués n’ont aucun effet négatif sur la qualité du produit.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

