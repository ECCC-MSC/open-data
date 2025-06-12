[In English](readme_rdps-datamart-alpha_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_fr.md) > Eléments du temps sur grille basés sur le SRPD sur DD-Alpha

# Données GRIB2 expérimentales d'éléments du temps sur grille basés sur le Système régional de prévision déterministe (SRPD)

Depuis près de trois décennies, le Système SCRIBE est utilisé pour aider les météorologues à préparer les bulletins météorologiques. La philosophie derrière SCRIBE est la suivante : un ensemble de matrices d’éléments du temps est généré pour certaines stations ou points d’échantillonnage, pour ensuite être transmis aux centres météorologiques régionaux. Les matrices sont ensuite décodées par SCRIBE et peuvent être modifiées via l’interface graphique par les usagers. Les données qui en résultent sont ensuite fournies à un générateur de texte, qui produit des prévisions publiques bilingues en langage clair.

Les différentes règles reliées aux matrices Scribe entravent l’innovation scientifique, n’exploitent pas la richesse des Prévision Numérique du Temps (PNT), réduisent la compréhension des prévisions météorologiques, et peuvent demander l’intervention fréquente des prévisionnistes.

Dans le cadre d’un plan de modernisation plus vaste du Service Météorologique Canadien (SMC), dans lequel le rôle du prévisionniste évolue, l’objectif est de remplacer les matrices Scribe, [disponibles sur le Datamart du SMC](https://dd.meteo.gc.ca/model_gem_regional/matrices/land_regions/), et leur nombre limité de points à travers le Canada par des [éléments du temps sur grille](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_f.pdf) ("WEonG"). 

Les éléments du temps sur grille du Système régional de prévision déterministe (SRPD) est un système de post-traitement conçu afin de générer les éléments du temps requis par les différents programmes de prévision (public, maritime, aviation, qualité de l’air, etc.). Ce système fusionne les sorties brutes du modèle et post-traitées, à l’aide de diverses approches diagnostiques. Des concepts horaires sont produits à partir de différents algorithmes en utilisant des sorties provenant du [Système régional de prévision déterministe (SRPD)](readme_rdps_fr.md).

## Adresse des données 

Les données du site web d'essai de données DD-Alpha du Datamart du SMC peuvent être [automatiquement récupérées avec le protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GRIB2.

Les données sur grille lat-lon tournées sont accessibles aux adresses suivantes : 

* Ancienne nomenclature : [https://dd.alpha.meteo.gc.ca/model_gem_regional/10km/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_gem_regional/10km/)
* Nouvelle nomenclature : [https://dd.alpha.meteo.gc.ca/model_rdps/10km/{HH}/{hhh}/](https://dd.alpha.meteo.gc.ca/model_rdps/10km/)

où :

* __HH__ : Heure UTC du début de la passe du modèle [00, 06, 12, 18]
* __hhh__ : Heure de prévision [001, 002, 003, ..., 084]

Un historique de 24 heures est conservé dans ce répertoire.

__Notes importantes__ :

* Les fichiers contenus dans le répertoire `https://dd.alpha.meteo.gc.ca/model_rdps` sont conformes à nos nouvelles normes de standardisation. Dans ces normes, les acronymes utilisés pour représenter les variables ont été remplacés par des noms plus explicites selon le style [_upper camel case_](https://fr.wikipedia.org/wiki/Camel_case). Ces fichiers vont remplacer dans les prochains mois les fichiers contenus dans le répertoire `https://dd.alpha.meteo.gc.ca/model_gem_regional`.
* Certains algorithmes ont besoin des valeurs des variables à `t-1`, afin d'uniformiser l'offre de données, les heures de prévision débutent à 001h.

## Spécification technique de la grille

![Image de la grille lat-lon tournée SRPD](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/grille_rdps_Rlatlon.png)

Valeurs données aux paramètres de la grille lat-lon tournée :

| Paramètre | Valeur |
| ------ | ------ |
| ni | 1102 |
| nj | 1076 | 
| résolution à 60° N | 10km |
| coordonnées du premier point de grille | 48.5° S ; 62.6° W | 

## Nomenclature des noms de fichiers 

Les fichiers ont la nomenclature suivante :

`{YYYYMMDD}T{HH}Z_MSC_RDPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2`

où :

* __YYYYMMDD__ : Année, mois et jour du début de la prévision
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HH__ : Heure UTC de la passe [00, 06, 12, 18]
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __RDPS-WEonG__ : Chaîne de caractères constante indiquant que les données proviennent des éléments du temps sur grille ("WEonG") du Système régional de prévision déterministe
* __VAR__ : Type de variable contenu dans le fichier selon l’ancienne nomenclature (acronyme, ex : VISIFG) ou la nouvelle nomenclature (_Upper camel case_, ex: LiquidFogVisibility) .
* __LVLTYPE-LVL__ : Niveau vertical [Sfc pour la surface]
* __Grille__ : Grille horizontale [RLatLon]
* __resolution__ : 0.09. Signifie une résolution de 0.09°(environ 10km) dans les directions longitudinale et latitudinale
* __PT{hhh}H__ : Echéance temporelle selon la norme [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T et H sont des caractères constants désignant Période, Temps et Heure. "hhh" représente l’heure de prévision [001, 002, 003, ..., 084]
* __grib2__ : Chaîne de caractères constante indiquant que le format est GRIB2.

Exemples de noms de fichier :

* 20250603T12Z_MSC_RDPS-WEonG_CONDALPCPN _Sfc_RLatLon0.09_PT024H.grib2
* 20250603T12Z_MSC_RDPS-WEonG_LiquidPrecip-CondAmt_Sfc_RLatLon0.09_PT024H.grib2

## Liste des variables

Liste des éléments du temps sur grille à la surface:

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/RDPS-WEonG_Variables-List_fr.csv");
</script>

## Support

Pour toute question relative à ces données, merci de [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

