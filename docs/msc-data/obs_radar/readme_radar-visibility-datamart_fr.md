[In English](readme_radar-visibility-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Données et produits radar](readme_radar_fr.md) > Produits de visibilité radar sur le Datamart du SMC

# Produits de visibilité des radars météorologiques canadiens

Les éoliennes peuvent contaminer les données des radars météorologiques, ce qui peut compromettre la capacité d'Environnement et changement climatique Canada (ECCC) à fournir des prévisions et des avertissements météorologiques de qualité aux Canadiens.

Afin d'appuyer les [lignes directrices d'ECCC concernant les emplacements des parcs éoliens et des radars météorologiques](https://www.canada.ca/fr/environnement-changement-climatique/services/conditions-meteorologiques-ressources-outils-generaux/apercu-radars/interference-eoliennes/lignes-directrices-concernant-lemplacement-des-eoliennes-et-des-radars-meteorologiques.html), des couches de visibilité de radars météorologiques ont été créées pour des hauteurs de surface de 150, 200 et 250 mètres au-dessus du sol (mAGL). Ceci correspond aux hauteurs typiques passées et présentes des éoliennes (de la base à la pointe ou au total) ainsi qu'aux hauteurs potentielles futures de celles-ci, compte tenu la tendance actuelle.

Ces couches de visibilité ont été générées à partir d'une analyse de cônes de visibilité utilisant les 32 radars météorologiques opérationnels en bande S d'ECCC comme observateurs et les trois hauteurs susmentionnées comme décalages de surface.

Au sein de ces couches de visibilité, les turbines de hauteurs de 150, 200 et 250 mAGL sont susceptibles d'être visibles par les radars météorologiques opérationnels d'ECCC et ont donc le potentiel de contaminer les données des radars météorologiques. Une couche de points comprenant les coordonnées des radars et une couche de polygones contenant les zones tampons de 10 et 60 kilomètres de rayon entourant chaque radar et délimitant les zones d'impact des turbines sur ces derniers sont également incluses dans cet ensemble de données.

## Adresse des données 

Les données du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données sont disponibles à l'adresse :

* [https://dd.meteo.gc.ca/radar/visibility](https://dd.meteo.gc.ca/radar/visibility)

__Note__:

Une [liste des sites radar](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) est disponible. Cette liste est mise à jour régulièrement.

## Nomenclature des noms de fichiers

Les fichiers suivent la nomenclature suivante :

* `{YYYYMMDD}_MSC_Radar-Viewsheds_AGL-{height}.json`
* `{YYYYMMDD}_MSC_Radar-ImpactZones.json`

où :

* __YYYYMMDD__ : Année, mois et jour de production des données [20250113]
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __Radar-Viewsheds__ : Chaîne de caractères constante indiquant que les données contiennent des couches de visibilité de radar météorologiques
* __Radar-ImpactZones__ : Chaîne de caractères constante indiquant que les données contiennent des couches de points et polygones délimitant les zones d'impacts des turbines
* __AGL-{height}__ : Hauteur de surface au-dessus du sol [150m, 200m, 250m]
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemples:

* 20250113_MSC_Radar-Viewsheds_AGL-150m.json
* 20250113_MSC_Radar-ImpactZones.json

## Contenu des données

__Couches de visibilité radar__

Le jeu de données de visibilité radar contient des polygones non projetés illustrant les emplacements à 150, 200 et 250 mAGL de hauteur de surface susceptibles d'être visibles par les 32 radars météorologiques opérationnels en bande S d'ECCC. À l’intérieur de ces couches de visibilité, les turbines d'une hauteur de 150, 200 et 250 mAGL sont susceptibles d'être visibles par les radars météorologiques opérationnels d'ECCC et donc de contaminer les données des radars météorologiques.

Il convient de noter que ces couches de visibilité ont été générées à l'aide d'un simple outil de visualisation et que les résultats peuvent donc ne pas être tout à fait exacts en raison des limites des données et/ou de l'outil. Il est possible que, dans certains cas, les turbines soient visibles ou non par les radars d'ECCC, bien qu'elles se trouvent à l'intérieur ou à l'extérieur de ces couches de visibilité. ECCC devrait être consulté sur toutes propositions de parcs éoliens au Canada le plus tôt possible dans la phase de planification du projet.

__Zones d'impact radar__

Le jeu de données des zones d'impact radar contient des polygones non projetés illustrant les zones tampons de 10 et 60 km de rayon autour des 32 radars météorologiques opérationnels en bande S d'ECCC. La zone tampon de 10 km de rayon entourant chaque radar représente la "zone d'impact certain" où des impacts significatifs sur le radar sont attendus, et où les éoliennes ne devraient donc pas être construites.

Les éoliennes se trouvant entre les zones tampons de 10 km et 60 km de rayon (la "zone d'impact modéré") sont plus susceptibles d'avoir un impact modéré à significatif sur le radar si elles y sont construites.

Les éoliennes situées à l'extérieur de ces zones tampons de 60 km et des couches de visibilité radar sont moins susceptibles d'avoir des impacts significatifs sur le radar.

Cependant, ECCC doit être consulté sur toutes propositions de parcs éoliens au Canada le plus tôt possible au cours de la phase de planification du projet, car des impacts peuvent encore se réaliser dans de rares cas.

## Notes et utilisation

Lors de l'utilisation des données décrites dans ce document, il est important de comprendre leur objectif, leurs limites et la façon dont elles interagissent avec d'autres ensembles de données radar, en particulier dans le contexte des interférences potentielles dues aux éoliennes. Vous trouverez ci-dessous des points importants à considérer lors de l'interprétation et de l'utilisation de ces données :

* __Avertissement__ : les couches de visibilité radar ont été générées à l'aide d'un simple outil de visualisation et les résultats peuvent donc ne pas être tout à fait exacts en raison des limites inhérentes aux données et/ou à l'outil. Dans certains cas, les turbines peuvent être visibles ou non par les radars d'ECCC, bien qu'elles se trouvent à l'intérieur ou à l'extérieur de ces couches de visibilité. Il convient également de noter que les données fournies ne le sont qu'à titre informatif. Bien que des efforts aient été déployés pour assurer l'exactitude, l'exhaustivité et la fiabilité des données, aucune garantie, expresse ou implicite, n'est donnée à leur sujet. L'utilisation de ces données se fait à vos propres risques, et nous déclinons toute responsabilité pour tout dommage ou perte résultant de leur utilisation. Pour toute question ou commentaire concernant cet ensemble de données, veuillez nous contacter à l'adresse suivante : radarsmeteo-weatherradars@ec.gc.ca. ECCC devrait être consulté pour toute proposition de parc éolien au Canada le plus tôt possible lors de la phase de planification du projet.

* __Objectif__ : Les couches de visibilité radar ont été créées pour indiquer les endroits où les éoliennes, dont la hauteur de la base à la pointe (ou la hauteur totale) est égale à 150, 200 et 250 mAGL, sont susceptibles d'être visibles par les radars météorologiques opérationnels en bande S d'ECCC et par conséquent, de contaminer les données de ceux-ci. Ces couches de visibilité ont été générées à l'aide d'une analyse de cônes de vue, qui prend en compte la ligne de visée entre les radars et les emplacements potentiels des éoliennes.

* __Interprétation des données__ : Il est important de noter que les couches de visibilité ont été générées à l'aide d'un simple outil de visualisation. Cela signifie que l'impact réel des éoliennes sur les données radar peut être différent de ce que la couche de visibilité suggère. Les couches de visibilité doivent être considérées comme un outil d'analyse préliminaire permettant d'identifier des zones potentiellement à risque, plutôt que comme une indication définitive de l'interférence des éoliennes avec les données radar.

* __Utilisation avec des données radar traitées__ : Lorsque vous superposez les couches de visibilité radar avec des produits radar traités par ECCC et disponibles sur les plateformes GeoMet du SMC, Datamart du SMC, MétéoCA et meteo.gc.ca, soyez conscient que les données radar que vous visualisez peuvent avoir été traitées pour supprimer les échos autres que météorologiques, y compris ceux des éoliennes, dans la mesure du possible. Ceci est particulièrement important car les systèmes de production de données radar intègrent souvent des algorithmes pour filtrer ces contaminations afin de garantir que les données présentées sont aussi propres et précises que possible.

* __Éviter les erreurs d'interprétation__ : Les couches de visibilité ne doivent pas être interprétées comme un indicateur direct de la contamination des données radar, mais plutôt comme un moyen de comprendre où des interférences sont possibles. Les utilisateurs doivent éviter de supposer que toutes les zones situées dans les couches de visibilité présenteront des échos d'éoliennes dans les données radar. Inversement, l'absence d'échos d'éoliennes dans les données radar traitées ne signifie pas que les éoliennes n'affectent pas le radar.

* __Applications pratiques__ : En termes pratiques, les couches de visibilité radar sont utilisées à meilleur escient en conjonction avec d'autres ensembles de données et outils d'analyse. Par exemple, si un nouveau parc éolien est prévu dans une zone où l'on s'attend à ce que les turbines soient visibles par les radars, des analyses supplémentaires devraient être menées pour mieux modéliser et simuler les impacts potentiels (si possible), y compris l'examen de données radar brutes pour vérifier s'il y a présence d'échos de turbines.

## Support

Pour toute question relative à ces données, [merci de nous contacter](https://meteo.gc.ca/mainmenu/contact_us_f.html)

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
