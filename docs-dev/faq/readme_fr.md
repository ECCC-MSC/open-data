[In English](readme_en.md)

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
* [Comment être informé des problèmes de production des données de modèles ?](#comment-etre-informe-des-problemes-de-production-des-donnees-de-modeles)
* [Peut-on avoir un fil de données GRIB ?](#peut-on-avoir-un-fil-de-données-grib)
* [Pourquoi ne pas produire un seul gros fichier GRIB avec toutes les variables ?](#pourquoi-ne-pas-produire-un-seul-fichier-grib-avec-toutes-les-variables)
* [Peut-on avoir accès aux observations en temps réel ?](#peut-on-avoir-accès-aux-observations-en-temps-réel)
* [Peut-on avoir accès aux avertissements ?](#peut-on-avoir-accès-aux-avertissements)
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
* [Comment utiliser AMQP sous Windows ?](#comment-utiliser-amqp-sous-windows)
* [Contactez-nous](#contactez-nous)


## Quelles données peut-on trouver sur le Datamart du SMC ?

Beaucoup de nos [données](../msc-data/readme_fr.md) sont disponibles sur le serveur de données ouvertes du Service météorologique canadien (SMC), appelé [Datamart du SMC](../msc-datamart/readme_fr.md).

Les termes et conditions d'utilisation des données météorologiques d'Environnement et Changement climatique Canada peuvent être consultés dans la [licence](../licence/readme_fr.txt).

Nous offrons aussi des services web géospatiaux (API) appelés [GeoMet du SMC](../msc-geomet/readme_fr.md).

Des [exemples et tutoriels](../usage/readme_fr.md) pour accéder et utiliser les données ouvertes du SMC sont mis à la disposition de nos usagers. 

Les changements et mises à jour aux services de données du Datamart et de GeoMet sont annoncés via les listes de diffusion respectives ci-dessous auxquelles nous encourageons fortement nos usagers de souscrire :

* https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info
* https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info 

Si vous désirez davantage d'information sur nos services et produits, n'hésitez pas à nous [contacter](../readme_fr/#contactez-nous).

**Note** : Une plateforme de discussion consacrée aux données ouvertes du SMC a été mise en place par une tierce 
partie afin de permettre à la communauté des usagers d'interagir plus facilement et de tirer profit de l'expérience de chacun:

http://meteocentre.com/help/msc-open-data/

Nous approuvons et applaudissons cette initiative, mais nous tenons à préciser qu'Environnement et Changement climatique Canada (ECCC) ainsi que le SMC ne sont pas responsables de ce site et que leurs employés n'ont pas l'obligation de répondre aux questions posées. Quand des employés d'ECCC ou du SMC participent, ils le font à titre personnel.
 
## Comment peut-on télécharger les données ?

Le Service météorologique du Canada (SMC) a mis en place un [fil de données](../msc-datamart/amqp_fr.md) annonçant les fichiers disponibles sur le Datamart du SMC. Ce fil de données utilise le protocole ''Advanced Message Queuing Protocol'' (AMQP). 

Il devient ainsi possible non seulement d'être avisé de la disponibilité des produits sur le Datamart du SMC dès que ceux-ci sont publiés, mais aussi de les recevoir automatiquement. 

Le service peut s'appliquer à une série spécifique de fichiers (alertes météorologiques, observations, données de modèle, etc.) et ainsi viser seulement les produits d'intérêt pour l'usager.

Pour les usagers de Windows, il suffit de télécharger la dernière version (fichier .exe) qui ne nécessite pas d’installer un environnement Python. Voir les détail dans le [guide d’installation](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst).

## Peut-on avoir accès aux données radar ?

Les données radar disponibles gratuitement sur le serveur de données ouvertes du SMC sont les [images GIF]( ../msc-data/obs_radar/readme_radarimage-datamart_fr.md). 

Nous offrons également la [mosaique radar nord-américaine](../msc-data/obs_radar/readme_radar_geomet_fr.md) via les services web géospatiaux WMS.

Les données brutes ainsi que divers autres produits, sont fournis par un [service à recouvrement de coûts](../cost-recovered/readme_fr/#fil-de-donnees-dedie). Dans le cadre de ce service, nous poussons les données vers le serveur FTP des clients et assurons un service 24/7. Les termes sous lesquels ces produits sont fournis sont les mêmes
que ceux décrits dans la licence ci-dessus.

La documentation concernant les formats de données radar peut être consultée ici:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf)

La documentation concernant les produits radar se trouve à l'adresse:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf)

Concernant les fils de données, les formats disponibles sont les suivants:

* NUMERIC (ASCII)
* Images GIF (les récentes données GIF sont disponibles gratuitement sur le Datamart du SMC)
* Format brut [IRIS]( https://my.vaisala.net/en/hydrology/offering/weatherradars/Pages/IRIS.aspx), pour les anciens radars à bande C
* Format brut [ODIM_H5]( https://support.hdfgroup.org/HDF5/users5.html), pour les nouveaux radars à bande S
   
## Peut-on accéder aux données radar archivées ?

Environnement et Changement climatique Canada n'a pas de service en ligne pour accéder aux données archivées. Le service de désarchivage est à [recouvrement de coût](../cost-recovered/readme_fr/#service-de-desarchivage), nous chargeons 99$/heure de travail nécessaire pour produire les données avec un coût minimum de 99$. Les données par elles-mêmes étant gratuites.

Les archives sont disponibles en format brut (IRIS/ODIM_H5) ou en format ASCII. Les informations concernant les formats et produits peuvent être consultées aux adresses respectives:

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf)

[https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf)

Des requêtes typiques de désarchivage demandent entre 2 et 4 heures de travail. Si intéressé, merci de compléter le formulaire ci-dessous et de le faire parvenir à l'adresse: ec.dps-client.ec@canada.ca


| Information | Valeur |
|-------------|:-----:|
|Noms des radars |       |       
|Type de produits (Raw, CAPPI, PRECIP, ECHOTOP, etc.) |       |
|Unités (dBZ, mm/hr) |       |
|Format (GIF, NumericA, IRIS/ODIM_H5) |       |
|Periode de temps (UTC) |       |
|Fréquence (default: 10 minutes) |       |
|Format de livraison (zip, tar, autre) |       |
|Date de livraison désirée (quand?) |       |
|Autres informations |       |
|Coordonnées de facturation |      |

## Est ce que les prévisions historiques des modèles numériques sont disponibles ?
Environnement et Changement climatique Canada n'a pas de service en ligne pour accéder aux données archivées. Le service de désarchivage est à [recouvrement de coût](../cost-recovered/readme_fr/#service-de-desarchivage), nous chargeons 99$/heure de travail nécessaire pour produire les données avec un coût minimum de 99$. Les données par elles-mêmes étant gratuites.

Dès que nous recevons les détails des données demandées, nous pouvons produire un échantillon et l’envoyer à l’usager pour validation. Un estimé peut alors être fourni, une fois la requête confirmée. Selon la nature des requêtes, il faut compter quelques centaines de dollars.

Pour toute commande, merci de compléter le formulaire ci-dessous et de le faire parvenir à l'adresse: ec.dps-client.ec@canada.ca

| Information | Valeur |
|-------------|:-----:|
|Modèle (SGPD, SRPD, SHRPD, SGPOG, autre) |       |       
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
* Les archives remontent aux 5 dernières années, selon la disponibilité des données 
* Compte-tenu du gros volume de demandes, un certian délai est à prévoir. Merci d'indiquer si la demande est urgente, nous tenterons alors de la prioriser.

## Comment être informé des changements aux bulletins ainsi qu'aux contenu et format de modèles ?

Pour les bulletins de stations canadiennes, tout changement dans l'en-tête et le nom des stations est annoncé via ce que nous appelons les GENOT (GEneral NOTification) message.

Nous avons une liste de diffusion pour distribuer les GENOTs, si cela vous intéresse, contactez-nous à l'adresse : ec.dps-client.ec@canada.ca et nous vous ajouterons à la liste de diffusion.

En parallèle, ces bulletins sont disponibles sur le Datamart du SMC à cette adresse :

[https://dd.meteo.gc.ca/doc/genots/](https://dd.meteo.gc.ca/doc/genots/)

Pour être averti des changements majeurs, tels qu'un changement de résolution par exemple, vous pouvez vous inscrire à la liste des GENOT 03. Vous pouvez trouver un exemple d'un tel bulletin à l'adresse:

[https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117](https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117)

Finalement, nous vous recommandons fortement de vous inscrire à la [liste de diffusion du Datamart du SMC](https://lists.ec.gc.ca/mailman/listinfo/dd_info) afin d'être averti de toute mise à jour ou changement concernant la disponibilité des données. 

## Comment être informé des problèmes de production des données de modèles ?

Il arrive parfois que les données de modèle soient en retard ou même absentes de notre serveur HTTPS de données.

Afin de savoir si ce délai ou cette absence est dû à un problème de production, vous pouvez consulter les bulletins AACN01 CWAO.  Ces derniers sont des bulletins émis par le CCMEP au besoin pour informer les bureaux du SMC et
d'autres clients de tout problème pouvant perturber ou retarder l'émission et/ou la distribution des produits opérationnels.

Pour consulter les derniers bulletins AACN01 CWAO, vous pouvez utiliser l'utilitaire de recherche de script mis à votre disposition par ECCC:

https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_fr.pdf

Par exemple, pour obtenir les bulletins AACN01 du jour, vous pouvez cliquer sur l'URL suivant:
http://dd.meteo.ec.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01

Pour un jour précis, vous pouvez préciser votre recherche. Par exemple, pour avoir les informations pour le 19 mai 2020, vous pouvez utiliser ce lien :

https://dd.meteo.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01&day=19&month=05&year=2020

Il existe par ailleurs une liste de diffusion des bulletins AACN01. Si vous êtes intéressé, veuillez nous contacter à l'adresse ec.dps-client.ec@canada.ca et nous vous ajouterons à la liste de diffusion.

## Peut-on avoir un fil de données de modèles numériques ?

Environnement et Changement climatique Canada offre un fil de données à [recouvrement de coûts](../cost-recovered/readme_fr/#fil-de-donnees-dedie) pour pousser chez le client les données PNT en format GRIB ou NetCDF. Ce service est supporté 24/7 et le coût dépend de la quantité de données demandées: le tarif de départ est de 500$ par mois + 500$ pour l'installation du fil de données jusqu'à 1G par jour.

Ajouter 500$ par mois pour chaque Gb de données supplémentaires par jour.

Merci de nous contacter si vous êtes intéressés par ce service.

## Pourquoi ne pas produire un seul gros fichier GRIB avec toutes les variables ?

Il a été choisi de mettre une variable par fichier car nous avons supposé que la plupart des utilisateurs n'auraient pas besoin de toutes les variables.

Cela étant dit, l'utilitaire [wget](https://www.gnu.org/software/wget/wget) possède des fonctionnalités qui visent à optimiser le processus de téléchargement. Par exemple, les utilisateurs peuvent rassembler leurs directives de téléchargement dans un fichier texte et l'utiliser comme argument pour la commande "wget -i list.txt".

En procédant ainsi, un seul socket sera ouvert et la requête sera traitée comme un seul téléchargement, sans ouvrir et fermer des sockets pour chaque fichier.

La vitesse de téléchargement sera alors la même que si tous les fichiers GRIB étaient dans un seul fichier zip.

## Peut-on avoir accès aux observations en temps réel ?

Nous avons 2 produits qui contiennent des observations du réseau de stations de Environnement et Changement climatique Canada.

L’un est de type une station par fichier, il s’agit des observations météorologiques au sol et marines par station, les [données SWOB](../msc-data/obs_station/readme_obs_insitu_swobdatamart_fr.md), disponibles en format XML. Toutes les données des stations canadiennes sont disponibles dans ce produit.

Le second regroupe les [données d’observation d’une même province ou territoire](../msc-data/obs_station/readme_obs_insitu_xmldatamart_fr.md) par fichier, en format XML. Toutes les stations canadiennes ne sont pas contenues dans ce produit. Ce sont ces données qui sont utilisées dans le site web des prévisions officielles meteo.gc.ca. De ce fait, elle sont soumises à certaines règles (ex : pour les vents, utilisation de la moyenne observée sur une période de 2 minutes, si cela n’est pas possible utilisation d’une moyenne sur 10 minutes).

Par conséquent, on ne peut pas vraiment comparer ces 2 jeux de données et il est fortement conseillé d’utiliser les données SWOB, plus complètes et soumises à aucune règle, pour la région d’intérêt.

## A quelle fréquence sont rafraichies les données d’observations rassemblées par province et territoire ?

Les fichiers sommaires provinciaux sont mis à jour 6 fois par heure, mais le simple fait que nous les mettions à jour ne signifie pas nécessairement qu'une des stations du fichier sommaire a mis à jour ses données depuis la dernière exécution.
   
Nous mettons à jour les observations sur une base horaire (et non à la minute) pour chaque station, au début de l'heure, mais une autre mise à jour (appelée obs spéciale ou "speci") à l’intérieur de l’heure est aussi possible si l'observateur estime qu'il y a eu un changement suffisamment important pour justifier une mise à jour.

Il est possible, par exemple, que le fichier de 1614Z ne contienne pas d'observations différentes de celles de 1611Z, de sorte que l'utilisateur ne doit pas toujours s'attendre à des changements de valeurs pour une station individuelle au cours de l'heure.

Nous ne présentons que les données que nous obtenons et, dans ce cas, la plupart des stations ne rapportent qu'une fois par heure. 
 
## Où pourrais-je trouver des données de bouées ?

Les données de bouées (observations marines) sont disponibles sur le Datamart du SMC à cette adresse :

https://dd.meteo.gc.ca/observations/swob-ml/marine/moored-buoys

Vous trouverez dans la documentation [documentation](../msc-data/obs_station/readme_obs_insitu_swobdatamart_fr.md), une liste des bouées disponibles actuellement. D’autres seront ajoutées au cours du temps.

Des rapports quotidiens de bouées du SMC sont aussi publiés sur le [site web de Pêches et Océans Canada](http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/msc-smc/index-fra.html).

Des informations sur les [bouées dérivantes](http://www.dfo-mpo.gc.ca/science/data-donnees/drib-bder/index-fra.html) sont également disponibles.

Finalement, ces données de bouées sont accessibles à travers les [bulletins alphanumériques](../msc-data/bulletins/readme_bulletins-datamart_fr.md)  disponibles sur le Datamart du SMC avec comme en-têtes SM/SN/SIVD17.

## Comment faire pour accéder aux avertissements ? 

Il y a plusieurs sources pour obtenir les avertissements.

Tout d’abord, les avertissements officiels sont disponibles en format PAC-XML sur le Datamart du SMC à cette adresse :

https://dd.meteo.gc.ca/alerts/cap

La [documentation](../msc-data/alerts/readme_alerts-datamart_fr.md) détaille ces données et donne également des informations concernant les critères d’alertes de la prévision publique ainsi des informations géographiques des emplacement des prévisions, pour tous les messages en format PAC.

Par ailleurs, ECCC a mis en place un fil de nouvelles ATOM via lequel les alertes et avertissements sont disponibles :

https://meteo.gc.ca/business/index_f.html#rss

Finalement, ECCC a mis en place un service expérimental pour envoyer les avertissements par messagerie électronique. Voir la documentation ici :

https://ecalertezmoi.meteo.gc.ca/guides/quickstart_fr.php

## Quelles sont les principales différences entre un fil de données  ATOM et le protocole AMQP pour accéder aux avertissements ?

La principale différence entre le fil de données ATOM et le protocole AMQP est que dans le cas du fil ATOM, l'utilisateur doit envoyer une requête pour savoir si les nouveaux fichiers sont disponibles, alors qu'avec l'AMQP, l'utilisateur est averti sans envoyer de requête.

Si l'on veut faire une analogie, les fils ATOM peuvent être considérés comme un facteur qui dépose des lettres dans la boîte aux lettres, alors que AMQP peut être considérée comme un livreur qui sonne à la porte pour remettre le colis postal.

Nous recommandons fortement d'utiliser le protocole AMQP qui est également une solution à plus long terme.

## Est-il possible d'obtenir un shapefile des régions d'avertissement ?

Un ensemble de fichiers en format Shapefile contenant les informations géographiques des emplacements des prévisions, pour tous les messages en format PAC, peut être trouvé dans ce répertoire (choisir la version la plus récente):

https://dd.meteo.gc.ca/meteocode/geodata/

Les ensembles de fichiers Shapefile à cet endroit sont les mêmes qui sont utilisés dans l'environnement opérationnel où les avertissements d'ECCC sont créés. Les ensembles Shapefiles ont des numéros de version afin de suivre l'évolution des emplacements utilisés dans cet environnement.

## Les images satellitaires sont-elles disponibles ?

Environnement et Changement climatique Canada ne distribue pas actuellement d’images satellites ou de produits dérivés aux usagers externes, à l'exception de notre [site web] (https://weather.gc.ca/satellite/index_f.html), car nous ne sommes pas le producteur des données.

Un site recommandé pour obtenir gratuitement les images satellites est celui de l'Université de Washington :

https://www.atmos.washington.edu/~ovens/loops/

Pour l’installation d'un fil de données d'images satellites, nous suggérons aux utilisateurs de contacter nos homologues américains à la NOAA ou de chercher un fournisseur dans le secteur privé.

## Peut-on avoir accès et utiliser les icônes du produit XML des Citypage ?

Ces icônes sont distribuées sous les [conditions générales standards d'Environnement et Changement climatique Canada] (https://www.canada.ca/fr/transparence/avis.html).

Pour faire un usage commercial de ces icônes, vous devez obtenir un consentement explicite préalable.

Vous pouvez télécharger toutes les icônes météorologiques de ECCC à l'adresse suivante : 

https://meteo.gc.ca/weathericons/NN.gif
où NN est un nombre compris entre 00 et 45.

Vous pouvez également créer vos propres icônes en utilisant les symboles météorologiques mondiaux de l'Organisation météorologique mondiale (OMM). Voir un ensemble complet de symboles météorologiques de l'OMM à cette adresse :

https://github.com/OGCMetOceanDWG/WorldWeatherSymbols

## Comment obtenir les températures minimales et maximales en format CSV ?

Pour obtenir des données de températures extrêmes prévues au format CSV, vous pouvez consulter au choix :

* Les bulletins de prévision FMCN31 à FMCN38 (format CSV), basés sur le [Système global de prévision déterministe (SGPD)](../msc-data/nwp_gdps/readme_gdps_en.md). Les prévisions à 00 UTC contiennent le maximum du jour en cours, le minimum et le maximum du deuxième jour et le minimum du troisième jour. Les prévisions de 1200 UTC contiennent les minima et maxima du jour deux et du jour trois.

* Les bulletins de prévision FMCN41 à FMCN48 (format CSV), basés sur le [Système régional de prévision déterministe (SRPD) ](../msc-data/nwp_rdps/readme_rdps_en.md). Les prévisions à  1200 UTC contiennent les minima et maxima du jour deux et les minima du jour trois. Les prévisions basées sur les données à 00UTC contiennent le maximum du jour en cours et le minimum et le maximum du jour deux.

Ces [bulletins](../msc-data/bulletins/readme_bulletins_fr.md) sont disponibles sur le Datamart du SMC à cette adresse :

https://dd.meteo.gc.ca/bulletins/alphanumeric/YYYYMMDD/FM/CWAO/

## Est-il possible d'avoir accès aux hauteurs cumulatives de pluie prévues?

En ce qui concerne les données QPF (Quantitative Precipitation Forecast) au format CSV, vous pourriez être intéressés par les bulletins FOCN03, à savoir les prévisions ponctuelles de variables météorologiques obtenues à partir des sorties directes du SRPD (Système régional de prévision déterministe) .

Chacun de ces bulletins est produit spécifiquement pour des sites de prévision canadiens individuels. Le contenu est donc variable. Par exemple, les valeurs des paramètres de prévision sont disponibles à des intervalles de 6 heures de 0 à 48 heures pour certains bulletins, et à des intervalles de 6 heures de 0 à 24 heures et à des intervalles de 12 heures de 24 à 48 heures pour certains autres.

Les éléments de prévision météorologique peuvent également varier d'un message à l'autre.

Ces [bulletins](../msc-data/bulletins/readme_bulletins_fr.md) sont disponibles sur le  Datamart du SMC à cette adresse :

https://dd.meteo.gc.ca/bulletins/focn03/YYYYMMDD/FO/

Une [interface de recherche de bulletins](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf) pour le serveur de données https du Service météorologique du Canada est également disponible à l’adresse :

https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl

## Puis-je obtenir des données d'équivalent en eau de la neige ?

L'estimation de la masse de neige est surtout valable pour le sol. Le paramètre GRIB SNOD représentant l’épaisseur de neige au sol est disponible en tant que valeur agrégée mais le paramètre SDEN (densité de neige) n'est disponible que pour la fraction du sol. 
Le produit SNOD x SDEN x facteur pour les unités fournit probablement la meilleure estimation actuellement disponible pour l'équivalent en eau de la neige. 

Sachez que le paramètre SDEN de la fraction de sol peut ou non être représentatif de la densité de neige pour les autres types de surface.

Par conséquent, la micro équation pour le calcul de l'équivalent en eau de la neige en mm (équivalent à kg/m2) à partir de la densité absolue SDEN et de l'épaisseur SNOD est :

* Si l'épaisseur est donnée en "cm" et SDEN en "kg/m3", ce que nous avons aux opérations alors : 

SWE = (SNOD * SDEN) / 100 -- SWE est en mm (ou kg/m2, c'est l'équivalent pour l'eau)

* Si l'épaisseur est donnée en "m" et le SDEN en "kg/m3" : 

SWE = SNOD * SDEN -- SWE est en mm (kg/2)

## Qu'est-ce que le système de coordonnées de référence ou datum d'un modèle X ?

Pour connaitre le système de coordonnées de référence d’un modèle et la projection utilisée pour produire nos fichiers de prévision numérique du temps, il suffit d’utiliser l'outil [GDAL]( https://www.gdal.org/GDAL) (gratuit).

La commande suivante vous fournira le référentiel et la projection du fichier :
gdalinfo file.grib2

En sortie, l'information commence par "Le système de coordonnées est :".

## Comment peut-on obtenir la topographie d'un modèle X ?

La topographie d’un modèle dont les données sont disponibles en format GRIB2 peut être obtenue en utilisant le champ HGT_SFC (topographie lissée du modèle).

## Puis-je avoir le masque terre-mer d’un modèle X ?

Pour un modèle dont les données sont disponibles en format GRIB2, le paramètre LAND_SFC_0 (Couverture terrestre) de l'heure de prévision 00h pour être utilisé déterminer ce masque.

Lorsque la valeur est 0, il s'agit de la mer, lorsque la valeur n'est pas 0, il s'agit de la terre (ou d'une partie de celle-ci).

## Je ne vois pas de «conditions actuelles» sous l'élément correspondant dans le fichier citypage_weather en format XML, est-ce normal ?

Certaines stations météorologiques sont automatiques (sans personnel) et ne signalent pas l'état des conditions actuelles.

Si vous regardez la page correspondante sur notre site web, par exemple pour la ville d’[Edmonton](https://weather.gc.ca/city/pages/ab-50_metric_e.html), vous verrez qu'il est écrit « Non observé » pour la condition.

C'est pourquoi aucune icône ou condition n'est signalée dans le fichier XML Citypage correspondant.

## Pourquoi les files d’attentes de message AMQP cessent après plusieurs heures d'inactivité ?

Les utilisateurs du service AMQP sont censés exécuter un démon qui télécharge des données en permanence, comme celui fourni par [Sarracenia] (https://github.com/MetPX/sarracenia/blob/master/doc/fr/sarra.rst). Dans le langage AMQP, une pompe, à savoir un hôte exécutant Sarracenia, est un [courtier](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst). Le courtier a une capacité limitée à mettre les produits en file d'attente lorsqu'un utilisateur est victime d'une longue interruption involontaire, par exemple de quelques heures à quelques jours. 

La performance de l'ensemble du service est affectée par la présence de files d'attente importantes pour un seul consommateur, il ne faut donc pas laisser les files d'attente s'accumuler indéfiniment. 

Nous maintenons les files d'attente en vie aussi longtemps que nous pouvons raisonnablement le faire, mais cette pratique vise uniquement à donner aux clients le temps de redémarrer leur service en cas d'échec. La durée des déconnexions qui peuvent être supportées en toute sécurité dépend du nombre de produits souscrits qui, à son tour, détermine le nombre de produits mis en file d'attente. En général, lorsqu'il y a une file d'attente de plus de 25 000 produits et qu'il n'y a pas de client, la file d'attente est purgée.

En général, il est préférable d'utiliser un accès continu plutôt qu'une consultation périodique, car cela permet de supprimer les pics de bande passante de téléchargement et de charge du serveur, et de réduire le risque que les files d'attente soient purgées sur le serveur. L'utilisation judicieuse de la directive "subtopic" dans les configurations réduira la taille des files d'attente, afin qu'elles puissent demeurer actives pendant les longues interruptions.

## Comment utiliser AMQP sous Windows ?

Si vous utilisez l’environnement Windows, vous devez télécharger la dernière version de Sarracenia à cette adresse :

https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/
Il s’agit d’un fichier EXE qui peut être utilisé sans avoir à installer d’environnement Python.

Voir les détails ici : https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst

## Contactez-nous
Si vous utilisez les données disponibles sur le Datamart du SMC, nous vous recommandons vivement de vous inscrire à la liste de diffusion dd_info afin d'être averti de toute mise à jour ou modification concernant les données disponibles. 

Vous pouvez vous inscrire ici :

https://lists.ec.gc.ca/mailman/listinfo/dd_info

Veuillez utiliser l'adresse suivante pour nous contacter pour tout commentaire ou question :

ec.dps-client.ec@canada.ca













