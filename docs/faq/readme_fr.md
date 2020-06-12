[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > FAQ

# FAQ des données ouvertes du SMC

Cette section contient les questions les plus fréquemment posées au sujet des données ouvertes du SMC.


## Table des matières

* [Peut-on avoir accès aux scores de vérification de vos modèles de prévision numérique du temps et comment se comparent-ils par rapport aux autres centres internationaux ?](#peut-on-avoir-acces-aux-scores-de-verification-de-vos-modeles-de-prevision-numerique-du-temps-et-comment-se-comparent-ils-par-rapport-aux-autres-centres-internationaux)
* [J’aimerais utiliser vos données à des fins lucratives, ai-je le droit ?](#j-aimerais-utiliser-vos-donnees-a-des-fins-lucratives-ai-je-le-droit)
* [Pourquoi les files d’attente de message AMQP cessent après plusieurs heures d'inactivité ?](#pourquoi-les-files-d-attente-de-message-amqp-cessent-apres-plusieurs-heures-d-inactivite)
* [Peut-on avoir accès aux données radar météorologiques ?](#peut-on-avoir-acces-aux-donnees-radar-meteorologiques)
* [Peut-on accéder aux données radar archivées ?](#peut-on-acceder-aux-donnees-radar-archivees)
* [Est-ce que les prévisions historiques des modèles de prévision numérique du temps sont disponibles ?](#est-ce-que-les-previsions-historiques-des-modeles-de-prevision-numerique-du-temps-sont-disponibles)
* [Comment être informé des changements aux bulletins ainsi qu'aux contenu et format des modèles de prévision numérique du temps ?](#comment-etre-informe-des-changements-aux-bulletins-ainsi-qu-aux-contenu-et-format-des-modeles-de-prevision-numerique-du-temps)
* [Comment être informé des problèmes de production des données de modèles de prévision numérique du temps ?](#comment-etre-informe-des-problemes-de-production-des-donnees-de-modeles-de-prevision-numerique-du-temps)
* [Pourquoi ne pas produire un seul gros fichier GRIB avec toutes les variables ?](#pourquoi-ne-pas-produire-un-seul-fichier-grib-avec-toutes-les-variables)
* [Qu'est-ce que le système de coordonnées de référence ou datum d'un modèle de prévision numérique du temps ?](#qu-est-ce-que-le-systeme-de-coordonnees-de-reference-ou-datum-d-un-modele-de-prevision-numerique-du-temps)
* [Comment peut-on obtenir la topographie d'un modèle de prévision numérique du temps ?](#comment-peut-on-obtenir-la-topographie-d-un-modele-de-prevision-numerique-du-temps)
* [Est-il possible d'avoir le masque terre mer d'un modèle de prévision numérique du temps ?](#est-il-possible-d-avoir-le-masque-terre-mer-d-un-modele-de-prevision-numerique-du-temps)
* [Est-il possible d’avoir accès à d’autres paramètres de modèles de prévision numérique du temps que ceux disponibles actuellement ou la liste est-elle exhaustive ?](#est-il-possible-d-avoir-acces-a-d-autres-parametres-de-modeles-de-prevision-numerique-du-temps-que-ceux-disponibles-actuellement-ou-la-liste-est-elle-exhaustive)
* [Puis-je obtenir les données d’équivalent en eau de la neige ?](#puis-je-obtenir-les-donnees-d-equivalent-en-eau-de-la-neige)
* [Dans le journal de chronologie des modifications des modèles de prévision numérique du temps, je vois plusieurs systèmes (ex : SRPEOT) non mentionnés parmi la liste des systèmes dont les données sont disponibles, où puis-je trouver ces données ?](#dans-le-journal-de-chronologie-des-modifications-des-modeles-de-prevision-numerique-du-temps-je-vois-plusieurs-systèmes-ex-srpeot-non-mentionnes-parmi-la-liste-des-systemes-dont-les-donnees-sont-disponibles-ou-puis-je-trouver-ces-donnees)
* [Quelle est la différence entre les deux jeux de données d'observations disponibles sur le Datamart du SMC ?](#quelle-est-la-difference-entre-les-deux-jeux-de-donnees-d-observations-disponibles-sur-le-Datamart-du-SMC?)
* [À quelle fréquence les données d’observations rassemblées par province et territoire sont-elles rafraichies ?](#a-quelle-frequence-les-donnees-d-observations-rassemblees-par-province-et-territoire-sont-elles-rafraichies)
* [Où pourrais-je trouver les données de bouées ?](#ou-pourrais-je-trouver-les-donnees-de-bouee)
* [Comment faire pour accéder aux avertissements ?](#comment-faire-pour-acceder-aux-avertissements)
* [Quelles sont les principales différences entre un fil de données ATOM et le protocole AMQP pour accéder aux avertissements ?](# quelles-sont-les-principales-differences-entre-un-fil-de-donnees-atom-et-le-protocole-amqp-pour acceder-aux-avertissements)
* [Les images satellitaires sont-elles disponibles ?](#les-images-satellitaires-sont-elles-disponibles)
* [Les données de foudre sont-elles disponibles ?](#les-donnees-de-foudre-sont-elles-disponibles)
* [Comment obtenir les températures minimales et maximales en format CSV ?](#comment-obtenir-les-temperatures-minimales-et-maximales-en-format-csv)
* [Est-il possible d'avoir accès aux hauteurs cumulatives de pluie prévue ?](#est-il-possible-d-avoir-acces-aux-hauteurs-cumulatives-de-pluie-prevue)
* [Je ne vois pas de « conditions actuelles » sous l'élément correspondant dans le fichier citypage_weather en format XML, est-ce normal ?](#je-ne-vois-pas-de-conditions-actuelles-sous-l-element-correspondant-dans-le-fichier-citypage-weather-en-format-xml-est-ce-normal)
* [Est-il possible d'avoir accès aux données observées passées de qualité de l'air et aux données d'émission des polluants utilisées pour calculer la cote air santé ?](#est-il-possible-d-avoir-acces-aux-donnees-observees-passees-de-qualite-de-l-air-et-aux-donnees-d-emission-des-polluants-utilisees-pour-calculer-la-cote-air-sante)
* [Existe-t-il une plateforme de discussion pour les usagers ?](#existe-t-il-une-plateforme-de-discussion-pour-les-usagers)

## Peut-on avoir accès aux scores de vérification de vos modèles de prévision numérique du temps et comment se comparent-ils par rapport aux autres centres internationaux ?

Le [Centre européen de prévision à moyen terme (CEPMT)](https://www.ecmwf.int/), désigné en 2011 comme le [''WMO Lead Centre for Deterministic NWP Verification''](https://confluence.ecmwf.int/pages/viewpage.action?pageId=24316358&src=sidebar), rend disponibles tous les scores en altitude et de surface de tous les centres participants à l’échange de scores des pays de l’[Organisation météorologique mondiale (OMM)](https://public.wmo.int/fr).

Ainsi, il est possible d'obtenir les [scores en altitude](https://apps.ecmwf.int/wmolcdnv/scores/time_series/msl) des modèles de prévision de Environnement et Changement climatique Canada et de les comparer aux scores des autres centres, selon le domaine souhaité (ex: hémisphère nord), pour les paramètres d'intérêt (ex: température à 850hPa), depuis 1998 à nos jours.

Les [scores de surface](https://apps.ecmwf.int/wmolcdnv/scores/surface.time_series/tp) sont relativement nouveaux et tous les centres ne fournissent pas encore leurs métriques, ce qui est notre cas, mais nous travaillons actuellement pour les rendre disponibles. Il sera donc possible prochainement de comparer nos scores de surface à ceux de nos homologues internationaux.

Par ailleurs, nous publions quotidiennement des [vérifications contre radiosondages et analyses](https://meteo.gc.ca/verification/index_f.html) pour le [Système global de prévision déterministe (SGPD)](../msc-data/nwp_gdps/readme_gdps_fr.md) et le [Système régional de prévision déterministe (SRPD)](../msc-data/nwp_rdps/readme_rdps_fr.md), suivant les standards définis par l'OMM.

## J’aimerais utiliser vos données à des fins lucratives, ai-je le droit ?

Oui, il est possible d’utiliser nos données à des fins lucratives. Vous trouverez toutes les informations nécessaires à l’utilisation de nos données dans la [licence d'utilisation](../licence/readme_fr.md).

## Pourquoi les files d’attentes de message AMQP cessent après plusieurs heures d'inactivité ?

Les utilisateurs du service [AMQPS](../msc-datamart/amqp_fr.md) sont censés exécuter un daemon qui télécharge des données en permanence, comme celui fourni par [Sarracenia](https://github.com/MetPX/sarracenia/blob/master/doc/fr/sarra.rst). Dans le langage AMQP, une pompe, à savoir un hôte exécutant Sarracenia, est un [courtier](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst). Le courtier a une capacité limitée à mettre les produits en file d'attente lorsqu'un utilisateur est victime d'une longue interruption involontaire, par exemple de quelques heures à quelques jours. 

La performance de l'ensemble du service est affectée par la présence de files d'attente importantes pour un seul consommateur, il ne faut donc pas laisser les files d'attente s'accumuler indéfiniment. 

Nous maintenons les files d'attente en vie aussi longtemps que nous pouvons raisonnablement le faire, mais cette pratique vise uniquement à donner aux clients le temps de redémarrer leur service en cas d'échec. La durée des déconnexions qui peuvent être supportées en toute sécurité dépend du nombre de produits souscrits qui, à son tour, détermine le nombre de produits mis en file d'attente. En général, lorsqu'il y a une file d'attente de plus de 25 000 produits et qu'il n'y a pas de client, la file d'attente est purgée.

En général, il est préférable d'utiliser un accès continu plutôt qu'une consultation périodique, car cela permet de supprimer les pics de bande passante de téléchargement et de charge du serveur, et de réduire le risque que les files d'attente soient purgées sur le serveur. L'utilisation judicieuse de la directive "subtopic" dans les configurations réduira la taille des files d'attente, afin qu'elles puissent demeurer actives pendant les longues interruptions.

## Peut-on avoir accès aux données radar météorologiques ?

Les données radar actuellement disponibles gratuitement sur le serveur de données ouvertes du SMC sont les [images GIF]( ../msc-data/obs_radar/readme_radarimage-datamart_fr.md). Nous offrons également la [mosaique radar nord-américaine](../msc-data/obs_radar/readme_radar_geomet_fr.md) via les services web géospatiaux WMS.

Les données brutes ainsi que divers autres produits, sont fournis par un [service à recouvrement de coûts](../cost-recovered/readme_fr.md#fil-de-donnees-dedie). Dans le cadre de ce service, nous poussons les données vers le serveur FTP des clients et assurons un service 24/7. La documentation concernant les [produits radar](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf) et les [formats de données radar](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf) est disponible.

Concernant les fils de données, les formats disponibles sont les suivants :

* NUMERIC (ASCII)
* Images GIF (les récentes données GIF sont disponibles gratuitement sur le Datamart du SMC)
* Format brut [IRIS](http://www.vaisala.com/en/defense/products/weatherradar/Pages/IRIS.aspx), pour les anciens radars à bande C
* Format brut [ODIM_H5](https://support.hdfgroup.org/HDF5/users5.html), pour les nouveaux radars à bande S
   
## Peut-on accéder aux données radar archivées?

Environnement et Changement climatique Canada n'a pas de service en ligne pour accéder aux données archivées. Le service de désarchivage est à [recouvrement de coût](../cost-recovered/readme_fr.md#service-de-desarchivage), nous chargeons 99$/heure de travail nécessaire pour produire les données avec un coût minimum de 99$. Les données par elles-mêmes étant gratuites.

Les archives sont disponibles en format brut (IRIS/ODIM_H5) ou en format ASCII. La documentation concernant les [produits radar](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Radar_Products_Available_CMC_Mai_2015_external.pdf) et des 
[formats de données radar](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/produits/samples/radar/vscan/Formats_used_in_URP_En_last_version.pdf) est disponible.

Des requêtes typiques de désarchivage demandent entre 2 et 4 heures de travail. Si intéressé, merci de compléter le formulaire ci-dessous et de le faire parvenir à l'adresse : ec.dps-client.ec@canada.ca

| Information | Valeur |
|-------------|:-----:|
|Noms des radars |       |       
|Type de produits (Raw, CAPPI, PRECIP, ECHOTOP, etc.) |       |
|Unités (dBZ, mm/hr) |       |
|Format (GIF, Numeric, IRIS/ODIM_H5) |       |
|Periode de temps (UTC) |       |
|Fréquence (default: 10 minutes) |       |
|Format de livraison (zip, tar, autre) |       |
|Date de livraison désirée (quand?) |       |
|Autres informations |       |
|Coordonnées de facturation |      |

## Est-ce que les prévisions historiques des modèles de prévision numérique du temps sont disponibles ?

Environnement et Changement climatique Canada n'a pas de service en ligne pour accéder aux données archivées. Le service de désarchivage est à [recouvrement de coût](../cost-recovered/readme_fr.md#service-de-desarchivage), nous chargeons 99$/heure de travail nécessaire pour produire les données avec un coût minimum de 99$. Les données par elles-mêmes étant gratuites.

Dès que nous recevons les détails des données demandées, nous pouvons produire un échantillon et l’envoyer à l’usager pour validation. Un estimé peut alors être fourni, une fois la requête confirmée. Selon la nature des requêtes, il faut compter quelques centaines de dollars. Pour toute commande, merci de compléter le formulaire ci-dessous et de le faire parvenir à l'adresse: ec.dps-client.ec@canada.ca

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

Notes :

* Les archives remontent aux 5 dernières années, selon la disponibilité des données 
* Compte-tenu du gros volume de demandes, un certain délai est à prévoir. Merci d'indiquer si la demande est urgente, nous tenterons alors de la prioriser

## Comment être informé des changements aux bulletins ainsi qu'aux contenu et format de modèles de prévision numérique du temps ?

Pour les bulletins de stations canadiennes, tout changement dans l'en-tête et le nom des stations est annoncé via ce que nous appelons les GENOT (GEneral NOTification) message. Nous avons une liste de diffusion pour distribuer les GENOTs, si cela vous intéresse, contactez-nous à l'adresse : ec.dps-client.ec@canada.ca et nous vous ajouterons à la liste de diffusion. En parallèle, ces [bulletins sont disponibles sur le Datamart du SMC](https://dd.meteo.gc.ca/doc/genots/). 

Pour être averti des changements majeurs, tels qu'un changement de résolution par exemple, vous pouvez consulter les bulletins GENOT 03. Vous pouvez trouver un [exemple d'un tel bulletin](https://dd.meteo.gc.ca/doc/genots/2014/02/18/NOCN03_CWAO_182045___01117).

Finalement, nous vous recommandons fortement de vous inscrire à nos listes de diffusion [dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info) et [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) afin d'être averti de toute mise à jour ou changement concernant la disponibilité des données. 

## Comment être informé des problèmes de production des données de modèles de prévision numérique du temps ?

Il arrive parfois que les données de modèle de prévision numérique du temps soient en retard ou même absentes de nos services de dissémination de données. Afin de savoir si ce délai ou cette absence est dû à un problème de production, vous pouvez consulter les bulletins AACN01 CWAO.  Ces derniers sont des bulletins émis par le CCMEP au besoin pour informer les bureaux du SMC et d'autres clients de tout problème pouvant perturber ou retarder l'émission et/ou la distribution des produits opérationnels.

Pour consulter les derniers bulletins AACN01 CWAO, vous pouvez utiliser l'[utilitaire de recherche de script](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_fr.pdf) mis à votre disposition par ECCC. [Exemple pour obtenir les bulletins AACN01 du jour](https://dd.meteo.ec.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01). Pour un jour précis, vous pouvez préciser votre recherche. [Exemple pour obtenir les informations pour le 19 mai 2020](https://dd.meteo.gc.ca/cgi-bin/bulletin_search.pl?product=AA&location=CN01&day=19&month=05&year=2020).

Il existe par ailleurs une liste de diffusion des bulletins AACN01. Si vous êtes intéressés, veuillez nous contacter à l'adresse ec.dps-client.ec@canada.ca et nous vous ajouterons à la liste de diffusion.

## Pourquoi ne pas produire un seul gros fichier GRIB avec toutes les variables ?

Il a été choisi de mettre une variable par fichier car nous avons supposé que la plupart des utilisateurs n'auraient pas besoin de toutes les variables. La vitesse de téléchargement sera la même que si tous les fichiers GRIB étaient dans un seul fichier zip.

## Qu'est-ce que le système de coordonnées de référence (datum) d'un modèle de prévision numérique du temps ?

Pour connaitre le système de coordonnées de référence d’un modèle de prévision numérique du temps et la projection utilisée pour produire nos fichiers de prévision numérique du temps, il suffit d’utiliser les outils [GDAL](https://www.gdal.org/GDAL) (logiciel libre). La commande suivante vous fournira le référentiel et la projection du fichier : `gdalinfo -proj4 file.grib2`.

En sortie, l'information commence par `The coordinates system is:`. Cette commande donne aussi accès à la projection sous format Proj4 qui est couramment utilisée dans les outils géospatiaux.

## Comment peut-on obtenir la topographie d'un modèle de prévision numérique du temps ?

La topographie d’un modèle de prévision numérique du temps dont les données sont disponibles en format GRIB2 peut être obtenue en utilisant le champ `HGT_SFC` (topographie lissée du modèle).

## Puis-je avoir le masque terre-mer d’un modèle de prévision numérique du temps ?

Pour un modèle de prévision numérique du temps dont les données sont disponibles en format GRIB2, le paramètre `LAND_SFC` (couverture terrestre) de l'heure de prévision 00h pour être utilisé déterminer ce masque. Lorsque la valeur est `0`, il s'agit de la mer, lorsque la valeur n'est pas `0`, il s'agit de la terre (ou d'une partie de celle-ci).

## Est-il possible d’avoir accès à d’autres paramètres de modèles de prévision numérique du temps que ceux disponibles actuellement ou la liste est-elle exhaustive ?

La liste n'est pas exhaustive. Nous sommes toujours très ouverts à recevoir de la rétroaction des usagers et de connaître leurs besoins. Il est possible de communiquer avec nous via l’adresse courriel : ec.dps-client.ec@canada.ca

## Puis-je obtenir des données d'équivalent en eau de la neige ?

L'estimation de la masse de neige est surtout valable pour le sol. Le paramètre GRIB `SNOD` représentant l’épaisseur de neige au sol est disponible en tant que valeur agrégée mais le paramètre `SDEN` (densité de neige) n'est disponible que pour la fraction du sol. Le produit `SNODxSDENxfacteur` pour les unités fournit probablement la meilleure estimation actuellement disponible pour l'équivalent en eau de la neige. Sachez que le paramètre `SDEN` de la fraction de sol peut ou non être représentatif de la densité de neige pour les autres types de surface.

Par conséquent, la micro équation pour le calcul de l'équivalent en eau de la neige en mm (équivalent à kg/m2) à partir de la densité absolue `SDEN` et de l'épaisseur `SNOD` s'exprime selon :

* Si l'épaisseur est donnée en "cm" et `SDEN` en "kg/m3", ce que nous avons aux opérations, alors `SWE = (SNOD * SDEN) / 100` ; `SWE` est en mm (ou kg/m2, c'est l'équivalent pour l'eau)
* Si l'épaisseur est donnée en "m" et le `SDEN` en "kg/m3", alors `SWE = SNOD * SDEN` ; `SWE` est en mm (kg/m2)

## Dans le journal de chronologie des modifications des modèles de prévision numérique du temps, je vois plusieurs systèmes (ex : SRPEOT) non mentionnés parmi la liste des systèmes dont les données sont disponibles, où puis-je trouver ces données ?

Ces données ne sont pas encore disponibles sur le Datamart du SMC. Pour être informé de l’ajout de jeux de données, vous pouvez vous abonner aux listes de diffusion [dd-info](https://lists.ec.gc.ca/mailman/listinfo/dd_info) et [GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info).

## Quelle est la différence entre les deux jeux de données d'observations disponibles sur le Datamart du SMC ?

Nous avons 2 produits qui contiennent des observations du réseau de stations de Environnement et Changement climatique Canada.

L’un est de type une station par fichier, il s’agit des observations météorologiques au sol et marines par station, les [données SWOB](../msc-data/obs_station/readme_obs_insitu_swobdatamart_fr.md), disponibles en format XML. Toutes les données des stations canadiennes sont disponibles dans ce produit.

Le second regroupe les [données d’observation d’une même province ou territoire](../msc-data/obs_station/readme_obs_insitu_xmldatamart_fr.md) par fichier, en format XML. Toutes les stations canadiennes ne sont pas contenues dans ce produit. Ce sont ces données qui sont utilisées dans le site web des prévisions officielles meteo.gc.ca. De ce fait, elles sont soumises à certaines règles (ex : pour les vents, utilisation de la moyenne observée sur une période de 2 minutes, si cela n’est pas possible utilisation d’une moyenne sur 10 minutes).

Par conséquent, on ne peut pas vraiment comparer ces 2 jeux de données et il est fortement conseillé d’utiliser les données SWOB, plus complètes et soumises à aucune règle, pour la région d’intérêt.

## À quelle fréquence les données d’observations rassemblées par province et territoire sont-elles rafraichies ?

Les [fichiers sommaires provinciaux](../msc-data/obs_station/readme_obs_insitu_xmldatamart_fr.md) sont mis à jour 6 fois par heure, mais le simple fait que nous les mettions à jour ne signifie pas nécessairement qu'une des stations du fichier sommaire a mis à jour ses données depuis la dernière exécution. Nous mettons à jour les observations sur une base horaire (et non à la minute) pour chaque station, au début de l'heure, mais une autre mise à jour (appelée obs spéciale ou "speci") à l’intérieur de l’heure est aussi possible si l'observateur estime qu'il y a eu un changement suffisamment important pour justifier une mise à jour.

Il est possible, par exemple, que le fichier de 1614Z ne contienne pas d'observations différentes de celles de 1611Z, de sorte que l'utilisateur ne doit pas toujours s'attendre à des changements de valeurs pour une station individuelle au cours de l'heure. Nous ne présentons que les données que nous obtenons et, dans ce cas, la plupart des stations ne rapportent qu'une fois par heure. 
 
## Où pourrais-je trouver des données de bouées ?

Les données de bouées (observations marines) sont disponibles sur le Datamart du SMC à cette adresse :

[https://dd.meteo.gc.ca/observations/swob-ml/marine/moored-buoys]( https://dd.meteo.gc.ca/observations/swob-ml/marine/moored-buoys)

Vous trouverez dans la [documentation](../msc-data/obs_station/readme_obs_insitu_swobdatamart_fr.md), une liste des bouées disponibles actuellement. D’autres seront ajoutées au cours du temps.

Des rapports quotidiens de bouées du SMC sont aussi publiés sur le [site web de Pêches et Océans Canada](http://www.meds-sdmm.dfo-mpo.gc.ca/isdm-gdsi/waves-vagues/msc-smc/index-fra.html). Des informations sur les [bouées dérivantes](http://www.dfo-mpo.gc.ca/science/data-donnees/drib-bder/index-fra.html) sont également disponibles. 

Finalement, ces données de bouées sont accessibles à travers les [bulletins alphanumériques](../msc-data/bulletins/readme_bulletins-datamart_fr.md)  disponibles sur le Datamart du SMC avec comme en-têtes SM/SN/SIVD17.

## Comment faire pour accéder aux avertissements ?

Il y a plusieurs sources pour obtenir les avertissements.

* Tout d’abord, les [avertissements officiels sont disponibles en format PAC-XML sur le Datamart du SMC](https://dd.meteo.gc.ca/alerts/cap). La [documentation](../msc-data/alerts/readme_alerts-datamart_fr.md) détaille ces données et donne également des informations concernant les critères d’alertes de la prévision publique ainsi des informations géographiques des emplacements des prévisions, pour tous les messages en format PAC.

* Nos services web géospatiaux permettent d'afficher la couche des avertissements seulement dans la [version Beta](../msc-geomet/readme_fr.md) actuellement. Veuillez surveiller notre liste de diffusion [GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) pour être informé lorsque ces avertissements seront disponibles dans GeoMet-Météo.

* Par ailleurs, ECCC a mis en place un [fil de nouvelles ATOM via lequel les alertes et avertissements sont disponibles](https://meteo.gc.ca/business/index_f.html#rss).

* Finalement, ECCC a mis en place le [service expérimental EC Alertez moi](https://ecalertezmoi.meteo.gc.ca/guides/quickstart_fr.php) pour envoyer les avertissements par messagerie électronique. 

## Quelles sont les principales différences entre un fil de données ATOM et le protocole AMQP pour accéder aux avertissements ?

La principale différence entre le fil de données ATOM et le protocole AMQP est que dans le cas du fil ATOM, l'utilisateur doit envoyer une requête pour savoir si les nouveaux fichiers sont disponibles, alors qu'avec l'AMQP, l'utilisateur est averti sans envoyer de requête.

Si l'on veut faire une analogie, les fils ATOM peuvent être considérés comme un facteur qui dépose des lettres dans la boîte aux lettres, alors que AMQP peut être considérée comme un livreur qui sonne à la porte pour remettre le colis postal. Nous recommandons fortement d'utiliser le protocole AMQP qui permet de récupérer les données source.

## Les images satellitaires sont-elles disponibles ?

Environnement et Changement climatique Canada ne distribue pas actuellement d’images satellites ou de produits dérivés aux usagers externes, à l'exception de notre [site web](https://weather.gc.ca/satellite/index_f.html), car nous ne sommes pas le producteur des données.

Un site recommandé pour obtenir gratuitement les images satellites est celui de l'[Université de Washington](https://www.atmos.washington.edu/~ovens/loops/). Pour l’installation d'un fil de données d'images satellites, nous suggérons aux utilisateurs de contacter nos homologues américains à la NOAA ou de chercher un fournisseur dans le secteur privé.

## Les données de foudre sont-elles disponibles ?

Actuellement, seule [la carte canadienne des dangers de la foudre est disponible](https://meteo.gc.ca/lightning/). Veuillez noter que vous devez mettre à jour manuellement le site web. Il ne se met pas à jour tout seul, contrairement au site des images radar. Les données ne sont pas encore disponibles parmi l'offre de données ouvertes, veuillez surveiller nos listes de diffusion [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) et [GeoMet-Info](http://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) pour être tenu informé.
 
En attendant, si vous souhaitez acheter des données sur la foudre en temps réel ou archivées, auprès du Réseau canadien de détection de la foudre (CLDN), veuillez contacter nos collègues à l'adresse : ec.rcdf-cldn.ec@canada.ca . Il y a un coût pour les entreprises privées. Le prix dépend de la superficie dont ils ont besoin pour les données en direct et de la durée des données archivées. Si le client envoie au CLDN ses spécifications, un estimé du coût sera transmis (demande envoyée à Vaisala). 

## Comment obtenir les températures minimales et maximales en format CSV ?

Pour obtenir des données de températures extrêmes prévues au format CSV, vous pouvez consulter au choix :

* Les bulletins de prévision FMCN31 à FMCN38 (format CSV), basés sur le [Système global de prévision déterministe (SGPD)](../msc-data/nwp_gdps/readme_gdps_en.md). Les prévisions à 00Z contiennent le maximum du jour en cours, le minimum et le maximum du deuxième jour et le minimum du troisième jour. Les prévisions de 12Z contiennent les minima et maxima du jour deux et du jour trois.

* Les bulletins de prévision FMCN41 à FMCN48 (format CSV), basés sur le [Système régional de prévision déterministe (SRPD) ](../msc-data/nwp_rdps/readme_rdps_en.md). Les prévisions à  12Z contiennent les minima et maxima du jour deux et les minima du jour trois. Les prévisions basées sur les données à 00Z contiennent le maximum du jour en cours et le minimum et le maximum du jour deux.

Ces bulletins sont disponibles sur le Datamart du SMC, à l'adresse : https://dd.meteo.gc.ca/bulletins/alphanumeric/YYYYMMDD/FM/CWAO/

## Est-il possible d'avoir accès aux hauteurs cumulatives de pluie prévue ?

En ce qui concerne les données QPF (Quantitative Precipitation Forecast) au format CSV, vous pourriez être intéressés par les bulletins FOCN03, à savoir les prévisions ponctuelles de variables météorologiques obtenues à partir des sorties directes du SRPD (Système régional de prévision déterministe).

Chacun de ces bulletins est produit spécifiquement pour des sites de prévision canadiens individuels. Le contenu est donc variable. Par exemple, les valeurs des paramètres de prévision sont disponibles à des intervalles de 6 heures de 0 à 48 heures pour certains bulletins, et à des intervalles de 6 heures de 0 à 24 heures et à des intervalles de 12 heures de 24 à 48 heures pour certains autres. Les éléments de prévision météorologique peuvent également varier d'un message à l'autre.

Ces [bulletins sont disponibles sur le  Datamart du SMC](https://dd.meteo.gc.ca/bulletins/focn03). Une [interface de recherche de bulletins](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/bulletins/CMC_Bulletin_Search_Help_en.pdf) pour le serveur de données HTTPS du Service météorologique du Canada est également [disponible](https://dd.weather.gc.ca/cgi-bin/bulletin_search.pl).

Aussi, une estimation optimale de la quantité de précipitation qui est survenue au cours de périodes passées récentes de 6h ou 24h est disponible dans les données de l'[Analyse régionale déterministe de précipitation](../msc-data/nwp_rdpa/readme_rdpa_fr.md). Cet estimé intègre des relevés provenant de capteurs de précipitation, de radar météo et de modèles de prévision numérique du temps. La couverture géographique est l'Amérique du Nord (Canada, États-Unis et le Mexique).

## Je ne vois pas de « conditions actuelles » sous l'élément correspondant dans le fichier citypage_weather en format XML, est-ce normal ?

Certaines stations météorologiques sont automatiques (sans personnel) et ne signalent pas l'état des conditions actuelles. Si vous regardez la page correspondante sur notre site web, par exemple pour la ville d’[Edmonton](https://weather.gc.ca/city/pages/ab-50_metric_e.html), vous verrez qu'il est écrit « Non observé » pour la condition. C'est pourquoi aucune icône ou condition n'est signalée dans le fichier XML Citypage correspondant.

## Est-il possible d'avoir accès aux données observées passées de qualité de l'air et aux données d'émission des polluants utilisées pour calculer la cote air santé ?

Au Canada, les données d'observation de qualité de l'air sont généralement produites par les provinces et municipalités et récoltées par ECCC. C’est vrai tant pour le temps réel que pour les données « officielles » qui font l'objet d'un contrôle qualité détaillé et qui sont habituellement publiées l'année suivante.  Ces données officielles sont assemblées dans la base de données du programme de [Surveillance national de la pollution atmosphérique (SNPA)](http://data.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/?lang=fr), maintenant sur le catalogue de données ECCC.

Aussi, un certain nombre de stations canadiennes sont disponibles dans la base de données américaine [AirNow](https://www.airnow.gov/aqi-and-health/), et sont aussi téléchargeables dans le projet ouvert [OpenAQ](https://openaq.org/#/map?parameter=o3&_k=6p035e). De son côté, ECCC publie uniquement les observations sous la forme de la cote air santé, et celles-ci se trouvent le [Datamart du SMC](../msc-data/aqhi/readme_aqhi_fr.md).

Enfin, il est possible de consulter [l'Inventaire national des rejets de polluants](https://www.canada.ca/fr/environnement-changement-climatique/services/inventaire-national-rejets-polluants/outils-ressources-donnees/explorerdonnees.html). Veuillez noter qu'on accorde beaucoup de temps aux installations polluantes pour déclarer leurs émissions, par conséquent l’information est publiée plus d’un an après la date courante, sur une base annuelle.

## Existe-t-il une plateforme de discussion pour les usagers ?

Une plateforme de discussion consacrée aux données ouvertes du SMC a été mise en place par une tierce partie afin de permettre à la communauté des usagers d'interagir plus facilement et de tirer profit de l'expérience de chacun:

[http://meteocentre.com/help/msc-open-data/](http://meteocentre.com/help/msc-open-data/)

Nous approuvons et applaudissons cette initiative, mais nous tenons à préciser qu'ECCC ainsi que le SMC ne sont pas responsables de ce site et que leurs employés n'ont pas l'obligation de répondre aux questions posées. Quand des employés d'ECCC ou du SMC participent, ils le font à titre personnel.