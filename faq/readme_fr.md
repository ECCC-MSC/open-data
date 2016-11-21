[In English](readme.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > FAQ

FAQ des données publiques du SMC
==========================================================

Cette section contient les questions les plus fréquemment posées au sujet des données ouvertes du SMC disponibles sur le Datamart.


Table des matières
----------------

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

Beaucoup de nos données sont disponibles sur le serveur de données ouvertes du Service météorologique canadien (SMC), appelé Datamart. Vous trouverez une courte 
description des produits disponibles ainsi qu'un lien vers une documentation détaillée de chacun d'entre eux dans ce README:

http://dd.meteo.gc.ca/about_dd_apropos.txt

Les termes et conditions d'utilisation des données météorologiques d'Environnement et changement climatique Canada peuvent être consultés ici:

http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt

Nous offrons aussi des services web géospatiaux appelés GeoMet du SMC, dont la documentation se trouve ici:

http://www.ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c

Une autre source décrivant les produits peut être trouvée dans le Guide des produits du CMC, disponible sur le site web Collaboration à cette adresse:

http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/table_of_contents_e.html

Si vous désirez davantage d'information sur nos services et produits, n'hésitez pas à nous contacter via l'adresse: ec.dps-client.ec@canada.ca

## Fournissez-vous un API à travers lequel il serait possible d'accéder aux données météorologiques en un temps et un lieu donné ?

Environnement et changement climatique Canada offre un API pour accéder aux données météorologiques via les services web géospatiaux du SMC appelés GeoMet, à 
travers le standard international reconnu WMS. La documentation se trouve ici:

http://ec.gc.ca/meteo-weather/default.asp?lang=En&n=C0D9B3D8-1c

Les données disponibles via WMS peuvent facilement être intégrées à des applications iOS, nous connaissons d'ailleurs plusieurs utilisations à succès de ce genre.

Pour information, plus de 400 couches sont rassemblées dans le WMS GetCapabilities:

http://ec.gc.ca/meteo-weather/default.asp?lang=Fr&n=C0D9B3D8-1#wms

Nous sommes également en train de rendre disponibles davantage de données météo dans la famille de standards OGC (i.e, WMS, WCS, WFS, SLD). Voir l'annonce de la 
version GeoMet-Beta:

http://lists.ec.gc.ca/pipermail/geomet-info/2016-June/000033.html

Les changements aux services web géospatiaux GeoMet-Beta seront annoncés via la liste de diffusion GeoMet-Info:

http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info

Finallement, puisque GeoMet représente des couches en standards ouverts, les usagers ne sont pas affectés lorsque les données sous-jacentes sont modifiées: les méthodes 
pour accéder aux données demeurent stables et fiables. GeoMet répond à plus d'1 million de requêtes quotidiennement et peut être utilisé librement en autant que la 
source des données soit attribuée. Voir la licence ci-dessous pour les détails: 

http://dd.meteo.gc.ca/doc/LICENCE_GENERAL.txt

## Comment peut-on télécharger les données ?

Le Service météorologique du Canada (SMC) a mis en place un fil de données annonçant les fichiers disponibles sur le Datamart. Ce fil de données
utilise le protocole ''Advanced Message Queuing Protocol'' (AMQP). Il devient ainsi possible non seulement d'être avisé de la disponibilité des 
produits sur le Datamart lorsque ceux-ci sont publiés, mais aussi de les recevoir automatiquement. Le service peut s'appliquer à une série spécifique de 
fichiers (alertes météorologiques, observations, données de modèle, etc.) et ainsi viser seulement les produits d'intérêt pour l'usager.

La documentation de ce service est disponible ici:
http://dd.weather.gc.ca/doc/README_AMQP.txt

Notez que la documentation originale mentionne le script "dd_subscribe" qui fonctionne à la fois avec Python2 et Python3, cependant nous allons migrer vers "sr_subscribe" 
qui ne fonctionne qu'avec Python3. La documentation associée se trouve ici:

http://metpx.sourceforge.net/sr_subscribe.1.html

http://metpx.sourceforge.net/Install.html

## Peut-on avoir accès aux données radar ?

## Peut-on accéder aux données radar archivées ?

## Est ce que les prévisions historiques des modèles numériques sont disponibles ?

## Comment être informé des changements aux bulletins ainsi qu'aux contenu et format de modèles ?

## Peut-on avoir un fil de données GRIB ?

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













