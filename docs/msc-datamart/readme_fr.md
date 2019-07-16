[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > Datamart du SMC

# Le Datamart du SMC

Le Service météorologique du Canada (SMC) met à la disposition des usagers spécialisés une multitude de données météorologiques, prévisionnelles et climatiques sur son serveur de données HTTPS.

Les usagers qui désirent accéder à ces données ouvertes doivent avoir une bonne connaissance de la météorologie et de l'informatique afin d'en faire bon usage.  Le mode d'accès privilégié est via des routines d'accès automatiques (scripts). 


## Accès

Le Datamart du SMC se trouve à l'adresse [https://dd.weather.gc.ca/](https://dd.weather.gc.ca/).

### Notifications en temps réel et récupération des données
  
Afin de faciliter l'extraction de données à jour sur le Datamart du SMC, le Service météorologique du Canada (SMC) a mis en place un fil de données pour annoncer la disponibilité des fichiers sur le Datamart du SMC. Ce fil de données utilise le protocole AMQP (Advanced Message Queuing Protocol). Cela permet non seulement à l'utilisateur d'être informé des produits disponibles au fur et à mesure qu'ils sont publiés, mais aussi de les recevoir automatiquement.

Le service peut filtrer des ensembles spécifiques de fichiers (alertes météo, observations, données de modèles, etc.), permettant des notifications uniquement pour les produits d'intérêt pour l'utilisateur.

C'est la méthode recommandée pour récupérer les données du Datamart du SMC.

La documentation de ce service se trouve sur la documentation [MSC Datamart AMQP documentation](amqp_fr.md).
  
Note: Les utilisateurs qui ont besoin de récupérer des données une seule fois peuvent utiliser [wget pour télécharger des données du Datamart du SMC](readme_wget-datamart_fr.md).

#### Méthode d'accès supplémentaire

Depuis le printemps 2019, un serveur alternatif HPFX d'accès aux données du Datamart du SMC est disponible pour contourner d'éventuels enjeux de bande passante. 

Ce serveur garantie un accès aux données beaucoup plus performant (bande passante multipliée par 10) pendant les périodes de la journée très en demande (autour de 12Z).

L'adresse de ce serveur HTTP est la suivante : [http://hpfx.collab.science.gc.ca/](http://hpfx.collab.science.gc.ca/)

Alimenté des divers sources de données via Sarracenia, l'arborescence des répertoires est modifiée par rapport à celle disponible sur le Datamart du SMC, avec présence de la date ce qui rend ces répertoires dynamiques et non plus statiques.

Une conséquence directe de cette hiérarchie par date, concerne la période de rétention des données qui devient identique pour tous les jeux de données et fonction de l'espace disque disponible.

L'accès aux données via le protocole AMQP est évidemment fortement conseillé.

Finalement, il est important de noter que contrairement au Datamart du SMC, il n'y a pas de redondance 24/7 du lien internet (support "/best effort/"). Dans le cas peu probable où le lien venait à briser, le Datamart du SMC deviendrait alors la source unique d'accès aux données. Ainsi, il est conseillé aux usagers désirant tester ce serveur 
alternatif de développer la capacité de retourner rapidement sur le serveur [https: //dd.meteo.gc.ca](https: //dd.meteo.gc.ca) , en cas de problèmes.

## Formats de données

Les données du Datamart du SMC sont disponibles en formats ouverts. Parmi ceux-ci :

* [GRIB2](../msc-data/readme_grib_fr.md)
* [NetCDF](https://www.unidata.ucar.edu/software/netcdf/)
* [GeoJSON](https://geojson.org/)
* [shapefile](https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf)
* CSV
* XML

## Utilisation

Des informations sur l'utilisation de ces services et des exemples sont disponibles sur la [page d'aperçu de l'utilisation](../usage/readme_fr.md).

## Gestion du changement 

Le SMC doit faire preuve de souplesse dans la façon dont il offre des données spécialisées aux utilisateurs intéressés. Par conséquent, nous devons être en mesure de mettre à jour ou de modifier les formats ou les offres de données en temps opportun, car la technologie, les normes et les innovations changent continuellement. Cependant, nous ferons de notre mieux pour informer nos utilisateurs à l'avance des changements à venir. 

Ainsi, aussi souvent que possible, nous utiliserons le serveur DD-Alpha, le site Web d'essai de données du Datamart du SMC, pour déposer des échantillons des nouvelles données modifiées afin d'aider nos utilisateurs à adapter leurs applications. 

Le serveur DD-Alpha se trouve à l'adresse [http://dd.alpha.weather.gc.ca/](http://dd.alpha.weather.gc.ca/).

Ce serveur, qui n'est pas opérationnel, donne également accès à des données expérimentales ou non opérationnelles.

## Liste de diffusion des annonces

Nous encourageons les utilisateurs à s'inscrire à la liste de diffusion d'annonces [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) pour être informés des améliorations et des changements apportés au Datamart du SMC.

## Soutien

Le serveur Datamart du SMC est opérationnel 24/7. Le soutien aux utilisateurs est fourni dans la mesure du possible pendant les heures normales de bureau. Les utilisateurs qui demandent de l'aide sont invités à [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).

