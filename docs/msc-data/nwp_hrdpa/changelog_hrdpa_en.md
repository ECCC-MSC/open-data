[En français](changelog_hrdpa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPA](readme_hrdpa_en.md) > HRDPA Changelog

# Chronology of changes to the High Resolution Deterministic Precipitation Analysis system (CaPA-HRDPA)

## Wednesday September 11, 2024

### Temporary removal of the Fire Weather network observations (OMNRF) from the Regional Deterministic Precipitation Analysis System (HRDPA) assimilation at the Canadian Meteorological Centre (CMC)

Starting on September 11, 2024, Fire Weather network observations from the Ontario Ministry of Natural Resources and Forestry (OMNRF) have been temporarily removed from the set of observations assimilated into the High Resolution Deterministic Precipitation Analysis (HRDPA). This update is effective at 06UTC for the final and at 12UTC for the preliminary analyses.

This update was required to prevent the influence of some erroneous observations from the OMNRF network on the final HRDPA analysis over certain regions in Southern Ontario – particularly in the Kingston-Ottawa and Huron-Erie regions. This has a minor impact on system performance, since in most cases, the gaps are properly filled by observations from the other networks, particularly the synoptic gauges, as well as the radar and satellite QPEs.

An investigation is in progress to identify the problematic stations and exclude them from the HRDPA analysis once the network is reinstated. The issue appears to mostly stem from false zero observations reported by certain gauges in the OMNRF network.

## Tuesday June 11, 2024

### Upgrade to Version 6.0.0 of the High Resolution Deterministic Precipitation Analysis (HRDPA) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the High Resolution Deterministic Precipitation Analysis (HRDPA) to v6.0.0.

Significant changes:

* Addition of 86 additional stations from partner network Saskatchewan Fire Weather Network (SKForestry) to improve analyses for this province.
* Assimilation of dual-polarized radar data for 32 Canadian S-band radars (DPQPE) and 65 US NEXRAD radars (DAA). Addition of 3 US radars.
* These changes lead to a significant improvement in skill scores for a majority of precipitation thresholds.

The official note announcing this implementation is available [at this link](https://dd.meteo.gc.ca/doc/genots/2024/06/10/NOCN03_CWAO_101857___46443).

The technical specifications document for HRDPA 6.0.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_HRDPA_6.0.0_e.pdf).

## Wednesday May 3, 2023

### HRDPA update following the replacement of GOES-17 by GOES-18

Since January 4, 2023 at 18Z, the GOES-18 satellite has taken over from GOES-17 as the operational western satellite. Within the operational HRDPA system, GOES satellite observations are used to perform some of the post-processing of radar precipitation estimates. In particular, GOES data are used to create a cloud mask to clean up the radar data.

Since the GOES-17 satellite disappeared on January 4, the HRDPA system has relied on the NT field of the HRDPS forecast model to build the cloud mask. This contingency solution allowed post-processing of the radar precipitation estimates, but with less reliability than with GOES data.

To further optimize the post-processing of the radar precipitation estimates, HRDPA was updated on May 3, 2023 to assimilate GOES-18 data in addition to the already assimilated GOES-16 data.

## Tuesday June 28, 2022

### Upgrade to Version 5.2.0 of the HRDPA adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to version 5.1.0 of the High Resolution Deterministic Precipitation Analysis System (CaPA-HRDPA) at the Canadian Meteorological Centre (CMC)

On Wednesday, December 1st, 2021, the Canadian Meteorological Centre (CMC) will upgrade its High Resolution Deterministic Precipitation Analysis system (CaPA-HRDPA (2.5km)) to version 5.1.0.

The changes included in this upgrade are summarized as follows :

* [HRDPS v6.0.0](../nwp_hrdps/changelog_hrdps_en.md) now provides the trial field instead of HRDPS v5.2.0
    * The 00-06h forecasts from HRDPS v6.0.0 are used in the creation of the trial field 
* Addition of 29 new American radars and the replacement of 19 Canadian C-band radars by S-band radars
* Assimilation of observations from three new partner surface station networks
* Updates to the static quality control masks for 8 radars
* Use of the cloud fields derived from GOES 16/17 satellites for the filtering of radar derived QPE

The official note announcing this implementation is available [at this location](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

A technical note with more details on these changes is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_hrdpa-510_e.pdf).

The technical specifications document for HRDPA v5.1.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_HRDPA_5.1.0_e.pdf).

## Tuesday January 21, 2020

### Upgrade to Version 4.7.0 of the CaPA-HRDPA adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to version 4.6.0 of the High Resolution Deterministic Precipitation Analysis system (CaPA-HRDPA) at the Canadian Meteorological Centre (CMC)

On Wednesday July 3rd 2019, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada (MSC) will upgrade the High Resolution Deterministic Precipication Analysis system (CaPA-HRDPA (2.5km)) to version 4.6.0.

Changes are summarized as follows:

* [HRDPS v5.1.0](../nwp_hrdps/changelog_hrdps_en.md) now provides the trial field instead of HRDPS v5.0.0.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2019/07/03/NOCN03_CWAO_031240___43184).


## Tuesday September 18, 2018

### Upgrade to version 4.5.0 of the High Resolution Deterministic Precipitation Analysis System (CaPA-HRDPA) at the Canadian Meteorological Centre (CMC)

On Tuesday, September 18, 2018, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will upgrade its Regional Deterministic Precipitation Analysis system (CaPA-HRDPA (2.5km)) to version 4.5.0.

The changes included in this upgrade are summarized as follows:

* The trial fields for these precipitaion analyses are generated from the new version of the system implemented on September 18, 2018:
    * CaPA-HRDPA now builds its trial fields from [HRDPS v5.0.0](../nwp_hrdps/changelog_hrdps_en.md)
* Assimilation of the observations from the CoCoRaHS network. (CaPA-HRDPA)
* New 24h analysis valid at 06h00 UTC in line with the climatological day. (CaPA-HRDPA)

A copy of the official note announcing this implementation is available at this location:

* [CaPA-HRDPA official announcement](http://dd.meteo.gc.ca/doc/genots/2018/09/17/NOCN03_CWAO_171416___54417)

Technical note with more details on these changes is available at this link:

* [CaPA-HRDPA technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_capa_hrdpa-450_e.pdf)


## Friday March 2, 2018

### Implementation of the High Resolution Deterministic Precipitation Analysis System (CaPA-HRDPA Version 4.1.0) at the Canadian Meteorological Centre (CMC)

On Friday, March 2nd 2018, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the Regional Deterministic Precipitation Analysis System by adding a new configuration of higher resolution analyses (CaPA-HRDPA). These new analyses at 2.5km horizontal resolution are in addition to those analyses already produced in operational mode at 15km resolution since 2011, and at 10km resolution since October 2012.

A copy of the official note announcing the implementation of these changes [is available at this link](http://dd.meteo.gc.ca/doc/genots/2018/03/02/NOCN03_CWAO_022008___00002).

A technical note with more details on this change [is available at this link](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/CAPA-HRDPA_4_1_0_Tech_note_e.pdf).



