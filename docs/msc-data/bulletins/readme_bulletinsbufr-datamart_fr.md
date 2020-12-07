[In English](readme_bulletinsbufr-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Bulletins binaires](readme_bulletins_fr.md) > Bulletins binaires sur le Datamart du SMC

# Données des bulletins en format binaire

Cette page décrit les données des [bulletins](readme_bulletins_fr.md) en format binaire.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. 
Les bulletins BUFR sont disponibles via le  protocole HTTP avec un fureteur standard. 

Les données sont accessibles à l’adresse suivante :

* [https://dd.weather.gc.ca/bulletins/alphanumeric/{YYYYMMDD}/IO](https://dd.weather.gc.ca/bulletins/alphanumeric)

* [https://dd.weather.gc.ca/bulletins/alphanumeric/{YYYYMMDD}/IU](https://dd.weather.gc.ca/bulletins/alphanumeric)

où :

__YYYYMMDD__ : Date de l’émission du bulletin BUFR en UTC.

Tout comme les bulletins alphanumériques, les bulletins BUFR sont conservés pendant six mois.

__Note__: Dans le contexte du passage des bulletins alphanumériques aux bulletins BUFR, les bulletins binaires sont distribués dans le même répertoire que les bulletins alphanumériques.
	
## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

Les noms des fichiers ont la forme :

IUnB0x_Ciii_DDHHHH__BUFR

où :

* __n__ : Type de bulletin 
* __x__ : Emplacement dans la matrice 
* __iii__ : Numéro d’identification de la station de Transport Canada
* __DD__ : Date du bulletin
* __HHH__ : Heure standard du bulletin

Exemple :

IUKB02_CWLT_130000__BUFR

## Contenu des dossiers

Ces bulletins font partie d’un réseau mondial d’échange de données de radiosonde mené sous les auspices de l’Organisation météorologique mondiale (OMM). 
Ces données de radiosonde sont recueillies et formatées selon les normes gérées par l’OMM au nom de ses membres. Les données sont formatées au moyen du 
code BUFR (4e édition - FM94), que l’on trouve dans le guide sur les codes de l’OMM (OMM - No 306), volume I.2 : [https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/VolumeI.2.html](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/VolumeI.2.html).  

Le modèle et les règles de codage du format BUFR pour ces données sont décrits dans le règlement B/C25 : 
[https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC25-TEMP.pdf](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC25-TEMP.pdf)
[https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC20-PILOT.pdf](https://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI2/LatestVERSION/BC20-PILOT.pdf)

Les documents binaires peuvent être consultés ou convertis en code ASCII, entre autres, au moyen d’un logiciel conforme au code BUFR. Plusieurs centres 
météorologiques et établissements de recherche météorologiques importants donnent accès au logiciel BUFR, libre de redevances. 
Le SMC donne accès à libECBUFR, une bibliothèque en format BUFR comprenant des outils pour coder ou décoder du format BUFR à ASCII et l’inverse: 
https://github.com/ECCC-MSC/libecbufr
Une fois la bibliothèque libECBUFR installée, la ligne de commande suivante permet de produire une version lisible des données : 
bufr_decoder -inbufr data.bufr 
où, data.bufr est le fichier BUFR.

Davantage d’information sont disponibles  quant à l’installation et à l’utilisation de libECBUFR dans la foire aux questions suivante : 
[https://github.com/ECCC-MSC/libecbufr/wiki/FAQ](https://github.com/ECCC-MSC/libecbufr/wiki/FAQ)

## Utilitaire de recherche de bulletins

Pour faciliter la recherche de bulletins, veuillez utiliser notre utilitaire de recherche de bulletins qui se trouve sur le Datamart :
[https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl](https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl)

Des informations détaillées, avec des exemples d’utilisation de ce script se trouvent dans le [document PDF](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_fr.pdf). 

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).




























