[In English](readme_alerts-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Alertes](readme_alerts_fr.md) > Alertes sur le Datamart du SMC

# Données d'avertissements météorologiques XML dans le format du Protocole d'Alerte Commun (PAC)

Cette page décrit les [données d'avertissements météorologiques dans le format du Protocole d'alerte commun (PAC)](readme_alerts_fr.md) disponibles en format XML.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML.

Les __bulletins sont disponibles__ à cette adresse :

[https://dd.meteo.gc.ca/today/alerts/cap/{YYYYMMDD}/{EEEE}/{hh}/](https://dd.meteo.gc.ca/today/alerts/cap)

avec :

* __YYYYMMDD__ : jour de la transmission de l'avertissement.

* __EEEE__ : Code de 4 lettres du bureau responsable, excepté les désignations LAND ou WATR réservées aux alertes de tornade ou d'orage violent.

* __hh__ : heure de transmission de l'avertissement (UTC).

* Les fichiers sont regroupés dans une arborescence basée sur la date et le code du bureau responsable (voir note1) de l'alerte. Font exception les alertes de tornade et d'orage violent qui sont rassemblées, selon la désignation LAND ou WATR (voir note2) plutôt que selon le bureau responsable.

* Le répertoire LAND contient les fichiers CAP-XML pour tous les avertissements de tornade, d'orage violent et de tsunami qui sont émis sur les zone terrestres du Canada.
 
* Le répertoire WATR contient les fichiers CAP-XML pour tous les avertissements de tornade qui sont émis sur les plans d'eau du Canada.

* Ce ne sont pas toutes les zones WATR au Canada qui sont configuées pour les avertissements de tornade. Aucune zone WATR au Canada n'est configurée pour les avertissements d'orage violent. 

Un ensemble de __fichiers en format Shapefile contenant les informations géographiques des emplacement des prévisions__, pour tous les messages en format PAC, peut être trouvé dans ce répertoire :

[https://dd.meteo.gc.ca/today/meteocode/geodata/](https://dd.meteo.gc.ca/today/meteocode/geodata/)

Les ensembles de fichiers Shapefile à cet endroit sont les mêmes qui sont utilisés dans l'environnement opérationnel où les avertissements d'ECCC sont créés. Les ensembles Shapefiles ont des numéros de version afin de suivre l'évolution des emplacements utilisés dans cet environnement.

## Nomenclature des noms de fichiers 

__Les fichiers suivent la nomenclature :__

T_BBBBNN_C_EEEE_YYYYMMDDhh_##########.cap

avec :
    
* __T__ : caractère constant. Spécification littérale du manuel WMO-386 comme préfixe 
  pour un fichier suivant cette convention de nom.          
* __BBBBNN (pour les alertes de tornades et orages violents)__ :  4 lettres et 2 chiffres représentant 2 lettres pour le code de province, de plan d'eau ou de territoire, 2 lettres pour le code de pays et 2 codes numériques digitaux fixés à 00 pour suivre le format de la structure de fichier. Ex: ABCN00.
* __BBBBNN (pour toutes les autres alertes)__ : 4 lettres et 2 nombres représentant l'en-tête traditionnelle des bulletins WMO sur les circuits de transmission WMO. Ex: WWCN11.

  Dans le cas où les 2 lettres représentent un code de province ou de plan d'eau, la liste des codes de province ou de territoire comprend :
  
    * BC – Colombie-Britannique
    * AB - Alberta
    * SK - Saskatchewan
    * MB - Manitoba
    * ON – Ontario
    * QC - Québec
    * YT - Yukon
    * NU - Nunavut
    * NT - Territoires du Nord-Ouest
    * NS – Nouvelle-Écosse
    * NB – Nouveau-Brunswick
    * PE – Île-du-Prince-Édouard
    * NL – Terre-neuve-et-Labrador
    * GL - Grands lacs
    * PC - Eaux du Pacifique
    * AT - Eaux de l'Atlantique
    * AC - Eaux de l'Arctique
 
* __C__ : caractère constant. Spécifié par l'OMM comme préfixe pour CCCC.                                     
* __EEEE__ : code de 4 lettres du bureau responsable (CWAO, CWTO, etc.), excepté les désignations LAND ou WATR réservées aux alertes de tornade ou d'orage violent.
* __YYYYMMDDhhmm__ : date et heure de transmission de l'avertissement (UTC). 
* **'##########'** : les 10 chiffres numériques identifiant le message PAC, trouvés dans le fichier, permettant d'en assurer l'unicité

**Exemples de nomenclature de fichiers** :

* **T_WWCN11_C_CWTO_201608041031_8263481729.cap** : bulletin d'avertissement de type WWCN11 pour le 
  bureau responsable CWTO (Centre de prévision des tempêtes de l'Ontario). 
  L'alerte a été transmise le 4 août 2016 à 1031 secondes UTC.

* **T_ABCN00_C_LAND_201608041521_0615296639.cap** : bulletin d'avertissement de type LAND pour la 
  province d'Alberta (AB). Cette alerte pouvait être soit un avertissement de tornade ou 
  d'orage violent. 
  L'alerte a été transmise le 4 août 2016 à 1521 secondes UTC.

* **T_QCCN00_C_WATR_201608041521_1920353215.cap** :  bulletin d'avertissement de type WATR pour la 
  province de Québec (QC). Cette alerte était un avertissement de tornade (les alertes 
  d'orage violent ne sont pas émises sur les plans d'eau).
  L'alerte a été transmise le 4 août 2016 à 1521 secondes UTC.

## Notes 

* Le terme bureau "responsable" est utilisé pour le distinguer du bureau "émetteur" qui envoie l'alerte. En temps normal, le bureau "responsable" est aussi le bureau "émetteur". Cependant, dans des situations de contingence, le bureau "émetteur" peut être différent. 

* Le bureau "responsable" est en charge du routage et la distribution des avertissements (le bon message à la bonne place) et le bureau "émetteur" est utilisé pour la compatabilité et l'évaluation de la performance.

* Liste des bureaux émetteurs:
  

| Code        |  Name English             |   Name French        |  Acronym English    |  Acronym French  |  City        | Time Zone Code  |
|-------------|---------------------------|----------------------|---------------------|------------------|--------------|-----------------|
| CWUL | Quebec Storm Prediction Centre |centre de prévision des intempéries du Québec|QSPC | CPIQ        | Montréal     | EST5EDT         |
| CWEG |Prairie and Arctic Storm Prediction Centre|centre de prévision des intempéries des Prairies et de l'Arctique|PASPC|CPIPA|Edmonton|MST7MDT|
| CWNT |Prairie and Arctic Storm Prediction Centre|centre de prévision des intempéries des Prairies et de l'Arctique|PASPC|CPIPA|Edmonton|MST7MDT|
| CWWG |Prairie and Arctic Storm Prediction Centre|centre de prévision des intempéries des Prairies et de l'Arctique|PASPC|CPIPA|Winnipeg|CST6CDT|
| CWVR |Pacific and Yukon Storm Prediction Centre|centre de prévision des intempéries de la région du Pacfique et du Yukon|PSPC|CPIP|Vancouver|PST8PDT|
| CWTO |Ontario Storm Prediction Centre|centre de prévision des intempéries de l'Ontario|OSPC|CPIO|Toronto|EST5EDT|
| CYQX |Newfoundland and Labrador Weather Office|centre de prévision des intempéries de Terre-Neuve-et-Labrador|NLWO|CPITNL|Gander|NST3:30NDT|
| CWAO |Canadian Meteorological Centre|Centre météorologique canadien|CMC|CMC|Montréal|EST5EDT|
| CWIS |Canadian Ice Service|Service canadien des glaces|CIS|SCG|Ottawa|EST5EDT|
| CWHX |Atlantic Storm Prediction Centre|centre de prévision des intempéries de la région de l'Atlantique|ASPC|CPIRA|Dartmouth|AST4ADT|

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).







