[In English](readme_meteocode-datamartxml_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données de prévision meteocode](readme_meteocode_fr.md) > Données XML de prévision meteocode sur le Datamart du SMC

# Données de prévision meteocode en format XML

Cette page décrit les fichiers de langage de balisage météorologique canadien (CMML) qui se trouvent sur le Datamart du SMC. Le CMML est un format XML contenant les prévisions officielles d'Environnement et Changement climatique Canada, interpollées aux heures.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les fichiers pour ces données couvrant le domaine terrestre se trouvent à l'adresse suivante :  
       
[https://dd.meteo.gc.ca/meteocode/{REGION}/cmml/](https://dd.meteo.gc.ca/meteocode)

où 'REGION' peut prendre une des valeurs suivantes :
 
* atl
* ont
* pnr
* pyr
* que  

Un historique des données de un mois est conservé dans ces répertoires.

Les [spécifications du format CMML](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/meteocode/cmml_specification_fr-v3.04.pdf) sont disponibles.

Les régions de prévisions publiques sont définies précisément et peuvent être trouvées dans un fichier géoréférencé en format Shapefile.

Ces fichiers se trouvent ici :

[https://dd.meteo.gc.ca/meteocode/geodata/](https://dd.meteo.gc.ca/meteocode/geodata/)

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les prévisions émises pour chaque province se trouvent dans un répertoire spécifique :
* __atl__ : Nouveau-Brunswick, Nouvelle-Écosse, Île-du-Prince-Édouard, Terre-Neuve-et-Labrador
* __ont__ : Ontario
* __pnr__ : Alberta, Saskatchewan, Manitoba, Territoires du Nord-Ouest, Nunavut
* __pyr__ : Colombie-Britannique, Yukon
* __que__ : Québec


Les noms des fichiers CMML suivent cette nomenclature :

TRANSMIT.FP[A-Z][A-Z][0-9][0-9].MM.DD.HHmmZ[.AMD].xml

où :
    
* MM.DD.HHmm est la date d'émission du bulletin
* Z est une constante qui pour indiquer que l'heure de début de la
      prévision est en temps UTC.
* __AMD__ : Optionnel. Si présent, cela indique que cette prévision est un amendement à la prévision précédente pour cette région.
* **FP[A-Z][A-Z][0-9][0-9]** est un code correspondant à la région de prévision :
     * __Nouveau-Brunswick ('atl')__
        * Jour 1 et 2 :
            * FPHX14: Nouveau-Brunswick 
	    * Jour 3 à 5 :
	        * FPHX54 : Nouveau-Brunswick 
     * __Nouvelle-Écosse ('atl')__
	    * Jour 1 et 2 :
	        * FPHX11 : Nouvelle-Écosse 
	    * Jour 3 à 5 :
	        * FPHX51 : Nouvelle-Écosse 
     * __Île-du-Prince-Édouard ('atl')__
	    * Jour 1 et 2 :
	        * FPHX15 : Île du Prince-Édouard
	    * Jour 3 à 5 :
	        * FPHX55 : Île du Prince-Édouard
     * __Terre-Neuve-et-Labrador ('atl')__
	    * Jour 1 et 2 :
	        * FPHX16 : Terre-Neuve
	        * FPHX17 : Labrador
	    * Jour 3 à 5 :
	        * FPHX56 : Terre-Neuve
	        * FPHX57 : Labrador
     * __Ontario ('ont')__
	    * Jour 1 et 2 :
	        * FPTO11 : Sud de l'Ontario et la région de la Capitale Nationale
	        * FPTO12 : Nord de l'Ontario
	        * FPTO13 : Extrême Nord de l'Ontario
	    * Jour 3 à 5 :
	        * FPTO51 : Sud de l'Ontario et la région de la Capitale Nationale
	        * FPTO52 : Nord de l'Ontario
	        * FPTO53 : Extrême Nord de l'Ontario
     * __Alberta ('pnr')__
	    * Jour 1 et 2 :
	        * FPWG15 : Sud de l'Alberta et parcs des montagnes
	        * FPWG14 : Centre et nord de l'Alberta
	    * Jour 3 à 5 :
	        * FPWG53 : Sud de l'Alberta et parcs des montagnes
	        * FPWG54 : Centre et nord de l'Alberta
     * __Saskatchewan ('pnr')__
	    * Jour 1 et 2 :
	        * FPWG13 : Sud de la Saskatchewan
	        * FPWG14 : Nord de la Saskatchewan
	    * Jour 3 à 5 :
	        * FPWG52 : Saskatchewan
    * __Manitoba ('pnr')__
	    * Jour 1 et 2 :
	        * FPWG11 : Sud du Manitoba
	        * FPWG12 : Centre et nord du Manitoba
	    * Jour 3 à 5 :
	        * FPWG51 : Manitoba
     * __Territoires du Nord-Ouest ('pnr')__
	    * Jour 1 et 2 :
	        * FPNT11 : Grand lac des Esclaves et fleuve Mackenzie
	        * FPNT12 : Delta du Mackenzie et de la côte de l'Arctique
	    * Jour 3 à 5 :
	        * FPNT51 : Grand lac des Esclaves et fleuve Mackenzie
	        * FPNT52 : Delta du Mackenzie et de la côte de l'Arctique
     * __Nunavut  ('pnr')__
	    * Jour 1 et 2 :
	        * FPNT13 : Kivalliq
	        * FPNT14 : Kitikmeot
	        * FPNT15 : Extrême-arctique
	        * FPNT16 : Qikiqtaaluk
	    * Jour 3 à 5 :
	        * FPNT53 : Kivalliq
	        * FPNT54 : Kitikmeot
	        * FPNT55 : Extrême-arctique
	        * FPNT56 : Qikiqtaaluk
     * __Colombie-Britannique et Yukon ('pyr')__
	    * Jour 1 et 2 :
	        * FPVR11 : Côte - sud
	        * FPVR12 : Côte - centre et nord
	        * FPVR13 : Interieur sud-ouest de la Colombie-Britannique
	        * FPVR14 : Districts de Columbia de la Colombie-Britannique
	        * FPVR15 : Districts de Kootenay de la Colombie-Britannique
	        * FPVR16 : Interieur-centre de la Colombie-Britannique
	        * FPVR17 : Sud-est du Yukon et le nord de la Colombie-Britannique
	        * FPVR18 : District de peace river en Colombie-Britannique
	        * FPVR19 : Ouest du yukon et le nord-ouest de la Colombie-Britannique
	    * Jour 3 à 5 :
	        * FPVR50 : Côte de la Colombie-Britannique
	        * FPVR52 : Interieur-centre de la Colombie-Britannique
	        * FPVR54 : Districts de Colombia et de Kootenay de la Colombie-Britannique
	        * FPVR56 : District de Peace River
	        * FPVR58 : Yukon et nord de la Colombie-Britannique
     * __Québec ('que')__
	    * Jour 1 et 2 :
	        * FPCN71 : Ouest du Québec
	        * FPCN72 : Nord du Québec
	        * FPCN73 : Centre du Québec
	        * FPCN74 : Est du Quebec
	        * FPCN75 : Extrême nord du Québec
	    * Jour 3 à 5 :
	        * FPUL55 : Ouest du Québec
	        * FPXK55 : Est du Quebec
	        * FPQB55 : Centre et nord du Québec
	        * FPQB57 : Extrême nord du Québec

__Note__ : L'année de la prévision n'est pas dans le nom de fichier.

Exemple de nom de fichier :

[https://dd.meteo.gc.ca/meteocode/pyr/cmml/TRANSMIT.FPVR11.10.30.2300Z.xml](https://dd.meteo.gc.ca/meteocode/pyr/cmml/TRANSMIT.FPVR11.10.30.2300Z.xml)

Ce fichier contient les prévisions émise par le bureau de Vancouver (répertoire 'pyr' et 'VR' dans le nom de fichier) en langue anglaise pour les jours de prévisions 1 et 2 ('11') qui débute le 30 octobre à 2300 UTC ('10.30.2300Z') en format CMML ('.xml').

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).



