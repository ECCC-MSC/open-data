[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > GeoMet du SMC


# GeoMet du SMC

La plateforme GeoMet du SMC rend publiquement accessible les données du Service météorologique du Canada (SMC) et d'Environnement et Changement climatique Canada (ECCC) via des services web interopérables et des interfaces de programmation d'applications (API). Par le biais de standards ouverts, ces services donnent rapidement et gratuitement accès à des milliers de jeux de données et produits météorologiques, climatiques et hydrométriques en temps réel et archivés qui peuvent être intégrés dans les applications spécifiques de l'usager et leurs systèmes d'aide à la décision. Les usagers peuvent développer des applications mobiles, créer des cartes interactives en ligne, ainsi que de visualiser et animer les données du SMC dans des logiciels de bureau. Les services GeoMet du SMC rendent également possible le découpage de données et la reprojection sur demande, tout autant que la conversion de formats et la visualisation personnalisée de couches de données.

## Services

Les services GeoMet du SMC peuvent être utilisés via des logiciels qui supportent les services web géospatiaux de l'Open Geospatial Consortium (OGC) suivants : [Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms), [Web Coverage Service (WCS)](https://www.opengeospatial.org/standards/wcs), [OGC API - Features](https://ogcapi.ogc.org/features/) et [OGC API - Coverages](https://ogcapi.ogc.org/coverages/).

La plateforme GeoMet du SMC comprend les services suivants :
<div class="card-deck">
  <div class="card text-black mb-3 text-center">
    <div class="card-header bg-light"><h5>GeoMet-Météo</h5></div>
    <div class="card-body">
      <p class="card-text">GeoMet-Météo donne accès aux données météorologiques, hydriques et environnementales du Service météorologique du Canada (SMC) par le biais de services web interopérables.</p>
    </div>
  </div>
  <div class="card mb-3 text-center">
    <div class="card-header bg-light"><h5>GeoMet-OGC-API</h5></div>
    <div class="card-body">
      <p class="card-text">
      GeoMet-OGC-API donne accès aux données d'Environnement et Changement climatique Canada (ECCC) et du Service météorologique du Canada (SMC) par le biais des standards émergeants de l'Open Geospatial Consortium (OGC).</p>
    </div>
  </div>
   <div class="card mb-3 text-center">
    <div class="card-header bg-light"><h5>GeoMet-Climat</h5></div>
    <div class="card-body">
      <p class="card-text">
      GeoMet-Climat donne accès aux données d'Environnement et Changement climatique Canada (ECCC) via des services web interopérables.</p>
    </div>
  </div>
</div>

Pour plus d'informations sur l'utilisation des services GeoMet du SMC, voir les pages suivantes:

*    [Vue d'ensemble de l'utilisation des services de données ouvertes](https://eccc-msc.github.io/open-data/usage/readme_fr/)
*    [Tutoriels et guides sur l'utilisation des services GeoMet du SMC](https://eccc-msc.github.io/open-data/usage/tutorials_fr/)

## Standards disponibles

Les services web sont des protocoles élaborés pour supporter des interactions machine-à-machine sur un réseau et sont typiquement utilisés via un accès programmatique et les outils et applications associées dans un environnement informatique de type client/serveur.

Les services web GeoMet du SMC implémentent les standards ouverts ratifiés par [l'Open Geospatial Consortium (OGC)](https://www.opengeospatial.org/) et [l'International Organization for Standardization (ISO)](https://www.isotc211.org/) qui rendent possible l'interopérabilité et ainsi simplifient la découverte, l'accès, la visualisation et l'intégration de données. Les standards de l'OGC et ISO jouent un rôle important pour le [WMO Information System](https://public.wmo.int/fr). Ces standards sont supportés par de nombreux logiciels libres et logiciels commerciaux.

Les services web de l'OGC suivant sont supportés par GeoMet du SMC :

<div class="card-deck">
  <div class="card text-black mb-3 text-center">
    <div class="card-header bg-light"><h5>Web Map Service</h5></div>
    <div class="card-body">
      <p class="card-text">
        Web Map Service (WMS) est un protocole standard qui permet aux utilisateurs de demander et de recevoir des images de cartes géospatiales à partir d'un serveur sur Internet.</p>
        <a href="../wms_fr" class="btn btn btn-primary">En savoir +</a>
    </div>
  </div>
  <div class="card mb-3 text-center">
    <div class="card-header bg-light"><h5>OGC API</h5></div>
    <div class="card-body">
      <p class="card-text">
      L'API OGC (Open Geospatial Consortium API) est un nouvel ensemble d'API Web standardisées (interfaces de programmation d'applications) qui facilitent l'accès et uniformise les données et services géospatiaux.</p>
      <a href="../ogc_api_fr" class="btn btn-primary">En savoir +</a>
    </div>
  </div>
</div>

<div class="card-deck">
  <div class="card mb-3 text-center">
    <div class="card-header bg-light"><h5>Web Coverage Service</h5></div>
    <div class="card-body">
      <p class="card-text">
      Web Coverage Service (WCS) est un protocole standard qui permet aux utilisateurs de demander et de récupérer des données géospatiales sous forme de couvertures ou de grilles sur Internet.</p>
      <a href="../wcs_fr" class="btn btn-primary">En savoir +</a>
    </div>
  </div>
  <div class="card mb-3 text-center">
    <div class="card-header bg-light"><h5>SpatioTemporal Asset Catalog</h5></div>
    <div class="card-body">
      <p class="card-text">
      SpatioTemporal Asset Catalog (STAC) est une norme communautaire de l'OGC qui fournit une structure commune pour décrire et cataloguer les actifs spatio-temporels.</p>
      <a href="../stac_fr" class="btn btn-primary">En savoir +</a>
    </div>
  </div>
</div>

Pour de plus amples informations concernant les [normes](https://www.ogc.org/standards) et les [normes communautaires](https://www.ogc.org/standards/community/) de l'Open Geospatial Consortium, veuillez consulter les références officielle

*   [Web Map Service (WMS)](https://www.opengeospatial.org/standards/wms)
*   [Web Coverage Service (WCS)](https://www.opengeospatial.org/standards/wcs)
*   [OGC API - Features](https://ogcapi.ogc.org/features/)
*   [OGC API - Coverages](https://ogcapi.ogc.org/coverages/)
*   [SpatioTemporal Asset Catalog (STAC) (expérimental)](https://stacspec.org/en)

## Contact et support

### <span class="badge badge-light">Liste d'information</span>

Nous encourageons les usagers à s'abonner à la liste d'information [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) afin d'être informés des améliorations et changements aux services GeoMet du SMC.


### <span class="badge badge-light">Support</span>

Les services GeoMet du SMC sont opérationnels 24/7. Le support aux usagers est offert sur la base du meilleur effort durant les heures de travail normales. Les usagers désirant du support sont invités à [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).
</br></br></br>



