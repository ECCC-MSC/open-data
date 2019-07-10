[In English](readme_naefs-datamartxml_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > SPENA

# Données XML du Système de Prévisions d'Ensemble Nord-Américain (SPENA)

Cette page décrit les données [système de prévisions d'ensemble Nord-Américain](readme_naefs_fr.md) disponibles en format GRIB2.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les fichiers XML de SPENA se trouvent à l'adresse suivante :

* [https://dd.meteo.gc.ca/ensemble/naefs/xml](https://dd.meteo.gc.ca/ensemble/naefs/xml)

Un historique de 30 jours de prévisions est conservé dans ce répertoire.

## Nomenclature des répertoires des fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

La structure des répertoires est basée sur la date d'intégration et la
variable contenu dans les fichiers XML. Ils suivent la nomenclature   
suivante:

* https://dd.meteo.gc.ca/ensemble/naefs/xml/AAAAMMJJ/ZZ/VARIABLE/TYPE

où :

* __AAAAMMJJ__ : Date du début d'intégration de la prévision
* __ZZ__ : Heure UTC d'intégration de la prévision. Peut être '00' ou '12'
* __VARIABLE__ : Élément du temps dans ce répertoire. Voir la section 'Liste
des variables' plus bas pour la liste complète des variables.
* __TYPE__ : Type de données. Pour l'instant, seules les sorties directes de
modèles sont disponibles ('raw').

Exemple : pour la prévision à 12Z du 7 mai 2010, les données bruts (raw)
pour la vitesse du vent à la surface de seront dans le répertoire:

[https://dd.meteo.gc.ca/ensemble/naefs/xml/20100507/12/WIND-SFC/raw](https://dd.meteo.gc.ca/ensemble/naefs/xml/20100507/12/WIND-SFC/raw)

## Nomenclature des noms de fichiers 

NOTE : TOUTES LES HEURES SONT EN UTC.

La nomenclature des fichiers est la suivante :

AAAAMMJJHH_GEPS-NAEFS-TYPE_EMPLACEMENT_PROVETAT_PAYS_VAR_DEB-FIN.xml.bz2

où :

* __AAAA__ : Année de la prévision, 4 chiffres.
* __MM__ : Mois de la prévision, 2 chiffres (janvier = 01).
* __JJ__ : Jour de prévision, 2 chiffres.
* __HH__ : Heure du début la prévision, 2 chiffres (00 ou 12 - représentant
l'heure en UTC).
* __GEPS-NAEFS__ : Un chaîne de caractères constante qui indique le modèle GEM
pour les EPSgramme (GEPS) dans le cadre du projets SPENA (en anglais,
l'acronyme est NAEFS).
* __TYPE__ : Peut prendre la valeur 'RAW' (brute) pour les données brutes du
modèle ou 'BC' pour les données débiaisées. (présentement seul RAW est
disponible).
* __EMPLACEMENT__ : Nom de l'emplacement pour lequel la prévision est émise.
* __PROVETAT__ : Province (Canada) ou État (États-Unis, Mexique) de
l'emplacement pour lequel la prévision est émise. Code de 2 lettres.  Pour
les autres pays le
code 'XX' est utilisé. Vous pouvez télécharger la liste anglaise de
correspondance des codes ici : 
[http://www.state.ia.us/tax/forms/84055.pdf](http://www.state.ia.us/tax/forms/84055.pdf)
* __PAYS__ : Pays de l'emplacement pour lequel la prévision est émise.
CA=Canada,
US=États-Unis, MX=Mexique, etc. Pour une liste complète des pays, voir la
section « Liste des pays » à la fin de ce fichier.
* __VAR__ : Variables (voir section suivante pour la liste).
* __DEB__ : Début de l'intervalle (en heures après la date de prévision) pour
lequel des prévisions sont émises.
* __FIN__ : Fin de l'intervalle (en heures après la date de prévision) pour
lequel des prévisions sont émises.

Exemple :

2010051000_GEPS-NAEFS-RAW_LONDON_ON_CA_MSLP_000-384.xml.bz2

Ce fichier représente les données des modèles pour la date du 10 mai 2010
à 00UTC (2010051000), en format brut (RAW) pour la ville de London 
(LONDON) en Ontario (ON) au Canada (CA). On y retrouvera les valeurs pour
la pression au niveau de la mer (MSLP) pour les 384 premières heures de   
prévisions (000-384). C'est un fichier XML (xml) compressé à l'aide de    
l'algorithme bzip2 (bz2).

Exemple d'URL pour un fichier sur internet :

[https://dd.meteo.gc.ca/ensemble/naefs/xml/20100507/00/MSLP/raw/2010050700_GEPS-NAEFS-RAW_LONDON_ON_CA_MSLP_000-384.xml.bz2](https://dd.meteo.gc.ca/ensemble/naefs/xml/20100507/00/MSLP/raw/2010050700_GEPS-NAEFS-RAW_LONDON_ON_CA_MSLP_000-384.xml.bz2)

## Contenu des fichiers

Les fichiers XML ont été compressés avec l'algorithme bzip2. Pour 
décompresser ces fichiers, vous pouvez utiliser le logiciel bunzip2 
(GNU/Linux, Mac OS X) ou encore 7-zip (Windows). Les fichiers sont encodés
en format UTF-8.

Chaque fichier est composé d'une section d'en-tête (<header>) indiquant la
localisation de l'emplacement, les dates et heures de début et fin des    
prévisions, la variable concernée, l'unité utilisé pour le représenter    
ainsi que la date et l'heure de création du fichier.

Viennent ensuite plusieurs sections pour la prévision (<forecast>). 
Chacune de ces sections correspond à une heure de prévision précise. Elles
contiennent chacune une série d'étiquettes <model> indiquant pour chaque  
modèle disponible la valeur de la variable pour ce modèle à cette heure de
prévision (voir la liste des modèles dans la section précédente « Liste   
des modèles ».
Note: Certains modèles n'ont pas de prévisions pour certaines heures.

Le contenu des fichiers est sous la forme :
```xml
<?xml version='1.0' encoding='UTF-8'?>
   <naefs_spena_forecast>
      <header>
         <location description="XXXXXXXXX" pays_country="XX" province_state="XX"/>
         <valid-begin-time>XXXXXXXX</valid-begin-time>
         <valid-end-time>XXXXXXXX</valid-end-time>
         <forecast_element no="X" type="XX" niveau_level="X" titre_francais="XXXXXXXXXXXXXXXXXX" unite_francaise="XXX" title_english="XXXXXXXXXXXXX" unit_english="XXX"/>
        <model_description>
          <model id='1' model='GEM' member='000' center='CMC' domain='global' data_type='RAW' member_type='control'/>
          <model id='2' model='GEM' member='001' center='CMC' domain='global' data_type='RAW' member_type='member'/>
          <model id='3' model='GEM' member='002' center='CMC' domain='global' data_type='RAW' member_type='member'/>
               ...
        </model_description>
         <creation_date>XXXXXXXXXXX</creation_date>
      </header>
   <forecast forecast_hour='XXX' valid_time='XXXXXXXXXX'>
      <model id='1'>XXX</model>
               ...
   </forecast>
   <forecast forecast_hour='XXX' valid_time='XXXXXXXXXX'>
      <model id='1'>XXX</model>
      <model id='2'>XXX</model>
               ...
   </forecast>
         ...
</naefs_spena_forecast>
```

## Liste des variables

Les fichiers XML sont produits pour 10 variables :
* Pression moyenne au niveau de la mer (MSLP)
* Accumulation totale de précipitation à la surface (APCP-SFC)
* Couvert nuageux total (TCDC)
* Vitesse du vent à 200 hpa (WIND-200HPA)
* Hauteur géopotentielle à 500 hpa (HGT-500HPA)
* Épaisseurs entre 1000-500 hpa (LAYER-1000-500HPA)
* Température de l'air à la surface (TMP-SFC)
* Humidité relative à la surface (RELH-SFC)
* Vitesse du vent à la surface (WIND-SFC)
* Direction du vent à la surface (WDIR-SFC)

Vous trouverez une liste en format XML des variables qui contient le nom  
du répertoire associé, les descriptions et les unités, en français et 
anglais à cette adresse :

[https://dd.meteo.gc.ca/ensemble/doc/naefs/xml/elements.xml](https://dd.meteo.gc.ca/ensemble/doc/naefs/xml/elements.xml)

## Emplacements disponibles

Les sorties XML des prévisions d'ensemble SPENA sont des interpolations
de points de grille des prévisions aux coordonnées latitude-longitude
de 540 emplacements :
* 273 au Canada
* 137 aux États-Unis
* 74 au Mexique
* 56 dans les tropiques et au Groenland

Vous trouverez une liste en format XML des emplacements qui contient :
* Le nom de l'emplacement
* La province ou l'État
* Le pays
* Les codes, lorsque qu'applicables: NAEFS, WMO, IATA, ICAO
* La longitude, la latitude et l'altitude (notez que l'altitude est 
manquante pour quelques emplacements)

Cette liste se trouve dans le fichier suivant :

[https://dd.meteo.gc.ca/ensemble/doc/naefs/xml/locations.xml](https://dd.meteo.gc.ca/ensemble/doc/naefs/xml/locations.xml)

La correspondance pour les codes de 2 lettres pour les provinces ou les
États peut-être trouvée dans ce document PDF :

[http://www.state.ia.us/tax/forms/84055.pdf](http://www.state.ia.us/tax/forms/84055.pdf)

## Support 

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
