[In English](readme_prev-vertical-pfl-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Prévisions des profils verticaux


# Données de prévisions des profils verticaux

Cette page décrit les données des prévisions des profils verticaux.

## Description

Les données verticales prévues pour différents sites au Canada

Les valeurs prévues (ProgTephi) contiennent les  valeurs prévues à partir du modèle GEM Régional de résolution de 10 km.

Données fournies et unités de mesure (pas nécessairement dans cet ordre):

* __TT__ : Température  (°C)
* __ES__ : Dépression du point de rosée (°C)
* __WD__ : Direction du vent  (degrés vrais)
* __UV__ : Vitesse du vent (noeuds)
* __HR__ : Humidité relative (fraction décimale; ex.  .58 = 58%) 
* __GZ__ : Hauteur géopotentielle (decamètres avec 2 décimales)
* __WW__ : Mouvement vertical (Pa/sec)

Niveaux de pression des données :
* Débutent à la surface
* GZ, ES, UV, WD, HR et TT disponibles à: SFC 1000 985 970 950 925 900 875 850 800 750 700 650 600 550 500 450 400 350 300 275 250 225 200175  150 100  70  50  30  20  10 mb
* WW disponibles pour 29 niveaux (pas à 70, 30 ou 20 mb)

Note: Certains des niveaux de pression peuvent être sous l'élévation de la station.

Pas de temps :
* Les valeurs des données sont fournies par pas de 3 heures entre 00 et 48 heures.

Format des données :
* En ASCII sous forme de fichiers .csv
* Les données pourront être fournies en format BUFR dans le futur

Logiciels d'affichage disponibles sur le marché.

Bien que Environnement et Changement climatique Canada ne fournisse pas de logiciels d'affichage afin de visualiser les données de façon graphique (style téphigramme), certains usagers utilisent les logiciels suivants :

* Buffkit :
    * http://wdtb.noaa.gov/tools/BUFKIT/index.html
* RAOB de la compganie Environmental Research Services :
    * http://www.raob.com/
* NCAR Command Language :
    * http://www.ncl.ucar.edu/get_started.shtml

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier CSV.

Les profils verticaux sont disponibles à cette adresse:
* https://dd.weatheroffice.ec.gc.ca/verticale_profile/

Un historique de 24 heures des données est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers  sont regroupés dans des structures de répertoires basées sur le type de produit (observation ou prévision) et le format des données.

__1- Les répertoires suivent la nomenclature suivante :__
* https://dd.weatheroffice.ec.gc.ca/vertical_profile/TYPE/FORMAT/

où:

* __TYPE__ : type du produit. Peut prendre la valeur 'observation' ou 'forecast'
* __FORMAT__ : format des données. Présentement, les données ne sont disponibles qu'en format 'csv'.

Exemple : 
https://dd.weatheroffice.ec.gc.ca/vertical_profile/forecast/csv/

__2- Les noms de fichiers suivent cette nomenclature :__

* TYPE_HH_AAAA.csv

où:

* __TYPE__ : chaîne de caractères pour le type de produit. Peut être "ObsTephi" ou "ProgTephi"
* __HH__ : Heure  de la passe. Peut être "00" ou "12"
* __AAAA__ : code de la station de 4 lettres. La liste complète peut-être trouvée ici:
    * https://dd.ec.gc.ca/vertical_profile/doc/station_list_for_vertical_profile.txt

Exemple : 
ProgTephi_12_WASA.csv

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).


