[En français](readme_lightning_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > Lightning

# Lightning density data

The [Canadian Lightning Detection Network](https://www.canada.ca/en/environment-climate-change/services/lightning/canadian-detection-network.html) provides lightning monitoring across most of Canada. The data distributed here represents a spatio-temporal aggregation of the observations of this network available with an accuracy of a few hundred meters. More precisely, every 10 minutes, the reported observations are processed in the following way:

* The location of observed lightning (cloud-to-ground and intra-cloud) in the last 10 minutes is extracted.
* Using a regular horizontal grid of about 2.5km by 2.5km, the number of observed lightning flashes within each grid cell is calculated.
* These grid data are normalized by the exact area of each cell (in km2) and by the accumulation period (10min) to obtain an observed flash density expressed in km-2 and min-1
* A mask is applied to remove data located more than 250km from Canadian land or sea borders.

## Access

### How to access the data

This data is available on the [MSC Datamart](../../msc-datamart/readme_en.md) data server services as well as [MSC GeoMet](../../msc-geomet/readme_en.md):

* [GeoTIFF data available on HPFX, the alternative server of the MSC Datamart](readme_lightning-datamart_en.md) 
cd
An [overview and examples to access and use the Meteorological Service of Canada's open data](../../usage/readme_en.md) is available.

### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use for this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.

### Metadata

The [metadata of the Lightning Density Data is available on the Open Government Portal](https://open.canada.ca/data/en/dataset/75dfb8cb-9efc-4c15-bcb5-7562f89517ce).

## Technical documentation

[Lightning: Lightning danger map, safety, statistics, science, frequently asked questions](https://www.canada.ca/en/environment-climate-change/services/lightning.html)