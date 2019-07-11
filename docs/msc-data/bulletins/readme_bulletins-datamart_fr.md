[In English](readme_bulletins-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > Bulletins alphanumériques sur le Datamart du SMC

# Données des bulletins alphanumériques

Cette page décrit les données des [bulletins alphanumériques](readme_bulletins_fr.md).

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. 

Les données sont accessibles aux adresses suivantes :

* [https://dd.meteo.gc.ca/bulletins/alphanumeric/](https://dd.meteo.gc.ca/bulletins/alphanumeric/)

Un historique de 6 mois est conservé dans ce répertoire.

## Nomenclature des répertoires et noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

Les bulletins sont regroupés dans des structures de répertoires basés sur la date et sur le type de bulletin.
Les répertoires suivent la nomenclature suivante:

YYYYMMDD/AA/BBBB/HH

où :
* __YYYYMMDD__ : Date de réception du bulletin (pas la date d'émission!).
* __AA__ : 2 lettres indiquant le type de bulletin. La référence complète
peut être trouvée dans le Manual on the Global Telecommunication System de
l'OMM, dans la section Supplément II-5, ce qui correspond aux pages
103-108. Le fichier se trouve en ligne à cette adresse : [https://www.wmo.int/pages/prog/www/ois/Operational_Information/Publications/WMO_386/WMO_386_Vol_I_2009_fr.pdf](https://www.wmo.int/pages/prog/www/ois/Operational_Information/Publications/WMO_386/WMO_386_Vol_I_2009_fr.pdf)
* __BBBB__ : 4 lettres représentant le code de l'émetteur du bulletin.

Les 2 lettres suivant "CW" ou "CY" dans le nom du répertoire représente le 
nom du bureau émetteur :

    * QX = Gander, (T.-N.) 
    * HX = Halifax (maintenant Dartmouth)  
    * UL = Montréal  
    * QB = Québec 
    * XK = Rimouski  
    * TO = Toronto  
    * WG = Winnipeg  
    * NT = Territoire du Nord-ouest  
    * VR = Vancouver  
    * CN = Canada  
    * US = États-Unis 
* __HH__ : Représente l'heure de réception du bulletin.

Le nom de fichier suit cette nomenclature :

BULLETIN_REGION_CODE1__CODE2

Exemple :

SOVD02_CWOW_250553___14352

Il n'y a pas de liste complète des bulletins publiés sur le Datamart du SMC.
Cependant, une fois le type de bulletin identifié dans le répertoire de
l'OMM, vous pouvez aisément vérifier si ce bulletin est disponible grâce à
l'[utilitaire de recherche de bulletins](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_fr.pdf).

### Avertissements météo

Les codes de 2 lettres pour les bulletins d'avertissements météo sont :
* __WA__ : Airmet
* __WC__ : Cyclone
* __WE__ : Tsunami
* __WF__ : Tornade
* __WH__ : Inondation
* __WL__ : Smog
* __WO__ : Spécial
* __WO__ : Ouragan
* __WP__ : Weather
* __WS__ : SIGMET
* __WT__ : Tropical
* __WU__ : Orage
* __WV__ : Volcanique
* __WW__ : Météorologique

Un exemple d'avertissement météo reçu le 9 juin 2010 à 07 UTC émit par le 
bureau d'Halifax est :

[https://dd.meteo.gc.ca/bulletins/alphanumeric/20100609/WW/CWHX/07/WWCN14_CWHX_090744___64416](https://dd.meteo.gc.ca/bulletins/alphanumeric/20100609/WW/CWHX/07/WWCN14_CWHX_090744___64416)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




























