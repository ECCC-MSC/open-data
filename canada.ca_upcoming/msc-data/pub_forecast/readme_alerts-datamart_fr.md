[In English](readme_alerts-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > PAC sur le Datamart du SMC

# Données d'avertissements météorologiques XML dans le format du Protocole d'alerte commun (PAC)

Cette page décrit les [données d'avertissements météorologiques dans le format du Protocole d'alerte commun (PAC)](readme_alerts_fr.md) disponibles en format XML.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage-overview/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier XML. Nous vous recommandons d’automatiser le téléchargement en le scriptant avec wget (lien externe, anglais) ou un programme équivalent. Pour plus d’information sur wget, consultez les notes d’utilisation.

Les bulletins sont disponibles à cette adresse:

https://dd.meteo.gc.ca/alerts/cap/

Un historique des données de un mois est conservé dans ce répertoire.

Un ensemble de fichiers en format Shapefile contenant les informations géographiques 
des emplacement des prévisions, pour tous les messages en format PAC, peut être trouvé 
dans ce répertoire:

https://dd.meteo.gc.ca/meteocode/geodata/

Les ensembles de fichiers Shapefile a cet endroit sont les mêmes qui sont 
utilisés dans l'environnement opérationnel où les avertissements 
d'ECCC sont créés. Les ensembles Shapefiles ont des numéros
de version afin de suivre l'évolution des emplacements utilisés dans cet 
environnement. À partir de la version 5.0.3, la date du début de validité 
de l'ensemble sera incluse dans la documentation.


## Nomenclature des noms de fichiers 

Les fichiers sont regroupés dans une arborescence basée sur la date et le 
code du bureau responsable (voir note1) de l'alerte. Font exception les alertes 
de tornade et d'orage violent qui sont rassemblées, selon la désignation LAND 
ou WATR (voir note2) plutôt que selon le bureau responsable.
Le répertoire LAND contient les fichiers CAP-XML pour tous les avertissements 
de tornade et d'orage violent qui sont émis sur les zone terrestres du Canada. 
Le répertoire WATR contient les fichiers CAP-XML pour tous les avertissements de 
tornade qui sont émis sur les plans d'eau du Canada.

Note1: Le terme bureau "responsable" est utilisé pour le distinguer du bureau "émetteur" 
qui envoie l'alerte. En temps normal, le bureau "responsable" est aussi le 
bureau "émetteur". Cependant, dans des situations de contingence, le bureau "émetteur"
peut être différent. Le bureau "responsable" est en charge du routage et la distribution
 des avertissements (le bon message à la bonne place) et le bureau "émetteur" est utilisé
pour la compatabilité et l'évaluation de la performance.  

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

**Le tableau ci-dessus se retrouve à l'adresse suivante : https://wiki.cmc.ec.gc.ca/images/b/b2/Offices_transm_alerts.docx**


Note2: Ce ne sont pas toutes les zones WATR au Canada qui sont configuées pour 
les avertissements de tornade. Aucune zone WATR au Canada n'est configurée pour 
les avertissements d'orage violent.

NOTE: TOUTES LES HEURES SONT EN UTC.

__Les répertoires suivent la nomenclature :__

alerts/cap/YYYYMMDD/EEEE/hh/

avec:

* __YYYYMMDD__ : jour de la transmission de l'avertissement.
* __EEEE__ : Code de 4 lettres du bureau responsable, excepté les désignations LAND ou 
  WATR réservées aux alertes de tornade ou d'orage violent.
* __hh__ : heure de transmission de l'avertissement (UTC).

__Les fichiers suivent la nomenclature :__

avec:
                                                                                                                        
* __T__ : caractère constant. Spécification littérale du manuel WMO-386 comme préfixe 
  pour un fichier suivant cette convention de nom.          
* __BBBBNN (pour les alertes de tornades et orages violents)__ : 4 lettres et 2 chiffres 
  représentant 2 lettres pour le code de province, de plan d'eau ou de territoire, 2 lettres pour 
  le code de pays et 2 codes numériques digitaux fixés à 00 pour suivre le format 
  de la structure de fichier. Ex: ABCN00.
  BBBBNN (pour toutes les autres alertes): 4 lettres et 2 nombres représentant l'en-tête 
  traditionnelle des bulletins WMO sur les circuits de transmission WMO. Ex: WWCN11.

Dans le cas où les 2 lettres représentent un code de province ou de plan d'eau, la liste des codes de 
province ou de territoire comprend:
  
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
 
* __C__: caractère constant. Spécifié par l'OMM comme préfixe pour CCCC.                                                           
* __EEEE__ : code de 4 lettres du bureau responsable (CWAO, CWTO, etc.), excepté les 
  désignations LAND ou WATR réservées aux alertes de tornade ou d'orage violent.
* __YYYYMMDDhhmm__ : date et heure de transmission de l'avertissement (UTC). 
* __##########__ : les 10 chiffres numériques identifiant le message PAC, trouvés dans le fichier, permettant d'en assurer
  l'unicité

Exemples de nomenclature de fichiers :

* T_WWCN11_C_CWTO_201608041031_8263481729.cap: bulletin d'avertissement de type WWCN11 pour le 
  bureau responsable CWTO (Centre de prévision des tempêtes de l'Ontario). 
  L'alerte a été transmise le 4 août 2016 à 1031 secondes UTC.

* T_ABCN00_C_LAND_201608041521_0615296639.cap: bulletin d'avertissement de type LAND pour la 
  province d'Alberta (AB). Cette alerte pouvait être soit un avertissement de tornade ou 
  d'orage violent. 
  L'alerte a été transmise le 4 août 2016 à 1521 secondes UTC.

* T_QCCN00_C_WATR_201608041521_1920353215.cap: bulletin d'avertissement de type WATR pour la 
  province de Québec (QC). Cette alerte était un avertissement de tornade (les alertes 
  d'orage violent ne sont pas émises sur les plans d'eau).
  L'alerte a été transmise le 4 août 2016 à 1521 secondes UTC.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).







