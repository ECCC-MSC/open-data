[In English](readme_ahccd-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [DCCAH](readme_ahccd_fr.md) > DCCAH sur le Datamart du SMC

# Données Climatiques Canadiennes Ajustées et Homogénéisées (DCCAH) en format GeoJSON

Les données DCCAH sont des ensembles de données de stations climatiques avec des ajustements (dérivés de procédures statistiques) aux données historiques originales aux stations pour tenir compte des discontinuités dues à des facteurs non climatiques, tels que les changements d'instruments ou le déplacement des stations.

Cet ensemble de données a été élaboré pour la recherche sur le climat, y compris les études sur le changement climatique. Les enregistrements de données à long terme sont souvent influencés par des changements (p. ex. exposition au site, emplacement, instrumentation, observateur et procédures d'observation) qui ne sont pas liés au climat. Ces changements non climatiques ont été détectés et supprimés à l'aide de procédures statistiques.

Au besoin, les données ont été corrigées pour certaines techniques de mesure dont on sait qu'elles peuvent entraîner des sous-estimations ou des surestimations. De plus, les données des stations voisines ont parfois été combinées pour créer des séries chronologiques plus longues.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les fichiers DCCAH  se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/climate/ahccd/geojson/historical/annual/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/ahccd/geojson/historical/annual/)
* [https://dd.meteo.gc.ca/climate/ahccd/geojson/historical/seasonal/{[DJF,MAM,JJA,SON]/[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/ahccd/geojson/historical/seasonal)
* [https://dd.meteo.gc.ca/climate/ahccd/geojson/historical/monthly/{[AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT]}](https://dd.meteo.gc.ca/climate/ahccd/geojson/historical/monthly)

Où :

* __historical__ : Données historiques à partir de 1840. Mise à jour annuelle.
* __monthly__ : Janvier à décembre 
* __seasonal__ : les saisons météorologiques standard sont utilisées : (de mars à mai (MAM, printemps), de juin à août (JJA, été), de septembre à novembre (SON, automne/automne) et de décembre à février (DJF, hiver))]
*  AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT : Les 10 provinces canadiennes et les 3 territoires canadiens

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les noms des fichiers ont la forme : 

AHCCD_hist_TemporalResolution_ProvTerr_XXXXXXX_Variable_TimeStep.json

Où :

* __AHCCD__ : Chaîne constante indiquant la source des données soit les données climatiques ajustées et homogénéisées pour de nombreuses stations climatologiques au Canada.
* __hist__ : Chaîne constante indiquant les données historiques. Varie selon la station et la variable, la disponibilité des données variant de 1840 à l'année précédente à l’année en cours
* __TemporalResoltion__ : Résolution temporelle, prenant l'une des valeurs : [annual, monthly, DJF, MAM, JJA, SON]
* __ProvTerr__ : Code de 2 lettres pour la province ou le territoire. Le code est l'une des 13 valeurs suivantes :
    * AB (Alberta)
    * BC (Colombie-Britannique)
    * MB (Manitoba)
    * NB (Nouveau-Brunswick)
    * NL (Terre-Neuve-et-Labrador)
    * NS (Nouvelle-Écosse)
    * NT (Territoires du Nord-Ouest)
    * NU (Nunavut)
    * ON (Ontario)
    * PE (Île-du-Prince-Édouard)
    * QC (Québec)
    * SK (Saskatchewan)
    * YT (Yukon)
* __XXXXXXX__ : Cilmate_ID des stations climatiques
* __Variable__ : Nom de la variable disponible dans le fichier, prenant l’une des valeurs: [TMEAN,TMIN,TMAX,PCP,RA,SN,SLP,PSFC,SFCWND]; TMEAN représente la température moyenne, TMIN représente la température minimale, TMAX représente la température maximale, PCP représente les précipitations totales, RA représente la pluie ; SN représente la neige ; SLP représente la pression au niveau de la mer ; PSFC représente la pression de surface ; SFCWND représente la vitesse du vent en surface.
* __TimeStep__ : Pas de temps, prenant l'une des valeurs : [P1Y, P1M] ; P1Y représente un pas de temps d'un an et P1M représente un pas de temps d'un mois.
* __json__ : Chaîne constante indiquant le format GeoJSON.

Exemple : AHCCD_hist_annual_QC_7040446_SLP_P1Y.json

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

La liste des variables DCCAH est :

* Température maximale (°C)
* Température minimale (°C)
* Température moyenne (°C)
* Précipitations sous forme de pluie (mm/période)
* Chutes de neige (mm/période)
* Précipitations totales (mm/période)
* Vitesse du vent (m/s)
* Pression au niveau de la station (Pa) 
* Pression au niveau de la mer (Pa)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



