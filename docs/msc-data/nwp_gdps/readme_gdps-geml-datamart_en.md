[En français](readme_gdps-geml-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [GDPS](readme_gdps_en.md) > GDPS-GEML on MSC Datamart

# Experimental Global Environmental eMuLator (GDPS-GEML) data in GRIB2 format

The Global Environmental eMuLator (GEML) is a component of the [experimental Global Deterministic Prediction System (GDPS)](readme_gdps_en.md#data-of-the-experimental-global-deterministic-prediction-system) and is an artificial intelligence (AI)-based weather emulator trained on past atmospheric states.

More specifically, this GEML model is based on data compatible with the ¼°, 13-level version of the [GraphCast model (Lam et al. 2023)](https://www.science.org/doi/10.1126/science.adi2336) from DeepMind. It was trained and refined by ECCC, using ECMWF’s ERA5 data (1979-2016) and operational analyses (2016-2021). The [weights have been recalculated](https://huggingface.co/ECCC-ASTD-MRD/geml) and are also available to the public.

Forecasts are carried out twice daily, each with a 10-day lead time. It generates the reference large-scale temperature and horizontal wind fields, toward which GDPS’s GEM forecasts are spectrally nudged. The geographical coverage is global with a horizontal resolution of 28 km. Data is available on 13 pressure levels, and employs a uniform latitude–longitude grid with 0.25-degree grid resolution. Six atmospheric variables defined on the 13 pressure levels, along with 4 surface variables are available every 6 hours.

## Data location

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GRIB2 file.

The data can be accessed at the following address :

[https://dd.weather.gc.ca/model_gdps-geml/{RES}/grib2/lat_lon/{HH}/{hhh}/](https://dd.weather.gc.ca/model_gdps-geml)

where :

* __RES__ : Horizontal resolution [25km]
* __HHH__ : UTC time of the beginning of the model run[00, 12]
* __hhhh__ : Forecast time[000, 006, ..., 240]

## Technical specification of the grid

Values given to the parameters of the 25km latitude-longitude grid:

| Parameter | Value |
| ------ | ------ |
| ni | 1440 |
| nj | 721 | 
| resolution | 0.25° |
| orientation iof the grid | 0° W  359.75° E | 

## File name nomenclature 

The files have the following nomenclature:

{YYYYMMDD}T{HH}Z_MSC_GDPS-GEML_{VAR}_{LVLTYPE-LVL}_{Grille}{resolution}_PT{hhh}H.grib2

where :

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 standards
* __HH__: UTC run time [00, 12]
* __Z__: Time zone (UTC time)
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __GDPS-GEML__: Constant string indicating that the data come from the experimental Global Environmental eMuLator (GEML), a component of the experimental Global Deterministic Prediction System (GDPS)
* __VAR__: Type of variable contained in the file (e.g. AirTemp)
* __LVLTYPE-LVL__ : Vertical level and height [ex: Sfc for the surface, AGL-2m for the height of 2m above ground, IsbL-0850 for the geopotential height at 850mb]
* __Grid__ : Horizontal grid [LatLon]
* __resolution__ : 0.25. Means a resolution of 0.25° (approx. 25km) in longitudinal and latitudinal directions
* __PT{hhh}H__: Timing according to [ISO8601](https://en.wikipedia.org/wiki/ISO_8601). P, T and H are constant characters for Period, Time and Hour. "hhh" represents the forecast time [000, 006, ..., 240]
* __grib2__: Constant character string indicating that the format is GRIB2.

Examples of filenames :

* 20250529T12Z_MSC_GDPS-GEML_SpecificHumidity_IsbL-0925_LatLon0.25_PT012H.grib2
* 20250529T00Z_MSC_GDPS-GEML_WindU_AGL-10m_LatLon0.25_PT234H.grib2

## List of variables

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/GDPS-GEML_Variables-List_en.csv");
</script>

Notes :

* u (UGRD) and v (VGRD) components of the wind vector are to be resolved relative to the defined grid, in the direction of increasing i and j coordinates. Please refer to Code Table 7 of the GRIB standard for further details.    
    
## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).

