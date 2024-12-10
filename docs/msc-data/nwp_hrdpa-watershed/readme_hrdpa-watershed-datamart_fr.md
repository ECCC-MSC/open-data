[In English](readme_hrdpa-watershed-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données de précipitations moyennes par bassin-versant AHRDP](readme_hrdpa-watershed_fr.md) > Bassin-versant AHRDP sur le Datamart du SMC


# Données Esri Shapefile de précipitations moyennes par bassin-versant de l'Analyse à haute résolution déterministe de précipitation (AHRDP)

Des données pour plus de 1900 bassins-versants sont disponibles. Afin de réduire le nombre de fichiers sur le Datamart, il a été nécessaire de regrouper les bassins-versants par bassin de drainage :

* Provinces Maritimes
* Saint-Laurent
* Nord du Québec et Labrador
* Sud-Ouest de la baie d'Hudson
* Fleuve Nelson
* Ouest de la baie d'Hudson
* Grand lac des Esclaves
* Pacifique
* Fleuve Yukon
* Arctique
* Fleuve Mississipi

En plus des précipitations moyennes, la moyenne de l'indice de confiance de l’analyse est aussi fourni. Tel qu'expliqué dans la documentation de l'analyse AHRDP, l'analyse est une moyenne pondérée d'une prévision numérique du temps et d'observations (in-situ et radar). Le poids total donné aux observations dans l'analyse (entre zéro et un) dans le calcul final est fourni avec la quantité de précipitations dans les fichiers de données sur grille de l’analyse AHRDP. Cette quantité peut être moyennée de façon à refléter le poids moyen donné aux observations dans le calcul de la moyenne pour le bassin-versant.

Elle peut être interprétée comme un indice de confiance pour la quantité de précipitation estimée. 

Des valeurs près de un indiquent que l'estimation provient essentiellement de données observées, alors que des valeurs près de zéro indiquent que l'estimé proposé par l’analyse AHRDP provient essentiellement d'une prévision à courte échéance des précipitations.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès aux fichiers Esri Shapefile.

Les données sont accessibles aux adresses suivantes :

* [https://dd.weather.gc.ca/analysis/precip/hrdpa_watershed/shapefile/{HH}](https://dd.weather.gc.ca/analysis/precip/hrdpa_watershed/shapefile)

où  :

* __HH__ : Période d’accumulation en heures: 06 ou 24 

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

CMC_HRDPA_WATERSHED-HHH-CC00cutoff_SFC_0_ps2.5km_AAAAMMJJHH_000_ID.SUF

où :

* __HHH__ : Durée de la période d'accumulation en heures (006 or 024)
* __CC__ : Temps de coupure de l'analyse en heures (01 or 07) après la fin de la période d'accumulation
* __AAAAMMJJHH__ : Date et heure de validité de l’analyse (correspondant à la fin de la période d'accumulation)
* __ID__ : Identificateur du bassin de drainage, de 01 à 11 :
	* 01 Provinces Maritimes
	* 02 Saint-Laurent
	* 03 Nord du Québec et Labrador
	* 04 Sud-Ouest de la baie d'Hudson
	* 05 Fleuve Nelson
	* 06 Ouest de la baie d'Hudson
	* 07 Grand lac des Esclaves
	* 08 Pacifique
	* 09 Fleuve Yukon
	* 10 Arctique
	* 11 Fleuve Mississipi

* __SUF__: suffixe du fichier au format Shapefile :
    * "dbf" – attributs des éléments contenus dans le fichier au format Shapefile
	* "prj" – fichier texte décrivant la projection des données
	* "shp" – fichier binaire décrivant la géométrie des données
	* "shx" – fichier d'index pour la géométrie des données

Exemple : 

* CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.dbf
* CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.prj
* CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.shp
* CMC_HRDPA_WATERSHED-024-0700cutoff_SFC_0_ps2.5km_2018021612_000_10.shx

Cet ensemble de fichiers contiendrait les prcipitations moyennes pour une période d'accumulation de 24h se terminant à 12 UTC le 16 février 2018 pour des bassins-versants du bassin arctique, et l'analyse aurait été produite sept heures après la fin de cette période d'accumulation.

Chaque fichier au format Shapefile contient de l'information sur tous les bassins-versants se trouvant dans un bassin de drainage particulier. L'aire de drainage associée à chaque bassin-versant est définie par un seul polygone. Sept attributs sont proposés pour chaque bassin-versant :

* __Station__    : Identification de la station
* __StationNam__ : Nom de la station
* __Stn_UID__    : Identificateur unique de la station (pour l'instant, correspond à l'identificateur de la
             station, suivi de _1)
* __Shp_Area__   : Aire du polygone (en km2)
* __Shp_Perime__ : Périmètre associé au polygone (en km)
* __PR_mm__      : Précipitations moyennes pour le bassin-versant défini par ce polygone (en mm)
* __CFIA__       : Moyenne de l'indice de confiance pour le bassin-versant défini par ce polygone (entre 0 et 1), reflétant le poids moyen accordé aux observations in-situ et radar dans le calcul de cette moyenne

## Liste des variables

Attention : les tableaux ci-dessous ne sont pas à jour (à venir), certaines variables sont manquantes. N'hésitez pas à [nous contacter](mailto:ec.dps-client.ec@canada.ca) pour plus d'information.

* __Station__    : Identification de la station
* __StationNam__ : Nom de la station
* __Stn_UID__    : Identificateur unique de la station (pour l'instant, correspond à l'identificateur de la station, suivi de _1)
* __Shp_Area__   : Aire du polygone (en km2)
* __Shp_Perime__ : Périmètre associé au polygone (en km)
* __PR_mm__      : Précipitations moyennes pour le bassin-versant défini par ce polygone (en mm)
* __CFIA__       : Moyenne de l'indice de confiance pour le bassin-versant défini par ce polygone (entre 0 et 1), reflétant le poids moyen accordé aux observations in-situ et radar dans le calcul de cette moyenne

## Support

Pour toute question relative à ces données, merci de [nous contacter]( https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
