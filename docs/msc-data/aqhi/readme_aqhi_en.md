[En français](readme_aqhi_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > AQHI

# Data and Products of the Air Quality Health Index (AQHI) observation and forecast

The **Air Quality Health Index AQHI** is a scale designed to help quantify the quality of the air in a certain region on a scale from 1 to 10. When the amount of air pollution is very high, the number is reported as 10+. It also includes a category that describes the health risk associated with the index reading e.g. Low, Moderate, High, or Very High Health Risk . The AQHI is calculated based on the relative risks of a combination of common air pollutants that are known to harm human health, including ground-level ozone, particulate matter, and nitrogen dioxide. The AQHI formulation captures only the short term or acute health risk exposure of hour or days at a maximum .
The formulation of the AQHI may change over time to reflect new understanding associated with air pollution health effects. The AQHI is calculated from data observed in real time, without being verified quality control.

## Access

### How to access the data

This data is available on the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and the [MSC Datamart](../../msc-datamart/readme_en.md) data server:

* [Data available via the GeoMet-Weather geospatial web services](readme_aqhi-geomet_en.md)
* [Data available on the GeoMet-OGC-API geospatial web services](https://api.weather.gc.ca/collections):
    * [AQHI - Observations](https://api.weather.gc.ca/collections/aqhi-observations-realtime)
    * [AQHI - Forecasts](https://api.weather.gc.ca/collections/aqhi-forecasts-realtime)
* [GeoJSON data for AQHI, available on HPFX, the alternative server of the MSC Datamart](readme_aqhi-datamartjson_en.md)
* [CSV data for AQHI, available on the MSC Datamart](readme_aqhi-datamartcsv_en.md), including chemical species forecast data from numerical air quality models
* [XML data for AQHI, available on the MSC Datamart](readme_aqhi-datamartxml_en.md) 

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

The [metadata of the Air Quality Health Index (AQHI) observation and forecast are available on the Open Government Portal](https://open.canada.ca/data/en/dataset/a563e47d-6eb9-4f7f-933c-222ae49fe57f).

## Products

* [Summary of the most recent Air Quality Health Index forecasts for a large number of cities in Canada](https://weather.gc.ca/airquality/pages/index_e.html)
* [Charts of forecasts of ozone, PM2.5 and PM10 near surface and at different altitudes](https://weather.gc.ca/aqfm/index_e.html)

## Partners and pollutants data

The national AQHI program is a joint partnership involving Environment and Climate Change Canada, Health Canada, as well as the provincial, municipal and NGO agencies.

To retrieve data by year, please consult Environment and Climate Change Canada’s (ECCC) [**National Air Pollution Surveillance (NAPS)**](https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b) Program. The NAPS program is the main source of ambient air quality data in Canada. For hourly PM2.5 data, please consult the [data catalogue](https://data-donnees.az.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/Data-Donnees/?lang=en) data folder for each year. 

For additional questions and data requests, you may contact the [NAPS inquiry center](mailto:rnspa-napsinfo@ec.gc.ca).
 
Please note that ECCC cannot provide individual pollutant data as this data is owned by the **provinces and territories**, and in some cases can be obtained from them directly. For any recent, missing data for specific provinces and territories, ECCC suggests you reach out to them separately. You may also consult the table below for NAPS partners and their webpages with real-time data:

   
| NAPS Partners | Links |
| ------ | ------ |
| Government of Newfoundland and Labrador, Department of Environment and Climate Change | https://www.gov.nl.ca/ecc/env-protection/science/airmon/ |
| Government of Prince Edward Island, Department of Environment, Energy and Climate Action | https://www.princeedwardisland.ca/en/topic/air |
| Government of Nova Scotia, Nova Scotia Environment | https://www.novascotia.ca/nse/air/\\ https://www.novascotia.ca/nse/airdata/ |
| Government of New Brunswick, Department of Environment and Local Government | http://www2.gnb.ca/content/gnb/en/departments/elg/environment/content/air_quality.html\\ http://www.elgegl.gnb.ca/AirNB/ |
| Government of Québec, Ministère de l’Environnement et de la Lutte contre les changements climatiques	 | https://www.environnement.gouv.qc.ca/air/inter_en.htm \\ https://www.environnement.gouv.qc.ca/air/reseau-surveillance/telechargement.asp |
| Ville de Montréal, Direction de l’environnement | https://montreal.ca/en/topics/air-quality\\ https://donnees.montreal.ca/ville-de-montreal/rsqa-polluants-gazeux#data |
| Government of Ontario, Ministry of the Environment, Conservation and Parks | http://www.airqualityontario.com/ |
| Manitoba Government, Department of Conservation and Climate | https://www.gov.mb.ca/sd/environment_and_biodiversity/air_quality/index.html \\https://web31.gov.mb.ca/EnvistaWeb/Default.ltr.aspx |
| Government of Saskatchewan, Saskatchewan Ministry of Environment | https://www.saskatchewan.ca/residents/environment-public-health-and-safety/environmental-health/outdoor-air-quality/air-quality-monitoring\\  http://environment.gov.sk.ca/airqualityindex |
| Government of Alberta, Environment and Parks | https://www.alberta.ca/air-quality.aspx\\  http://airdata.alberta.ca/ |
| Government of British Columbia, Ministry of Environment and Climate Change | https://www2.gov.bc.ca/gov/content/environment/air-land-water/air/air-quality\\  https://envistaweb.env.gov.bc.ca/ |
| Metro Vancouver, Department of Parks & Environment | https://metrovancouver.org/services/air-quality-climate-action/current-air-quality |
| Government of Yukon, Department of Environment | https://yukon.ca/en/waste-and-recycling/pollution/air-quality-monitoring |
| Government of the Northwest Territories, Department of Environment and Natural Resources | http://www.enr.gov.nt.ca/en/services/air-quality\\ http://aqm.enr.gov.nt.ca/ |
| Government of Nunavut, Department of Environment | https://gov.nu.ca/environment/information/environmental-protection |

Note: Nunavut does not have a real-time data page link.

You can also access the data from the American [AirNow](https://www.airnow.gov/) portal.

## Technical documentation

* [Guide to Air Quality Health Index forecasts](https://www.canada.ca/en/environment-climate-change/services/weather-health/publications/guide-air-quality-index-forecasts.html)

## Changelog

The chronology of changes to the Air Quality Health Index (AQHI) program is available [here](changelog_aqhi_en.md).

