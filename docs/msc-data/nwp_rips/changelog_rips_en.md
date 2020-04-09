[En français](changelog_rips_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RIPS](readme_rips_en.md) > RIPS Changelog

# Chronology of changes to the  Regional Ice Prediction System (RIPS)

## Thursday September 17, 2015

### The Canadian Meteorological Centre (CMC) installs RIPS version 2.2

On September 17, 2015, CMC implemented version 2.2 of the Regional Ice Prediction System (RIPS). Here is the list of the major changes included in this upgrade:

* Assimilation of AMSR2 data
* Assimilation of Canadian Ice Service regional (weekly) chart data
* Modifications to the passive microwave data processing:
    * Thinning of SSMIS data along the satellite track (assimilate only 1 of 3 scan lines)
    * Reduction of the observation-error standard deviation of SSMIS data from 0.1 to 0.05 (because of thinning)
    * Reject all data over lakes (as in version 1.0)
    * Wind filter to eliminate spurious ice concentration retrievals
A technical note with more details on this change is available [at this link](file:///C:/Users/prisc/docs/msc-data/open-data/docs/msc-data/nwp_reps/changelog_reps_en.md).

## Tuesday July 23 2013

### The Canadian Meteorological Centre (CMC) installs version 2.0 of RIPS-F (forecast component)

On July 23, 2013, the CMC implemented, for the first time, the Forecast Component of the Regional Ice Prediction System (RIPS-F 2.0.0). RIPS-F system is the forecasting component of RIPS 2.0.0 based on the Los-Alamos sea-ice model (CICEv4.1). Each 6h (i.e., 4 times a day), following the analysis production in RIPS-A, RIPS-F generates initial conditions for ice concentration (from the analysis), sea surface temperature (CMC analysis at 00Z), ice velocity (previous forecast) and ice thickness and mixed layer depth (both from GLORYS1v1 climatology). The surface forcing during the 48h forecast comes from the RDPS for the atmoshpere and time-interpolated surface currents (GLORYS1v1 monthly climatology). There are no open boundary conditions for ice considered in this new version.

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_ripsf_20140506_e.pdf).

## Friday May 17, 2013

### The Canadian Meteorological Centre (CMC) upgrades RIPS-A (analysis component) to version 2.0

On May 17, 2013, CMC implemented a new experimental version of the Analysis Component of the Regional Ice Prediction System (RIPS-A 2.0.0). RIPS-A provides near real-time gridded estimates of ice concentration for all ice affected areas around North America and Greenland, and is primarily aimed to satisfy the operational requirements of the Canadian Ice Service. Three major modifications have been considered in this new version:

    1. The first modification is the assimilation of passive microwave data from three satellite platforms to complement the already assimilated Special Sensor Microwave/Imager data from one platform.
    2. The second change is the assimilation of ice concentration information derived from the Advanced Scatterometer data.
    3. The third is the use of an estimate of analysis uncertainty to identify areas where the estimated ice concentration in the analysis is then replaced by spatially interpolated values.

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/lib/technote_ripsa_20140505_e.pdf).