[In English](readme_en.md)

![ECCC logo](img_eccc-logo.png)

# Documentation des données ouvertes du Service météorologique du Canada

Le Service météorologique du Canada met à la disposition du secteur privé, des universitaires et du grand public, les données météorologiques, climatiques, hydrologiques et environnementales.

## Données ouvertes disponibles

Les **[données ouvertes du Service météorologique du Canada](msc-data/readme_fr.md)** fournissent des renseignements à jour sur les conditions météorologiques et environnementales, l'eau et le climat passés, présents et futurs au Canada et dans le monde. Les principales catégories de données disponibles sont :

* Alertes météorologiques, conditions actuelles et prévisions publiques
* Observations météorologiques, hydrologiques et environnementales et données prévisionnelles
* Données climatiques
  
## Accès aux données

L'accès aux données ouvertes disponibles sur le Datamart du SMC et sur GeoMet du SMC est anonyme et gratuit. Les services de données ouvertes disponibles sont :

* **[GeoMet du SMC](msc-geomet/readme_fr.md)**
    * API pour accéder aux données brutes et produits
    * Visualiser et animer les données météorologiques
    * Intégrer les données sur des cartes web, des applications mobiles et logiciels de bureau
    * Services web géospatiaux pour rogner, reprojeter et convertir les données, et davantage
* **[Datamart du SMC](msc-datamart/readme_fr.md)**
    * Données brutes et produits disponibles sur un serveur accessible sur le Web
    * Service de notifications en temps réel et récupération des données
* **[Services à recouvrement de coûts](cost-recovered/readme_fr.md)**
    * Récupération de données archivées
    * Fils de données dédiés avec support 24/7

## Utilisation et tutoriels

Aperçu, exemples et tutoriels pour accéder aux données ouvertes du Service météorologique du Canada et leur utilisation.

* **[Aperçu de l'utilisation](usage/readme_fr.md)**

**Tutoriels** :

* **Accéder et utiliser les données dans le logiciel de bureau QGIS** :
    * [Ajouter, effectuer des requêtes et animer des couches WMS](usage/tutorial_WMS_QGIS_fr.md)	
    * [Ajouter et effectuer des requêtes aux couches OGC API Features](usage/tutorial_OAFeat_QGIS_fr.md)
    * [Ajouter des données brutes](usage/tutorial_raw-data_QGIS_fr.md)
* **[Créer des cartes interactives sur le web avec OpenLayers et Leaflet](usage/tutorial_web-maps_fr.md)** :
    * Ajouter des couches
    * Afficher des boîtes de dialogue
    * Animer des couches temporelles

* **[Créer des graphiques et des tableaux à partir de l'API GeoMet du SMC](usage/tutorial_graphs-tables_fr.md)** :
    * Préparation et soumission de requêtes WMS
    * Création d'un graphique intéractif
    * Afficher un tableau de valeurs de données
    
**Cas d'utilisation** :

* [Arthur : profits anticipés selon la probabilité de précipitation](../usage/use-case_arthur/use-case_arthur_fr/) :
    * **Accéder et utiliser l'API GeoMet du SMC directement dans un script Python**, spécifiquement le standard OGC Web Map Service (WMS) pour créer des tables et graphiques
* [Cathy : suivre les niveaux d'eau aux stations hydrométriques](../usage/use-case_oafeat/use-case_oafeat-script_fr/) :
    * **Accéder et utiliser l'API GeoMet du SMC directement dans un script Python**, spécifiquement le standard OGC API - Features (OAFeat) pour créer des séries temporelles et cartes interactives

**Documentation technique** :

* **[Documentation technique des services web géospatiaux / API](msc-geomet/web-services_fr.md)**
* **[Utiliser GDAL à partir de la ligne de commandes](../usage/tutorial_gdal/tutorial_gdal_fr/)**

## Découverte des données et métadonnées

### Portail du gouvernement ouvert du Canada

Les métadonnées du Service météorologique du Canada sont disponibles sur le [portail du gouvernement ouvert du Canada](https://ouvert.canada.ca/fr/donnees-ouvertes), qui permet aux utilisateurs de rechercher des données ouvertes pertinentes aux Canadiens et Canadiennes, apprendre comment travailler avec les jeux de données et voir ce que les citoyens ont fait avec les données ouvertes dans l'ensemble du pays.

### Le Système d'Information de l'OMM (WMO WIS)

Le [Système d'Information de l'OMM (WMO WIS)](https://community.wmo.int/activity-areas/wis/wis-overview) rend possible la découverte de données météorologiques et hydrologiques faisant autorité et supporte la récupération et l'échange de données entre les Centres de l'Organisation météorologique mondiale (OMM) et leurs usagers. Le catalogue WIS décrit les données et produits disponibles au sein de l'OMM. Les données et produits sont ajoutés au catalogue WIS par le biais de la soumission de métadonnées qui décrivent leur contenu, leur structure et les méthodes d'accès.

Le SMC est un 'Data Collection or Production Centre' (DCPC) pour WIS et rend disponible un service 'Discovery, Access and Retrieval' (DAR) disponible sur [https://api.weather.gc.ca/wis/catalogue/csw](https://api.weather.gc.ca/wis/catalogue/csw). Le service DAR supporte plusieurs interfaces de recherche, tel que par le biais de la spécification 'Catalogue Services for the Web' (CSW) de l'OGC, la spécification 'Search/Retrieval via URL' (SRU), ainsi que le standard 'Open Archives Initiative Protocol for Metadata Harvesting' (OAI-PMH).

## Évènements

Série d'évènements organisés autour des données ouvertes du SMC :

* [Forum de données ouvertes du SMC - 8 Juillet 2019](events/2019-07_open-data-forum_fr.md)
* [Hackathon METEOHACK - 8 au 11 juillet 2019](events/2019-07_hackathon-METEOHACK_fr.md) 

## Licence

La licence d'utilisation finale détermine les conditions d'utilisation des données et des informations. La principale exigence est d'indiquer clairement qu'Environnement et changement climatique Canada est la source des données, [veuillez consulter la licence pour plus de détails](licence/readme_fr.md).

## Foire aux questions

Les questions les plus fréquemment posées au sujet des données ouvertes du SMC sont rassemblées dans une [FAQ](faq/readme_fr.md). Si vous ne trouvez pas la réponse à votre question, n'hésitez pas à nous contacter.

## Votre avis nous intéresse

Afin que la documentation des données ouvertes du Service météorologique du Canada réponde à vos besoins, merci de nous faire part de votre avis en répondant à ce court [questionnaire](https://eccc.sondage-survey.ca/f/s.aspx?s=35b3c882-2af9-488f-ad98-9112d2892b8f&lang=FR).

## Contactez-nous

Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les utilisateurs qui demandent de l'aide sont invités à [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

