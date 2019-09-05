[In English](ceiling_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [Données du SMC](../msc-data/readme_fr.md) > Plafonds


# Plafonds

Le modèle GEM, en configuration régionale, produit cette prévision de plafonds nuageux. Elle se présente en 4 panneaux pour des périodes de prévision de 6, 12, 18 et 24 heures (à 0000 et 1200). Cette carte affiche une prévision des nuages bas (moins de 6 500 pieds) et des nuages moyens (de 6 500 à 24 000 pieds).

| 6 heures  | 12 heures |
|-----------|-----------|
| 18 heures | 24 heures |

* La couverture géographique pour l'ensemble des panneaux est la suivante : L'Amérique du Nord et les régions de l'Arctique, l'Atlantique Nord, le nord de l'Europe et de l'Asie et le Pacifique Nord.
* Les identificateurs de transmission sont les suivants : CMC784, CMC785.

__Échantillon de carte (4 panneaux)__

![echantillon de carte](http://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/samples_products/difax_reg_prog_4-panel-ceilings.gif)

## Givrage et Niveau de congélation (panneau supérieur gauche)

### Champs

* Nuages bas
    * Représentation : Une ligne tiretée entourant une zone en pointillés pâles indique la prévision modélisée d'une couche nuageuse couvrant plus de 6/10 de la voûte céleste et une base inférieure à  6 500 pi au-dessus du niveau moyen de la mer.
* Nuages moyens
    * Représentation : Ligne continue délimitant une zone en pointillés foncés indique la prévision modélisée d'une couche nuageuse couvrant plus  6/10 de la voûte céleste entre 6 500 et 24 000 pi au-dessus du niveau moyen de la mer.

### Pointage

Dans les régions pointillées, la base et le sommet des nuages sont pointés en milliers de pieds (12 = 12 000 pi) au dessus du niveau moyen de la mer.  Le chiffre du bas indique la base et le chiffre du haut indique le sommet. Les sommets supérieurs à 24 000 pi sont pointés 99.
