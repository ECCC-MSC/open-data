[In English](readme_gdps-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_gdps_fr.md) > Eléments du temps sur grille basés sur le SGPD sur DD-Alpha

# Données GRIB2 expérimentales d'éléments du temps sur grille basés sur le Système global de prévision déterministe (SGPD)

Depuis près de trois décennies, le [système SCRIBE](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/product-pages/alpha_glb_scrib_scribe-documentation_gen_f.html) est utilisé pour aider les météorologues à préparer les bulletins météorologiques. La philosophie derrière SCRIBE est la suivante : un ensemble de matrices d’éléments du temps est généré pour certaines stations ou points d’échantillonnage, pour ensuite être transmis aux centres météorologiques régionaux. Les matrices sont ensuite décodées par SCRIBE et peuvent être modifiées via l’interface graphique par les usagers. Les données qui en résultent sont ensuite fournies à un générateur de texte, qui produit des prévisions publiques bilingues en langage clair.

Les différentes règles reliées aux matrices Scribe entravent l’innovation scientifique, n’exploitent pas la richesse des Prévision Numérique du Temps (PNT), réduisent la compréhension des prévisions météorologiques, et peuvent demander l’intervention fréquente des prévisionnistes.

Dans le cadre d’un plan de modernisation plus vaste du Service Météorologique Canadien (SMC), dans lequel le rôle du prévisionniste évolue, l’objectif est de remplacer les matrices Scribe, [disponibles sur le Datamart du SMC](https://dd.meteo.gc.ca/model_gem_regional/matrices/land_regions/), et leur nombre limité de points à travers le Canada par des [éléments du temps sur grille](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_f.pdf) ("WEonG"). 

Les Éléments du temps sur grille du Système global de prévision déterministe (SGPD) est un système de post-traitement conçu afin de générer les éléments du temps requis par les différents programmes de prévision (public, maritime, aviation, qualité de l’air, etc.). Ce système fusionne les sorties brutes du modèle et post-traitées, à l’aide de diverses approches diagnostiques. Des concepts horaires sont produits à partir de différents algorithmes en utilisant des sorties provenant du [Système global de prévision déterministe (SGPD)](../readme_gdps_fr.md)

## Adresse des données 

Les données du site web d'essai de données DD-Alpha du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sur grille lat-lon sont accessibles à l’adresse suivante : 

[https://dd.alpha.meteo.gc.ca/model_gem_global/15km/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_gem_global/15km/)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 12]
* __hhh__ : Heure de prévision [001, 002, 003, ..., 144]

Un historique de 24 heures est conservé dans ce répertoire.

Note: Certains algorithmes ont besoin des valeurs des variables à `t-1`, afin d'uniformiser l'offre de données, les heures de prévision débutent à 001h.

## Spécification technique de la grille

Valeurs données aux paramètres de la grille lat-lon :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 2400 |
| nj | 1201 | 
| résolution à 60° N | 15km |
| coordonnées du premier point de grille | 90° S ; 180° W | 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_GDPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 12]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __GDPS-WEonG__ : Chaîne de caractères constante indiquant que les données proviennent des éléments du temps sur grille ("WEonG") du Système global de prévision déterministe
* __VAR__ : Type de variable contenu dans le fichier (ex: VISIFG).
* __LVLTYPE-LVL__ : Niveau vertical [Sfc pour la surface]
* __Grille__ : Grille horizontale [LatLon]
* __resolution__ : 0.15. Signifie une résolution de 0.15°(environ 15km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [001, 002, 003, ..., 144]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemple de nom de fichier :

* 20220821T12Z_MSC_GDPS-WEonG_BLSN_Sfc_LatLon0.15_PT024H.grib2

## Liste des variables

Liste des éléments du temps sur grille à la surface:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS-WEonG_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
