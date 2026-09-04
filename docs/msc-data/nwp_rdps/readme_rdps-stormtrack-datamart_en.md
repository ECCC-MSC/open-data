[In French](readme_rdps-stormtrack-datamart_fr.md)

! [ECCC logo](.. /.. /img_eccc-logo.png)

[ToM](.. /.. /readme_en.md) > [MSC data](.. /readme_en.md) > [RDPS](readme_rdps_en.md) > Storm tracks from the RDPS on the MSC Datamart

# Storm track data generated from the Regional Deterministic Prediction System

The Storm track product is an automated system that detects, identifies, tracks and characterizes low-pressure systems based on the outputs of numerical weather prediction models (deterministic and ensemble) or reanalyses.  It makes it possible to produce maps and animations describing the evolution of extratropical and tropical cyclones throughout their lifetime.

Once determined at each forecast of the model, the storm centres are linked together using the method developed by [Mark R. Sinclair](https://journals.ametsoc.org/view/journals/wefo/12/3/1520-0434_1997_012_0595_oiocat_2_0_co_2.xml), which seeks the best possible extension of a trajectory, taking into account the previous position, the speed of movement, the direction of movement and temporal continuity. Only systems with a lifespan of at least 24 hours are retained as valid storms.

## Data location 

MSC Datamart data can be [automatically retrieved with the Advanced Message Queuing Protocol (AMQP)](../../msc-datamart/amqp_en.md) as soon as they become available. An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is also available.

The data is available using the HTTPS protocol and resides in a directory that is plainly accessible to a web browser. Visiting that directory with an interactive browser will yield a raw listing of links, each link being a downloadable GeoJSON file.

The data can be accessed at the following adress : 

* [https://dd.weather.gc.ca/today/model_rdps/storm-tracks/{HH}/](https://dd.weather.gc.ca/today/model_rdps/storm-tracks)

where :

* __HH__: Model run start, in UTC [00, 06, 12, 18]

## Technical specifications

The following information is available for each storm centre:

* A marker indicating the position of the center
* A line connecting the successive positions of the center
* The position of the centre
* Date and time (UTC)
* The duration of the storm
* Pressure, vorticity, and circulation values
* For tropical cyclones only: the values of low-level baroclinicity (600-900 mb), low-level (600-900 mb) and high-level (300-600 mb) thermal wind structure, maximum vorticity at 850 mb, maximum thickness 250-850 mb, and maximum surface wind

#### Extra-tropical cyclones

Extra-tropical cyclones are tracked base on either their minimum central mean sea level pressure (MSLP) or on their maximum values of gradient wind vorticity.

For vorticity based tracking, cyclones (i.e. vorticity maxima) must reach a given threshold value (at 1000 mb: +0.75x10-5 s-1, at 500 mb: +1.5x10-5 s-1). Vorticity fields are smoothed using a Cressman filter with a smoothing radius of 800 km to removed (real and ficticious) small scale details and retain only the synoptic scale features.

For pressure based traking, cyclone centers are determined from filtered MSLP fields obtained with a Cressman filter and a smoothing radius of 300 km. However, the minimum central pressure values mapped are the raw MSLP values at the center locations found in the filtered MSLP fields.

In all cases, cyclones must last at least 24h to be considered.

#### Tropical cyclones

The tropical cyclone tracking algorithm uses the same core than the extra-tropical pressure-based tracking algorithm. In order to identify cyclones with tropical characteristics, 4 additional parameters are considered here:

* 850-hPa relative vorticity filtered with a Cressman filter using a 300-km radius
* 250-850 hPa thickness
* Surface (10 m) wind speed
* Low level baroclinicity (noted B) measured in terms of asymetry of the 600-900 hPa thickness field. The definition of B employed here follows Sinclair, M. R., 2004: Extratropical Transition of Southwest Pacific Tropical Cyclones. Part II: Midlatitude Circulation Characterisitcs, Mon. Wea. Rev., 132, p. 2149.

To be defined as a tropical cyclone, a low pressure centre must meet the following 4 criteria:

* Possess a maximum of 850 mb relative vorticity greater than +2,5x10-5 s-1 whitin a radius of 150 km.
* Possess a maximum of 250-850 mb thickness greater than 935 dam whitin a radius of 150 km (indicating a deep warm core structure).
* Generates a surface (10 m) wind speed greater than 22 knots within a radius of 225 km.
* Evolve in a barotropic or weakly baroclinic environment, defined here by a value of B lower than 25 m.

A track is started only when all the above criteria are met. When a cyclone not longer meets all the (4) criteria, it is classified as a post-tropical cyclone. The cyclone will be tagged as "Extratropical" if evoling in a baroclinic environment (B > 25m) or as "Remnant" if still in a barotropic environment. Note that a cyclone will still be tagged as being extratropical even if the value of B decreases later below 25 m (e.g. due to an occlusion of the cyclone).

## Filename nomenclature 

The files have the following nomenclature :

* Tropical cyclones: `{YYYYMMDD}T{HH}Z_MSC_RDPS-StormTracks_TropicalCyclone_PT{hhh}H.json`
* Extra-tropical cyclones:
    * `{YYYYMMDD}T{HH}Z_MSC_RDPS-StormTracks_GradientWindVorticity-IsbL-0500_PT{hhh}H.json`
    * `{YYYYMMDD}T{HH}Z_MSC_RDPS-StormTracks_GradientWindVorticity-IsbL-1000_PT{hhh}H.json`
    * `{YYYYMMDD}T{HH}Z_MSC_RDPS-StormTracks_Pressure-MSL_PT{hhh}H.json`

where:

* __YYYYMMDD__ : Year, month and day of the beginning of the forecast
* __T__: Time delimiter according to ISO8601 norms
* __HH__ : UTC run time [00, 06, 12, 18]
* __Z__: Time zone (UTC hour)
* __MSC__: Constant string indicating that the data is from the Meteorologcal Service of Canada (MSC)
* __RDPS-StormTracks__: Constant string indicating that data is from Regional Deterministic Prediction System (RDPS) forecasts of storm tracks
* __TropicalCyclone__: A constant string of characters indicating predictions of tropical cyclone tracks
* __GradientWindVorticity-IsbL-0500__: Constant string indicating predictions of storm tracks detected by their wind vorticity gradient at 500 mb
* __GradientWindVorticity-IsbL-1000__: A constant string of characters indicating predictions of storm tracks detected by their wind vorticity gradient at 1000 mb
* __Pressure-MSL__: Constant string of characters indicating forecasts of storm tracks detected by their mean sea level pressure
* __PT{hhh}H__: Forecast hours based on [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) norms. P, T and H are constant character designating Period, Time and Hour. "HHH" represents the hour at which the storm track is forecasted
* __json__ : constant string indicating the GeoJSON format

Filenames examples: 

* 20251016T12Z_MSC_RDPS-StormTracks_TropicalCyclone_PT048H.json
* 20251012T12Z_MSC_RDPS-StormTracks_GradientWindVorticity-IsbL-0500_PT024H.json

## Support

If you have any questions about this data, please [contact us](https://weather.gc.ca/mainmenu/contact_us_e.html).

## Announcements from the dd_info mailing list 

Announcements related to this dataset are available in the [dd_info list](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/).




