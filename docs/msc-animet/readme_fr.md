[En anglais](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > AniMet du SMC

# AniMet du SMC

AniMet du SMC est un outil simple permettant aux utilisateurs d'interagir avec les données météorologiques ouvertes du SMC et de créer des animations météorologiques personnalisées pour n'importe quelle région du monde. Les animations résultantes peuvent être téléchargées et partagées avec un permalien.

AniMet du SMC peut être utilisé pour présenter une variété d'événements météorologiques tels que les tempêtes, les vagues de chaleur, les trajectoires d'ouragans, les événements liés à la qualité de l'air, les rafales de vent extrêmes, et bien plus encore.

Dans sa version actuelle, AniMet du SMC donne accès aux couches de [GeoMet-Météo](../msc-geomet/readme_fr.md).

# Accès

**Accès à AniMet du SMC : [https://eccc-msc.github.io/msc-animet/](https://eccc-msc.github.io/msc-animet/)**

Un exemple simple de l'animation d'une couche radar créée avec AniMet du SMC :

<video controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/MSC-AniMet_Radar-Pluie_Sud-Ontario_20230323T0830Z.mp4" type="video/mp4">
</video>

# Utilisation

Les principales étapes d'utilisation :

1. Ajouter des couches météorologiques à la carte
2. Personnaliser le contenu de la carte
3. Configurer l'animation
4. Créer et partager la carte et l'animation

## 1 - Ajouter des couches météorologiques

Ajouter des couches dans le panneau `Ajouter des couches GeoMet-Météo` :

* Parcourir l'arborescence des couches pour trouver la couche désirée
* Utiliser la boîte de recherche pour filtrer parmi les couches disponibles
* Cliquer sur le signe `+` pour ajouter une couche à la carte

Astuce : cliquer sur le nom du panneau, `Ajouter des couches GeoMet-Météo`, pour agrandir ou réduire le panneau.

## 2 - Personnaliser le contenu de la carte

Configurer les couches dans le panneau `Configuration des couches` et personnaliser la carte.

Couches :

* Réorganiser les couches à l'aide des flèches vers le haut et vers le bas
  * Les flèches ne sont affichées que si plusieurs couches ont été ajoutées
* Modifier les couleurs des couches
  * Visualiser et sélectionner la palette de couleurs de la couche à partir des styles disponibles
* Ajuster l'opacité des couches
* Activer la visibilité des couches
  * L'icone de la visibilité d'une couche deviendra rouge s'il n'y a pas de chevauchement avec la plage temporelle choisie


Temps :

* Les contrôles de la carte en bas à gauche de la carte permettent aux utilisateurs de visualiser les pas de temps disponibles
* Le pas de temps actuel et la passe du modèle (le cas échéant) sont affichés en bas à droite de la carte
* La plage temporelle et l'intervalle désirés peuvent être ajustés au haut du panneau `Configuration des couches`
* La plage temporelle et l'intervalle peuvent être réinitialisés pour correspondre à une couche spécifique en cliquant sur l'icône de l'horloge à côté du nom de la couche
* Survoler l'icone de l'horloge d'une couche fournit ses dimensions temporelles : le pas de temps actuel, la plage de la passe de modèle ainsi que l'intervalle

Carte :

* Agrandir et déplacer la carte sur votre zone d'intérêt
* Redimensionner la carte et l'animation à l'aide de l'outil située dans le coin inférieur droit de la carte
* Pivoter la carte en appuyant sur les touches _alt-shift_ et en faisant glisser la carte

## 3 - Configurer l'animation

Configurer l'animation dans le panneau `Configuration de l'animation` :

* Fournir un titre d'animation personnalisé, si désiré
* Sélectionner la légende à afficher
* Définir la vitesse de l'animation en images par seconde
* Choisir l'affichage du temps entre l'heure locale et UTC
* Choisir la carte de fond entre la carte de fond claire et foncée

## 4 - Créer et partager la carte et l'animation

Après avoir cliqué sur le bouton `Créer l'animation` et que le processus de génération est terminé, le bouton `Télécharger l'animation` apparaîtra.

Récupérer et partager le permalien avec le bouton `Partager` en haut à droite :

* Vous pouvez copier et sauvegarder le permalien pour une utilisation ultérieure
* Partager directement le permalien par courriel ou sur les médias sociaux
  * Pour partager l'animation sur les médias sociaux, le fichier doit d'abord être enregistré localement

Le [permalien](https://fr.wikipedia.org/wiki/Permalien) vous permet d'ouvrir AniMet du SMC avec un ensemble déterminé de couches et leur configuration, ainsi qu'un zoom, une étendue et une taille de carte spécifiques. Les dimensions temporelles ne sont pas incluses dans le permalien en raison de la nature évolutive et de la disponibilité des données archivées.

# Informations supplémentaires

## Liste d'information

AniMet du SMC exploite les données des [services web 24/7 de GeoMet du SMC](../msc-geomet/readme_fr.md). Nous encourageons les utilisateurs à s'inscrire à la liste de diffusion [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) pour être informés des améliorations et des changements apportés à AniMet du SMC.

## Code source

Le code source d'AniMet du SMC est disponible publiquement sur GitHub : [https://github.com/ECCC-MSC/msc-animet](https://github.com/ECCC-MSC/msc-animet)


## Support

AniMet du SMC est un outil de démonstration des données ouvertes du SMC et ne bénéficie pas d'un support opérationnel. Le support aux utilisateurs est oofert sur la base du meilleur effort durant les heures de travail normales. Les utilisateurs qui souhaitent obtenir du support sont invités à [nous contacter](https://www.meteo.gc.ca/mainmenu/contact_us_f.html).