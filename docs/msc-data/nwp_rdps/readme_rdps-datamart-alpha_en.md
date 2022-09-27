[In French](readme_rdps-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_fr.md) > [Données du SMC](../readme_fr.md) > [SRPD](readme_rdps_en.md) > RDPS Weather Elements on the Grid on DD-Alpha

# Experimental GRIB2 Weather Elements on the Grid data based on the Regional Deterministic Prediction System (RDPS)

For nearly three decades, the [SCRIBE system](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/product-pages/alpha_glb_scrib_scribe-documentation_gen_e.html) has been used to assist meteorologists in preparing weather reports. The philosophy behind SCRIBE is that a set of weather element matrices are generated for selected stations or sample points and then transmitted to regional weather centers. The matrices are then decoded by SCRIBE and can be modified via the graphical interface by the users. The resulting data is then provided to a text generator, which produces bilingual public forecasts in plain language.

The various rules related to the Scribe matrices hinder scientific innovation, do not exploit the richness of the Numerical Weather Prediction (NWP), reduce the understanding of weather forecasts, and require constant intervention from forecasters.

As part of a larger modernization plan for the Meteorological Service of Canada (MSC), in which the role of the forecaster is evolving, the goal is to replace the Scribe matrices, [available on the MSC Datamart](https://dd.meteo.gc.ca/model_gem_regional/matrices/land_regions/), and their limited number of points across Canada with [Weather Elements on the Grid](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_weong-hrdps_e.pdf) ("WEonG"). In other words, for each grid point of a specific numerical prediction system, a set of weather elements will be created to meet the requirements of the various forecast programs. The forecaster will not only have access to a larger set of points (grids) to produce regional forecasts, but each of these grid points will provide a consistent set of weather elements.

## Data Address

MSC testing data repository DD-Alpha data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../.../msc-datamart/amqp_en.md) as soon as it becomes available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTP protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GRIB2 file.

The rotated lat-lon grid data can be accessed at the following address: 

[https://dd.alpha.meteo.gc.ca/model_gem_regional/10km/{HH}](https://dd.alpha.meteo.gc.ca/model_gem_regional/10km/)

where :

* __HH__: Model run start, in UTC [00, 06, 12, 18]

A 24-hour history is kept in this directory.

## Technical specification of the grid

![SRPD rotated lat-lon grid image](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_rdps/grille_rdps_Rlatlon.png)

Values given to the parameters of the rotated lat-lon grid:

| Parameter | Value |
| ------ | ------ |
| ni | 1102 |
| nj | 1076 | 
| resolution at 60° N | 10km |
| coordinates of first grid point | 48.5° S; 62.6° W | 

## Nomenclature of file names 

The files have the following nomenclature:

`{YYYYMMDD}T{HH}Z_MSC_RDPS-WEonG_{VAR}_{LVLTYPE-LVL}_{Grid}{resolution}_PT{hhh}H.grib2`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 standards
* __HH__: UTC run time [00, 06, 12, 18] 
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __RDPS-WEonG__ : Constant string indicating that the data are from the Regional Deterministic Prediction System weather elements on the grid ("WEonG")
* __VAR__ : Variables contained in the files (ex: VISIFOG).
* __LVLTYPE-LVL__ : Vertical level [Sfc for the surface]
* __Grid__ : Horizontal grid [RLatLon]
* __resolution__ : 0.09. Means a resolution of 0.09° (about 10km) in the longitudinal and latitudinal directions
* __PT{hhh}H__ : Time delay according to the standard [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T and H are constant characters designating Period, Time and Hour. "hhh" represents the forecast time [000, 001, 002, ..., 084]
* __grib2__: Constant string indicating that the format is GRIB2.

Example file name:

* 20220821T12Z_MSC_RDPS-WEonG_BSNOW_Sfc_RLatLon0.09_PT024H.grib2

## List of variables

List of surface weather elements on the grid:

| Abbreviation of GRIB2 parameter | Description | Unit |
|------------------------|-------------|----------|
| BSNOW | Presence of blowing snow | Binary (0/1) |
| CFRZR | Probability of freezing rain | %|
| CICEP | Probability of ice pellets | %|
| CONDARAIN | Conditional amount of liquid precipitation | m |
| CONDASNOW | Conditional amount of solid snow | m | 
| CONDICEP | Conditional amount of solid ice pellets | m|
| CP | Character of precipitation | 0=no precipitation; 1=showers; 2=intermittent; 3=continuous|
| CRAIN | Probability of rain | % | 
| CSNOW | Probability of snow | % | 
| DIST | Model orography | m | 
| DPT | Dew point temperature | C |
| DPTYPE | Dominant precipitation type  | 101=rain; 110=hail; 111=drizzle; 203=freezing rain; 212=freezing drizzle; 308=ice pellets; 405=snow; 409=snow pellets; 413=ice crystals; 414=snow grains |
| FZPRATE | Conditional freezing precipitation amount | m |
| GUST | Gust | m/s |
| HSNOWL | Height of snow level | m |
| LAND | Land/Water mask | fraction |
| PARAIN | Probability of liquid precipitation | % | 
| PBSNOW | Probability of blowing snow | % |
| PDZ  | Probability of drizzle | % | 
| PFRDZ | Probability of freezing drizzle | % |
| PFRZR | Probability of freezing precipitation | % | 
| POP | Probability of precipitation | % | 
| PRATE | Conditional precipitation rate | m | 
| PSNOWS | Probability of snow squall | % | 
| PTYPE | Instantaneous precipitation type | 1=rain; 2=rain/snow; 3=freezing rain; 4=ice pellets; 5=snow; 6=none; 7=drizzle; 8=freezing drizzle; 9=freezing rain/ice pellets |
| SCNDPTYPE | Secondary precipitation type | 101=rain; 110=hail; 111=pellets; 203=freezing rain; 212=freezing pellets; 308=pellets; 405=snow; 409=snow pellets; 413=ice pellets; 414=snow grains|
| SK | Day/Night sky conditions (combined cloud cover and opacity) | 0-1=sunny/clear; 2-3=mainly sunny/cloudy periods; 4-5-6=mix of sun and clouds/partly cloudy; 7-8=mainly cloudy/mainly cloudy; 9=cloudy/cloudy; 10=cloudy/overcast |
| TMP | Temperature | C |
| TPII | Total precipitation intensity index | 0=no intensity; 1=low intensity; 2=moderate intensity; 3=high intensity |
| TSTM | Probability of thunderstorm occurrence | % | 
| VISIFOG | Visibility in ice fog | m |
| VISLFOG | Visibility through liquid fog | m |
| WDIR  | Wind Direction | True Degree | 
| WIND | Wind Speed | m/s |

## Support

If you have any questions regarding this data, please [contact us](https://meteo.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) list.
