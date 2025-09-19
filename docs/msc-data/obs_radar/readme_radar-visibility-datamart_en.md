[In French](readme_radar-visibility-datamart_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TdM](../../readme_en.md) > [MSC Data](../readme_en.md) > [Radar Data and Products](readme_radar_en.md) > Radar visibility products on the MSC Datamart

# Canadian weather radar visibility products

Wind turbines can contaminate weather radar data which can compromise Environment and Climate Change Canada’s (ECCC) ability to provide quality weather forecasts and warnings to Canadians.

In support of ECCC’s [wind farm and weather radar siting guidelines](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/wind-turbine-interference.html), weather radar visibility layers were created for 150, 200 and 250 meters above ground level (mAGL) surface heights, which are representative of typical past and present wind turbine heights (base-to-tip or total) as well as potential future turbine heights given the trend.

These visibility layers were generated from a viewshed analysis using ECCC’s 32 operational S-Band weather radars as observers and the three abovementioned heights as surface offsets.

Within these visibility layers, turbines that are 150, 200 and 250 mAGL tall are likely to be visible to ECCC’s operational weather radars and therefore have the potential to contaminate weather radar data. A polygon layer containing 10 and 60 kilometer radius buffers around each radar denoting the turbine-radar impact zones are also included in this dataset.

## Data Address 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as it becomes available. An [overview and examples to access and use Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available via the HTTPS protocol. It is possible to access it with a standard browser. In this case, we obtain a list of links giving access to a GeoTIFF file.

The data are available at the address :

* [https://dd.weather.gc.ca/today/radar/visibility](https://dd.weather.gc.ca/today/radar/visibility)

__Note__: 

* A [list of radar sites](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/obs_radar/radars_list.pdf) is available. This list will be updated regularly.

## Nomenclature of file names

Files follow the following nomenclature:

* `{YYYYMMDD}_MSC_Radar-Viewsheds_AGL-{height}.json`
* `{YYYYMMDD}_MSC_Radar-ImpactZones.json`

where:

* __YYYYMMDD__ : Year, month and day of the data production
* __MSC__: Constant string for Meteorological Service of Canada, the data source
* __Radar-Viewsheds__ : Constant string indicating that the data contains meteorological radar visibility layers
* __Radar-ImpactZones__ : Constant string indicating that the data contains turbine radar impact zones
* __AGL-{height}__ : Surface heights above ground level [150m, 200m, 250m]
* __json__ : Constant string indicating that the format is GeoJSON

Example:

* 20250113_MSC_Radar-Viewsheds_AGL-150m.json
* 20250113_MSC_Radar-ImpactZones.json

## Data content

__Radar visibility layers__

The radar visibility dataset contains unprojected polygons illustrating the locations at 150, 200 and 250 mAGL surface heights that are likely visible to ECCC’s 32 operational S-Band weather radars. Within these visibility layers, turbines that are 150, 200 and 250 mAGL tall are likely to be visible to ECCC’s operational weather radars and therefore have the potential to contaminate weather radar data.

Note that these visibility layers were generated using a simple viewshed tool and therefore the results may not be completely accurate due to limitations in the data and/or tool. There could be cases where turbines may or may not be visible to ECCC’s radars despite being outside or within these visibility layers. ECCC should be consulted on all wind farm proposals in Canada as early as possible in the project planning phase.

__Radar impact zones__

The radar impact zones dataset contains unprojected polygons illustrating the 10 and 60 km radius buffers around ECCC's 32 operational S-Band weather radars. The 10 km radius buffer around each radar represents the “definite impact zone” where significant impacts to the radar are expected, and therefore turbines should not be built within this zone.

Turbines that fall between the 10 km and 60 km radius buffers (the “moderate impact zone”) are more likely to cause moderate-to-significant impacts to the radar if built within this zone.

Turbines outside of these 60 km buffers and radar visibility layers are less likely to cause significant impacts to the radar.

However, ECCC should still be consulted on all wind farm proposals in Canada as early as possible in the project planning phase, as impacts could still be realized in rare cases.

## Notes and usage

When using the data described in this document, it is important to understand its purpose, limitations, and how it interacts with other radar datasets, especially in the context of potential interference from wind turbines. Below are important points to keep in mind when interpreting and using the data:

* __Disclaimer__: Note that the radar visibility layers were generated using a simple viewshed tool and therefore the results may not be completely accurate due to limitations in the data and/or tool. There could be cases where turbines may or may not be visible to ECCC’s radars despite being outside or within these visibility layers. Also note that the data provided is for informational purposes only. While efforts have been made to ensure accuracy, completeness, and reliability, no guarantee, express or implied, is made regarding the data. The use of this data is at your own risk, and we disclaim any liability for any damages or losses resulting from its use. For any questions or feedback regarding this dataset, please contact us at radarsmeteo-weatherradars@ec.gc.ca. ECCC should be consulted on all wind farm proposals in Canada as early as possible in the project planning phase.

* __Purpose__: The radar visibility layers were created to show locations where wind turbines with base-to-tip (or total) heights equal to 150, 200 and 250 mAGL are likely to be visible to ECCC’s operational S-Band weather radars and therefore have the potential to contaminate weather radar data. These visibility layers were generated using a viewshed analysis, which considers the line-of-sight from the radars to potential turbine locations.

* __Interpretation of the data__: It is important to note that the visibility layers were generated using a simple viewshed tool. This means that the actual impact of wind turbines on radar data might differ from what the visibility layer suggests. The visibility layers should be seen as a preliminary analysis tool for identifying areas of potential concern, rather than a definitive source of turbine-radar interference.

* __Usage with processed radar data__: When overlaying the radar visibility layers with actual ECCC processed radar products available on GeoMet, WeatherCAN, WXO and datamart/hpfx platforms, be aware that the radar data you are viewing may have already undergone processing to remove non-meteorological echoes, including those from wind turbines, when possible. This is particularly important because radar production systems often include algorithms to filter out such contamination to ensure that the data presented is as clean and accurate as possible.

* __Avoiding misinterpretation__: The visibility layers should not be interpreted as a direct indicator of radar data contamination but rather to understand where interference might occur. Users should avoid the assumption that all areas within the visibility layers will show wind turbine echoes in the radar data. Conversely, the absence of turbine echoes in processed radar data does not mean turbines are not affecting the radar.

* __Practical applications__: In practical terms, the radar visibility layers are best used in conjunction with other datasets and analysis tools. For example, if a new wind farm is planned within an area where turbines are expected to be visible to radars, additional studies should be conducted to better model and simulate potential impacts if possible, including the consideration of raw radar data to see if turbine echoes are present.

## Support

If you have any questions about these data, [please contact us](https://meteo.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available via the [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) list.
