[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > AniMet du SMC

# AniMet du SMC

AniMet du SMC est un outil simple permettant aux utilisateurs d'interagir avec les données ouvertes météorologiques, climatiques, hydrologiques et environnementales du SMC et de créer des animations personnalisées pour n'importe quelle région du monde. Les animations résultantes peuvent être téléchargées et partagées avec un permalien.

AniMet du SMC peut être utilisé pour présenter une variété d'événements météorologiques tels que les tempêtes, les vagues de chaleur, les trajectoires d'ouragans, les événements liés à la qualité de l'air, les rafales de vent extrêmes, et bien plus encore. Les utilisateurs peuvent visualiser, combiner et animer plus de 17 000 couches.

AniMet du SMC donne accès aux couches de [GeoMet-Météo et GeoMet-Climat](../msc-geomet/readme_fr.md).

# Accès

**Accès à AniMet du SMC : [https://eccc-msc.github.io/msc-animet/](https://eccc-msc.github.io/msc-animet/)**

Un exemple simple d'animation MSC AniMet montrant le type significatif de précipitations, la pression au niveau de la mer et l'épaisseur entre 1000mb et 500mb. Il s'agit d'un [préréglage de la météo d'hiver](https://eccc-msc.github.io/msc-animet/?layers=RDPS_10km_PrecipType-Significant1h;0.75;1;1;PRECIPNW-FR;1,RDPS_10km_Pressure_MSL-Contour;0.5;0;1;SeaLevelPressure_4mb;0,RDPS_10km_Thickness-Contour_1000to500mb;0.5;0;1;0;0&extent=-19274854,2826576,486792,11953986&overlays=Boundaries&range=83,4,l,PT1H).

<video controls width="85%">
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/MSC-AniMet_Type_de_precipitation_fr.mp4" type="video/mp4">
</video>
<br>


# Utilisation

Les principales étapes d'utilisation :

1. Ajouter des couches météorologiques et climatiques à la carte
2. Personnaliser le contenu de la carte
3. Configurer l'animation
4. Créer et partager la carte et l'animation

## 1 - Ajouter des couches météorologiques et climatiques

#### <span class="badge badge-info">1.1 - Préréglages</span>

Les préréglages sont des groupes de couches fréquemment utilisées que les utilisateurs peuvent ajouter à la carte, comme les conditions météorologiques actuelles, les données synoptiques classiques, la télédétection, les conditions météorologiques hivernales et estivales et la qualité de l'air. Ils permettent de configurer rapidement des vues d'analyse météorologique courantes. Quand un préréglage est sélectionné, les couches s'ajoutent automatiquement.

![Prereglages](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Prereglages_fr.jpg)


#### <span class="badge badge-info">1.2 - Couches disponibles</span>

Les utilisateurs peuvent sélectionner une couche en saisissant une variable, un système, un niveau ou en parcourant toutes les couches disponibles dans l'arborescence. Consultez la [liste des jeux de données disponibles](../msc-data/readme_fr.md) pour obtenir des informations supplémentaires sur les offres de données ouvertes du MSC.

![Arborescence](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Arborescence_Couches_fr.jpg)


* Des sources de données supplémentaires peuvent être ajoutées via le bouton `+`. Accédez à des services WMS tiers supplémentaires, notamment ceux du **CEPMMT**, de la **NASA**, de **NOAA-nowCOAST**, de **NOAA-NCEP** et du service CartoService du ministère de l'Énergie et des Ressources naturelles du Québec.

![Source de donnees](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Source_Donnee_Additionnel_fr.jpg)



#### <span class="badge badge-info">1.3 - Ensembles de données vectorielles de l'utilisateur</span>

MSC AniMet prend désormais en charge l'ajout de vos propres jeux de données `GeoJSON`, `TopoJSON`, `GPX`, `IGX` et `KML` à la carte. Il vous suffit de glisser-déposer vos jeux de données sur la carte pour les visualiser avec vos couches favorites. Un style par défaut est attribué aux jeux de données de l'utilisateur ; il n'est pas possible de le modifier.


---------------------

## 2 - Personnaliser le contenu de la carte

Configurer les couches dans le panneau `CONFIGURER` et personnaliser la carte.

##### <span class="badge badge-info">2.1 - Personnaliser du style de la couche et de la légende</span>

* `Sélectionner la passe de modèle` : Lorsqu’elle est disponible, modifiez l’exécution du modèle associée à la couche en cliquant sur la date.
* Réorganisez les couches à l’aide des flèches haut et bas.
    * Les flèches sont affichées uniquement si plusieurs couches ont été ajoutées.
* `Temporel` : En survolant l'icône d'horloge (🕓) d'une couche, on obtient les dimensions temporelles : le pas de temps actuel, la plage d'exécution du modèle et l'intervalle. L’étendue temporelle et l’intervalle peuvent être réinitialisés pour correspondre à une couche spécifique en cliquant sur l’icône horloge.
* `Opacité` : Ajustez l’opacité de la couche de 0 à 100 %.
* `Régler la visibilité` : masquer ou afficher la couche.
    * L’icône en forme d’œil de la couche devient rouge si l’heure actuelle de la carte est en dehors de l’intervalle temporel de la couche.
* `Sélectionner le style de la couche` : Pour modifier les couleurs de la couche, cliquez sur l’icône de palette.
    * Visualisez et sélectionnez la rampe de couleurs parmi les styles disponibles.
    * Sélectionnez les légendes à afficher via la case à cocher `Afficher la légende`. Les légendes peuvent être redimensionnées et déplacées sur la carte, et ces modifications seront reflétées dans l’animation exportée.
* `Interpolation` : Pour afficher l’interpolation pour les couches GeoMet-Météo prises en charge, permettant des visuels plus fluides et un rendu moins pixelisé grâce à une mise à l’échelle et un rééchantillonnage des données source à la volée. Pour activer l’interpolation, cliquez sur l’icône ✨ de la couche dans le panneau de configuration.


<video width="800" controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Personnaliser_Couche_Legende_Style_fr.mp4" type="video/mp4">
</video>

</br></br>



#### <span class="badge badge-info">2.2 - Utilisation du contrôleur de temps</span>

* L’heure actuelle affichée sur la carte est indiquée au-dessus du contrôleur temporel.
* Le début et la fin de l’animation peuvent être modifiés à l’aide des curseurs situés à gauche et à droite du contrôleur temporel.
* Les commandes de lecture permettent de lancer, arrêter et naviguer entre les pas de temps.
    * Les options de lecture sont situées au-dessus du bouton lecture/pause et permettent à l’utilisateur de boucler l’animation en continu ou de la lire en sens inverse.
    * L’étendue temporelle des couches ajoutées est mise à jour et les limites temporelles de la carte peuvent être ajustées lorsque certains pas de temps ne sont plus disponibles.
* Le point orange sur la barre de lecture indique le pas de temps actuellement affiché par rapport à l’étendue temporelle définie.
* L’encoche orange est l’indicateur temporel. Elle affiche l’heure actuelle en relation avec les couches de données actuellement visibles sur la carte.
* L’intervalle de pas de temps peut être sélectionné via le menu déroulant à droite du contrôleur temporel.
* Cliquez sur ⏮️⏭️ pour aller au premier/dernier pas de temps et sur ⏪⏩ pour passer au pas de temps suivant ou précédent.
* Choisissez d’afficher l’heure selon le fuseau horaire local de l’utilisateur (déterminé via le navigateur) ou en UTC via l’interrupteur `Heure locale`.
* Via le chevron situé à côté de l’interrupteur `UTC/Heure locale`, les utilisateurs peuvent sélectionner un fuseau horaire spécifique pour la carte. Il est possible de revenir au fuseau horaire du système via la flèche bleue de réinitialisation dans le menu déroulant des fuseaux horaires.
* La vitesse de lecture de l’animation peut maintenant être modifiée via le contrôleur temporel afin d’ajuster le nombre d’images par seconde affichées lors de l’animation. La vitesse de lecture par défaut est de 4 images par seconde et peut être augmentée jusqu’à 10 images par seconde pour une animation plus fluide. Pour modifier la vitesse de lecture de l’animation, utilisez l’icône ⚙️ dans le contrôleur temporel.


![Controleur temporel](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Bouton_Controleur_Temporel_fr.png)


**Cet exemple montre comment utiliser les paramètres du contrôleur temporel.**

<video width="800" controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Controleur_Temporel_Tuto_fr.mp4" type="video/mp4">
</video>

</br>

#### <span class="badge badge-info">2.3 - Personnaliser la carte de base et les superpositions</span>

Dans le coin supérieur, cliquez sur `Personnaliser la carte` (icône 🌎) pour modifier le fond de carte et les superpositions.</br>

* Sélectionner une projection
    * `3857` Web Mercator
    * `3978` Lambert conique conforme
    * `3995` Stéréographique polaire arctique
    * `4326` WGS84 (lat/lon)
* Ajouter des graticules.
* Sélectionner des fonds de carte OpenStreetMap, les contours des limites / la couleur d’arrière-plan.
* Ajouter des superpositions (noms de villes, cartographie topographique et autre).
* Zoomer et déplacer la carte vers votre zone d’intérêt.
* Redimensionner la carte et l’animation avec la poignée `+/-` située dans le coin inférieur droit de la carte.
* Faire pivoter la carte en maintenant les touches `Alt-Shift` enfoncées et en faisant glisser la carte.


![Fond de carte](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Fond_Carte_fr.jpg)


#### <span class="badge badge-info">2.4 – Utilisation des outils d’annotation</span>

Les utilisateurs peuvent aussi surligner ou annoter la carte avec des zones de texte et des formes. Il suffit de faire un `clic droit` sur la carte et de sélectionner une option de marquage. Toutes les annotations ajoutées sont conservées dans l’animation générée.

* Pour supprimer une annotation, faites un `clic droit` dessus et appuyez sur la touche de suppression `Del/Suppr`.
* Pour déplacer une forme, maintenez le `clic droit` enfoncé tout en la faisant glisser sur la carte.


![Outils annotation](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Outils_Annotations_fr.jpg)


<video width="700" controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Annotations_fr.mp4" type="video/mp4">
</video>

</br>

#### <span class="badge badge-info">2.5 - Afficher les propriétés des données</span>


L'utilisateur peut cliquer n'importe où sur la carte interactive pour afficher les valeurs brutes et les propriétés complètes des points. Si plusieurs couches sont superposées, toutes les données disponibles s'afficheront dans les fenêtres contextuelles. Cliquez sur les coordonnées en haut de la fenêtre contextuelle pour modifier leur mode d'affichage.

![Proprietes donnees](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Proprietes_Donnees_fr.jpg)

-------------------------

## 3 - Configurer l'animation

Configurez l’animation dans le panneau `EXPORTER` :

* Ajoutez un titre personnalisé pour l’animation, si désiré.
* Définissez la vitesse de l’animation en images par seconde.
* Ajoutez des bordures colorées aux légendes (correspondant aux points à côté des libellés de couche dans l’animation finale).
* Le contour rouge indique ce qui sera inclus dans le rendu de l’animation, et les éléments blancs représentent l’espace utilisé par l’en-tête, le pied de page et l’horloge.
    * Un message d’avertissement s’affichera si les légendes visibles ne sont pas entièrement incluses dans la zone de sortie de l’animation.
* Différents formats d’image (ratio d’aspect) peuvent être sélectionnés pour s’adapter aux besoins de l’utilisateur et faciliter le partage sur les réseaux sociaux.
* Prévisualisez l’animation créée avant de la télécharger.


![Configure animation](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Configurer_Animation_fr.jpg)


## 4 - Créer et partager la carte et l'animation

Après avoir cliqué sur le bouton `Créer l'animation` et que le processus de génération est terminé, le bouton `Télécharger` apparaîtra.

Récupérer et partager le permalien avec le bouton `Partager` en haut à droite :

* Vous pouvez copier et sauvegarder le permalien pour une utilisation ultérieure
* Partager directement le permalien par courriel ou sur les médias sociaux
    * Pour partager l'animation sur les médias sociaux, le fichier doit d'abord être enregistré localement

Le [permalien](https://fr.wikipedia.org/wiki/Permalien) vous permet d'ouvrir AniMet du SMC avec un ensemble déterminé de couches et leur configuration, ainsi qu'un zoom, une étendue et une taille de carte spécifiques. Les dimensions temporelles ne sont pas incluses dans le permalien en raison de la nature évolutive et de la disponibilité des données archivées.

# Informations supplémentaires

#### *Liste d'information*

AniMet du SMC exploite les données des [services web 24/7 de GeoMet du SMC](../msc-geomet/readme_fr.md). Nous encourageons les utilisateurs à s'inscrire à la liste de diffusion [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) pour être informés des améliorations et des changements apportés à AniMet du SMC.

#### *Vidéo de démonstration*

Une [vidéo de démonstration](https://vimeo.com/1093851275?share=copy#t=2217.201) présentant les fonctionnalités d'AniMet du SMC est disponible sur Vimeo. Il s'agit d'une démonstration d'une précédente version d'AniMet (juin 2025).

#### *Code source*

Le code source d'AniMet du SMC est disponible publiquement sur GitHub : [https://github.com/ECCC-MSC/msc-animet](https://github.com/ECCC-MSC/msc-animet)


## Support

AniMet du SMC est un outil de démonstration des données ouvertes du SMC. Le support aux utilisateurs est offert sur la base du meilleur effort durant les heures de travail normales. Les utilisateurs qui souhaitent obtenir du support sont invités à [nous contacter](https://www.meteo.gc.ca/mainmenu/contact_us_f.html).
