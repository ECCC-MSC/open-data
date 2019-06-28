[In English](readme_wget-datamart_en.md)

![ECCC logo](../img_eccc-logo.png)

# Utilisation de wget pour les données du Datamart du SMC

Cette brève page d’exemples et de notes d’utilisation illustre les possibilités de téléchargement de données en lots, sélectionnées dans la base de données ouvertes du Datamart du SMC. Veuillez vous référer au manuel officiel de [wget](https://www.gnu.org/software/wget/) (lien externe, en anglais seulement) pour de plus amples détails. Les exemples ci-dessous ont été testés sous Linux et sous l’invite de commande de Windows XP.

Ces exemples sont donnés pour des cas d'utilisation à caractère unique, ou pour accèder à des données dans le passé. Pour récupérer les données en temps réel, nous engageons fortement les usagers à utiliser le [Protocole avancé de mise en file d'attente des messages (AMQP)](../msc-datamart/amqp_fr.md).

Note:

Les utilisateurs de l’invite de commandes Windows devraient remplacer les guillemets simples (') par des guillemets doubles (") dans les exemples ci-dessous.

## __Pour aller chercher un fichier particulier__  de la base de données 00Z du SGPD (Système global de prévision déterministe)

    wget https://dd.meteo.gc.ca/model_gem_global/25km/grib2/lat_lon/00/HHH/nom_de_fichier

    wget -nd -r -l1 -A '*HGT_ISBY*aaaammjjhh_P036.grib2' https://dd.meteo.gc.ca/model_gem_global/25km/grib2/lat_lon/00/036/

Commentaires :

* "aaaammjjhh" réfère à la date de production. hh peut être soit 00 ou 12
* Les options -r et -A acceptent l’utilisation de caractères de remplacement (*, ?, [ ]). Il est possible de se prévaloir de puissantes fonctions de sélection des fichiers en combinant les caractères de remplacement avec une connaissance de la nomenclature des fichiers. Pour passer un argument à l’option -A, le guillemet double devrait être utilisé sous l’invite de commande Windows et le guillemet simple sous les interpréteurs de commandes de style Unix
* Afin de procéder à la sélection des fichiers selon les caractères de remplacement qui lui ont été fournis, wget télécharge le fichier index.html. Quelques versions de wget laissent ce fichier traîner dans le répertoire de téléchargement une fois l’opération complétée. Ce petit problème peut être réglé en mettant à jour votre version de wget

## __Pour aller chercher des champs à partir d’une liste générée localement__ :

    wget -nd -nc -i liste-fichiers -P répertoire-cible -B URL-de-base

Commentaires :

* "liste-fichiers" est un fichier de texte contenant la liste des fichiers désirés
* Les noms de fichiers contenus dans "liste-fichiers" doivent être complets et conformes à la nomenclature des fichiers, ce qui inclut la date du jour. Ceci vous oblige à regénérer une nouvelle liste chaque jour, une étape qu’il est possible d’automatiser. Cette étape a l’avantage d’économiser la bande passante et le temps de téléchargement

* Voici un exemple de valeur correcte d'URL-de-base: https://dd.meteo.gc.ca/radar/PRECIPET/GIF/CASRA/

## Pour aller chercher les prévisions de température du SRPD (Système régional de prévision déterministe) à 00h pour la passe 00Z, à 2m et à tous les niveaux de pression :

    wget -nd -r -l1 -A '*TMP_TGL*aaaammjjhh_P000.grib2,*TMP_ISBL*aaaammjjhh_P000.grib2' -R '*ISBL_[12]00*' https://dd.meteo.gc.ca/model_gem_regional/10km/grib2/00/000/

Commentaires :

* Notez l’utilisation de l’option `-R` pour rejeter les champs isobariques à 100 et 200 hPa
