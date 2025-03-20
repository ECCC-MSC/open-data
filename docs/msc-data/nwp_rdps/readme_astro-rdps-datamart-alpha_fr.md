[In English](readme_astro-rdps-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_fr.md) > Produits astronomie basés sur le SRPD sur DD-Alpha

# Produits GRIB2 d'astronomie basés sur le Système régional de prévision déterministe (SRPD)

Cette page décrit les données de prévision de [scintillation](https://meteo.gc.ca/astro/seeing_f.html) (ou "seeing") et de [transparence](https://meteo.gc.ca/astro/transparence_f.html). La scintillation est utilisée en astronomie pour qualifier l'état de turbulence atmosphérique tandis que la transparence fait référence à la clarté du ciel et se mesure comme la capacité à observer les étoiles en fonction de leur luminosité ou de leur magnitude. 

Ces données sont générées à partir du [Système régional de prévision déterministe](./readme_rdps_fr.md) aux heures jusqu'à 84 heures et projetées sur une grille polaire stéréographique à 35km de résolution.

Elles permettront aux astronomes amateurs et professionnels, mais aussi à tout usager intéressé par les conditions du ciel, à mieux planifier leurs activités.

## Adresse des données 

Les données du site web d'essai de données DD-Alpha du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sont accessibles à l’adresse suivante : 

[https://dd.alpha.meteo.gc.ca/model_gem_regional/astronomy/grib2/{HH}](https://dd.alpha.meteo.gc.ca/model_gem_regional/astronomy/grib2)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]

Un historique de 24 heures est conservé dans ce répertoire.

## Spécification technique de la grille

![Image de la grille PS astro-SRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/grille_rdps-astro_PS.png)

Valeurs données aux paramètres de la grille polaire stéréographique :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 245 |
| nj | 190 | 
| résolution à 60° N | 35km |
| coordonnées du premier point de grille | 20.10° N ; 136.48° W | 
| orientation de la grille (par rapport à l’axe des j) | -111,0° |  

## Nomenclature des noms de fichiers 

NOTE: TOUTES LES HEURES SONT EN UTC.

Les fichiers ont la nomenclature suivante :

```
{YYYYMMDD}T{HH}Z_MSC_RDPS_{VAR}_EATM_{Grille}{resolution}_PT{hh}H.grib2
```

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDPS__ : Chaîne de caractères constante indiquant que les données sont basées sur le Système régional de prévision déterministe 
* __VAR__ : Variable contenue dans le fichier [SEEI, TRSP]
* __EATM__ : Atmosphère entière. Considérée comme une seule couche
* __Grille__ : Grille horizontale [PS]
* __resolution__ : Résolution horizontale, ici 35km
* __PT{h}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). « h » représente l’heure de prévision [0, 1, 2, ..., 84]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2

Exemple de nom de fichier : 20210208T00Z_MSC_RDPS_SEEI_EATM_PS35km_PT84H.grib2

## Liste des variables

Les variables prévues disponibles dans les fichiers 2D sont décrites ci-dessous.

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPS-Astronomy_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).