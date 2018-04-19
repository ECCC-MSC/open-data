# DPS content currently published on Canada.ca

# MSC GeoMet

MSC GeoMet page:
* URL: https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data/geospatial-web-services.html
 
## MSC GeoMet 2 switchover documentation update

Objectives:
* Update Canada.ca's MSC GeoMet documentation to correspond to MSC GeoMet 2 documentation
* Lots of information in the GeoMet-1 version of the page is not valid for GeoMet 2

When: 
* The replacement of GeoMet-1 with GeoMet-2 is planned to happen on April 25, 10h30 EST, 2018

Local copies of content:
 * [GeoMet-1_en](geomet-1_en.md)
 * [GeoMet-1_fr](geomet-1_fr.md)
 * [GeoMet-2_en](geomet-2_en.md)
 * [GeoMet-2_fr](geomet-2_fr.md)

Main changes from GeoMet-1 to GeoMet-2 versions:
* updated a few locations to indicate it's for MSC open data, not just NWP and radar like GeoMet-1 was
* updated intro to focus on WMS, removed KML
* added mobile app in intro
* removed mention of the upcoming migration to GeoMet 2 in intro
* completely removed the "Keyhole Markup Language (KML)" subsection given this feature has been deprecated
* removed or updated the FAQ subsections that refer to the deprecated KML capability
* removed the FAQ subsection about contours, which is not true anymore thanks to the support of the SLD standard in GeoMet 2
* removed the FAQ subsection about the color schemes, which was misleading given there's multiple WMS styles available, plus not true anymore with GeoMet-2's SLD support
* fixed typo in MSC tooltip from 'Meteorological Services of Canada' to 'Meteorological Service of Canada'
* renamed most occurrences of GeoMet to MSC GeoMet
* updated EC to ECCC references

Notes regarding the new page:
* this documentation voluntarily don't mention WCS and WFS at this point
* this doc doesn't mention GeoMet-2's REFERENCE TIME support to access previous NWP model runs, we keep such detailed info for the renewed full-fledge doc
* the doc doesn't mention GeoMet-Beta either, users will be informed about GeoMet-Beta in the GeoMet-Info list