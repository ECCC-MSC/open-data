[In English](readme_nowcasting-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Prévisions immédiates](readme_nowcasting_fr.md) > Prévisions immédiates sur le Datamart du SMC


# Matrices scribe de prévision immédiates

Les fichiers de [matrices de prévisions immédiates](readme_nowcasting_fr.md) sont mis à jour à chaque heure et contiennent un ensemble cohérent d'éléments du temps observés et prévus à très court terme pour des points de prévision correspondant généralement à des sites de stations d'observation. Il y a plus de 450 points de prévision dans la matrice.

Les observations horaires de surface (METAR-SPECI) et synoptiques sont traités ainsi que les observations de foudre.

On utilise des modèles de prévision numérique du temps, des modèles statistiques ainsi que des système de prévisions immédiates de pair avec les observations pour préparer les données prévues. 

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à adresse suivante :

* [https://dd.meteo.gc.ca/nowcasting/matrices/](https://dd.meteo.gc.ca/nowcasting/matrices/)

Un historique de 24 heures est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

SCRIBE.NWCSTG.10.24.06Z.n.Z

où :

* __SCRIBE__ : Nom du système principal de production
* __NWCSTG__ : Identification du type de données (ici Prévisions immédiates) des matrices présentes dans le fichier
* __10.24.06Z__ : MM.DD.HHZ MM: Mois, DD: date. HH: Heure UTC de la passe. Z:  Identificateur UTC
* __n__ : Extension de fichier identifiant le type Prévisions immédiates
* __Z__ : Identificateur de compression Unix

## Données

### Exemple et description du contenu d'une matrice de prévision immédiate.

 
|  1    |  2 | 3 | 4 |  5  | 6|   7  | 8 |  9  | 10| 11| 12 | 13|  14 |  15 |16 | 17| 18|  19 |20|  
|--------|-----|---|---|-----|---|-----|---|-----|----|---|---|---|-----|-----|----|---|---|----|---|
|DATE    |  HR |/10|   |PCPN1|POP|PCPN2|POP|PCPN3|POP|   | Qp | Tp|  T  |  Td | DD| VV|GST|(SM) |TP|
|20040122 0200| 10| 41| -S  |100|     |  0|     |  0|100| 0.2| SN| -6.0| -8.0|200| 22| 33| 2.00|PP|
|20040122 0300| 10| 24| -S  |100|     |  0|     |  0|100| 0.2| SN| -6.0| -7.0|200| 15|   | 1.75|PP|
|20040122 0400| 10| 23| -S  |100|     |  0|     |  0|100| 0.2| SN| -5.0| -6.0|200| 17|   | 2.50|PP|
|20040122 0500|  9| 25| -S  |100|     |  0|     |  0| 90| 0.0|   | -5.0| -6.0|206| 17|   | 7.98|  |
|20040122 0600|  9| 87|     |  0|     |  0|     |  0|  0| 0.0|   | -5.0| -6.0|190| 11|   |12.00|  |
|20040122 0700| 10| 50| -S  |100|     |  0|     |  0|100| 0.0|   | -4.0| -6.0|185|  9|   | 6.75|  |
|20040122 0800| 10| 88| -S  |100|     |  0|     |  0| 80| 0.0|   | -3.0| -5.0|203| 17|   |10.21|  |
|20040122 0900|  9|999| -SW |100|     |  0|     |  0| 60| 0.0|   | -2.7| -5.1|221| 18| 29|15.00|  |
|20040122 1000|  9|999| -SW |100|     |  0|     |  0| 60| 0.0|   | -3.8| -7.2|229| 24| 34|15.00|  |
|20040122 1100|  9|999| -SW |100|     |  0|     |  0| 30| 0.0|   | -4.8| -7.5|236| 30| 40|15.00|  |
|20040122 1200|  9|999|     |  0|     |  0|     |  0|  8| 0.0|   | -5.9| -8.6|242| 36| 46|15.00|  |
|20040122 1300|  9|999|     |  0|     |  0|     |  0| 11| 0.0|   | -5.9| -8.7|252| 38| 48|15.00|  |
|20040122 1400|  9|999|     |  0|     |  0|     |  0| 15| 0.0|   | -6.0| -8.8|261| 39| 49|15.00|  |
|20040122 1500|  9|999|     |  0|     |  0|     |  0| 16| 0.0|   | -6.0| -9.4|270| 41| 51|15.00|  |
|20040122 1600|  9|999|     |  0|     |  0|     |  0| 22| 0.0|   | -6.0|-10.0|274| 41| 51|15.00|  |
|20040122 1700|  9|999| -S  |100|     |  0|     |  0| 80| 0.2| SN| -6.0|-10.0|278| 41| 51|15.00|  |
|20040122 1800| 10|999| -S  |100|     |  0|     |  0|100| 0.5| SN| -6.0|-10.0|282| 41| 51|15.00|  |
|20040122 1900|  9|999| -S  |100|     |  0|     |  0| 80| 0.4| SN| -6.7|-10.8|281| 41| 51|15.00|  |
|20040122 2000|  9|999| -S  |100|     |  0|     |  0| 80| 0.2| SN| -7.3|-11.7|279| 40| 50|15.00|  |


Dans cet exemple la séquence de données commence à 02Z puis est suivie par 6 heures d'observations précédentes l'heure de la passe 08Z, puis se termine 12 heures plus tard à 20Z, pour totaliser 19 heures de données (6 heures de données passées, plus l'heure courante d'observation (moment de la passe) et 12 heures de données prévues)
 
### Description des colonnes de gauche à droite.

__Colonne no. :__

__1 & 2__ : Les deux premières colonnes donne la date et l'heure. Le moment de la
       passe courante est la 7e ligne de la matrice (celle entre les deux lignes en pointillés)

__3 & 4__ : la colonne 3 donne la nébulosité du ciel en dixièmes, et la colonne 4
       la hauteur du plafond en  centaines de pieds. Si aucun plafond n'est prévu le code «999» 
       sera utilisé. Notez que cette valeur du plafond est là seulement pour des raisons techniques et 
       n'est pas très fiable, certainement pas pour la prévision à l'aviation.

__5, 6, 7, 8, 9, 10__ : Ces six colonnes représentes les types de précipitations
       avec leur probabilité d'occurrence, qui ne doit pas être confondu avec la
       probabilité globale des précipitations située dans la colonne 11 (POP). 
       La probabilité de précipitations du type donne la probabilité
       d'occurrence de ce type, dans l'exemple, seulement de la neige et des
       averses de neige sont observées et les prévues, avec une probabilité
       de 100%. La valeur totale sera jamais plus grande que 100%.

|(P): prévue  |  (O): observée |
|-------------|----------------|
|Averses de pluie |  RW  (P & O) |
|Pluie         |   R   (P & O) |
|Averses de neige |  SW  (P & O) |
| Neige        |      S   (P & O) |
| Bruine      |       L   (P & O) |
|Pluie verglaçante | ZR  (P & O) |
| Bruine verglaçant | ZL  (P & O) |
| Averse de grésil |  IPW (P & O) |
| Grésil  |  IP  (P & O)  |
| Tonner  |  T   (P & O)  |
|  Grêle  |  A   (P & O)  |
|  Non disponible |    NA  (P & O) |


__L'intensité des précipitations est donnée par :__
* (-) très faible à faible
* ( ) (pas de signe) modérée
* (+) Forte
        
Dans certaines circonstances, par exemple lorsque la température est proche de zéro, il est possible d'avoir plus d'un type de précipitation à un moment donné, par exemple; neige mélangée avec de la pluie et occasionnellement de la pluie verglaçante. Dans cette situation, la condition dominante (neige) serait rapportée dans le type 1 (PCPN1) tandis que les précipitations associées seraient de type 2 (PCPN2) pour la pluie et de type 3 (PCPN3) pour la pluie verglaçante.

__11__ :     La colonne 11, nommée "POP", représente la probabilité de précipitations de tous les types 
        ensemble. Dans la section des observations, à savoir de 02Z à 07Z la POP observées pourraient 
        être inférieure à 100%. En d'autres termes, même s'il ne précipite pas à la station, un POP peut 
        exister si certaines informations existent dans les observations telles que
        "averses dans le voisinage", présence suffisante de nuages convectifs dans le METAR, échos radar ou 
        foudre autour de la station.

__12, 13__ : Les deux colonnes suivantes se réfèrent à la quantité de précipitations, en mm/h d'eau (ou cm/h pour la neige)
        et au type de précipitations correspondant à cette accumulation. Dans l'exemple, un total de 0,6 cm
        de neige (pas des mm ici car il qu'il neige) accumulées de 02Z à 04Z est observé, et une accumulation de la neige 
        de 1,3 cm est prévue de 17Z à 20Z. Seul le type dominant de précipitations (type qui a le POP supérieur) des
        3 types possibles sera considéré pour l'accumulées pendant une heure donnée.

__14, 15__ : Ces deux colonnes contiennent la température et le point de rosée observations et prévus;

__16, 17, 18__ : Les trois colonnes suivantes sont dédiées au vent: la direction, la vitesse (km/h) et les rafales (km/h).

__19, 20__ : Les deux dernières colonnes donnent la visibilité (une distance de référence en miles statutaires)
        et le type d'obstacle à la visibilité. Les valeurs observées représentent une synthèse des valeurs de la visibilité signalée
        dans les observations de surface METAR SPECI. Les visibilités prévues utilisent un ensemble prédéfini (case) de valeurs correspondant
        à des catégories de visibilité, par exemple les faibles visibilités correspondent à des visibilités de 0.5 mn, 
        les visibilités passables sont de 1.0 et 3.0 mn et les bonnes visibilités sont de 9.0 ou 15 ou plus.
        Un type d'obstacle à la visibilité accompagnera une visibilité inférieure à 6 miles, observés ou prévus


Le code des types possibles de visibilité utilisés dans les matrices de prévisions immédiates sont :

|(P): prévue  |  (O): observée  |
|-------------|-----------------|
|Dans les précipitations | PP (F & O) |
|        Brouillard    |          FG (F & O) |
|        Bancs de Brouillard  |   BF (F & O)
|        Brume       |            BR (F & O)|
|        Risque de Brouillard  |  RF (F)|
|        Brouillard glacé    |    IF (F & O)|
|        Poudrerie           |    BS (F & O)|
|        Poudrerie basse     |    DS (F & O)|
|        Brume sèche         |    HZ (F & O)|
|        Fumée               |    FU (F & O)|
|        Chasse Poussière    |    BD (F & O) |
|        Non disponible      |    NA (F & O)  | 


### Notes

* Bien que les éléments du temps des prévisions immédiates sont très dépendants des observations, une prévision sera toujours produit même si les observations de surface sont incomplètes, manquantes ou non disponibles à un endroit donné. Les observastions provenant de la télédétection tels que le radar, le satellite et le réseau de détection de foudre seront utilisés et ultimement les éléments météorologiques .
du Système Régional de Prévision Déterministe Canadien (SRPD PNT) seront utilisés.

* Une [liste des stations](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_nowcasting/nowcasting.geojson) est disponible en format GeoJSON.

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



