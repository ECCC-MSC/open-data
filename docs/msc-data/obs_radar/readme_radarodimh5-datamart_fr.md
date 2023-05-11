[In English](readme_radarimage-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données et produits radar](readme_radar_fr.md) > Volume scans ODIM_H5 sur le Datamart du SMC

# Volume scans des données radar en Bande S 

Les fichiers bruts des radars en bande S sont distribués au format Leonardo Rainbow version 5 (RB5). La stratégie de balayage du radar en bande S est basée sur le "volume polaire de six minutes" (PVOL6). L'acronyme PVOL trouve son origine dans la norme ODIM actuellement utilisée en Europe et en Australie. Le PVOL6S se compose de 17 balayages qui sont acquis séquentiellement, dans l'ordre décroissant (haut vers le bas), de sorte que le balayage le plus bas est collecté le plus près de l'heure nominale du volume. Tous les balayages sont Doppler et à double polarisation. Les angles d'élévation sont compris entre 0.4° et 24.4° et la largeur du faisceau radar est de 0.9°. Les 6 balayages les plus bas sont à double fréquence de répétition d'impulsions (PRF) (600/450 Hz), ont une résolution azimutale de 0.5° et un pas de portée de 0.5 km, et s'étendent jusqu'à une portée de 240 km. Les autres élévations sont à PRF unique (600-1200 Hz) avec une résolution azimutale de 1° et un pas de portée de 0.5 km. La portée maximale de ces élévations est configurée pour permettre un échantillonnage vertical jusqu'à 20 km d'altitude. Le PVOL6S est collecté régulièrement toutes les six minutes, à partir de la minute 0.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier hdf5.

Les données sont disponibles à l'adresse :

[https://hpfx.collab.science.gc.ca/{YYYYMMDD}/WXO-DD/radar/volume-scans/{RADAR_ID}](https://hpfx.collab.science.gc.ca/)

où :

* __YYYYMMDD__ : Année, mois et jour
* __RADAR_ID__ : Identifiant du radar, code de 5 lettres en lettres majuscules (voir la liste ci-dessous).

Un historique de plusieurs semaines est conservé dans ce répertoire.

__Notes__: 

* Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste sera mise à jour régulièrement.

## Nomenclature des noms de fichiers

Les fichiers suivent la nomenclature suivante :

`{YYYYMMDD}T{HHmm}Z_MSC_Radar-VolumeScans_{RADAR_ID}.hdf5`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et  minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-VolumeScans__ : Chaîne de caractères constante indiquant que les données contiennent des volume scans
* __RADAR_ID__ : Code de 5 lettres en majuscule représentant l'identifiant du radar, code de 5 lettres en lettres majuscules
* __hdf5__ : Chaîne de caractères constante indiquant que le format est HDF5

Exemple:

* 20230511T0036Z_MSC_Radar-VolumeScans_CASBV.hdf5

## Contenu des fichiers

Les volumes scans, également appelés données brutes, sont générés dans le format natif RAINBOW de Leonardo (*). Au cours d'un cycle de 6 minutes, nous distribuons 10 fichiers de PVOL6S.vol pour les fichiers de volume complet soit 17 scans pour chacun des 10 paramètres suivants:

* dBuZ: Facteur de réflectivité radar à polarisation horizontale non corrigé
* dBZ: Facteur de réflectivité du radar à polarisation horizontale corrigé
* V: Vitesse radiale du vent à polarisation horizontale
* W: Largeur spectrale polarisée horizontalement
* uPhiDP: Phase différentielle HV
* PHIDP: Phase différentielle corrigée HV
* ZDR: Réflectivité différentielle logarithmique (H/V)
* RhoHV: Coefficient de corrélation entre H et V
* SQI: Indice de qualité du signal H
* KDP: Phase différentielle spécifique

(*) Format HDF5 : https://support.hdfgroup.org/HDF5/users5.html

## Support

Pour toute question relative à ces données, [merci de nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).
