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

Le serveur AMQP sécurisé (SSL, couche de sockets sécurisée) se trouve à l'adresse : dd.meteo.gc.ca .

Il est possible de se connecter de façon anonyme sur le serveur en utilisant la combinaison :

- __Nom d'usager__: anonymous
- __Mot de passe__: anonymous

### Chemin d'accès

Pour le sujet (option subtopic), il suffit de mettre le répertoire du produit, en remplaçant la barre oblique "/" par un point ".". 

Ce sujet est : REPERTOIRE.DU.PRODUIT.SUR.LE.DATAMART

- '__\*__' caractère de remplacement (wildcard) (un seul '*' par répertoire)
- '__#__' signifie les possibilités restantes et doit être à la fin de la clé.

### Script d'utilisation

Le script permettant de récupérer les produits sur le Datamart du SMC et de les placer dans un répertoire local choisi par l'usager, utilise le client Sarracenia (Souscrire, annoncer, et récursivement ré-annoncer afin de communiquer instantanément et ad vitam aeternam). 

Ce client est élaboré pour accomplir des téléchargements d´une façon très fiable et est largement utilisé au sein du gouvernement du Canada :

[https://metpx.github.io/sarracenia/](https://metpx.github.io/sarracenia/)

Un survol est disponible ici : [https://metpx.github.io/sarracenia/Explanation/Overview.html](https://metpx.github.io/sarracenia/Explanation/Overview.html)

Le guide d’installation peut être trouvé à cette adresse : [https://metpx.github.io/sarracenia/Tutorials/Install.html](https://metpx.github.io/sarracenia/Tutorials/Install.html)

Quant au guide d’utilisation, il est disponible ici : [https://metpx.github.io/sarracenia/How2Guides/subscriber.html](https://metpx.github.io/sarracenia/How2Guides/subscriber.html)

Plusieurs exemples de fichiers de configuration sont également mis à la disposition des usagers : [https://github.com/MetPX/sarracenia/tree/stable/sarracenia/examples/subscribe](https://github.com/MetPX/sarracenia/tree/stable/sarracenia/examples/subscribe).

__NOTES__:

__Pour faciliter le support__, il est suggéré aux usagers de s'identifier afin de retracer plus facilement les queues en cas de problèmes. Il est donc très fortement recommandé d'ajouter l'une des lignes suivantes dans la configuration Sarracenia:

* `queueName q_${BROKER_USER}.${PROGRAM}.${CONFIG}.${HOSTNAME}`  (option dynamique)
* `queueName q_anonymous.subscribe./nom_config/./nom_compagnie/` (option statique)

Exemple : `q_anonymous.sr_subscribe.citypage.compagnie`

Aussi, voici une liste de recommandations pour l'usager "anonymous" qui souhaite récupérer un sous-ensemble significatif de données sans crainte de perte d'information:

* L'option `expire` permet d'ajuster la période de rétention souhaitée par l'utilisateur. On suggère une valeur supérieure à 5 minutes, qui est la valeur par défaut.  
* Augmenter le nombre d'instances dans la configuration ce qui permet de traiter plus efficacement les messages afin de minimiser leur nombre dans la queue.
* Séparer les configurations en plusieurs configurations plus petites afin d'éviter d'atteindre le maximum de 10000 messages dans une queue (le nom des queues doit être différent entre les configurations).

## Environnement Windows

Dans l’environnement Windows, il suffit de télécharger la dernière version de Sarracenia à cette adresse :

[https://github.com/MetPX/sarracenia/releases](https://github.com/MetPX/sarracenia/releases)

Il s’agit d’un fichier EXE qui peut être utilisé sans avoir à [installer](https://github.com/MetPX/sarracenia/blob/master/doc/fr/Install.rst) d’environnement Python.

## Exemples

Voici quelques exemples pour recevoir les alertes, les citypage_weather pour une ville et certains champs GRIB du SRPD :

* Les commandes disponibles sont :

    * [alerts](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/ddc_cap-xml.conf):
    
        * `sr3 add subscribe/ddc_cap-xml.conf`
        * `sr3 start subscribe/ddc_cap-xml.conf`
        * `sr3 stop subscribe/ddc_cap-xml.conf`
        * `sr3 cleanup subscribe/ddc_cap-xml.conf`
	
    * [citypage_weather](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/dd_citypage.conf):
    
        * `sr3 add subscribe/dd_citypage.conf`
        * `sr3 start subscribe/dd_citypage.conf`
        * `sr3 stop subscribe/dd_citypage.conf`
        * `sr3 cleanup subscribe/dd_citypage.conf`
	
    * [RDPS](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/dd_rdps.conf):
    
        * `sr3 add subscribe/dd_rdps.conf`
        * `sr3 start subscribe/dd_rdps.conf` 
        * `sr3 stop subscribe/dd_rdps.conf`
        * `sr3 cleanup subscribe/dd_rdps.conf`
	
    * [bulletins](https://github.com/MetPX/sarracenia/blob/development/sarracenia/examples/subscribe/dd_aacn_bulletins.conf):

        * `sr3 add subscribe/dd_aacn_bulletins.conf`
        * `sr3 start subscribe/dd_aacn_bulletins.conf`
        * `sr3 stop subscribe/dd_aacn_bulletins.conf`
        * `sr3 cleanup subscribe/dd_aacn_bulletins.conf`

* Ls fichiers de configuration sont placés ici :  `~/.config/sr3/subscribe`
* Les logs se retrouvent ici :  `~/.cache/sr3/log`
* Pour faire du ménage, la commande est la suivante : `sr3 cleanup subscribe/config_name.conf` 

Note: La commande `sr3 add` place automatiquement l'exemple de fichier de configuration dans le répertoire `~/.config/sr3/subscribe` de l'usager.

## Liens externes

* Protocol AMQP sur Wikipédia :
[https://fr.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](https://fr.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
* Librairie python pour AMQP :
[https://pypi.python.org/pypi/amqplib](https://pypi.python.org/pypi/amqplib)

## Bonnes pratiques

* Pour les utilisateurs d'applications "NodeJS", nous recommandons l'utilisation de la bibliothèque [amqplib](https://github.com/amqp-node/amqplib)
* Nous déconseillons également l'utilisation de la bibliothèque "NodeJS" `node-amqp`, car il s'agit pour l'instant d'un projet non maintenu

## Pour nous joindre

Si vous utilisez les données disponibles sur le Datamart du SMC, nous recommandons fortement de vous inscrire à la liste de diffusion du Datamart du SMC afin d'être averti de tout changement ou mise à jour des données disponibles.

Vous pouvez vous inscrire ici :
[https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/)

Le soutien aux utilisateurs est fourni dans la mesure du possible pendant les heures normales de bureau. Les utilisateurs qui demandent de l'aide sont invités à [communiquer avec nous](https://meteo.gc.ca/mainmenu/contact_us_f.html).
