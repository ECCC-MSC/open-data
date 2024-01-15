[In English](tutorial_OAFeat_Power-BI_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [Aperçu de l'utilisation](readme_fr.md) > Utilisation d'OGC API - Features en avec Power BI

# Tutoriel : interroger et utiliser les données avec GeoMet-OGC-API Features en utilisant Power BI

Les services web [OGC API - Features](https://eccc-msc.github.io/open-data/msc-geomet/ogc_api_fr/#ogc-api-features) disponibles dans GeoMet-OGC-API permettent d'interroger des données géospatiales vectorielles et de les récupérer aux formats GeoJSON et CSV. Le fichier de sortie peut alors être utilisé pour l'affichage ou le traitement ultérieur des données ([voir les exemples R et Excel/VBA utilisant ces mêmes fichiers!](../tutorial_OAFeat_R-Excel_fr/)) Ce tutoriel vous montrera comment vous pouvez :

* Interroger et récupérer les données géospatiales vectorielles de GeoMet-OGC-API avec [Power BI](https://www.microsoft.com/fr-fr/power-platform/products/power-bi/) au format CSV
* Spécifier les données que vous voulez à partir des [Collections des données ouvertes](https://api.weather.gc.ca/collections?lang=fr)
* Charger les données dans la [page Rapport de Power BI](https://learn.microsoft.com/fr-fr/power-bi/create-reports/desktop-report-view) et afficher les données à l'aide d'une carte simple.

## Construire l'URL pour obtenir les données souhaitées

Nous allons donc ajouter les données à [Power BI](https://www.microsoft.com/fr-fr/power-platform/products/power-bi/) en spécifiant un URL Web. Vous pouvez également télécharger les données au format CSV sur votre station et les charger dans [Power BI](https://www.microsoft.com/fr-fr/power-platform/products/power-bi/) à partir de là, mais comme vous n'en avez pas besoin, il est généralement préférable d'effectuer une requête à partir du Web.

Tout d'abord, nous allons nous rendre à l'URL des [Collections de données ouvertes](https://api.weather.gc.ca/collections?lang=fr) et sélectionner celle que nous voulons. Dans ce cas, nous choisirons les données hydrométriques en temps réel, puis nous cliquerons sur ``Parcourez les items de « Données hydrométriques en temps réel »``. Si vous suivez bien, l'URL de la page devrait ressembler à ``https://api.weather.gc.ca/collections/hydrometric-realtime/items?lang=fr``. Nous pourrions l'utiliser comme ceci, mais filtrons d'abord quelques valeurs!

Nous allons faire défiler le tableau vers le bas et cliquer sur ``DATETIME`` deux fois pour trier le tableau par dates en ordre décroissant. Changeons aussi la ``Limite`` sous le tableau à 100. Décidons également de sélectionner un `PROV_TERR_STATE_LOC` spécifique, nous prendrons ``BC``. Maintenant que nous avons fait cela, nous pouvons voir que l'URL a changé pour refléter notre sélection et ressemble maintenant à `https://api.weather.gc.ca/collections/hydrometric-realtime/items?lang=fr&limit=100&offset=0&sortby=-DATETIME&PROV_TERR_STATE_LOC=BC`. Il y a d'autres choses avec lesquelles nous pourrions jouer, mais pour le bien de cet exemple, nous nous en tiendrons à cet URL.

Notez que si vous souhaitez télécharger ces données au format CSV, vous pouvez simplement cliquer sur le lien ``CSV`` en haut à droite de l'écran, mais comme nous l'avons vu précédemment, il n'est pas nécessaire de les télécharger pour les utiliser dans ``Power BI``.

## Scénario simple avec Power BI

Ouvrons maintenant ``Power BI``! Une fois ouvert, nous cliquons sur ``Get data``, dans la barre de recherche nous cherchons ``Web``, nous le sélectionnons et nous cliquons sur ``Connect``. Dans la boîte de dialogue qui vient de s'ouvrir, nous allons sélectionner ``Advanced`` et coller notre URL dans la première boîte de texte. Pour indiquer à ``Power BI`` que nous voulons les données au format CSV, nous ajouterons sur la deuxième ligne ``&f=csv``. Vous pouvez maintenant cliquer sur le bouton ``OK`` et dans la prochaine boîte de dialogue qui s'ouvre, cliquez sur ``Connect``.

Vous verrez alors le tableau avec toutes les valeurs à l'intérieur. Si vous êtes habitué à ``Power BI``, vous pouvez décider d'utiliser ``Transform Data`` pour formater le tableau comme vous le souhaitez. Sinon, vous pouvez simplement cliquer sur ``Load``.

Maintenant que nous avons introduit notre table, nous pouvons commencer par changer son nom puisqu'elle prend par défaut la fin de l'URL comme nom. Nous l'appellerons simplement ``Données hydrométriques en temps réel BC``. Pour cet exemple, allons dans le panneau ``Visualizations`` sur la droite et sélectionnons ``Map``. Déplaçons le coin pour l'étendre suffisamment pour que nous puissions voir tout ce qu'il y a à l'intérieur.

Nous pouvons maintenant faire glisser les données que nous voulons dans le champ approprié du panneau ``Fields`` vers le panneau ``Visualizations``. Glissons ``x`` dans Longitude et ``y`` dans Latitude. Nous pouvons également faire glisser ``DISCHARGE`` dans ``Size`` pour obtenir des cercles de tailles différentes en fonction de cette valeur. Nous pouvons aussi changer de sous-fenêtre (``Sub-Pane``) dans `Visualizations` et aller dans ``Format`` et changer les couleurs des données en appuyant sur le bouton `fx`. Nous allons mettre un gradient de couleurs avec du vert, du jaune et du rouge en fonction du ``LEVEL`` (voir l'image ci-dessous). Nous allons aussi spécifier quelques valeurs au lieu de laisser Minimum, Milieu et Maximum car il y a beaucoup de valeurs aberrantes et les couleurs ne seraient différentes que pour 2 ou 3 points. Enfin, nous pouvons simplement changer le titre de la carte en quelque chose d'autre, renommons-le ``Discharge and Level by Station, BC``, centrons-le et agrandissons-le un peu.

Et voilà! Avec cet exemple simple, vous comprenez maintenant comment vous pouvez interroger les données de nos services et les utiliser comme bon vous semble! Vous pouvez également configurer un rafraîchissement programmé pour votre propre tableau de bord (qui ne sera pas expliqué ici) ou simplement utiliser le bouton ``Refresh`` à l'intérieur pour rafraîchir les données manuellement. Voici une image qui montre le résultat final ainsi que les champs qui ont été mentionnés dans ce tutoriel :

![Vue cartographique complète de Power BI avec champs](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_Power-BI_Map_en.jpg)

![Formatage couleur de Power BI](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_Power-BI_Format_en.jpg)
