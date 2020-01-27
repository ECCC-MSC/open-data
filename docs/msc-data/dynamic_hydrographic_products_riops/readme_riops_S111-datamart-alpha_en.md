[En français](readme_riops_S111-datamart-alpha_fr.md)

![ECCC logo](../../img_eccc-logo.png)

# S-111 Dynamic Hydrographic Products(DHP) in HDF5 format using RIOPS(Regional Ice Ocean Prediction System) surface currents data. 

The S-111 Dynamic Hydrographic Products(DHP) for oceanographic models currents is in an open standard HDF5 format with a specification provided by the [ International Hydrographic Organisation(IHO) ](https://iho.int). Each S-111 data file is a 1x1 degrees regular bounding box tiled subset of RIOPS surface currents data. The S-111 tiled files are using the EPSG:4326 as its GIS Common Reference System(CRS) to define all geographical coordinates locations.

The data coding format 3 (Ungeorectified gridded data or point set data at one or more times) of the [ IHO S-111 format specification ](http://registry.iho.int/beta/productspec/view.do?idx=168&product_ID=S-111&statusS=5&domainS=ALL&category=product_ID&searchValue=) is used because it allows to directly use RIOPS data, which itself use a a polar stereographic grid, without any interpolation.

S-111 currents are expressed as a Speed(in knots) and a Direction(navigatioal angle) using the HDF5 H5T_COMPOUND data type.