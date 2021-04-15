[In English](amqp_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [MSC Datamart](readme_fr.md) > AMQP


# Protocole avancé de mise en file d'attente des messages

## À propos

Le serveur de données brutes HTTPS appelé le "Datamart du SMC" est un service de téléchargement en temps réel, sur demande. L'usager doit en effet agir pour demander une donnée particulière, et la demande n'aura de succès que si la donnée a été préalablement publiée sur le serveur. 

Le moment exact de l'apparition des données sur le Datamart du SMC est plus ou moins prévisible : un nouvel avertissement météorologique peut y apparaître à tout moment, alors que certaines autres données ont un horaire de production assez régulier (mais tout de même sujet à des perturbations occasionnelles). Or, il peut être important pour certaines applications d'obtenir des données dès leur publication. 

Les tentatives d'obtenir des données du Datamart du SMC dès leur apparition sur le serveur génèrent de nombreuses requêtes prématurées qui sont évidemment infructueuses. Ceci motive l'utilisation d'une solution plus élégante et plus commode pour les usagers.

Afin de faciliter l'obtention en temps opportun des données du Datamart du SMC, le Service météorologique du Canada (SMC) a donc mis en place un fil de données annonçant les fichiers disponibles sur le Datamart du SMC. Ce fil de données utilise le protocole ''Advanced Message Queuing Protocol'' (AMQP). Il devient ainsi possible non seulement d'être avisé de la disponibilité des produits sur le Datamart du SMC lorsque ceux-ci sont publiés, mais aussi de les recevoir automatiquement. 

Le service permet de cibler les notifications pour une série spécifique de fichiers (alertes météorologiques, observations, données de modèle, etc.) et ainsi viser seulement les produits d'intérêt pour l'usager.


## Description

Le script est en langage python [https://www.python.org/](https://www.python.org/) et doit être installé sur le système où il sera requis. De plus, la librairie python-amqplib doit également être installée. Consulter la documentation spécifique à votre système d'exploitation pour savoir comment installer ce logiciel et cette librairie.

Le serveur AMQP sécurisé (SSL, couche de sockets sécurisée) se trouve à l'adresse: dd.meteo.gc.ca 

Il est possible de se connecter de façon anonyme sur le serveur en utilisant la combinaison:

- __Nom d'usager__: anonymous
- __Mot de passe__: anonymous

### Chemin d'accès

Pour le sujet (option subtopic), il suffit de mettre le répertoire du produit, en remplaçant la barre oblique "/" par un point ".". 
Ce sujet est  : REPERTOIRE.DU.PRODUIT.SUR.LE.DATAMART

- '__*__' caractère de remplacement (wildcard) (un seul '*' par répertoire)
- '__#__' signifie les possibilités restantes et doit être à la fin de la clé.

### Script d'utilisation

Le script permettant de récupérer les produits sur le Datamart du SMC et de les placer dans un répertoire local choisi par l'usager, utilise le client Sarracenia (Souscrire, annoncer, et récursivement ré-annoncer afin de communiquer instantanément et ad vitam aeternam). 

Ce client est élaboré pour accomplir des téléchargements d´une façon très fiable et est largement utilisé au sein du gouvernement du Canada :

[https://github.com/MetPX/Sarracenia](https://github.com/MetPX/Sarracenia)

Un survol est disponible ici : [https://github.com/MetPX/sarracenia/blob/master/doc/fr/sarra.rst](https://github.com/MetPX/sarracenia/blob/master/doc/fr/sarra.rst)

Le guide d’installation peut être trouvé à cette adresse :  [https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst)

Quant au guide d’utilisation, il est disponible ici :  [https://github.com/MetPX/sarracenia/blob/master/doc/fr/subscriber.rst](https://github.com/MetPX/sarracenia/blob/master/doc/fr/subscriber.rst)

Plusieurs exemples de fichiers de configuration sont également mis à la disposition des usagers: [https://github.com/MetPX/sarracenia/tree/master/sarra/examples/subscribe](https://github.com/MetPX/sarracenia/tree/master/sarra/examples/subscribe)

__NOTE__:

__Pour faciliter le support__, il est suggéré aux usagers de s'identifier afin de retracer plus facilement les queues en cas de problèmes. Il est donc très fortement recommandé d'ajouter l'une des lignes suivantes dans la configuration de sr_subscribe:

* queue_name q_${BROKER_USER}.${PROGRAM}.${CONFIG}.${HOSTNAME}  (option dynamique)
* q_anonymous.sr_subscribe./nom_config/./nom_compagnie/ (option statique)

Exemple : q_anonymous.sr_subscribe.citypage.compagnie

## Environnement Windows

Dans l’environnement Windows, il suffit de télécharger la dernière version de Sarracenia à cette adresse :

[https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/](https://hpfx.collab.science.gc.ca/~pas037/Sarracenia_Releases/)

Il s’agit d’un fichier EXE qui peut être utilisé sans avoir à [installer](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst) d’environnement Python.

## Exemples

Voici quelques exemples pour recevoir les alertes, les citypage_weather pour une ville et certains champs GRIB du SRPD

* Les commandes disponibles sont:
    * alerts : sr_subscribe [amqp_cap.xml.conf](./amqp_cap-xml.conf) start/stop/status
    * citypage_weather : sr_subscribe [amqp_citypage.conf](./amqp_citypage.conf) start/stop/status
    * rdps_grib : sr_subscribe [amqp_rdps-grib.conf](./amqp_rdps-grib.conf) start/stop/status
* Les logs se retrouvent sous : ~/.cache/sarra/log
* Pour faire du ménage, utiliser : sr_subscribe configname.conf cleanup

## Liens externes

Protocol AMQP sur Wikipédia :
[https://fr.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](https://fr.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)

Librairie python pour AMQP :
[https://pypi.python.org/pypi/amqplib](https://pypi.python.org/pypi/amqplib)


## Pour nous joindre

Si vous utilisez les données disponibles sur le Datamart du SMC, nous recommandons fortement de vous inscrire à la liste de diffusion du Datamart du SMC afin d'être averti de tout changement ou mise à jour des données disponibles.

Vous pouvez vous inscrire ici :
[https://lists.ec.gc.ca/mailman/listinfo/dd_info](https://lists.ec.gc.ca/mailman/listinfo/dd_info)

Vous pouvez nous contacter à cette adresse pour toute question ou commentaire : [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca) 
