[In English](changelog_multisystems_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [Données du SMC](readme_fr.md) > Le journal des modifications aux services opérationnels du CMC


# Changements apportés aux services opérationnels du Centre Météorologique Canadien (CMC)


## Le mardi 21 janvier 2020

### Nouvelle infrastructure de calcul haute performance

Un projet majeur de migration vers une nouvelle infrastructure de superinformatique utilisée par le Service météorologique du Canada a été effectué avec succès le 21 janvier 2020. Cette migration a été le résultat d'un effort conjoint et soutenu pendant plusieurs mois par des experts du Centre météorologique canadien, de la Direction des sciences et de la technologie et de Services partagés Canada.

Au cours des prochaines années, cette mise à niveau importante permettra d'autres transferts technologiques de la recherche et du développement vers les opérations, ce qui favorisera l'amélioration continue des services de prévisions météorologiques et environnementales offerts aux Canadiens et aux autres organismes, utilisateurs et partenaires des gouvernements fédéral et provinciaux.

La note officielle annonçant ce changement est disponible via [ce lien](https://dd.meteo.gc.ca/doc/genots/2020/01/17/NOCN03_CWAO_171911___36984).

## Le jeudi 7 juin 2018

### Remplacement du satellite GOES-13 par GOES-16 et remplacement du satellite Meteosat-10 par Meteosat-11

Le jeudi 7 juin 2018, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du Service météorologique du Canada (SMC) a procédé à une mise à jour de la version 6.0.0 de son système global de prévision déterministe (SGPD), de la version 4.3.0 de son système global de prévision d'ensemble (SGPE) et de la version 5.1.0 de son système régional de prévision déterministe (SRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes :

* Remplacement des observations AMV (Atmospheric Motion Vector) du satellite GOES-13* par celles de GOES-16 dans les systèmes SGPD SGPE et SRPD.
* Remplacement des observations CSR (Clear Sky Radiance) du satellite Meteosat-10** par celles du satellite Meteosat-11 dans les systèmes SGPD et SRPD.

'* Les observations AMV de GOES-13 ont cessé de façon définitive d’être distribuées sur le GTS à partir du 8 janvier 2018.

** Le satellite Meteosat-11 a remplacé Meteosat-10 le 20 février 2018, mais les observations CSR de Meteosat-11 n'ont pas été assimilées entre le 20 février 2018 et le 7 juin 2018.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2018/06/18/NOCN03_CWAO_181607___62703).

## Le mercredi 6 septembre 2017

### Nouvelle infrastructure de calcul haute performance

La migration vers une nouvelle infrastructure de superinformatique utilisée par le Service météorologique du Canada a été effectuée avec succès le 6 septembre 2017. Cette migration a été le résultat de plusieurs mois d’efforts soutenus et conjoints de la part des artisans du Centre météorologique canadien, de la Direction générale des sciences et de la technologie et de Services partagés Canada.

Notre capacité de calcul haute performance atteint maintenant le pétaflop (1015 flops), un niveau comparable à celui des principaux centres météorologiques mondiaux. Cette mise à jour majeure nous permettra dans les années à venir de transférer les technologiques de la recherche et du développement vers les opérations, soutenant ainsi l’amélioration en continue des services en prévisions météorologiques et environnementales offerts aux Canadiens et Canadiennes, aux agences gouvernementales fédérales et provinciales, ainsi qu’aux autres usagers et partenaires.

La note officielle annonçant ce changement est disponible via [ce lien](https://dd.meteo.gc.ca/doc/genots/2017/08/31/NOCN03_CWAO_312003___11256).
Un document avec des détails techniques à ce sujet est disponible via [ce lien](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/HPC_Migration2017_tech_f.pdf).

## Le mercredi 16 mars 2016

### Remplacement du satellite MTSAT-2 par Himawari-8 ainsi que l'ajout des données AMV (de NPP) et ISS-RapidScat

Le mercredi 16 mars 2016, à compter de la passe de 1200 UTC, le Centre météorologique canadien (CMC) du service météorologique du Canada (SMC) procèdera à la mise en œuvre oprérationnelle de la version 5.1.0 de son système global de prévision déterministe (SGPD), de la version 4.2.0 de son système global de prévision d'ensemble (SGPE) et de la version 4.2.0 de son système régional de prévision déterministe (SRPD).

Seulement la composante de l'assimilation des données a été modifiée afin d'inclure les observations suivantes :

* Remplacement des observations AMV (Atmospheric Motion Vector) et CSR (Clear Sky Radiance) du satellite japonais MTSAT-2 par celles d'Himawari-8 dans les systèmes SGPD et SRPD. Comme les CSR ne sont pas assimilés dans le SGPE, seuls les AMV seront remplacés dans le SGPE;
* Ajout d'AMV mesuré par l'instrument Visible Infrared Imaging Radiometer Suite (VIIRS) à bord du satellite SUOMI National Polar-orbiting Partnership (NPP) aux trois systèmes SGPD, SGPE et SRPD;
* Ajout de vents marins provenant du diffusiomètre RapidScat monté sur la station spatiale internationale (ISS), aux trois systèmes SGPD, SGPE et SRPD.
* En ce qui concerne les observations CSR, l'algorithme d'écrémage des observations prises par satellites géostationnaires sera modifié.

La note officielle annonçant ce changement est disponible [en cliquant ici](https://dd.meteo.gc.ca/doc/genots/2016/03/15/NOCN03_CWAO_151730___00994).

## Le mardi 7 mai 2013

### CMC ajoute les données METOP-1 à la famille GPS-ro dans son système d'assimilation de données

## Le lundi 15 avril 2013

### CMC ajoute les satwinds de METEOSAT10 et ASCAT provenant du satellite METOP-1 à son système d'assimilation de données