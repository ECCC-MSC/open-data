[In English](readme_cangrd-datamart_en.md)


![ECCC logo](../../img_eccc-logo.png)


[TdM](../../readme_fr.md) > [Données ouvertes publiques du SMC](../readme_fr.md) > CanGRD sur le Datamart du SMC

# Données climatiques historiques sur grille canadienne (CANGRD) en format GeoTIFF

CANGRD est basé sur les données climatiques canadiennes ajustées et homogénéisées (DCCAH) pour les observations climatiques historiques à partir de 1948 sur l'ensemble du Canada, et à partir de 1900 pour le sud du Canada, jusqu'à la fin de l'année civile précédente. Les anomalies de température maximales et minimales quotidiennes mensuelles, saisonnières et annuelles sont calculées à chaque station d'observation et pour chaque année en soustrayant la moyenne de référence adéquate (définie comme moyenne sur la période de référence 1961-1990) des valeurs mensuelles, saisonnières et annuelles correspondantes. Les anomalies de précipitations totales mensuelles, saisonnières et annuelles sont calculées de la même façon. De plus, les anomalies de précipitations sont ensuite normalisées en divisant par la période de référence moyenne et exprimées en pourcentage pour produire des écarts de précipitations normalisés.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTP. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoTIFF.

Les fichiers CANGRD se trouvent à l'adresse suivante :

* /climate/cangrd/geotiff/historical /annual/[anomaly, trend].
* /climate/cangrd/geotiff/historical/seasonal/[DJF,MAM,JJA,SON]/[anomaly, trend].
* /climate/cangrd/geotiff/historical/monthly_ens/anomaly

où :

* __historical__ : Simulations historiques à partir de 1948 sur l'ensemble du Canada, et à partir de 1900 pour le sud du Canada, jusqu'à la fin de l'année civile précédente.
* __monthly__ : Janvier à décembre 
* __seasonal__ : Les saisons météorologiques standard sont utilisées : (de mars à mai (MAM, printemps), de juin à août (JJA, été), de septembre à novembre (SON, automne/automne) et de décembre à février (DJF, hiver))].
* __anomaly__ : Les anomalies sont calculées à chaque station d'observation et pour chaque année en soustrayant la moyenne de référence adéquate (définie comme moyenne sur la période de référence 1961-1990) à celle des valeurs mensuelles, saisonnières et annuelles correspondantes (anomalies de température et de précipitations : 1948-2017).
* __trend__ : Les données de tendance représentent le changement de température ou l’écart relatif des précipitations sur la période étudiée (tendance moyenne des températures : 1948-2016 ; tendance des précipitations : 1948-2012).

## Nomenclature des noms de fichiers

NOTE : TOUTES LES HEURES SONT EN UTC.

CANGRD_hist_TemporalResolution_Value_ProjectionResolution_Variable_TimePeriod.tif

avec :

* __CANGRD__ : Chaîne constante indiquant la source des données, c'est-à-dire les anomalies de température et de précipitations annuelles, saisonnières et mensuelles, qui ont été interpolées à partir des stations de la base de données climatiques canadiennes ajustées et homogénéisées de l'AHCCD.
* __hist__ : Chaîne constante indiquant les simulations historiques.
* __TemporalResolution__ : Résolution temporelle, prenant l'une des valeurs : [annual, monthly, DJF, MAM, JJA, SON]
* __Value__ : Catégorie de valeurs, prenant l'une des valeurs :  [anom, trend]
* __Projection__ : Projection de la grille, prenant la valeur :[ps] ; ps indique une projection polaire stéréographique
* __Resolution__ : Résolution de la grille, prenant la valeur : [50km
* __Variable__ : Nom de la variable climatique disponible dans le fichier, prenant l'une des valeurs : [PCP, TMIN, TMAX, TMEAN] ; PCP représente les précipitations totales, TMIN représente la température minimale, TMAX représente la température maximale, TMEAN représente la température moyenne.
* __TimePeriod__ : Période temporelle, prenant l'une des valeurs : [YYYY, YYYY-MM, YYY1-YYY2] ; YYYY-MM représente l'année-mois pour les anomalies, YYY1-YYY2 représente l'intervalle d'années utilisé dans les tendances.
* __tif__ : Chaîne constante indiquant le format GeoTIFF.

Exemples :

* CANGRD_hist_annual_anom_ps50km_TMEAN_1903.tiff
* CANGRD_hist_DJF_trend_ps50km_PCP_1948-2012.tiff

## Spécifications de la grille

La grille CANGRD est une projection stéréographique polaire avec une résolution spatiale de 50 km. La grille est une matrice de 125 (colonnes) par 95 (lignes), où le coin sud-ouest (0,0) est à 40,0451° de latitude nord et 129,8530° de longitude ouest. La projection est vraie à 60,0°N et centrée sur 110,0°W. 

## Liste des variables

Les variables et unités disponibles pour CANGRD sont :

* Anomalie de température maximale (°C)
* Anomalie de température minimale (°C)
* Anomalie de température moyenne (°C)
* Tendance de la température moyenne (°C)
* Anomalie totale des précipitations (%)
* Tendance relative des précipitations totales (%)

## Support

Pour toute question relative à ces données, merci de nous contacter à l'adresse : ec.dps-client.ec@canada.ca

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).



