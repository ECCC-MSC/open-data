[[En Français](readme_grib_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [MSC Data](readme_en.md) > GRIB

# Use of GRIB2 data format

## On the GRIB format

GRIB is a file format for the storage and transport of gridded meteorological data, such as Numerical Weather Prediction model output. It is designed to be self-describing, compact and portable across computer architectures. The [GRIB standard](https://www.wmo.int/pages/prog/www/WDM/Guides/Guide-binary-2.html) was designed and is maintained by the World Meteorological Organization (WMO).

GRIB data is used by individuals, institutions and businesses who have the means and motivation to tap into numerical data from weather models in the rawest possible form. GRIB data is often only one step removed from the original model output. Once decoded, the data can be post-processed for visualization, or used as input for numerical weather prediction applications that require gridded data.

The [GRIB2](https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/) format represents an enlarging and a significant modernization of the GRIB standard. It is being phased in by the ECMWF and some national Numerical Weather Prediction institutions, notably in the US and Europe. A significant modernization and broadening of the GRIB standard, Edition 2 is not backward-compatible with Edition 1.

Before 2010, the Canadian Meteorological Centre was offering it's data only in GRIB1 format. Since 2011, the CMC aims to distribute only in GRIB2 format.

A GRIB2 file contains one or more data records, arranged as a sequential bit stream. Each record begins with a header, followed by packed binary data. The header is composed of unsigned 8-bit numbers (octets). It contains information about:

* The qualitative nature of the data (field, level, date of production, forecast valid time, etc)
* The header itself (meta-information on header length, header byte usage, presence of optional sub-headers)
* The method and parameters to be used to decode the packed data
* The layout and geographical characteristics of the grid the data is to be plotted on

## Software supporting the GRIB2 format

The Meteorological Service of Canada does not distribute publicly any decoding or visualization software for the GRIB2 format. Here is a non exhaustive list of links to find software to manipulate and display GRIB data:

Decoding and processing:
* [wgrib2](https://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/)
** [Tricks for wgrib2](https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/tricks.wgrib2)
* [GDAL](https://gdal.org/drivers/raster/grib.html)
    
Visualization and interpolation:
* [INGRIDDS](http://winweather.org/)
* [OpenGRADS Bundle pour GRIB2](http://opengrads.org/doc/bundle/grads/)
* [GEMPAK](https://www.unidata.ucar.edu/software/gempak/)
* [NCAR NCL](http://ngwww.ucar.edu/ncl/)