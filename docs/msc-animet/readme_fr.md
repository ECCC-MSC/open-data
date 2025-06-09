[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_fr.md) > AniMet du SMC

# AniMet du SMC

AniMet du SMC est un outil simple permettant aux utilisateurs d'interagir avec les données ouvertes météorologiques, climatiques, hydrologiques et environnementales du SMC et de créer des animations personnalisées pour n'importe quelle région du monde. Les animations résultantes peuvent être téléchargées et partagées avec un permalien.

AniMet du SMC peut être utilisé pour présenter une variété d'événements météorologiques tels que les tempêtes, les vagues de chaleur, les trajectoires d'ouragans, les événements liés à la qualité de l'air, les rafales de vent extrêmes, et bien plus encore.

AniMet du SMC donne accès aux couches de [GeoMet-Météo et GeoMet-Climat](../msc-geomet/readme_fr.md).

# Accès

**Accès à AniMet du SMC : [https://eccc-msc.github.io/msc-animet/](https://eccc-msc.github.io/msc-animet/)**

Un exemple simple d'animation montrant des orages au crépuscule, avec l'imagerie satellitaire GOES et une couche radar :

<video controls width="66%">
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/MSC-AniMet_20240522T2224Z_Orages_2024-04-22.mp4" type="video/mp4">
</video>
<br>

# Utilisation

Les principales étapes d'utilisation :

1. Ajouter des couches météorologiques et climatiques à la carte
2. Personnaliser le contenu de la carte
3. Configurer l'animation
4. Créer et partager la carte et l'animation

## 1 - Ajouter des couches météorologiques et climatiques

Couches :

* Ajouter des couches dans le panneau `GeoMet-Météo` ou `GeoMet-Climat`. Des sources supplémentaires de données peuvent être ajoutées via le bouton `+`.
* Parcourir l'arborescence des couches pour trouver la couche désirée
* Utiliser la boîte de recherche pour filtrer parmi les couches disponibles
* Cliquer sur le signe `+` pour ajouter une couche à la carte

Superpositions :

* Sélectionner le panneau 'Superpositions' pour ajouter de l'information au-dessus des couches affichées
* Les superpositions présentement disponibles sont les frontières géopolitiques, les villes et les délimitations des plans d'eau candiens en provenance de Ressources naturelles Canada. Ces couches ne sont disponibles qu'à certains niveaux de zoom

## 2 - Personnaliser le contenu de la carte

Configurer les couches dans le panneau `Configuration des couches` et personnaliser la carte.

Couches :

* Lorsque possible, changer la passe de modèle associée à la couche
* Réorganiser les couches à l'aide des flèches vers le haut et vers le bas
    * Les flèches ne sont affichées que si plusieurs couches ont été ajoutées
* Modifier les couleurs des couches
    * Visualiser et sélectionner la palette de couleurs de la couche à partir des styles disponibles
* Ajuster l'opacité des couches
* Activer la visibilité des couches
    * L'icone de la visibilité d'une couche deviendra rouge si la date de la carte est à l'extérieur de la plage temporelle pour cette couche


Temps :

* L'heure actuelle affichée sur la carte est affichée au-dessus du contrôleur temporel
* Le début et la fin de l'animation peuvent être modifiés à l'aide des curseurs situés à gauche et à droite de la barre de progression
* Les contrôles de lecture permettent de jouer, d'arrêter et de passer d'un pas de temps à l'autre
    * Les options de lecture sont situées au-dessus du bouton de lecture/pause et permettent à l'utilisateur de jouer l'animation en boucle ou en sens inverse
    * L'étendue temporelle des couches ajoutées sont périodiquement mises à jour automatiquement et les limites temporelles de la carte peuvent être mises à jour lorsque les pas de temps précédents ne sont plus disponibles
* Le point orange sur la barre de lecture indique le pas de temps actuellement affiché par rapport à l'étendue temporelle définie
* Choisissez d'afficher l'heure à l'heure locale de l'utilisateur (déterminée par le navigateur) ou à l'heure UTC via le bouton `Heure locale`
* La plage temporelle et l'intervalle peuvent être réinitialisés pour correspondre à une couche spécifique en cliquant sur l'icône de l'horloge à côté du nom de la couche dans le panneau de configuration des couches
* En survolant l'icône de l'horloge d'une couche dans le panneau de configuration des couches, on obtient les dimensions temporelles : le pas de temps actuel, la plage d'exécution du modèle et l'intervalle

Carte :

* Agrandir et déplacer la carte sur votre zone d'intérêt
* Redimensionner la carte et l'animation à l'aide de l'outil situé dans le coin inférieur droit de la carte
* Pivoter la carte en appuyant sur les touches _alt-shift_ et en faisant glisser la carte.
* Sélectionner les légendes à afficher à l'aide du bouton `LÉGENDES`. Les légendes peuvent être redimensionnées et déplacées sur la carte et ces changements seront reflétés dans l'animation produite
* L'icône du globe en haut de la carte permet aux utilisateurs de passer d'une projection cartographique à l'autre, d'afficher des graticules et de modifier la couleur de la carte

## 3 - Configurer l'animation

Configurer l'animation dans le panneau `Configuration de l'animation` :

* Fournir un titre d'animation personnalisé, si désiré
* Définir la vitesse de l'animation en images par seconde
* Choisir la carte de fond entre la carte de fond claire et foncée
* Le contour rouge montre ce qui sera inclus dans l'animation et les éléments blancs montrent l'espace utilisé par l'en-tête, le pied de page et l'horloge murale de l'animation
    * Un message d'avertissement s'affiche si les légendes affichées ne sont pas entièrement contenues dans la zone de sortie de l'animation
* Différents formats de sortie peuvent être sélectionnés pour l'animation afin de répondre aux besoins de l'utilisateur et de permettre un partage facile sur les plateformes de médias sociaux

## 4 - Créer et partager la carte et l'animation

Après avoir cliqué sur le bouton `Créer l'animation` et que le processus de génération est terminé, le bouton `Télécharger l'animation` apparaîtra.

Récupérer et partager le permalien avec le bouton `Partager` en haut à droite :

* Vous pouvez copier et sauvegarder le permalien pour une utilisation ultérieure
* Partager directement le permalien par courriel ou sur les médias sociaux
    * Pour partager l'animation sur les médias sociaux, le fichier doit d'abord être enregistré localement

Le [permalien](https://fr.wikipedia.org/wiki/Permalien) vous permet d'ouvrir AniMet du SMC avec un ensemble déterminé de couches et leur configuration, ainsi qu'un zoom, une étendue et une taille de carte spécifiques. Les dimensions temporelles ne sont pas incluses dans le permalien en raison de la nature évolutive et de la disponibilité des données archivées.

# Informations supplémentaires

## Liste d'information

AniMet du SMC exploite les données des [services web 24/7 de GeoMet du SMC](../msc-geomet/readme_fr.md). Nous encourageons les utilisateurs à s'inscrire à la liste de diffusion [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) pour être informés des améliorations et des changements apportés à AniMet du SMC.

## Code source

Le code source d'AniMet du SMC est disponible publiquement sur GitHub : [https://github.com/ECCC-MSC/msc-animet](https://github.com/ECCC-MSC/msc-animet)


## Support

AniMet du SMC est un outil de démonstration des données ouvertes du SMC. Le support aux utilisateurs est offert sur la base du meilleur effort durant les heures de travail normales. Les utilisateurs qui souhaitent obtenir du support sont invités à [nous contacter](https://www.meteo.gc.ca/mainmenu/contact_us_f.html).
