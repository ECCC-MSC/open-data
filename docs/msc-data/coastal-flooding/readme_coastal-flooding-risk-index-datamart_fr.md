[In English](readme_coastal-flooding-risk-index-datamart_en.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [Submersion côtière](readme_coastal-flooding_fr.md) > Indice de risque de submersion côtière sur le Datamart du SMC

# Données d'indice de risque de submersion côtière 

Cette page décrit les données d'indice de risque de [Submersion côtière](readme_coastal-flooding_fr.md) en format GeoJSON disponibles sur le Datamart du SMC.

## Adresse des données 

Les données du site web d'essai de données DD-Alpha du Datamart du SMC peuvent être [automatiquement récupérées avec le Protocole avancé de mise en file d'attente des messages (AMQP)](../../msc-datamart/amqp_fr.md) dès qu'elles deviennent disponibles. Un [survol et exemples pour accéder et utiliser les données ouvertes du Service météorologique du Canada](../../usage/readme_fr.md) est également disponible.

Les données sont disponibles via le protocole HTTPS. Il est possible d’y accéder avec un fureteur standard. Dans ce cas, on obtient une liste de liens donnant accès à un fichier GeoJSON.

Les données d'indice de risque de submersion côtière se trouvent à l'adresse :

[https://dd.alpha.meteo.gc.ca/coastal-flooding/risk-index/](https://dd.alpha.meteo.gc.ca/coastal-flooding/risk-index)

Un historique de 7 jours est conservé dans ce répertoire.

## Nomenclature des noms de fichiers 

Les noms de fichiers suivent la nomenclature ci-dessous :

`{YYYYMMDD}T{HHmm}Z_MSC_CoastalFloodRiskIndex_{SPC-Code}_{coverage-code}_{PTxxxH}_{version-id}.json`

où :

* __YYYYMMDD__ : Année, mois et jour de l'émission des données
* __T__ : Délimiteur temporel selon les normes ISO8601
* __HHmm__ : Heure et minute à laquelle les données sont émises
* __Z__ : Fuseau horaire (heure UTC)
* __MSC__ : Chaîne de caractères constante pour Meteorological Service of Canada, la source des données
* __CoastalFloodRiskIndex__ : Chaîne de caractères constante indiquant le nom du produit contenu dans les fichiers, soit l'indice de risque de submersion côtière
* __SPC-code__ : Identifiant du centre de prévision des intempéries responsable d'émettre et de distribuer le produit [aspc, nlwo, ospc, paspc, pspc, qspc]. Voir la liste des bureaux émetteurs ci-dessous
* __coverage-code__ : Région couverte pour l'indice de risque de submersion côtière. Voir la liste des régions couvertes pour chaque bureau émetteur ci-dessous
* __PTxxxH__ : Heure de validité 
     * __PTxxxHxxM__ : Heure de validité avec les minutes 
     * NOTE : le nom de fichier peut utiliser soit {PTxxxH} soit {PTxxxHxxM}, à la discrétion du générateur de données
* __version-id__ : 
     * v1 pour la version originale
     * v2 pour la nouvelle version après un amendement, v3 pour un autre amendement, v4 et ainsi de suite
* __json__ : Chaîne de caractères constante indiquant que le format est GeoJSON

Exemple :

* 20240618T2200Z_MSC_CoastalFloodRiskIndex_aspc_atlantic_PT014H00M_v1.json

Note:

* Les données sont générées 1 fois par jour et sont valides pour les 24 prochaines heures. Plus spécifiquement, les données sont valides 
de 12UTC ce jour à 12UTC le jour suivant.

### Liste des bureaux émetteurs et des régions couvertes:

| SPC-code | Nom du bureau émetteur | coverage-code | Région couverte |
| ------ | ------ | ------ | ------ |
| aspc | Centre de prévision des intempéries de la région de l'Atlantique | aspc | Atlantique |
| aspc | Centre de prévision des intempéries de la région de l'Atlantique | aspc-magdalen | Île de la Madeleine |
| aspc | Centre de prévision des intempéries de la région de l'Atlantique | aspc-nb | Nouveau-Brunswick |
| aspc | Centre de prévision des intempéries de la région de l'Atlantique | aspc-ns | Nouvelle-Écosse |
| aspc | Centre de prévision des intempéries de la région de l'Atlantique | aspc-pei | Île-du-Prince-Edouard |
| nlwo | Centre de prévision des intempéries de Terre-Neuve-et-Labrador | nlwo | Terre-Neuve-et-Labrador |
| ospc | Centre de prévision des intempéries de l'Ontario | ospc | Ontario |
| ospc | Centre de prévision des intempéries de l'Ontario | ospc-n | Nord de l'Ontario |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc | Arctique et Manitoba |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-baffin | Terre de Baffin |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-qujuqtaaluk | Nord de la Terre de Baffin |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-higharctic | Extrême-Arctique |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-kitikmeot | région administrative du Nunavut (*) |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-kivalliq | région administrative du Nunavut (**) |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-mb | Manitoba |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-nwt | Northwest Territories |
| paspc | Centre de prévision des intempéries des Prairies et de l'Arctique | paspc-yt | Yukon Territory |
| pspc | Centre de prévision des intempéries de la région du Pacfique et du Yukon | pspc | Colombie-Britannique |
| pspc | Centre de prévision des intempéries de la région du Pacfique et du Yukon | pspc-n | Nord de la Colombie-Britannique |
| pspc | Centre de prévision des intempéries de la région du Pacfique et du Yukon | pspc-s | Sud de la Colombie-Britannique |
| qspc | Centre de prévision des intempéries du Québec | qspc | Québec |
| qspc | Centre de prévision des intempéries du Québec | qspc-n | Nord du Québec |
| qspc | Centre de prévision des intempéries du Québec | qspc-s | Sud du Québec |

(*) La région Kitikmeot comprend les parties sud et est de l'île Victoria et la partie adjacente du continent jusqu'à la péninsule de Boothia, ainsi que l'île du Roi-Guillaume et la partie sud de l'île du Prince-de-Galles.
(**) La région Kivalliq comprend la partie du continent située à l'ouest de la baie d'Hudson, ainsi que l'île Southampton et l'île Coats.

## Support

Pour toute question relative à ces données, merci de [nous contacter](https://weather.gc.ca/mainmenu/contact_us_f.html).

## Annonces de la liste de diffusion dd_info 

Les annonces reliées à ce jeu de données sont disponibles via la liste [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).
