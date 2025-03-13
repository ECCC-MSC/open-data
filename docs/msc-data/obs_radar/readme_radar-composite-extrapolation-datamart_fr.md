[In English](readme_radar-composite-extrapolation-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données et produits radar](readme_radar_fr.md) > Composite radar extrapolée sur le Datamart du SMC

# Composite radar nord-américaine extrapolée

Ce produit est une composite de l'extrapolation radar à une résolution de 1 km sur le domaine nord-américain. Il utilise uniquement la composite radar à haute résolution (1 km) de 6 minutes (celle affichée sur les différentes plateformes publiques gouvernementales) comme entrée.

En utilisant une modification de la bibliothèque à code source ouvert PySTEPS, un champ de mouvement est calculé, et les échos radar sont projetés dans le temps. Le mouvement est basé sur les similarités entre la réflectivité radar dans une séquence temporelle à plusieurs échelles spatiales.

La réflectivité radar future est extrapolée, puis convertie en taux de précipitations de MM/HR (pluie) ou CM/HR (neige). Une séquence de sortie du radar futur est générée toutes les 6 minutes.

Il est important de noter que cette sortie n'est qu'une projection des échos existants, sans tenir compte de la croissance et de la décroissance attendues dans une séquence radar réelle. Des erreurs existeront, en particulier près des limites de la couverture radar ou près des caractéristiques géographiques. Par conséquent, le produit doit être utilisé avec prudence en considérant qu'il n'existe pas de solution parfaite étant donné les limites de la prévisibilité.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les données sont disponibles à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/radar/composite-extrapolation](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour

__Notes__: 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Spécifications techniques

L'extrapolation est réalisée exclusivement dans la zone de couverture du réseau de radars du domaine nord-américain (Canada et États-Unis), avec une portée maximale de 240 km pour les radars canadiens et de 460 km pour les radars américains.

Le produit est disponible en dBZ, MM/HR et CM/HR.

Le composite est disponible toutes les 6 minutes, avec un délai de production et de disponibilité d'environ 7 minutes après l'heure valide.

## Nomenclature des noms de fichiers 

Les fichiers suivent la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-Composite-Extrapolation_{UNIT}_{res}_PT{mmm}M.tif`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-Composite-Extrapolation__ : Chaîne de caractères constante indiquant que les données contiennent la composite radar nord-américaine extrapolée
* __UNIT__ : Chaîne de caractères indiquant l'unité [MMHR,CMHR] selon le type de précipitation (pluie, neige)
* __res__ : Résolution horizontale [1km]
* __PT{mmm}M__ : Temps de validité en minutes
* __tif__ : Chaîne de caractères constante indiquant que le format est GeoTIFF

Exemple:

* 20240214T1550Z_MSC_Radar-Composite-Extrapolation_MMHR_1km_PT042M.tif

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
