[In English](readme_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > Politique d'utilisation

# Politique d'utilisation des services de données ouvertes du SMC

La Politique d'utilisation des services de données ouvertes du SMC détermine ce qui constitue une utilisation appropriée des services de données ouvertes du SMC et fournit aux utilisateurs les pratiques exemplaires pour une utilisation optimale. Cette politique d'utilisation des services complémente la [licence d'utilisation finale](../licence/readme_fr.md).

## Utilisation acceptable des données ouvertes du SMC

L'objectif de la politique d'utilisation des services est de garantir que tous les utilisateurs bénéficient d'un accès efficace et ininterrompu aux services de données libres et ouvertes du SMC.

Les utilisateurs des données ouvertes du SMC doivent :

* Afficher clairement l'attribution de la source des données, tel l'exige la [licence d'utilisation finale](../licence/readme_fr.md)
* Ne pas encourager activement ou passivement la violation des droits d'auteur
* Demander et récupérer uniquement les données que vous avez l'intention d'utiliser
* S'inscrire aux listes d'annonces [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info.comm.collab.science.gc.ca/) et/ou [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/) pour être informé des changements apportés aux services de données du SMC et pouvoir s'adapter en conséquence

Veuillez vous référer aux règles d'utilisation et aux pratiques exemplaires suivantes pour garantir une bonne utilisation des services de données ouvertes du SMC.

## Règles d'utilisation et pratiques exemplaires

Pratiques exemplaires :

* Examiner et évaluer le flux de votre application et déterminer quel mécanisme d'accès aux données du SMC répond le mieux à vos besoins. Par exemple, la création d'une archive locale de données devrait être effectuée en utilisant les services du Datamart du SMC, et non les services GeoMet du SMC
* Ajouter un entête HTTP Agent-Utilisateur (HTTP User-Agent) significatif aux requêtes HTTP
* S'assurer qu'il n'y a pas d'utilisation d'entêtes 'no-cache' dans les requêtes HTTP, comme 'Cache-Control : no-cache' et 'Pragma : no-cache'
* Examiner les registres d'application (logs) pour s'assurer que des demandes valides sont faites et que le flux de travail attendu est correctement mis en oeuvre

Règles d'utilisation des services GeoMet du SMC :

* La récupération par lot des tuiles WMS est interdite. Les services de données ouvertes du SMC se réservent le droit de bloquer les applications implémentant ce comportement
* Pour les flux spécifiques aux couches de GeoMet du SMC, l'extension du fournisseur pour les requêtes WMS GetCapabilities spécifiques aux couches doit être utilisée pour récupérer des charges utiles XML plus petites
    * Un exemple est fourni dans la section [Conseils d'utilisation de GeoMet du SMC](../msc-geomet/readme_fr.md#Accès)

Règles d'utilisation des services HTTPS de Datamart du SMC :

* Pour les flux de données en temps réel, utiliser le [service de notifications et de récupération de données en temps réel AMQPS](../msc-datamart/amqp_fr.md)
    * Ne pas demander les listes de répertoires pour évaluer la disponibilité de nouvelles données, le service de notifications AMQPS doit être utilisé pour ce besoin
    * L'utilisation des commandes `wget` ou `curl` est réservée à la récupération de données « ad hoc » seulement. Pour la récupération systématique de données, le service AMQPS doit être utilisé

## Mise à jour de la Politique d'utilisation des services

Cette politique est sujet à changement afin de garantir la qualité du service pour les utilisateurs des données du SMC. Les mises à jour seront communiquées via les listes d'annonces [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info.comm.collab.science.gc.ca/) et [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info.comm.collab.science.gc.ca/).