[In English](readme_hurricanes-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Trajectoires d'ouragans](readme_hurricanes_fr.md) > Trajectoires d'ouragans sur le Datamart du SMC

# Données des trajectoires d'ouragans

Cette page décrit les données des [trajectoires d'ouragans](readme_hurricanes_fr.md).

Le Centre canadien des ouragans fournit des fichiers en format shapefile dans le cadre des prévisions régulières lors de la saison des ouragans.

Les fichiers permettront aux utilisateurs de tracer l'itinéraire des tempêtes prévues dans un système de cartes géographiques de leur choix. Il y a quatre formats shapefiles (*.shp) qui sont produits et comportent chacun un bulletin de prévisions sur 6 heures lorsque des tempêtes d'origine tropicale menace ou risque de menacer le territoire canadien.

Les trajectoires d'ouragans émises par le Centre canadien de prévision des ouragans sont publiées sur le Datamart du SMC. Ces données sont rendues disponibles en mode expérimental afin d'offrir aux usagers une opportunité d'ingérer et de tester les données en temps réel. Le service sera fourni au mieux de nos possibilités mais veuillez noter qu'il existe une possibilité non négligeable d'interruptions occasionnelles non-annoncées et non-remédiées de ce service expérimental de données, et ce jusqu'à nouvelle annonce.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier shapefile.

Les fichiers shapefile sont disponibles à cette adresse :
 
* [https://dd.meteo.gc.ca/trajectoires/hurricane/shapefile/{nom-tempête}/](https://dd.meteo.gc.ca/trajectoires/hurricane/shapefile)

où :
* __nom-tempête__ est le nom de la tempête en lettres majuscules (p. ex. « BERTHA »)

30 avril : l'historique est effacé

## Nomenclature des répertoires et noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

La convention régissant les noms de fichiers est la suivante :

YYYYMMDD_HHMMZ_STORM-NAME.TYPE.shp

où :

* __YYYYMMDD__HHMM__ : Date d'émission de la prévision (UTC).
* __Z__ : Chaîne de caractère constante indiquant le fuseau horaire Zulu (code pour UTC).
* __STORM-NAME__ : Nom de la tempête (p. ex. BERTHA - ouragan, post-tropical, etc.).
* __TYPE__ : Type de fichier shapefile :

    * « pts » pour points, qui contient majoritairement des données/attributs
    * « lin » pour les segments de ligne qui relient les points de suivi de la prévision
    * « rad » pour les informations des rayons de prévisions de vent (quadrants)
    * « err » pour les informations sur l'erreur de prévision de trajectoire (« cône d'erreur »)

## Contenu du fichier

Il y aura 2 types de fichiers, point et ligne.

Lorsque l'utilisateur interroge le fichier shapefile par points, le contenu de
chaque colonne est donné comme suit :

| Élément   |  Définition    |
|------------|----------------|
|ADVDATE |	heure d'émission de la prévision en format YYMMDD/HHMM (UTC) |
|BASIN |	Région - 'al' pour l'Atlantique (toujours 'al' pour Centre canadien des ouragans)|
|DATELBL |	Étiquette à utiliser sur une carte|
|ERRCT |	Rayon d'erreur de suivi de la prévision en miles nautiques qui, lorsque cartographié, représente la zone/le cône d'incertitude moyenne dans la prévision de suivi (centre de la tempête) |
|LAT |		Latitude de la position du centre de la tempête|
|LON |		Longitude de la position du centre de la tempête|
|MAXWND |	Intensité - vitesse maximale soutenue des vents en noeuds (miles nautiques à l'heure).  Pour obtenir des km/h, multiplier par 1,84 |
|MSLP |		Pression minimale au centre, en hectopascals
|RXXYY Columns |	douze colonnes représentent les rayons du vent (R) en milles nautiques pour 3 catégories primaires de prévisions : 34 (coups de vent de 34 noeuds),  48 (force de vents de tempête de 48 noeuds) et 64 (force du vent d'ouragans de 64 noeuds). NE, SE, SO, NO représentent les 4 principaux quadrants géographiques entourant la tempête. |
|STORMNAME |	Nom de la tempête - p. ex., BERTHA|
|STORMTYPE |	Type de tempête au moment de l'émission de la prévision : DT = dépression tropicale; TT = tempête tropicale; OU = ouragan; PT = post-tropicale |
|TAU |		Heure prévue à partir de l'heure d'émission, p. ex., 48 = 48 heures/2 jours|
|TCDVLP	|	État de la tempête au moment de l'heure de prévision TAU (DT, TT, OU, PT)|
|TIMEZONE |	fuseau horaire local reflétant la région géographique d'une tempête active|
|VALIDTIME |	Temps pendant lequel la prévision à l'heure TAU est valide. En format DD/HHMM (UTC)|
|TIMESTAMP |     Format ISO pour le paramètre VALIDTIME. Format:  YYYY-MM-DDTHH:MMZ|

Les éléments des fichiers shapefile 'lin' ont les mêmes définitions que les éléments des fichiers 'pts'.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
