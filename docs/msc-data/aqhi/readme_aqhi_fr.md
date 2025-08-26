[In English](readme_aqhi_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > CAS

# Données et produits d'observations et prévisions qui sont générés pour le programme Cote Air Santé (CAS)

La **Cote air santé CAS** est une échelle conçue pour quantifier la qualité de l'air dans une région donnée, sur une échelle de 1 à 10. La cote 10+ indique que la pollution de l'air est très élevée. La Cote air santé comprend également une catégorie décrivant le risque pour la santé correspondant au nombre indiqué risque faible, modéré, élevé ou très élevé . La Cote air santé est calculée en fonction des risques relatifs que représente une combinaison de polluants atmosphériques courants connus pour leurs effets néfastes sur la santé humaine, tels que l'ozone troposphérique, les matières particulaires et le dioxyde d'azote. La formulation de la Cote air santé rend uniquement compte du risque pour la santé aigu ou à court terme contact en heures ou en jours au maximum .
Cette formulation pourrait changer avec le temps, pour rendre compte d'une nouvelle compréhension des effets de la pollution atmosphérique sur la santé. La Cote air santé est calculée à partir de données observées en temps réel, sans vérification contrôle de la qualité.

## Accès

### Comment accéder aux données

Ces données sont respectivement disponibles sur les API / services web [GeoMet du SMC](../../msc-geomet/readme_fr.md) et le serveur de données [Datamart du SMC](../../msc-datamart/readme_fr.md) :

* [Données disponibles via les services web géospatiaux GeoMet-Météo](readme_aqhi-geomet_fr.md)
* [Données disponibles sur les services web géospatiaux GeoMet-OGC-API du SMC](https://api.meteo.gc.ca/collections) :
    * [CAS - Observations](https://api.meteo.gc.ca/collections/aqhi-observations-realtime)
    * [CAS - Prévisions](https://api.meteo.gc.ca/collections/aqhi-forecasts-realtime)
* [Données pour la CAS, disponibles en format GeoJSON sur HPFX, le serveur alternatif du Datamart du SMC](readme_aqhi-datamartjson_fr.md)
* [Données pour la CAS, disponibles en format CSV sur le Datamart du SMC](readme_aqhi-datamartcsv_fr.md), dont des données de prévisions d'espèces chimiques provenant de modèles numériques de qualité de l'air
* [Données pour la CAS, disponibles en format XML sur le Datamart du SMC](readme_aqhi-datamartxml_fr.md)

Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est disponible.

### Licence

La [licence d’utilisation finale pour les serveurs de données d’Environnement et Changement climatique Canada](../../licence/readme_fr.md) précise les conditions d'utilisation de ces données.

### Politique d'utilisation des services de données ouvertes du SMC

La [Politique d'utilisation des services de données ouvertes du SMC](../../usage-policy/readme_fr.md) détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale.

### Métadonnées de découverte

Les [métadonnées d'observations et prévisions qui sont générés pour le programme Cote Air Santé (CAS) sont accessibles sur le portail du gouvernement ouvert](https://ouvert.canada.ca/data/fr/dataset/a563e47d-6eb9-4f7f-933c-222ae49fe57f)

## Produits

* [Sommaire des prévisions les plus récentes de la Cote air santé dans un grand nombre de villes au Canada](https://meteo.gc.ca/airquality/pages/index_f.html)
* [Carte de prévisions de l'ozone, PM2.5, et PM10 près de la surface et à différentes altitudes](https://meteo.gc.ca/aqfm/index_f.html)

## Partenaires et données de polluants

Le programme national AQHI est un partenariat entre Environnement et Changement climatique Canada, Santé Canada, ainsi que les agences provinciales, municipales et les ONG.

Pour obtenir des données annuelles de polluants, veuillez consulter le [**Programme  de surveillance national de la pollution atmosphérique (SNPA)**](https://ouvert.canada.ca/data/fr/dataset/1b36a356-defd-4813-acea-47bc3abd859b) d'Environnement et Changement climatique Canada (ECCC). Le programme SNPA est la principale source de données sur la qualité de l'air ambiant au Canada. Pour obtenir les données horaires des PM2.5, veuillez consulter le [catalogue de données](https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/Data-Donnees/?lang=fr) pour chaque année.
 
Pour toute question supplémentaire ou demande de données, veuillez contacter le [centre d'information du SNPA](mailto:rnspa-napsinfo@ec.gc.ca).

Veuillez noter que ECCC ne peut fournir de données individuelles sur les polluants, car ces données appartiennent aux **provinces et territoires** et, dans certains cas, peuvent être obtenues directement auprès d'eux. Pour toute donnée récente manquante concernant des provinces et territoires spécifiques, ECCC vous recommande de les contacter séparément. Vous pouvez également consulter le tableau ci-dessous pour connaître les partenaires du programme SNPA et leurs pages web contenant des données en temps réel :


| Partenaires du SNPA | Liens |
| ------ | ------ |
| Gouvernement de Terre-Neuve-et-Labrador, ministère de l'Environnement et des Changements climatiques | https://www.gov.nl.ca/ecc/env-protection/science/airmon/ |
| Gouvernement de l'Île-du-Prince-Édouard, ministère de l'Environnement, de l'Énergie et de l'Action climatique | https://www.princeedwardisland.ca/en/topic/air |
| Gouvernement de la Nouvelle-Écosse, Environnement de la Nouvelle-Écosse | https://www.novascotia.ca/nse/air/\\ https://www.novascotia.ca/nse/airdata/ |
| Gouvernement du Nouveau-Brunswick, ministère de l'Environnement et des Gouvernements locaux | http://www2.gnb.ca/content/gnb/en/departments/elg/environment/content/air_quality.html\\ http://www.elgegl.gnb.ca/AirNB/ |
| Gouvernement du Québec, Ministère de l’Environnement et de la Lutte contre les changements climatiques | https://www.environnement.gouv.qc.ca/air/inter_en.htm \\ https://www.environnement.gouv.qc.ca/air/reseau-surveillance/telechargement.asp |
| Ville de Montréal, Direction de l’environnement | https://montreal.ca/en/topics/air-quality\\ https://donnees.montreal.ca/ville-de-montreal/rsqa-polluants-gazeux#data |
| Gouvernement de l'Ontario, ministère de l'Environnement, de la Protection de la nature et des Parcs | http://www.airqualityontario.com/ |
| Gouvernement du Manitoba, ministère de la Protection de la nature et du Climat | https://www.gov.mb.ca/sd/environment_and_biodiversity/air_quality/index.html \\https://web31.gov.mb.ca/EnvistaWeb/Default.ltr.aspx |
| Gouvernement de la Saskatchewan, ministère de l'Environnement de la Saskatchewan | https://www.saskatchewan.ca/residents/environment-public-health-and-safety/environmental-health/outdoor-air-quality/air-quality-monitoring\\ http://environment.gov.sk.ca/airqualityindex |
| Gouvernement de l'Alberta, Environnement et Parcs | https://www.alberta.ca/air-quality.aspx\\ http://airdata.alberta.ca/ |
| Gouvernement de la Colombie-Britannique, ministère de l'Environnement et des Changements climatiques | https://www2.gov.bc.ca/gov/content/environment/air-land-water/air/air-quality\\ https://envistaweb.env.gov.bc.ca/ |
| Métropole de Vancouver, Département des parcs et de l'environnement | https://metrovancouver.org/services/air-quality-climate-action/current-air-quality |
| Gouvernement du Yukon, Département de l'environnement | https://yukon.ca/en/waste-and-recycling/pollution/air-quality-monitoring |
| Gouvernement des Territoires du Nord-Ouest, ministère de l'Environnement et des Ressources naturelles | http://www.enr.gov.nt.ca/en/services/air-quality\\ http://aqm.enr.gov.nt.ca/ |
| Gouvernement du Nunavut, ministère de l'Environnement | https://gov.nu.ca/environment/information/environmental-protection |

Note : le Nunavut ne dispose pas de lien vers une page de données en temps réel.

Vous pouvez également accéder aux données à partir du portail américain [AirNow](https://www.airnow.gov/).

## Documentation technique

* [Guide des prévisions de la côte air santé ](https://www.canada.ca/fr/environnement-changement-climatique/services/meteo-sante/publications/guide-previsions-cote-air-sante.html)

## Registre des changements 

La chronologie des changements apportés au programme Cote Air Santé (CAS) est disponible [ici](changelog_aqhi_fr.md).


