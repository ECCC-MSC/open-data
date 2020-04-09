[In English](changelog_rips_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPG](readme_rips_fr.md) > Changements au SRPG

# Chronologie des changements apportés au Système régional de prévision de glace (SRPG)

## Le jeudi 17 septembre 2015

### Mise à jour du système régional de prévision de glace (SRPG version 2.2) au Centre météorologique canadien (CMC)

Le jeudi 17 septembre 2015 à partir de 0600 UTC, le Centre Météorologique Canadien (CMC) a procédé à une mise à jour du système régional de prévision de glace (SRPG version 2.2). Voici la liste des changements inclus dans cette mise à jour:

* Assimilation des données AMSR2
* Assimilation des cartes de glace régionales (hebdomadaires) du Service canadien des glaces
* Modifications au traitement des données micro-ondes:
    * Réduction à un tier du nombre de balayages pour les données SSMIS
    * Réduction de la déviation standard de l'erreur d'observation de SSMIS de 0.1 à 0.05 (en lien avec le point précédant)
    * Rejet des données au-dessus des lacs (comme dans la version 1.0 du SRPG)
    * Élimination de recouvrements erronés causés par des vents trop importants

Une note technique avec de plus amples détails est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_rips_20150917_e.pdf) (en anglais).

## Le mardi 23 juillet 2013

### Le Centre Météorologique Canadien (CMC) installe la composante prévision du Système régional de prévision de glace (SRPG-F)

Le 23 juillet 2013, le CMC a implanté, en mode expérimental, pour la première fois, la composante prévision du Système régional de prévision de glace (SRPG-F), version 2.0. Notons que SRPG-F est la composante de prévision de SRPG 2.0.0, basée sur le modèle de glace CICE v4.1 (Los-Alamos sea-ice model). Tous les 6 heures (4 x jour), après la production de l'analyse dans SRPG-A, SRPG-F génère des conditions initiales pour la concentration de glace (analyse), la température de surface de mer (analyse CMC à 00Z), la vitesse de glace (prévision précédente), et l'épaisseur de glace et la profondeur de la couche de mélange (climatologie GLORYS1v1). Le forçage de surface pendant la prévision de 48h vient du système régional SPRD pour l'atmosphère et de courants de surface interpolé dans le temps (climatologie mensuelle GLORYS1v1). Il n'y a pas de conditions frontières pour la glace.

Pour plus d'informations sur ce système, une note technique (Anglais seulement, pour le moment) est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_ripsf_20140506_e.pdf).

## Le lundi 17 mai, 2013

### Le Centre Météorologique Canadien (CMC) a mis à jour la composante analyse du Système régional de prévision de glace (SRPG-A) en passant à la version 2.0

Le 17 mai 2013, le CMC a implanté, en mode expérimental, une nouvelle version de la composante analyse du Système régional de prévision de glace (SRPG-A). Rappelons que le système SRPG-A fournit des estimés aux points de grille presque en temps réel de concentration de glace pour toutes les zones touchées par la glace autour de l'Amérique du Nord et le Groenland, et vise essentiellement à répondre aux besoins opérationnels du Service canadien des glaces. Trois modifications importantes ont été apportées dans cette nouvelle version :

    1. La première modification est l'assimilation de données micro-ondes passives de trois plates-formes satellites pour compléter les données "Special Sensor Microwave / Imager" déjà assimilées à partir d'une plateforme.
    2. Le deuxième changement est l'assimilation de l'information de la concentration des glaces provenant des données de diffusomètre avancées (Advanced Scatterometer data).
    3. Le troisième changement concerne  l'utilisation d'une estimation de l'incertitude d'analyse pour identifier les zones où la concentration de glace estimée dans l'analyse est ensuite remplacée par des valeurs interpolées spatialement.

Pour plus d'informations sur ce système, une note technique (Anglais seulement, pour le moment) est  disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_ripsa_20140505_e.pdf).