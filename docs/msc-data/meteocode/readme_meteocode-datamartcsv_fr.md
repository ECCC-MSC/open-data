[In English](readme_meteocode-datamartcsv_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données de prévision meteocode](readme_meteocode_fr.md) > Données CSV de prévision meteocode sur le Datamart du SMC

# Données de prévision meteocode en format CSV

Ce document décrit le contenu des fichiers de [données meteocode](readme_meteocode_fr.md) en format CSV.

Les fichiers des données meteocode sur le domaine terrestre en format CSV sont créés à partir des fichiers en format CMML grâce la technologie [XSLT](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/meteocode/cmml2csv.xsl). Les fichiers CSV ne contiennent pas plus d'information que les fichiers CMML, ils sont simplement dans un format différent. De plus, chaque fichier CMML contient plusieurs régions alors que chaque fichier CSV n'est valide que pour une seule région.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les données pour les différentes régions du pays sont disponibles aux  adresses suivantes :

* [https://dd.meteo.gc.ca/meteocode/mtm/csv/](https://dd.meteo.gc.ca/meteocode/mtm/csv/)
* [https://dd.meteo.gc.ca/meteocode/ont/csv/](https://dd.meteo.gc.ca/meteocode/ont/csv/)
* [https://dd.meteo.gc.ca/meteocode/pnr/csv/](https://dd.meteo.gc.ca/meteocode/pnr/csv/)
* [https://dd.meteo.gc.ca/meteocode/pyr/csv/](https://dd.meteo.gc.ca/meteocode/pyr/csv/)
* [https://dd.meteo.gc.ca/meteocode/que/csv/](https://dd.meteo.gc.ca/meteocode/que/csv/)

Un historique des données de 24 heures est conservé dans ces répertoires.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les noms de fichiers ont la forme suivante :

YYYY-MM-DDTHH-MM-SSZ_FPAANN_rRRRR_BB.csv

où :

* __YYYY-MM-DDTHH-MM-SSZ__ : Date d'émission de la prévision. En format ISO 8601.
* __FP__ : Chaîne de caractères constante, signifiant prévision publique
(en anglais: Forecast Public).
* __AANN__ : Voir la section 'Nom de fichier' dans la [documentation des fichiers CMML](readme_meteocode-datamartcsv_fr.md).
* __r__ : Caractère constant indiquant le début du code de région.
* __RRRR__ : Code alphanumérique indiquant la région de prévision publique. Peut être d'une longueur arbitraire (ex: 3pe, 10zf, 71.14). 
* __BB__ : Chaîne de caractères indiquant l'élément du temps. Peut prendre
une de ces valeurs: TA (température de l'air), TD (point de rosée), PA (accumulation de précipitation), POP (probabilité de précipitation), WS (vitesse et direction du vent), 
WG (rafale), CC (couverture nuageuse).

Selon la valeur de AA, le fichier CSV est acheminé dans le répertoire
selon cette liste :

* QX (Gander,N.F.) - mtm
* HX (Halifax,  now Dartmouth ) - mtm
* UL (Montréal) - que
* QB (Québec)  - que
* XK (Rimouski) - que
* CN (Canada) - que
* TO (Toronto) - ont
* WG (Winnipeg) - pnr
* NT (Northwest Territories) - pnr
* VR (Vancouver) - pyr

Exemple :

2009-11-17T09-47-00Z_FPXK55_ r74.18_TD.csv

Ce nom de fichier indique qu'il contient le point de rosée (TD) pour la
prévision créé le 17 novembre 2009 à 9:47 UTC (2009-11-17T09-47-00Z) émise
par le bureau de prévision du Québec (FPXK) pour les jours 3 à 7 (55) pour la région de Chevery
(r74.18).

**Note**:

La [liste complète des régions de prévisions ainsi que le code associé](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/meteocode/table_region_code_name.xlsx) est disponible.

Les codes sont séparés par les bureaux de prévision car un même code peut être utilisé par dans plus d'une région, selon :

    code bulletin, code région, nom_français, nom_anglais


## Contenu des fichiers

* Pour chaque région de prévisions, 7 fichiers sont produits. Le contenu de chaque fichier est décrit dans les sections ci-bas.
* Les valeurs ''-9999.00'' indiquent une donnée invalide ou manquante pour la température de l'air ou le point de rosée. 
* Si les rafales ne sont pas disponibles dans le fichier CMML à une heure de validité donnée, alors le ichier CSV associé ne contient pas de données pour cette date spécifique. 
* Toutes les dates sont dans le format ISO 8601.


__1. Température de l'air (TA)__

Ce fichier contient les températures de l'air.

La première ligne de ces fichiers contient les paramètres:

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : nom du fichier CMML d'où origine le fichier CSV.
* Les 2 autres valeurs représentent le contenu des colonnes dans le
fichier, à savoir :
    * Heure de validité de la prévision;
    * Température de l'air en degré Celsius.

__2. Point de rosée (TD)__ 

Ce fichier contient les valeurs du point de rosée.

La première ligne de ces fichiers contient les paramètres: 

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : nom du fichier CMML d'où origine le fichier CSV.
* Les 2 autres valeurs représentent le contenu des colonnes dans le fichier, à savoir :
    * Heure de validité de la prévision.
    * Température du point de rosée en degré Celsius.

__3. Accumulation de précipitations (PA)__ 

Ces fichiers contiennent les accumulations et le type de précipitation.

La première ligne de ces fichiers contient les paramètres:

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : Nom du fichier CMML d'où origine le fichier CSV.
* Les autres valeurs représentent le contenu des colonnes dans le fichier, à savoir :
    * Heure de début de la période d'accumulation.
    * Heure de fin de la période d'accumulation.
    * Quantité cumulative inférieure du type de précipitations actuel en mm.
    * Quantité cumulative supérieure du type de précipitations actuel en mm.
    * Limite inférieure de la quantité de précipitations en mm.
    * Limite supérieur de la quantité de précipitations en mm.
    * Type de précipitations. Peut être parmi ces valeurs :
        * Rain (pluie)
        * Snow (neige)
        * Ice pellet (grésil)
        * Freezing rain (pluie verglaçante)

__4. Probabilité de précipitation (POP)__ 

Ce fichier contient les probabilités de précipitations.

La première ligne de ces fichiers contient les paramètres:

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : Nom du fichier CMML d'où origine le fichier CSV.
* Les autres valeurs représentent le contenu des colonnes dans le fichier, à savoir :
    * Heure de début de la période de la probabilité de précipitation.
    * Heure de fin de la période de la probabilité de précipitation.
    * Probabilité de précipitation, en pourcentage.

__5. Vent (WS)__  

Ce fichier contient les valeurs pour la vitesse et la direction du vent.

La première ligne de ces fichiers contient :

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : Nom du fichier CMML d'où origine le fichier CSV.
* Les autres valeurs représentent le contenu des colonnes dans le fichier, à savoir :
    * Heure de début de la période.
    * Heure de fin de la période.
    * Vitesse du vent minimale, en km/h.
    * Vitesse du vent maximale, en km/h.
    * Chaîne de caractères pour la direction du vent. Peut prendre une des valeurs suivantes :
        * east
        * nil
        * north (nord)
        * northeast (nord-est)
        * northwest (nord-ouest)
        * west (ouest)
        * easterly (du secteur est)
        * northerly (du secteur nord)
        * northeasterly (du secteur nord-est)
        * northwesterly (du secteur nord-ouest)
        * westerly (du secteur ouest)
        * southerly (du secteur sud)
        * southeasterly (du secteur sud-est)
        * southwesterly (du secteur sud-ouest)
        * south (sud)
        * southeast (sud-est)
        * southwest (sud-ouest)
        * variable 

__6. Rafale (WG)__

Ce fichier contient les valeurs pour la vitesse des rafales.

La première ligne de ces fichiers contient les paramètres:

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : Nom du fichier CMML d'où origine le fichier CSV.
* Les autres valeurs représentent le contenu des colonnes dans le fichier, à savoir :
    * Heure de début de la période.
    * Heure de fin de la période.
    * Vitesse des rafales minimale, en km/h.
    * Vitesse des rafales maximale, en km/h.

__7. Couverture nuageuse (CC)__

Ce fichier contient la couverture nuageuse en format décimal.

La première ligne de ces fichiers contient les paramètres:

où :

* **Region_en** : Nom anglais de la région de prévision.
* **Region_fr** : Nom français de la région de prévision.
* **CMML** : Chaîne de caractères constantes.
* **cmml_filename.xml** : Nom du fichier CMML d'où origine le fichier CSV.
* Les autres valeurs représentent le contenu des colonnes dans le fichier, à savoir :
    * Heure de validité pour la couverture nuageuse.
    * Couverture nuageuse, en dixième.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).
