[En français](tutorial_graphs-tables_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_en.md) > [Usage overview](readme_en.md) > Create interactive web graphs and tables

# Tutorial : Create interactive web graphs and tables

Geospatial web services from [MSC's GeoMet](../msc-geomet/readme_en.md) can easily be integrated into open and free web libraries such as [Plotly.js](https://plotly.com/javascript/) to create interactive graphics for web pages and mobile applications. This tutorial will show you how to work with the WMS (Web Map Service) standard using Plotly. Upon completion, you will be able to display any WMS layer from GeoMet from SMC on an interactive graph, query the layer for data, and display it in a table.

- [Send a GetCapabilities request](#send-a-getcapabilities-request-and-fetch-time-parameters)
- [Prepare queries](#prepare-queries)
- [Adjust hours](#adjust-hours)
- [Send queries](#send-prepared-queries)
- [Interactive web graph creation with Plotly.js](create-an-interactive-graph-with-plotlyjs)
- [View data in a table](#view-data-in-table)
- [Add a heatmap to a table](#add-a-heatmap-to-a-table)

## Send a GetCapabilities request and fetch time parameters

The following steps will show you how to create a simple web table with an interactive Plotly.js chart. The graph will display the probabilities that there is more than 0.2mm, 1.0mm, 2.5mm, and 5.0mm of precipitation at a specific location. (`REPS.DIAG.6_PRMM.ERGE0.2`,`REPS.DIAG.6_PRMM.ERGE1`, `REPS.DIAG.6_PRMM.ERGE2.5` and`REPS.DIAG.6_PRMM.ERGE5`). We will also query the `RDPS.ETA_TT`,`RDPS.ETA_WD` and `RDPS.ETA_WSPD` layers to be able to visualize and display the data concerning the modulus and direction of the winds as well as the temperature.

### HTML

```html
<html lang="en">

<head>
	<meta charset="utf-8">
	<title>Graph and table example</title>
	<meta name="description" content="Graph and table example">
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
					<caption id="table-title">Forecast for a 6 hours period</caption>
					<caption id="table-footer">*Please note that these data come from non-expert meteorological models.</caption>
					<thead>
						<tr>
							<th>Starting</th>
							<th>≥0.2 mm</th>
							<th>≥1.0 mm</th>
							<th>≥2.5 mm</th>
							<th>≥5.0 mm</th>
							<th>Temp.</th>
							<th>Winds</th>
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
In order to use Plotly, we need to import the required JS and CSS libraries. A `<div>` element is added to the body of our HTML document and assigned an `id` attribute with a value of `reps0`. The "id" value will be referenced in the JavaScript code in order to specify where to place the interactive graphic in the HTML document.

Some CSS is also added in order to define the style of the table and the height and width of the chart.

### Javascript

With the HTML code now complete, let's turn our attention to writing the JavaScript code needed to create our web application.

```javascript
const parser = new DOMParser();
const [coordX, coordY] = [45.472, -73.750]; //CYUL airport
const layer02 = 'REPS.DIAG.6_PRMM.ERGE0.2'; //Regional precipitation >= 0.2mm
const layer1 = 'REPS.DIAG.6_PRMM.ERGE1'; //Regional precipitation >= 1mm
const layer25 = 'REPS.DIAG.6_PRMM.ERGE2.5'; //Regional precipitation >= 2.5mm
const layer5 = 'REPS.DIAG.6_PRMM.ERGE5'; //Regional precipitation >= 5mm
const layerTemp = 'RDPS.ETA_TT'; //Temperature
const layerWindDir = 'RDPS.ETA_WD'; //Wind direction
const layerWindSp = 'RDPS.ETA_WSPD'; //Wind speed
const server = 'https://geo.weather.gc.ca/geomet?service=WMS&version='; //SMC's GeoMet server
const getCapab = server + '1.3.0&request=GetCapabilities&layers='; //Link to GetCapabilities
let [version, request, info_format] = ['1.3.0', 'GetFeatureInfo', 'application/json']; //Version, request and format for the information
let [minx, miny, maxx, maxy] = [coordX - 0.25, coordY - 0.25, coordX + 0.25, coordY + 0.25]; //bbox around CYUL airport
```
To keep things in order, we initially initialize constants that contain the essential information. We need the coordinates of the requested place (`coordX`,`coordY`), the 7 layers that we want to query (`layer02`,` layer1`, etc.), the link to the MSC's GeoMet server in order to be able to perform our `fetch()` requests, the version, the type of request and the format of the response. Once the parameters have been selected, you must calculate the values ​​of the query's `bbox` parameter (location targeted by the query).

Using the `Fetch` API, we can do a GetCapabilities on the `layer02` variable for the `REPS.DIAG.6_PRMM.ERGE0.2` layer. Once converted to text and read, the `result` variable contains all the information about that layer.
With the `DOMParser` of the declared `parser` constant, we will be able to query the response so that we can retrieve the `dimension` for the time information.

Once our constants and variables have been declared and initialized, we can now define our first `getCapabilities()` method, which will be responsible for retrieving our time information.

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
The asynchronous function is created to retrieve the start time, end time and the time interval currently available for the data in the layer (REPS.DIAG.6_PRMM.ERGE02). When a response is received, the DOMParser() is used to retrieve the content of the GetCapabilities <Dimension> tag and returns an array containing three elements representing the start and end time of the available weather data as well as the interval of the weather data. data.

We can now develop the main algorithm of the application.

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
    document.getElementById("title").innerHTML = "CYUL forecast for " + begin; //Titre du DOM
    let adjustedUTC = adjustUTC(headers[0]); //Ajuste les heures en fonctions du fuseau horaire de l'utilisateur
    let promises = []; //Tableau pour les Promises
    /*
     * La boucle for envoie de manière asynchrone toutes les requêtes contenues dans "headers"
     * Comme nous avons besoin du résultat de toutes les requêtes avant de tracer le graphique et remplir le tableau,
     * l'utilisation du Promise.all est élémentaire
     */
    for (let i = 1; i < headers.length; ++i) {
      promises.push(sendRequests(headers, i)); //Pousse dans la tableau des Promise, la promesse du résultat de la requête
    }
    Promise.all(promises)
      .then((results) => {
        traceGraph(adjustedUTC, results); //Trace the graph
        createTable(adjustedUTC, results); //Populate table
      }).catch(err => { //Catch failed fetch
        console.log(err);
      });
  }).catch(err => {
    console.log(err);
  });
```

## Prepare queries

The `prepareRequests` method is a short method that will be used to initialize an array (Array) containing all the information required to send requests to GeoMet. The first step will be to iterate through all the available times starting with `startDate` and adding` dif` to `endDate`. Subsequently, it suffices to initialize the URLs of each layer by omitting the `time =` parameter in order to have the basic requests for the `sendRequests` method.

```javascript
function prepareRequests(headers, server) {
  const interval = headers[0];
  let startDate = headers[1];
  let dif = headers[2];
  let timesteps = [];
  timesteps.push(startDate.toISOString().replace('.000', '')); //Remove trailing zeroes for compatibility with time= parameter
  let increment = startDate;
  for (let i = 0; i < dif; ++i) {
    increment.setHours(increment.getHours() + Number(interval)); //Set the hour according to the intervals supported
    timesteps.push(increment.toISOString().replace('.000', '')); //Add to timesteps array
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

## Adjust hours 

By default, valid times are `UTC-0`. Therefore, when the requests are sent and we try to display them, it is preferable to adjust the hours according to the local time zone in order to have a more representative idea of reality.
The `adjustUTC ()` method converts zulu dates to `ISO-8601` format and is then adjusted to the user's local time.


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
## Send prepared queries

Remember that the for loop sends asynchronously all the requests contained in "headers". As we need the result of all queries before we plot the graph and populate the array, using the `Promise.all` is elementary in order to be able to display the result of our sent queries. For more information on using `Promises`, you can consult the [official documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

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
Now we have been able to write the necessary methods to query a layer by doing a `GetCapabilities`, perform a `GetFeatureInfo` to look up the information on our layers and finally collect the results by appending them to an array.

The asynchronous `GetCapabilities` method which serves as a foundation for our main algorithm returns an array containing three elements: The start date, the end date and the availability interval of our weather layer. These values ​​are essential to be able to send our requests to GeoMet.

The `prepareRequests` method calculates all the parameters of `time =` for the `GetFeatureInfo` requests to be made. Subsequently, the URLs are also created and the method returns an array containing the time periods and the URLs.
Finally, we can, using the `sendRequests` method, send all our requests to GeoMet and save the results.

Now that we have in the `results` variable, the result of all our queries, we can finally start to develop our `traceGraph` method to plot our graph using `Plotly.js`.

## Interactive web graph creation with Plotly.js

The `traceGraph` method uses the date array and the results array to plot a graph. The dates are in ISO-8601 format and will be concatenated in order to view the data in `YYYY-MM-DD HH:MM` format.
In our case, as the values of our layers used represent periods of 6 hours, an additional date is added 6 hours after the last available value of our weather layers in order to have a graph representative of reality.

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

Here's an example of the graph
<iframe height="300" style="width: 100%;" scrolling="no" title="" title="Création de graphique avec GeoMet" src="https://codepen.io/opdelta/embed/YzVEEJg?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See then Pen <a href="https://codepen.io/opdelta/pen/YzVEEJg">
  </a> by opdelta (<a href="https://codepen.io/opdelta">@opdelta</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>


## View data in a table

For the creation of the table, we can now manipulate the results of our queries to display them in the HTML table of the document.

We want to create a method that will take as parameters, the table of dates and the table of results. In our cases, the `data` array contains the following elements:

 * [0] = REPS.DIAG.6_PRMM.ERGE0.5 data table
 * [1] = REPS.DIAG.6_PRMM.ERGE1 data table
 * [2] = REPS.DIAG.6_PRMM.ERGE2.5 data table
 * [3] = REPS.DIAG.6_PRMM.ERGE5 data table
 * [4] = REPS.ETA_TT data table
 * [5] = REPS.ETA_WD data table
 * [6] = REPS.ETA_WSPD data table

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
When using the `RDPS.ETA_WD` layer to get the wind direction, the returned value is an angle. We can convert the angle to cardinal with the following method:

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

Here is an example of the representation of the graph and the table on the same page.

 <iframe height="300" style="width: 100%;" scrolling="no" title="" src="https://codepen.io/opdelta/embed/bGWaQGO?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/opdelta/pen/bGWaQGO">
  </a> by opdelta (<a href="https://codepen.io/opdelta">@opdelta</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>


## Add a heatmap to a table

Now we are able to query a layer by doing a `getCapabilities`, manipulate the time periods available for a particular layer, send requests to GeoMet in order to obtain the weather information necessary to display a graph and a table of this data. The table being now finished, we can add a little CSS in order to have a "heat map" according to the forecasts of each period of time.

Before adding our CSS, we can initialize a new global constant:

```javascript
const colorArray = ["low0","low1","low2","low3","medium1","medium2","medium3","high1","high2","high3","high4"];
```

the variable `colorArray` has 11 color variants defined in our CSS document like this:

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

Depending on the forecast value, we want the representative cell in the table to turn darker. In our `createTable()` method, let's add this `for` loop at the very end just below the line `cell5.innerHTML = data [3] [i] + "%"; `:

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

Here's an example of the final product

<iframe height="300" style="width: 100%;" scrolling="no" title="" src="https://codepen.io/opdelta/embed/oNWpQWp?default-tab=html%2Cresult" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/opdelta/pen/oNWpQWp">
  </a> by opdelta (<a href="https://codepen.io/opdelta">@opdelta</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>