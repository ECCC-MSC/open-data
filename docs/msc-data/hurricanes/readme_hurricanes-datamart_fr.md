[In English](readme_hurricanes-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Trajectoires d'ouragans](readme_hurricanes_fr.md) > Trajectoires d'ouragans sur le Datamart du SMC

# Données des trajectoires d'ouragans

Cette page décrit les données des [trajectoires d'ouragans](readme_hurricanes_fr.md) disponibles sur le Datamart du SMC en format GeoJSON lorsque des tempêtes d'origine tropicale menacent ou risquent de menacer le territoire canadien.

Les trajectoires d'ouragans dans la région atlantique, provenant du [Centre national des ouragans de la NOAA](https://www.nhc.noaa.gov/) sont rediffusées par le [Centre canadien des ouragans](https://www.canada.ca/fr/environnement-changement-climatique/services/previsions-faits-ouragans/produits.html) et sont aussi disponibles en format GeoJSON. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont disponibles sur le Datamart du SMC, à cette adresse :

     * [https://dd.meteo.gc.ca/today/hurricanes/](https://dd.meteo.gc.ca/today/hurricanes)

## Nomenclature des noms de fichiers

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Hurricane_{NAME}.json`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et minute de l'émission des données
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Hurricane__ : Chaîne de caractères constante indiquant le nom du produit contenu dans les fichiers, soit les trajectoires d'ouragans
* __NAME__ :  Chaîne de caractères constante indiquant le nom de l'ouragan
* __json__ : Chaîne de caractères constante indiquant le format GeoJSON

Ex: `20240708T2100Z_MSC_Hurricane_ANDREA.json`

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
