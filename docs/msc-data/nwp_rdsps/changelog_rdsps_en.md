[En français](changelog_rdsps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [RDSPS](readme_rdsps_en.md) > RDSPS Changelog

# Chronology of changes to the Regional Deterministic Storm-surge Prediction System (RDSPS)

## Wednesday December 1st, 2021

### Replacement of the Regional Deterministic Storm-surge Prediction System (RDSPS) at the Canadian Meteorological Centre (CMC)

On Wednesday December 1st, 2021, starting with the 1200 UTC run, the Canadian Meteorological Centre (CMC) will replace the Regional Deterministic Storm-surge Prediction System (RDSPS) by the new Global Deterministic Storm-surge Prediction System (GDSPS) and will upgrade its version to 1.9.0.

Associated Notes:

* [Official note announcing the implementation](http://dd.weather.gc.ca/doc/genots/2021/11/29/NOCN03_CWAO_XXXX).
* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_notes/technote_rdsps-190_e.pdf).
* [Technical specifications of RDSPS 1.9.0](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.9.0_e.pdf).

## Tuesday January 12, 2021

### Upgrade to Version 1.8.0 of the Regional Deterministic Storm-surge Prediction System (RDSPS) at the Canadian Meteorological Centre (CMC)

Addition of a post processing component to provide a prediction of tidal heights using Webtide.

For more information, please consult the technical specifications document for RDSPS v1.8.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.8.0_e.pdf).

## Tuesday January 21, 2020

### Upgrade to Version 1.7.0 of the RDSPS adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md)

## Wednesday July 3, 2019

### Upgrade to Version 1.6.0 of the Regional Deterministic Storm-surge Prediction System (RDSPS) at the Canadian Meteorological Centre (CMC)

Effective Wednesday July 3rd, 2019, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will update the Regional Deterministic Storm-surge Prediction System (RDSPS) to v1.6.0.

The modifications to RDSPS v1.6.0 compared with the previous operational version are as follows:

* [GDPS v7.0.0](/../nwp_gdps/changelog_gdps_en.md) replaces v6.0.0 as the pilot system.
For more information, please consult the technical specifications document for RDSPS v1.6.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.6.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdsps-160_e.pdf).

## Wednesday January 30, 2019

### Upgrade to Version 1.5.0 of the Regional Deterministic Storm-surge Prediction System (RDSPS) at the Canadian Meteorological Centre (CMC)

Effective January 30, 2019, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada will update the Regional Deterministic Storm-surge Prediction System (RDSPS) to v1.5.0.

The modifications to RDSPS v1.5.0 compared with the previous operational version are as follows:

* The mean sea level pressure replaces surface pressure as an input variable.
* The inclusion of a corrective process to "level" the storm surge forecast which is output directly by the model.

For more information, please consult the technical specifications document for RDSPS v1.5.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.5.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdsps-150_e.pdf).

## Wednesday November 1, 2017

### The Regional Deterministic Storm-surge Prediction System (RDSPS) is declared operational at the Canadian Meteorological Centre (CMC)

Effective November 1, 2017, after two years running in experimental mode, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada declared operational the Regional Deterministic Storm-surge Prediction System (RDSPS v1.3.0).

The RDSPS provides storm-surge forecasts along the Atlantic Coast of Canada. Forecasts are launched twice a day at 00 and 12 UTC and integrated out to 10 days. Forecasts are driven with hourly wind and surface pressure fields provided by the Global Deterministic Prediction System (GDPS). RDSPS products are generated on a 1/30 degree resolution latitude-longitude grid from 42N to 60N and 72W to 44W.

The RDSPS was developed in partnership with Dalhousie University and is based on the Dalcoast5 storm surge model.

A scientific article with more details is available [at this link](https://www.sciencedirect.com/science/article/pii/S1463500314001772).

The technical specifications document for RDSPS 1.3.0 is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_1.3.0_e.pdf).
