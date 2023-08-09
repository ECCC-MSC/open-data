[In French](readme_ciops-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC Open Data](../readme_en.md) > [CIOPS](readme_ciops_en.md) > Coastal Ice Ocean Prediction System (CIOPS) on MSC Datamart 

# Coastal Ice Ocean Prediction System (CIOPS) ocean-ice forecasts data in NetCDF format

The ocean-ice forecasts from the CIOPS-East and CIOPS-West systems are available as hourly products. These products are available in NetCDF format on a latitude and longitude grid. The CIOPS-East domain covers the Gulf of St. Lawrence, the North West Atlantic and the east coast of Canada at a resolution of 2km (0.03 x 0.02 degree). The CIOPS-West main domain covers the North East Pacific and the west coast of Canada, also at a resolution of 2km (0.03 x 0.02 degree). The CIOPS-West system also outputs a regional enhancement at 500m resolution (0.008 x 0.005 degree) that covers the Salish Sea region only.

## Data location 

HPFX data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible via web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable NetCDF file.

The data can be accessed at the following URLs: 

* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/east/2km/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)
* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/west/2km/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)
* [https://hpfx.collab.science.gc.ca/{YYYMMDD}/WXO-DD/model_ciops/salish-sea/500m/{HH}/{hhh}/](https://hpfx.collab.science.gc.ca/)                  

where:

* __YYYYMMDD__ : Year, month and day
* __HH__ : Model run start, in UTC [00, 06, 12, 18]
* __hhh__ : Forecast hour [000, 001, 002, ..., 048] 

A history of several weeks is kept in these directories.

## Technical specification of the grids

### East ocean domain

![Image of the CIOPS - East ocean domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-east.png)

| Parameter | Value |
| ------ | ------ |
| ni | 1333 |
| nj | 980 |
| nk | 99 |
| resolution | 2km |

### West ocean domain

![Image of the CIOPS - West ocean domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-west.png)

| Parameter | Value |
| ------ | ------ |
| ni | 600 |
| nj | 785 |
| nk | 68 |
| resolution | 2km |

### Oceanic domain over the Salish Sea

![Image of the CIOPS - Salish Sea ocean domain](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp_ciops/grille_ciops-salishsea.png)

| Parameter | Value |
| ------ | ------ |
| ni | 629 |
| nj | 888 |
| nk | 39 |
| resolution | 500m |

## Filename nomenclature

NOTE: ALL HOURS ARE IN UTC.

The files have the following nomenclature: 

`{YYYYMMDD}T{HH}Z_MSC_CIOPS-{Domain}_{Var}_{LVLTYPE}-{LVL}_{Grid}{resolution}_PT{hhh}H.nc`

where:

* __YYYYMMDD__: Year, month and day of the beginning of the forecast
* __T__ : Time delimiter according to ISO8601 norms
* __HH__: UTC run time [00, 06, 12, 18]
* __Z__ : Time zone (UTC hour)
* __MSC__ : Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __CIOPS__ : Constant string indicating that the data is from the Coastal Ice Ocean Prediction System
* __Domain__ : Constant string indicating the domain [East, West, SalishSea]
* __Var__ : Variable included in the file (see the list below)
* __LVLTYPE__ : Vertical level type [Sfc for the surface, DBS for depth below the surface]
* __LVL__ : Vertical level value where applicable [0.5m, `all` for all available levels]
* __Grid__ : Constant string indicating the grid projection [LatLon]
* __resolution__ : Indicating resolution in degree in latitude and longitude directions [0.03x0.02, 0.008x0.005] 
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "hhh" is the forecast hour [000, 001, 002, ..., 048]
* __nc__ : File extention indicating the NetCDF format

Examples:

* 20220225T00Z_MSC_CIOPS-East_SeaIceDivergence_Sfc_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-West_SeaWaterSalinity_DBS-0.5m_LatLon0.03x0.02_PT002H.nc
* 20220301T00Z_MSC_CIOPS-SalishSea_SeaWaterPotentialTemp_DBS-all_LatLon0.008x0.005_PT002H.nc

## Levels

### East ocean domain

The three-dimensional fields are provided on 99 depth levels in the East ocean domain.

__Depth levels (m)__: 0.50594902, 1.55457, 2.65451, 3.8087499, 5.0204301, 6.29286, 7.62957, 9.0342503, 10.5108, 12.0634, 13.6964, 15.4145, 17.222401, 19.125401, 21.128799, 23.238501, 25.4604, 27.801001, 30.266899, 32.865299, 35.603699, 38.490002, 41.532398, 44.7397, 48.121201, 51.686501, 55.445999, 59.410198 63.590698, 67.9991, 72.648102, 77.550697, 82.720802, 88.172798, 93.921799, 99.983803, 106.375, 113.114 120.218, 127.707, 135.60001, 143.918, 152.68201, 161.91701, 171.645, 181.89, 192.679, 204.037, 215.993 228.57401, 241.81, 255.73199, 270.37201, 285.76001, 301.93201, 318.92001, 336.76099, 355.48901, 375.14301, 395.76001, 417.37799, 440.039, 463.78699, 488.681, 514.80499, 542.32397, 571.61401, 603.60602, 640.60901, 687.87701, 754.76501, 850.67902, 975.659, 1120.37, 1275.53, 1435.96, 1599.4301, 1765.0699, 1932.58, 2101.8501, 2272.8701, 2445.6499, 2620.1799, 2796.5, 2974.6201, 3154.54, 3336.27, 3519.8301, 3705.2, 3892.3999, 4081.4199, 4272.2598, 4464.8999, 4659.3301, 4855.54, 5053.52, 5253.2402, 5454.6699, 5657.8101.

### West ocean domain

The three-dimensional fields are provided on 68 depth levels in the West ocean domain.

__Depth levels (m)__: 0.50752997, 1.55757, 2.6693399, 3.8578801, 5.1419101, 6.5445399, 8.0939703, 9.8241596, 11.775, 13.9924, 16.5266, 19.431101, 22.7589, 26.5595, 30.875799, 35.741402, 41.181301, 47.2131, 53.851898, 61.114101, 69.023003, 77.612503, 86.930801, 97.042702, 108.032, 120.001, 133.077, 147.408, 163.166, 180.552, 199.79201, 221.14301, 244.892, 271.358, 300.88901, 333.86499, 370.69, 411.79599, 457.62799, 508.642, 565.29401, 628.02802, 697.26099, 773.37, 856.68103, 947.45001, 1045.86, 1151.99, 1265.86, 1387.38, 1516.37, 1652.5699, 1795.67, 1945.3, 2101.03, 2262.4199, 2429.03, 2600.3799, 2776.04, 2955.5701, 3138.5701,3324.6399, 3513.45, 3704.6599, 3897.98, 4093.1599, 4289.96, 4488.1602.

### Oceanic domain over the Salish Sea

The three-dimensional fields are provided on 39 depth levels in the Salish sea domain.

__Depth levels (m)__: 0.5, 1.5, 2.50001, 3.50003, 4.5000701, 5.5001502, 6.5003099, 7.5006199, 8.5012398, 9.50243, 10.5048, 11.5093, 12.5182, 13.5354, 14.569, 15.6343, 16.7612, 18.007099, 19.4818, 21.389999, 24.1003, 28.2299, 34.685799, 44.5177, 58.484299, 76.585602, 98.063004, 121.867, 147.089, 173.114, 199.573, 226.25999, 253.067, 279.935, 306.83401, 333.75, 360.67499, 387.603, 414.534.

## List of variables 

<table id="csv-table" class="display"></table>

<link href="https://cdn.jsdelivr.net/npm/simple-datatables@latest/dist/style.css" rel="stylesheet" type="text/css">
<script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest"></script>
<script src="../../../js/variables_datatable.js" type="text/javascript"></script>
<script>
  loadTable("csv-table", "../../../assets/csv/CIOPS_en.csv", "EN");
</script>

Note: The unit `PSU` (Practical Salinity Unit) is equivalent to g/kg or per thousand (‰). It is based on the properties of sea water conductivity.

## Support

If you have any questions about this data, please contact us at: [ec.dps-client.ec@canada.ca](mailto:ec.dps-client.ec@canada.ca)

## Announcements from the dd_info mailing list

Announcements related to this dataset are available in the [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info).

