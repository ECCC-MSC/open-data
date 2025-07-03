[En français](readme_rdsps_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > RDSPS

# Data and Products of the Regional Deterministic Storm Surge Prediction System (RDSPS)

The Regional Deterministic storm Surge Prediction System (RDSPS) produces storm surge forecasts using the DalCoast ocean model. DalCoast (Bernier and Thompson 2015) is a storm surge forecast system for the east coast of Canada based on the depth-integrated, barotropic and linearized form of the Princeton Ocean Model. The model is forced by the 10 meters winds and sea level pressure from the [Global Deterministic Prediction System (GDPS)](../nwp_gdps/readme_gdps_en.md).

During the post processing phase tidal heights are predicted using Webtide (Dupont et al., 2002). The tidal heights (SSHT) from Webtide and surge forecast (ETAS) from Dalcoast are summed to obtain an estimate of the total water level (SSH).

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server service:

* [NetCDF data available on the MSC Datamart](readme_rdsps-datamart_en.md)

An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Discovery metadata

Upcoming.

## Technical documentation

* [Current version of the Regional Deterministic Storm Surge Prediction System](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_RDSPS_e.pdf)
* [Technical Note](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_rdsps_e.pdf)

## Changelog

The chronology of changes to the Regional Deterministic Storm Surge Prediction System (RDSPS) is available [here](changelog_rdsps_en.md).
