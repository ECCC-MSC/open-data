[In English](tutorial_graphs-tables_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [Aperçu de l'utilisation](readme_fr.md) > Créer des graphiques et des tableaux à partir de l'API GeoMet du SMC

# Tutoriel : créer des graphiques interactifs et des tableaux

Les services web [GeoMet du SMC](../msc-geomet/readme_fr.md) peuvent facilement être intégrés dans des bibliothèques web libres et gratuites telles que [Plotly.js](https://plotly.com/javascript/) pour créer des graphiques interactifs pour pages web et applications mobiles. Ce tutoriel montre comment travailler avec le standard WMS (Web Map Service) en utilisant Plotly afin de représenter des données sur un graphique intéractif et afficher des données dans un tableau.

- [Effectuer un GetCapabilities](#effectuer-un-getcapabilities-et-obtenir-les-parametres-de-temps)
- [Préparation des requêtes](#preparation-des-requetes)
- [Ajustement des heures](#ajustement-des-heures)
- [Envoi des requêtes](#envoi-des-requetes-preparees)
- [Création d'un graphique interactif avec Plotly.js](#creation-dun-graphique-interactif-avec-plotlyjs)
- [Visualisation des données dans un tableau](#visualisation-des-donnees-dans-un-tableau)
- [Ajout d'une carte de fréquentation selon les prévisions dans le tableau](#ajout-dune-carte-de-frequentation-selon-les-previsions-dans-le-tableau)

## Effectuer un GetCapabilities et obtenir les paramètres de temps

Les étapes suivantes montrent comment créer un tableau web simple avec un graphique Plotly.js. Le graphique affiche les probabilités qu'il y ait plus de 0.2mm, 1.0mm, 2.5mm et 5.0mm de précipitations à un endroit précis, basées sur le [Système régional de prévision d'ensemble](https://eccc-msc.github.io/open-data/msc-data/nwp_reps/readme_reps_fr/).

Les couches `RDPS.ETA_TT`, `RDPS.ETA_WD` et `RDPS.ETA_WSPD` sont utilisées pour afficher respectivement les prévisions les plus récentes de température, de direction et module du vent à partir du [Système régional de prévision déterministe](docs\msc-data\nwp_reps\readme_reps_fr.md).

### HTML

```html
<html lang="fr">

<head>
	<meta charset="utf-8">
	<title>Exemple de graphique et tableau</title>
	<meta name="description" content="Exemple de graphique et tableau">
	<link href="style.css" rel="stylesheet">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
</head>

<body>
	<div class="container">
		<div class="row title">
			<header class="masthead mb-auto">
				<div class="inner">
					<h1 class="masthead-brand" id="title"></h1>
				</div>
			</header>
		</div>
		<div class="row graph-and-table">
			<div class="reps0 col-sm-12">
				<div id="reps0">
				</div>
			</div>
			<div class="table-probs col-sm-offset-0 col-sm-12">
				<table id="table-probs" class="probs" media="print">
					<caption id="table-title">Prévisions sur une période de 6 heures</caption>
					<caption id="table-footer">*Veuillez noter que ces données proviennent de modèles météorologiques et sont non expertisées.</caption>
					<thead>
						<tr>
							<th>Débutant le</th>
							<th>≥0.2 mm</th>
							<th>≥1.0 mm</th>
							<th>≥2.5 mm</th>
							<th>≥5.0 mm</th>
							<th>Temp.</th>
							<th>Vents</th>
						</tr>
					</thead>
					<tbody>
					</tbody>
				</table>
			</div>
		</div>
		<div class="col-sm-offset-0 col-sm-3">
			<div class="class-sm-offset-1 col-sm-12">
				<p></p>
			</div>
			<div class="class-sm-offset-1 col-sm-12">
				<p></p>
			</div>
		</div>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
	<script src="https://cdn.plot.ly/plotly-2.0.0.min.js"></script>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	<script src="main.js"></script>
</body>

</html>

```
### CSS

```css
 html,
 body {
   height: 100%;
   background-color: rgb(255, 255, 255);
 }
 h1 {
   text-align: center;
 }
 body {
   display: -ms-flexbox;
   display: -webkit-box;
   display: flex;
   -ms-flex-pack: center;
   -webkit-box-pack: center;
   justify-content: center;
   color: #fff;
   text-shadow: 0 .05rem .1rem rgba(0, 0, 0, .5);
   -webkit-print-color-adjust: exact;
 }
 #reps0 {
   display: flex;
 }
 #table-title {
   padding-top: .75rem;
   padding-bottom: .75rem;
   color: #6c757d;
   text-align: center;
   caption-side: top;
 }
 .probs {
   border: 1px solid #C0C0C0;
   border-collapse: collapse;
   padding: 5px;
   margin: auto;
 }
 .probs th {
   border: 1px solid #C0C0C0;
   padding: 5px;
   background: #F0F0F0;
   background: #797979;
   color: white;
   text-align: center;
 }
 .probs td {
   border: 1px solid #C0C0C0;
   text-align: center;
   padding: 5px;
 }
  #nan {
    background-color: #797979;
  }
  h1#title.masthead-brand {
    text-align: center;
  }
  div.row.title {
    margin: auto;
    display: inline;
  }
```
Afin d'utiliser Plotly, les bibliothèques JS et CSS requises doivent être importées. Un élément `<div>` est ajouté dans le corps de notre document HTML et assigné d'un attribut `id` avec une valeur de `reps0`. La valeur "id" est référencée dans le code Javascript

Un peu de CSS est également ajouté afin de définir le style du tableau et la hauteur et la largeur du graphique.

### Javascript

Le code HTML étant terminé, voici les étapes pour écrire un code JavaScript nécessaire à la création d'une application web

```javascript
const parser = new DOMParser();
const [coordX, coordY] = [45.472, -73.750]; //Aéroport de Montréal Pierre-Elliott Trudeau International (CYUL)
const layer02 = 'REPS.DIAG.6_PRMM.ERGE0.2'; //Probabilités de précipitations >= 0.2mm
const layer1 = 'REPS.DIAG.6_PRMM.ERGE1'; //Probabilités de précipitations >= 1mm
const layer25 = 'REPS.DIAG.6_PRMM.ERGE2.5'; //Probabilités de précipitations >= 2.5mm
const layer5 = 'REPS.DIAG.6_PRMM.ERGE5'; //Probabilités de précipitations >= 5mm
const layerTemp = 'RDPS.ETA_TT'; //Température
const layerWindDir = 'RDPS.ETA_WD'; //Direction du vent
const layerWindSp = 'RDPS.ETA_WSPD'; //Module du vent
const server = 'https://geo.weather.gc.ca/geomet?service=WMS&version='; //Serveur de GeoMet du SMC
const getCapab = server + '1.3.0&request=GetCapabilities&layers='; //Lien vers le GetCapabilities
let [version, request, info_format] = ['1.3.0', 'GetFeatureInfo', 'application/json']; //Version, requête et format de l'information
let [minx, miny, maxx, maxy] = [coordX - 0.25, coordY - 0.25, coordX + 0.25, coordY + 0.25]; //boîte autour de CYUL
```
Pour garder les choses en ordre, il faut initialiser à prime abord, des constantes qui contiennent les informations essentielles. Pour ce faire, il faut entrer coordonnées du lieu (`coordX`, `coordY`), les 7 couches désirées (`layer02`, `layer1`, etc.), le lien vers le serveur de GeoMet du SMC afin de pouvoir effectuer les requêtes `fetch()`, la version, le type de requête et le format de la réponse. Une fois les paramètres sélectionnés, il faut calculer les valeurs du paramètre `bbox` de la requête (lieu visé par la requête). 

En utilisant l'API `Fetch`, il est possible d'effectuer un GetCapabilities sur la variable `layer02` pour la couche `REPS.DIAG.6_PRMM.ERGE0.2`. Une fois convertie en texte, la variable `result` contient toutes les informations sur cette couche. 
Avec le `DOMParser` de la constante `parser` déclarée, la `dimension` pour les informations de temps devient disponible. 

Une fois les constantes et variables déclarées et initialisées, une méthode `getCapabilities()`, permet de récupérer les informations de temps.

```javascript
async function getCapabilities() {
  let response = await fetch(getCapab + layer02);
  let data = await response.text().then((data) =>
    parser
      .parseFromString(data, "text/xml")
      .getElementsByTagName("Dimension")[0]
      .innerHTML.split("/")
  );
  return [data[0], data[1], data[2]];
}
```
La fonction asynchrone est créée pour récupérer l'heure de début, de fin et l'intervalle de temps actuellement disponible pour les données de la couche (REPS.DIAG.6_PRMM.ERGE02). Lorsqu'une réponse est reçue, le DOMParser() est utilisé pour récupérer le contenu de la balise GetCapabilities <Dimension> et renvoie un tableau contenant trois éléments représentant l'heure de début et de fin des données météo disponibles ainsi que l'intervalle des données.

L'algorithme principal peut maintenant être développé. 

```javascript
getCapabilities().then(function(response) {
  let startTime = response[0]; //Initialise la date de début
  let endTime = response[1]; //Initialise la date de fin
    let interval = response[2].match(/\d+/)[0]; //RegEx pour avoir le nombre d'heures d'intervalles: Par exemple: PT6H -> 6
    startDate = new Date(startTime); //Objet Date pour la date de début
    endDate = new Date(endTime); //Objet Date pour la date de fin
    var dif = (Math.abs(endDate - startDate) / 36e5) / interval; //Différence entre la date de début et celle de fin selon l'intervalle
    let headers = [];
    headers.push(interval, startDate, dif); //Pousse les informations nécéssaires pour la préparation des requêtes
    headers = prepareRequests(headers, server); //Prépare les requêtes. Headers[0] contient les dates et le reste du tableau, les URLs
    let begin = startTime.split('T')[0]; //Titre de la page
    document.getElementById("title").innerHTML = "Pr&eacute;visions CYUL du " + begin; //Titre du DOM
    let adjustedUTC = adjustUTC(headers[0]); //Ajuste les heures en fonctions du fuseau horaire de l'utilisateur
    let promises = []; //Tableau pour les Promises
    /*
     * La boucle for envoie de manière asynchrone toutes les requêtes contenues dans "headers"
     * Puisque le résultat de toutes les requêtes est nécessaire avant de tracer le graphique et remplir le tableau,
     * l'utilisation du Promise.all est élémentaire
     */
    for (let i = 1; i < headers.length; ++i) {
      promises.push(sendRequests(headers, i)); //Pousse dans la tableau des Promise, la promesse du résultat de la requête
    }
    Promise.all(promises)
      .then((results) => {
        traceGraph(adjustedUTC, results); //Tracer le graphique
        createTable(adjustedUTC, results); //Remplir le tableau
      }).catch(err => { 
        console.log(err);
      });
  }).catch(err => {
    console.log(err);
  });
```

## Préparation des requêtes

La méthode `prepareRequests` est une courte méthode qui servira à initialiser un tableau (Array) contenant toutes les informations requises pour envoyer les requêtes à GeoMet. La première étape est d'itérer à travers toutes les heures disponibles en commençant par `startDate` et en additionnant `dif` jusqu'à `endDate`. Par la suite, il suffit d'initialiser les URLs de chaque couche en omettant le paramètre `time=` afin d'avoir les requêtes de bases pour la méthode `sendRequests`.

```javascript
function prepareRequests(headers, server) {
  const interval = headers[0];
  let startDate = headers[1];
  let dif = headers[2];
  let timesteps = [];
  timesteps.push(startDate.toISOString().replace('.000', '')); //Enlever le .000 à la fin pour la compatibilité avec le paramètre time=
  let increment = startDate;
  for (let i = 0; i < dif; ++i) {
    increment.setHours(increment.getHours() + Number(interval)); //Incrémenter les heures en fonction de l'intervalle
    timesteps.push(increment.toISOString().replace('.000', ''));
  }
  let url02 = server +
    version + '&request=' + request + '&layers=' + layer02 + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layer02 + '&x=1&y=1';
  let url1 = server +
    version + '&request=' + request + '&layers=' + layer1 + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layer1 + '&x=1&y=1';
  let url25 = server +
    version + '&request=' + request + '&layers=' + layer25 + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layer25 + '&x=1&y=1';
  let url5 = server +
    version + '&request=' + request + '&layers=' + layer5 + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layer5 + '&x=1&y=1';
  let urlTemp = server +
    version + '&request=' + request + '&layers=' + layerTemp + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layerTemp + '&x=1&y=1';
  let urlWd = server +
    version + '&request=' + request + '&layers=' + layerWindDir + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layerWindDir + '&x=1&y=1';
  let urlWspd = server +
    version + '&request=' + request + '&layers=' + layerWindSp + '&crs=EPSG:4326&bbox=' +
    minx + ',' + miny + ',' + maxx + ',' + maxy + '&exceptions=xml&width=10&height=10&INFO_FORMAT=' +
    info_format + '&query_layers=' + layerWindSp + '&x=1&y=1';
  let info = [];
  info.push(timesteps, url02, url1, url25, url5, urlTemp, urlWd, urlWspd);
  return info;
}
```

## Ajustement des heures

Par défaut, les heures valides sont en `UTC-0`. De ce fait, lorsque les requêtes sont envoyées et que l'on tente de les afficher, il est préférable d'ajuster les heures en fonction du fuseau horaire locale afin d'avoir une idée plus représentative de la réalité.
La méthode `adjustUTC()` convertie les dates en zulu en format `ISO-8601` et ajuste les heures en fonction de l'heure locale de l'utilisateur.


```javascript
function adjustUTC(time) {
  let adjustedDate = [];
  let dateTime;
  for (let i = 0; i < time.length; ++i) {
    dateTime = new Date(time[i]);
    adjustedDate.push(dateTime);
  }
  return adjustedDate;
}

```
## Envoi des requêtes préparées

Puisque la boucle `for` envoie de manière asynchrone toutes les requêtes contenues dans "headers", le résultat de toutes les requêtes est nécessaire avant de tracer le graphique et remplir le tableau. L'utilisation du `Promise.all` est donc élémentaire afin de pouvoir afficher le résultat des requêtes envoyées. Pour plus d'informations sur l'utilisation des `Promise`, consulter la [documentation officielle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

```javascript
async function sendRequests(headers, nb) {
  let responses = [];
  let datesMod = [];
  let url = headers[nb].concat("&time=" + headers[0][0]);
  for (let k = 0; k < headers[0].length; ++k) {
    datesMod.push(headers[0][k]);
  }
  for (let i = 0; i < datesMod.length; ++i) {
    try {
      if (i != 0) {
        url = url.replace(/[^=]*$/.exec(url), datesMod[i]);
      }
      let response = await fetch(url);
      let data = await response.json();
      responses.push(data.features[0].properties.value);
    } catch (e) {
      console.log(e);
    }
  }
  return responses;
}
```

La méthode asynchrone `GetCapabilities` retourne un tableau contenant trois éléments: La date de début, la date de fin et l'intervalle des disponibilités de la couche météo. Ces valeurs sont essentielles pour pouvoir envoyer les requêtes à GeoMet.

La méthode `prepareRequests` calcule tous les paramètres de `time=` pour les requêtes `GetFeatureInfo` à faire. Par la suite, les URLs sont également créés et la méthode retourne un tableau contenant les périodes de temps et les URLs.
A l'aide de la méthode `sendRequests`, il ne reste plus qu'à envoyer toutes les requêtes à GeoMet et enregistrer les résultats dans la variable `results`.

La méthode `traceGraph` peut alors être développée pour tracer le graphique à l'aide de `Plotly.js`.

## Création d'un graphique interactif avec Plotly.js

La méthode `traceGraph` utilise le tableau de dates et le tableau de résultats pour tracer un graphique. Les dates sont en format ISO-8601 et seront concaténées afin de visualiser les données en format `YYYY-MM-DD HH:MM`. 
Ici, puisque les valeurs des couches utilisées représentent des périodes de 6 heures, une date supplémentaire est ajoutée 6 heures après la dernière valeur disponible des couches météos afin d'avoir un graphique représentatif de la réalité.

```javascript
function traceGraph(xaxis, yaxis) {
  let date = [];
  let tempRounded = [];
  let windKm = [];
  let lastDate = new Date(xaxis[xaxis.length-1]);
  lastDate.setHours(lastDate.getHours() + 6);
  lastDate = lastDate.toLocaleString('fr-CA');
  lastDate = lastDate.substring(0, lastDate.indexOf('m'));
  lastDate = lastDate.replace(' h ', 'h');

  for (let i = 0; i < xaxis.length; ++i) {
    date[i] = xaxis[i].toLocaleString('fr-CA');
    date[i] = date[i].substring(0, date[i].indexOf('m'));
    date[i] = date[i].replace(' h ', 'h');
  }
  date.push(lastDate);
  for (let j = 0; j < yaxis[4].length; ++j) {
    tempRounded[j] = Number(Math.round(yaxis[4][j]));
  }
  for (let k = 0; k < yaxis[6].length; ++k) {
    if (!isNaN(Math.round(yaxis[6][k]))) {
      windKm[k] = Number(Math.round(yaxis[6][k] * 3.6));
    }
  }
  for (let l = 0; l < yaxis.length; ++l) {
    yaxis[l].push(0);
  }
  var trace1 = {
    x: date,
    y: yaxis[0],
    mode: 'lines+markers',
    name: '≥ 0.5mm',
    line: {
      color: 'rgb(144, 224, 239)',
      width: 3,
      shape: 'hv'
    },
    fill: 'tozeroy',
  };
  var trace2 = {
    x: date,
    y: yaxis[1],
    mode: 'lines+markers',
    name: '≥ 1.0mm',
    line: {
      color: 'rgb(72, 202, 228)',
      width: 3,
      shape: 'hv'
    },
    fill: 'tozeroy',
  }
  var trace3 = {
    x: date,
    y: yaxis[2],
    mode: 'lines+markers',
    name: '≥ 2.5mm',
    line: {
      color: 'rgb(0, 150, 199)',
      width: 3,
      shape: 'hv'
    },
    fill: 'tozeroy',
  }
  var trace4 = {
    x: date,
    y: yaxis[3],
    mode: 'lines+markers',
    name: '≥ 5.0mm',
    line: {
      color: 'rgb(2, 62, 138)',
      width: 3,
      shape: 'hv'
    },
    fill: 'tozeroy',
  }
  var layout = {
    title: 'Probabilités de précipitations',
    automargin: true,
    showlegend: true,
    showlegend: true,
    legend: {
      "orientation": "h"
    },
    xaxis: {
      showticklabels: true,
      tickangle: 0,
      nticks: 6,
      tickfont: {
        family: 'Old Standard TT, serif',
        size: 12,
        color: 'black'
      },
    },
    yaxis: {
      title: 'Probabilités (%)',
      range: [0, 100]
    }
  };
  
var data = [trace1, trace2, trace3, trace4 /*trace5, trace6*/];
  Plotly.newPlot('reps0', data, layout);
}
```

Voici un exemple du graphique.
<iframe height="300" style="width: 100%;" scrolling="no" title="" title="Création de graphique avec GeoMet" src="https://codepen.io/opdelta/embed/YzVEEJg?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Voir le "Pen" <a href="https://codepen.io/opdelta/pen/YzVEEJg">
  </a> by opdelta (<a href="https://codepen.io/opdelta">@opdelta</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>


## Visualisation des données dans un tableau

Les résultats des requêtes peuvent être utilisés pour afficher les données dans un tableau. Une méthode est créée avec en paramètres le tableau des dates et le tableau des résultats. 
Ici, le tableau `data` contient les éléments suivants:

 * [0] = Tableau des données REPS.DIAG.6_PRMM.ERGE0.5
 * [1] = Tableau des données REPS.DIAG.6_PRMM.ERGE1
 * [2] = Tableau des données REPS.DIAG.6_PRMM.ERGE2.5
 * [3] = Tableau des données REPS.DIAG.6_PRMM.ERGE5
 * [4] = Tableau des données REPS.ETA_TT
 * [5] = Tableau des données REPS.ETA_WD
 * [6] = Tableau des données REPS.ETA_WSPD

```javascript
function createTable(date, data) {
  for (let z = 0; z < data.length; ++z) {
    data[z].pop();
  }
  let table = document.querySelector("#table-probs");
  let row;
  for (let k = 0; k < date.length; ++k) {
    date[k] = date[k].toLocaleString('fr-CA');
    date[k] = date[k].substring(0, date[k].indexOf('m'));
    date[k] = date[k].replace(' h ', 'h');
  }
  for (let i = 0; i < date.length; ++i) {
    row = table.insertRow(-1);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(-1);
    let cell4 = row.insertCell(-1);
    let cell5 = row.insertCell(-1);
    let cell6 = row.insertCell(-1);
    let cell7 = row.insertCell(-1);
    if (!isNaN(Math.round(data[4][i]))) {
      cell6.innerHTML = Math.round(data[4][i]) + " °C";
    } else {
      cell6.setAttribute("id", "nan");
    }
    if (!isNaN(Math.round(data[5][i])) && !isNaN(Math.round(data[6][i]))) {
      cell7.innerHTML = Math.round(data[6][i] * 3.6) + " km/h " + degToCompass(data[5][i]);
    } else {
      cell7.setAttribute("id", "nan");
    }
    cell1.innerHTML = date[i];
    cell2.innerHTML = data[0][i] + " %";
    cell3.innerHTML = data[1][i] + " %";
    cell4.innerHTML = data[2][i] + " %";
    cell5.innerHTML = data[3][i] + " %";
  }
}
```
Lorsqu'on utilise la couche `RDPS.ETA_WD` pour avoir la direction du vent, la valeur retournée est un angle qui peut être converti en cardinal avec la méthode suivante:

```javascript
function degToCompass(num) {
  let val = Number((num / 45));
  let arr = ["N", "NE", "E", "SE", "S", "SO", "O", "NO"];
  if (Math.round((val % 8)) == 8) {
    return "Variables";
  }
  return arr[Math.round((val % 8))];
}
```

 Voici un exemple de la représentation du graphique et du tableau dans la même page. 

 <iframe height="300" style="width: 100%;" scrolling="no" title="" src="https://codepen.io/opdelta/embed/bGWaQGO?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href="https://codepen.io/opdelta/pen/bGWaQGO">
  </a> by opdelta (<a href="https://codepen.io/opdelta">@opdelta</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>


## Ajout d'une carte de fréquentation selon les prévisions dans le tableau


Afin d'avoir une carte de fréquentation dans le tableau HTML, il faut ajouter les éléments CSS nécéssaires pour représenter la palette de couleur souhaitée:

```css
.low1 {
   background-color: #d8f3dc;
   color: black;
 }
 
 .low2 {
   background-color: #B7E4C7;
   color: black;
 }
 
 .low3 {
   background-color: #95D5B2;
   color: black;
 }
 
 .medium1 {
   background-color: #74C69D;
   color: black;
 }
 
 .medium2 {
   background-color: #52B788;
   color: black;
 }
 
 .medium3 {
   background-color: #40916C;
   color: white;
 }
 
.high1 {
   background-color: #2D6A4F;
   color: white;
 }
 
.high2 {
   background-color: #245741;
   color: white;
 }
 
 .high3 {
   background-color: #1B4332;
   color: white;
 }
.high4 {
  background-color: #081C15;
  color: white;
}
```

Ces valeurs sont utilisées dans la variable globale `colorArray` initialisée au tout début du script pour permettre une association des valeurs avec les couleurs correspondantes.
```javascript
const colorArray = ["low0","low1","low2","low3","medium1","medium2","medium3","high1","high2","high3","high4"];
```

Dans la méthode `createTable()`, une boucle `for` est ajoutée juste en dessous de la ligne `cell5.innerHTML = data[3][i] + "%";` afin d'effectuer l'association requise entre l'élément CSS et la valeur présente dans le tableau. 

```javascript
for (let j = 0; j < 4; ++j) {
      switch(j) {
        case 0:
          let val = data[0][i] / 10;
          cell2.classList.add(colorArray[Math.round(val % 11)]);
          break;
        case 1:
          let val1 = data[1][i] / 10;
          cell3.classList.add(colorArray[Math.round(val1 % 11)]);
          break;
        case 2:
          let val2 = data[2][i] / 10;
          cell4.classList.add(colorArray[Math.round(val2 % 11)]);
          break;
        case 3:
          let val3 = data[3][i] / 10;
          cell5.classList.add(colorArray[Math.round(val3 % 11)]);
          break;
      }
    }
```

Voici un exemple du résultat final.

<iframe height="300" style="width: 100%;" scrolling="no" title="" src="https://codepen.io/opdelta/embed/oNWpQWp?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href="https://codepen.io/opdelta/pen/oNWpQWp">
  </a> by opdelta (<a href="https://codepen.io/opdelta">@opdelta</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>