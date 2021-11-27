[En français](changelog_hrdpa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HRDPA](readme_hrdpa_en.md) > HRDPA Changelog

# Chronology of changes to the High Resolution Deterministic Precipitation Analysis system (CaPA-HRDPA)

## Wednesday December 1st, 2021

### Upgrade to version 5.1.0 of the High Resolution Deterministic Precipitation Analysis System (CaPA-HRDPA) at the Canadian Meteorological Centre (CMC)

On Tuesday, December 1st, 2021, the Canadian Meteorological Centre (CMC) will upgrade its High Resolution Deterministic Precipitation Analysis system (CaPA-HRDPA (2.5km)) to version 5.1.0.

The changes included in this upgrade are summarized as follows :

* [HRDPS v6.0.0](../nwp_hrdps/changelog_hrdps_en.md) now provides the trial field instead of HRDPS v5.2.0
    * The 00-06h forecasts from HRDPS v6.0.0 are used in the creation of the trial field 
* Addition of 29 new American radars and the replacement of 19 Canadian C-band radars by S-band radars
* Assimilation of observations from three new partner surface station networks
* Updates to the static quality control masks for 8 radars
* Use of the cloud fields derived from GOES 16/17 satellites for the filtering of radar derived QPE

The official note announcing this implementation is available [at this location](https://dd.meteo.gc.ca/doc/genots/2021/11/29/NOCN03_CWAO_xxxx).

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



