[In English](changelog_rdaqa_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [ARDQA](readme_rdaqa_fr.md) > Changements au ARDQA

# Chronologie des changements apportés à l'Analyse régionale déterministe de la qualité de l'air (ARDQA)

## Le mardi 21 janvier 2020

### Mise à jours de ARDQA à la version 1.3.0 suite à la nouvelle infrastructure de calcul haute performance. 

Voir les détails via [ce lien](../changelog_multisystems_fr.md).

## Le jeudi 16 avril 2015

### Le Centre météorologique canadien (CMC) met à jour la version 1.0.0 de l'analyse régionale déterministe de la qualité de l'air (ARDQA) avec version 1.1.0

Depuis février 2013, les analyses de surface ont été générées par l'ARDQA pour l'ozone et les particules fines (PM2.5). Le CMC, en collaboration avec la Division de la Recherche en Qualité de l'Air de la direction des Sciences et Technologies Atmosphériques procéde par la présente avec une importante mise à jour en ajoutant trois nouveaux polluants à l'ARDQA : dioxyde d'azote (NO2), particules de moins de 10um (PM10), et dioxyde de soufre (SO2). De plus, un nouveau produit deviendra disponible: une carte géographique de la Cote Air Santé (CAS) pour le domaine entier du Système de Prévision Déterministique Régional de la Qualité de l'Air (SPDRQA) (couverture presqu'enti`re du Canada et des États-Unis).

Initialement les produits générés par le système ARDQA seront disponibles seulement aux clients internes d'Environnent Canada via la page ressource de la cote air santé et aussi via l'interface vizaweb. Dans le futur, ces produits seront également disponibles sur le [portail de données publiques d'Environnement Canada, aussi appelé le datamart](https://dd.weather.gc.ca/).

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](https://dd.weather.gc.ca/doc/genots/2015/04/13/NOCN03_CWAO_132005___00001).

La note technique de l'implementation est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/RDAQA_v110_Technical_note_FR.pdf).

## Le jeudi 28 février 2013

### Le Centre météorologique canadien (CMC) ajoute à ses produits l'analyse régionale déterministe de la qualité de l'air (ARDQA) version 1.0.0

Le jeudi 28 février 2013, le Centre météorologique canadien (CMC) mettra en œuvre un système qui générera une analyse de surface pour les espèces chimiques de la qualité de l'air. Au début, les analyses seront générées pour l'ozone (O3) et les particules fines (PM2.5). La recherche se poursuit en ce qui concerne la production des analyses pour le dioxyde d'azote (NO2) dans le but d'ajouter ces analyses de NO2 plus tard dans l'année 2013.

Le système ARDQA utilise les observations de surface d'O3 et de PM2.5 provenant des réseaux provinciaux et municipaux du Canada, le réseau Canadien d'échantillonnage des précipitations et de l'air (RCEPA) et le programme [EPA/AIRNOW aux États-Unis](https://airnow.gov/). Les champs d'essai pour les analyses sont fournis par le système régional de prévision déterministe de la qualité de l'air (SRPDQA) qui génère des prévisions de 48 heures sur une grille dont la résolution est de 10-km à l'horizontal et avec 80 niveaux à la verticale.

Deux analyses sont générées pour chaque heure de la journée. L'analyse préliminaire est produite environ une heure après l'heure de validité et utilise prés de 98% et 80% des stations Canadiennes et Américaines, respectivement. L'analyse finale est produite environ deux heures après l'heure de validité et utilise près de 99% et 95% des stations Canadiennes et Américaines, respectivement.

Les statistiques de la vérification objective ont été calculées pour O3 et PM2.5 pour les saisons hivernale et estivale. Des détails additionals sur ces vérifications sont disponibles dans la note officielle ci-dessous.

Lors d'une passe expérimentale du système ARDQA effectuée au cours de l'automne 2012, une évaluation subjective a été réalisée par les membres des bureaux régionaux d'Environnement Canada. Les conclusions de cette évaluation étaient les suivantes: les incréments calcules pour l'O3 ont été considérés comme étant continus et logiques, et ont générés des analyses qui étaient régulièrement meilleures que le modèle. Pour les PM2.5, les concentrations maximales générées dans les analyses étaient généralement considérées comme étant valides. cependant, la distribution horizontale des incréments était souvent considérée comme étant exagérée. Toutefois, les corrections appliquées au modèle dans les analyses de PM2.5 où on trouve des moniteurs ont souvent aidé les prévisionnistes à anticiper des tendances similaires dans les zones urbaines pauvres en moniteurs de PM2.5.

Initialement les produits générés par le système ARDQA seront disponibles seulement aux clients internes d'Environnent Canada via la page ressource de la cote air santé et aussi via l'interface vizaweb. Dans le futur, ces produits seront également disponibles sur le [portail de données publiques d'Environnement Canada, aussi appelé le datamart](https://dd.weather.gc.ca/).

Une copie de la note officielle annonçant ce changement est disponible [via ce lien](https://dd.weather.gc.ca/doc/genots/2013/02/26/NOCN03_CWAO_262215___00276).

Une note technique à ce sujet est disponible [via ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/op_systems/doc_opchanges/technote_rdaqa100_20130228_f.pdf).