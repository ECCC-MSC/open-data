[In English](readme.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > FAQ

# FAQ des données publiques du SMC

Cette section contient les questions les plus fréquemment posées au sujet des données ouvertes du SMC.


## Table des matières

* [Quelles données peut-on trouver sur le Datamart du SMC ?](#quelles-donnees-peut-on-trouver-sur-le-datamart-du-smc)
* [Fournissez-vous un API à travers lequel il serait possible d'accéder aux données météorologiques en un temps et un lieu donné ?](#fournissez-vous-un-api-à-travers-lequel-il-serait-possible-d-accéder-aux-données-météorologiques-en-un-temps-et-un-lieu-donné)
* [Comment peut-on télécharger les données ?](#comment-peut-on-télécharger-les données)
* [Peut-on avoir accès aux données radar ?](#peut-on-avoir-accès-aux-données-radar)
* [Peut-on accéder aux données radar archivées ?](#peut-on-accéder-aux-données-radar-archivées)
* [Est ce que les prévisions historiques des modèles numériques sont disponibles ?](#est-ce-que-les-prévisions-historiques-des-modeles-numeriques-sont-disponibles)
* [Comment être informé des changements aux bulletins ainsi qu'aux contenu et format de modèles ?](#comment-être-informé-des-changements-aux-bulletins-ainsi-qu-'-aux-contenu-et-format-de-modèles)
* [Peut-on avoir un fil de données GRIB ?](#peut-on-avoir-un-fil-de-données-grib)
* [Pourquoi ne pas produire un seul gros fichier GRIB avec toutes les variables ?](#pourquoi-ne-pas-produire-un-seul-fichier-grib-avec-toutes-les-variables)
* [Peut-on avoir accès aux observations en temps réel ?](#peut-on-avoir-accès-aux-observations-en-temps-réel)
* [Peut-on avoir accès aux avertisssements ?](#peut-on-avoir-accès-aux-avertissements)
* [Est-il possible d'obtenir un shapefile des régions d'avertissement ?](#est-il-possible-d-'-obtenir-un-shapefile-des-régions-d-'-avertissements)
* [Les images satellitaires sont-elles dipsonibles ?](#les-images-satellitaires-sont-elles-disponibles)
* [Peut-on avoir accès et utiliser les icônes du produit XML des Citypage ?](#peut-on-avoir-accès-et-utiliser-les-icônes-du-produit-xml-des-citypage)
* [Comment obtenir les températures minimales et maximales en format CSV ?](#comment-obtenir-les-températures-minimales-et-maximales-en-format-csv)
* [Est-il possible d'avoir accès aux hauteurs cumulatives de pluie ?](#est-il-possible-d-'-avoir-accès-aux-hauteurs-cumulatives-de-pluie)
* [Qu'est ce que le système de coordonnées de référence ou datum d'un modèle X ?](#qu-'-est-ce-que-le-système-de-coordonnées-de-référence-ou-datum-d-'-un-modèle-x)
* [Comment peut-on obtenir la topographie d'un modèle X ?](#comment-peut-on-obtenir-la-topographie-d-'-un-modèle-x)
* [Est-il possible d'avoir le masque terre mer d'un modèle X ?](#est-il-possible-d-'-avoir-le-masque-terre-mer-d-'-un-modèle-x)
* [Je ne vois pas de condition sous l'élément correspondant dans le fichier XML Citypage](#je-ne-vois-pas-de-condition-sous-l-'-élément-correspondant-dans-le-fichier-xml-citypage)
* [Pourquoi les queues de message cessent après plusieurs heures d'inactivité en utilisant AMQP ?](#pourquoi-les-queues-de-message-cessent-après-plusieurs-heures-d-'-inactivité-en-utilisant-amqp)
* [Contactez-nous](#contactez-nous)


## Quelles données peut-on trouver sur le Datamart du SMC ?

Beaucoup de nos données sont disponibles sur le serveur de données ouvertes du Service météorologique canadien (SMC), appelé Datamart du SMC. Vous trouverez une courte 
description des produits disponibles ainsi qu'un lien vers une documentation détaillée de chacun d'entre eux dans ce README:

[https://dd.meteo.gc.ca/about_dd_apropos.txt](https://dd.meteo.gc.ca/about_dd_apropos.txt)

Les termes et conditions d'utilisation des données météorologiques d'Environnement et changement climatique Canada peuvent être consultés ici:

[https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt](https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt)

Nous offrons aussi des services web géospatiaux appelés GeoMet du SMC, dont la documentation se trouve ici:

[https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c](https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c)

Une autre source décrivant les produits peut être trouvée dans le Guide des produits du CMC, disponible sur le site web Collaboration à cette adresse:

[https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/table_of_contents_e.html](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/table_of_contents_e.html)

Si vous désirez davantage d'information sur nos services et produits, n'hésitez pas à nous contacter via l'adresse: ec.dps-client.ec@canada.ca

## Fournissez-vous un API à travers lequel il serait possible d'accéder aux données météorologiques en un temps et un lieu donné ?

Environnement et changement climatique Canada offre un API pour accéder aux données météorologiques via les services web géospatiaux du SMC appelés GeoMet, à 
travers le standard international reconnu WMS. La documentation se trouve ici:

[https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/outils-donnees-specialisees/services-web-geospatiaux.html](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/outils-donnees-specialisees/services-web-geospatiaux.html)

Les données disponibles via WMS peuvent facilement être intégrées à des applications iOS, nous connaissons d'ailleurs plusieurs utilisations à succès de ce genre.

Pour information, plus de 400 couches sont rassemblées dans le WMS GetCapabilities:

[https://ec.gc.ca/meteo-weather/default.asp?lang=Fr&n=C0D9B3D8-1#wms](https://ec.gc.ca/meteo-weather/default.asp?lang=Fr&n=C0D9B3D8-1#wms)

Nous sommes également en train de rendre disponibles davantage de données météo dans la famille de standards OGC (i.e, WMS, WCS, WFS, SLD). Voir l'annonce de la 
version GeoMet-Beta:

[http://lists.ec.gc.ca/pipermail/geomet-info/2016-June/000033.html](http://lists.ec.gc.ca/pipermail/geomet-info/2016-June/000033.html)

Les changements aux services web géospatiaux GeoMet-Beta seront annoncés via la liste de diffusion GeoMet-Info:

[http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info)

Finallement, puisque GeoMet représente des couches en standards ouverts, les usagers ne sont pas affectés lorsque les données sous-jacentes sont modifiées: les méthodes 
pour accéder aux données demeurent stables et fiables. GeoMet répond à plus d'1 million de requêtes quotidiennement et peut être utilisé librement en autant que la 
source des données soit attribuée. Voir la licence ci-dessous pour les détails: 

[https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt](https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt)

## Comment peut-on télécharger les données ?

Le Service météorologique du Canada (SMC) a mis en place un fil de données annonçant les fichiers disponibles sur le Datamart du SMC. Ce fil de données
utilise le protocole ''Advanced Message Queuing Protocol'' (AMQP). Il devient ainsi possible non seulement d'être avisé de la disponibilité des 
produits sur le Datamart du SMC lorsque ceux-ci sont publiés, mais aussi de les recevoir automatiquement. Le service peut s'appliquer à une série spécifique de 
fichiers (alertes météorologiques, observations, données de modèle, etc.) et ainsi viser seulement les produits d'intérêt pour l'usager.

La documentation de ce service est disponible ici:
[https://dd.weather.gc.ca/doc/README_AMQP.txt](https://dd.weather.gc.ca/doc/README_AMQP.txt)

Notez que la documentation originale mentionne le script "dd_subscribe" qui fonctionne à la fois avec Python2 et Python3, cependant nous allons migrer vers "sr_subscribe" 
qui ne fonctionne qu'avec Python3. La documentation associée se trouve ici:

[http://metpx.sourceforge.net/sr_subscribe.1.html](http://metpx.sourceforge.net/sr_subscribe.1.html)

[http://metpx.sourceforge.net/Install.html](http://metpx.sourceforge.net/Install.html)

## Peut-on avoir accès aux données radar ?

Les données radar disponibles gratuitement sur le serveur de données ouvertes du SMC sont les images GIF. Les informations au sujet de ce service sont disponibles ici:

[https://dd.meteo.gc.ca/radar/doc/README_radar.txt](https://dd.meteo.gc.ca/radar/doc/README_radar.txt)

Nous offrons également la mosaique radar nord-américaine via les services web géospatiaux WMS:

[https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1](https://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1)

La licence des termes d'utilisation pour ces produits se trouve ici:

[https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt](https://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt)

Aucun des points ci-dessus ne comprend les données brutes. Ceux-ci, ainsi que divers autres produits, sont fournis par un service à recouvrement de coûts. Dans le cadre 
de ce service, nous poussons les données vers le serveur FTP des clients et assurons un service 24/7. Les termes sous lesquels ces produits sont fournis sont les mêmes
que ceux décrits dans la licence ci-dessus.

La documentation concernant les formats de données radar peut être consultée ici:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf)

La documentation concernant les produits radar se trouve à l'adresse:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf)

Concernant les fils de données, les formats disponibles sont les suivants:

    * NUMERICA (ASCII)
    * Images GIF (les récentes données GIF sont disponibles gratuitement sur le Datamart du SMC))
    * Format brut IRIS : Spécifications: https://my.vaisala.net/en/hydrology/offering/weatherradars/Pages/IRIS.aspx

Les détails concernant les frais sont les suivants:

    
    * 1-5 radars (QC, Atl ou Pac région) : $1,600/mois
    * 6-10 (toute région): $1,800/mois
    * 11+: $2,000/mois
    * Plus des frais fixes d'installation du fil de données de $2,000 
    
Ces tarifs sont donnés à titre indicatif seulement et sont sujets à changement.

Concernant les tailles des fichiers:

    * 1 heure de volume scan pour 1 radar sans précipitation représente environ 4.5 Mb
    * 1 heure de volume scan pour 1 radar avec précipitation représente environ 13 Mb
    
Les chiffres ci-dessus dépendent des conditions météo et sont donnés qu'à titre de référence seulement.

## Peut-on accéder aux données radar archivées ?

Environnement et changement climatique Canada n'a pas de service en ligne pour accéder aux données archivées. Le service de désarchivage est à recouvrement de coût, nous
chargeons 99$/heure de travail nécessaire pour produire les données avec un coût minimum de 99$. Les données par elles-mêmes étant gratuites.

Les archives sont disponibles en format brut (IRIS) ou en format ASCII. Les informations concernant les formats et produits peuvent être consultées aux adresses:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf)

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf)

Des requêtes typiques de désarchivage demandent entre 2 et 4 heures de travail. Si intéressé, merci de compléter le formulaire ci-dessous et de le faire
parvenir à l'adresse: ec.dps-client.ec@canada.ca


| Information | Valeur |
|-------------|:-----:|
|Noms des radars |       |       
|Type de produits (Raw, CAPPI, PRECIP, ECHOTOP, etc.) |       |
|Unités (dBZ, mm/hr) |       |
|Format (GIF, NumericA, IRIS/MRO) |       |
|Periode de temps (UTC) |       |
|Fréquence (default: 10 minutes) |       |
|Format de livraison (zip, tar, autre) |       |
|Date de livraison désirée (quand?) |       |
|Autres informations |       |
|Coordonnées de facturation |      |

## Est ce que les prévisions historiques des modèles numériques sont disponibles ?

Environnement et changement climatique Canada n'a pas de service en ligne pour accéder aux données archivées. Le service de désarchivage est à recouvrement de coût, nous
chargeons 99$/heure de travail nécessaire pour produire les données avec un coût minimum de 99$. Les données par elles-mêmes étant gratuites.

Dès que nous recevons les détails des données demandées, nous produisons les archives en format GRIB et les envoyons aux usagers. Un estimé peut être fourni, une fois 
les informations reçues. Selon la nature des requêtes, il faut compter quelques centaines de dollars.

Si intéressé, merci de compléter le formulaire ci-dessous et de le faire parvenir à l'adresse: ec.dps-client.ec@canada.ca

| Information | Valeur |
|-------------|:-----:|
|Modèle (SGPD, SRPD, SHRPD, SPENA, autre) |       |       
|Type de données (prévisions, analyses or cartes)  |       |
|Variables (ex: WIND_TGL_40m) |       |
|Dates (ex: 2006-01-01 à 2008-12-31 )  |       |
|Heures des passes (ex: 00Z, 12Z) |     |
|Heures des prévisions (e.g. 000, 003, 006) |       |
|Couverture géographique (domaine lat/lon défini par l'usager, domaine disponible sur le Datamart du SMC)  |       |
|Résolution spatiale horizontale (ex: 10km/0.24 degrés)  |       |
|Niveaux (surface, niveaux de pression, altitude en mètres au dessus du sol) |        |
|Mode de livraison | FTP  |
|Nom et coordonnées de personne à facturer |    |

Notes:
* Les requêtes telles que "toutes les variables à tous les niveaux" ne sont pas acceptées. Merci de spécifier
* Les archives remontent aux 5 dernières années, selon la disponibilité des données 

## Comment être informé des changements aux bulletins ainsi qu'aux contenu et format de modèles ?

Pour les bulletins de stations canadiennes, tout changement dans l'en-tête et le nom des stations est annoncé via ce que nous appelons les GENOT (GEneral NOTification) message.
Nous avons une liste de diffusion pour distribuer les GENOTs, si cela vous intéresse, envoyez-nous votre adresse courriel et nous vous ajouterons à la liste de diffusion.

Pour être averti des changements majeurs, tels qu'un changement de résolution par exemple, vous pouvez vous inscrire à la liste des GENOT 03. Vous pouvez trouver un exemple 
d'un tel bulletin à l'adresse:

[https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117](https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117)

Finalement, nous vous recommandons fortement de vous inscrire à la list de diffusion du Datamart du SMC afin d'être averti de toute mise à jour ou changement concernant la 
disponibilité des données. Vous pouvez vous abonner ici:

[http://lists.cmc.ec.gc.ca/mailman/listinfo/dd_info](http://lists.cmc.ec.gc.ca/mailman/listinfo/dd_info)

Merci d'utiliser l'adresse courriel ci-dessous pour toute question ou commentaire:

ec.dps-client.ec@canada.ca

## Peut-on avoir un fil de données GRIB ?

Environnement et changement climatique Canada offre un fil de données pour pousser chez le client les données PNT en format GRIB. Ce service est supporté 24/7 et le coût 
dépend de la quantité de données demandées: le tarif de départ est de 500$ par mois + 500$ pour l'installation du fil de données jusqu'à 1G par jour.
Ajouter 500$ par mois pour chaque Gb de données supplémentaires par jour.

Merci de nous contacter si vous êtes intéressés par ce service.

## Pourquoi ne pas produire un seul gros fichier GRIB avec toutes les variables ?

## Peut-on avoir accès aux observations en temps réel ?

## Peut-on avoir accès aux avertisssements ?

## Est-il possible d'obtenir un shapefile des régions d'avertissement ?

## Les images satellitaires sont-elles dipsonibles ?

## Peut-on avoir accès et utiliser les icônes du produit XML des Citypage ?

## Comment obtenir les températures minimales et maximales en format CSV ?

## Est-il possible d'avoir accès aux hauteurs cumulatives de pluie ?

## Qu'est ce que le système de coordonnées de référence ou datum d'un modèle X ?

## Comment peut-on obtenir la topographie d'un modèle X ?

## Je ne vois pas de condition sous l'élément correspondant dans le fichier XML Citypage

## Pourquoi les queues de message cessent après plusieurs heures d'inactivité en utilisant AMQP ?

## Contactez-nous













