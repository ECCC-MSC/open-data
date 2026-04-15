[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC AniMet

# MSC AniMet

MSC AniMet is a simple tool enabling users to interact with MSC Open Data weather, climate, water and environmental data and create custom weather animations for any area in the world. The resulting animations can be downloaded and shared with a permalink.

MSC AniMet can be used to showcase a diversity of weather events such as storms, heat waves, hurricane trajectories, air quality events, extreme wind gusts, and much more. Users can visualize, combine and animate over 17 550 layers.

MSC AniMet provides access to [GeoMet-Weather and GeoMet-Climate](../msc-geomet/readme_en.md) layers.

# Access

**Access to MSC AniMet: [https://eccc-msc.github.io/msc-animet/](https://eccc-msc.github.io/msc-animet/)**

A simple example of an MSC AniMet animation showing the significant precipitation type, sea level pressure, and thickness between 1000mb and 500mb. This is a [winter weather preset](https://eccc-msc.github.io/msc-animet/?layers=RDPS_10km_PrecipType-Significant1h;0.75;1;1;PRECIPNW;1,RDPS_10km_Pressure_MSL-Contour;0.5;0;1;SeaLevelPressure_4mb;0,RDPS_10km_Thickness-Contour_1000to500mb;0.5;0;1;0;0&extent=-23847063,1369205,1166371,12922284&overlays=Boundaries&range=83,4,l,PT1H).

<video controls width="85%">
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/MSC-AniMet_Precipitation_type_en.mp4" type="video/mp4">
</video>
<br>



#  Usage workflow

The main usage workflow:

1. Add weather and climate layers to the map.
2. Customize the content of the map.
3. Configure the animation.
4. Create and share the map and animation.

## 1 - Add weather and climate layers

#### <span class="badge badge-info">1.1 - Presets</span>
Presets are groups of commonly used layers that users can add to the map such as currents conditions, classic synoptic, remote sensing, winter/summer weather and air quality. They are used to quickly set up common meteorological analysis views. When presets are selected, layers are automatically added.

![Presets](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Presets_en.jpg)



#### <span class="badge badge-info">1.2 - Available layers</span>

Users can choose a layer by typing a variable, a system, a level or by browsing though all available layers in the layer tree. Refer to the [list of available datasets](../msc-data/readme_en.md) for additional information on MSC Open Data offerings.

![Layer tree](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Layer_Tree_en.jpg)


* Additional data sources may be added via the `+` button. Access additional third-party WMS services, including those from **ECMWF**, **NASA**, **NOAA-nowCOAST**, **NOAA-NCEP**, and Quebec’s Ministry of Energy and Natural Resources CartoService.

![Data source](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Additionnal_Data_Source_en.jpg)



#### <span class="badge badge-info">1.3 - User's own vector datasets</span>

 MSC AniMet now supports adding your own `GeoJSON`, `TopoJSON`, `GPX`, `IGX`, and `KML` datasets to the map. Simply drag and drop your datasets onto the map to see them alongside your favourite layers. There's a default style assigned to a user's own dataset, it's not possible to change the style.


---------------------

## 2 - Customize content of the map

Users can configure and customize existing layers on the map in the `CONFIGURE` panel.

##### <span class="badge badge-info">2.1 - Customizing a layer style and legend</span>

* `Select model run`: When available, change layer's corresponding model run by clicking on the date.
* Reorder layers with the up and down arrows.
    * Arrows are shown only if multiple layers have been added.
* `Temporal`: Hovering over a layer's clock (🕓 icon) provides the temporal dimensions: the current timestep, model run range and interval. The temporal range and interval can be reset to match a specific layer by clicking on the clock.
* `Opacity` : Adjust layer opacity from 0-100%
* `Toggle visibility`: hide or show layer.
    * A layer's visibility eye icon will turn red if the current map time is outside of the layer's temporal range.
* `Select layer style` : To change layer colors, click on the palette icon.
    * View and select the layer color ramp from available styles.
    * Select which legends to display via the `Display legend` check box. Legends can be resized and moved on the map and these changes will be reflected in the outputted animation.
* `Interpolation`: To show interpolation for supported GeoMet-Weather layers, enabling smoother visuals and a less pixelated look via on-the-fly upscaling and resampling of source data. To enable interpolation click on the layer's ✨ icon in the layer configuration panel.


<video width="800" controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Customize_Layer_Legend_Style_en.mp4" type="video/mp4">
</video>
</br>
</br>

#### <span class="badge badge-info">2.2 - Using the time controller</span>

* The current time displayed on the map is displayed above the temporal controller.
* The start and end of the animation can be modified via the sliders on the left and right of the temporal controller.
* Playback controls allow for playing, stopping, and moving between time steps.
    * Playback options are located above the play/pause button and allow the user to loop the animation continuously or play the animation in reverse.
    * The temporal extent of added layers are updated and the temporal bounds of the map maybe updated as previous timesteps are no longer available.
* The orange dot on the playback bar shows the current displayed timestep in relation to the defined temporal extent.
* The orange notch is the time indicator. It displays the current time in relation to the current data layers displayed on the map.
* The timestep interval can be selected via the dropdown menu to the right of the temporal controller.
* Click on ⏮️⏭️ to move to the first/last timestep and ⏪⏩ to step to the next or previous timestep.
* Choose whether to display the time in the user's local time (determined via the browser) or in UTC via the `Local time` switch.
* Via the chevron located next to the `UTC/Local` switch, users can select a specific timezone for the map. Users can revert to their system's time zone via the blue revert arrow in the timezone dropdown menu.
* The playback speed of the animation can now be modified via the temporal controller to adjust the number of images per second shown when animating via the temporal controller. The default playback is 4 images per second and can be increased to 10 images per second for a smoother animation. To modify animation playback speed, use the ⚙️ icon in the temporal controller.


![Time controller](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Time_Controller_Button_en.png)


**This is an example on how to use the time controller settings.** </br>

<video width="800" controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Time_Controller_Tuto_en.mp4" type="video/mp4">
</video>


</br>

#### <span class="badge badge-info">2.3 - Customize the basemap and overlays</span>
On the top corner, click on `Customize map` (🌎 icon) to modify the basemap and overlays.</br>

* Select a projection
    * `3857` Web Mercator
    * `3978` Lambert Conic Conformal
    * `3995` Arctic Polar Stereographic
    * `4326` WGS84 (lat/lon)
* Add graticules.
* Select OpenStreetMap basemaps, boundary outlines/background color.
* Add overlays (city names, topographic baseline and other).
* Zoom and pan the map to your area of interest.
* Resize the map and the animation with the `+/-` handle at the bottom right corner of the map.
* Rotate the map by pressing the `Alt-Shift` keys and dragging on the map.


![Basemap](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Basemap_en.jpg)


#### <span class="badge badge-info">2.4 - Using the markup tools</span>

Users can also highlight or annotate their map with textboxes and shapes. Simply `right-click` on the map and select a markup option. All added markups are preserved in the resulting animation.

* To delete the annotation, `right-click` on it and press the `Delete/Del` key.
* To move the shape, hold `right-click` while dragging over the map.

![Markup tools](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Markup_Tools_en.jpg)

<video width="700" controls>
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Annotations_en.mp4" type="video/mp4">
</video>

</br>


#### <span class="badge badge-info">2.5 - Display data properties</span>

User can click anywhere on the interactive map to display the raw values and shows full properties at points. If multiple layers are superposed, all available data will be displayed in the popups. Click on the coordinates on top of the popup box to change how they are displayed.


![Data properties](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Data_Properties_en.jpg)




---------------------

## 3 - Configure the animation

Configure the animation in the `EXPORT` panel:

* Provide a custom animation title, if desired.
* Set animation speed in frames per second.
* Add colored borders to legends (matching the dots next to layer labels in the final animation).
* The red outline shows what will be included in the animation output and the white elements show the space used by the animation header, footer and wall clock.
    * A warning message will be displayed if displayed legends are not entirely contained within the area of the animation output.
* Various aspect ratios can be selected for the animation output to match the user's needs and allow for easy sharing on social media platforms.
* Preview the created animation before downloading it.


![Configure animation](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/Configure_Animation_en.jpg)


---------------------


## 4 - Create and share the map and animation

After clicking on the `Create animation` button and the generation process is completed, the `Download` button will appear.

Retrieve and share the permalink with the share `➦` button at the top-right:

* You can copy and save the permalink for later use.
* Directly share the permalink by email or on social media services.
    * To share the animation on social media, the file must first be saved locally.

The [permalink](https://en.wikipedia.org/wiki/Permalink) allows you to open MSC AniMet with a determined set of layers and their configuration, as well as a specific map zoom, extent and size. The temporal dimensions are not included in the permalink due to the evolving nature and availability of archived data.

# Additional information

#### *Announcement mailing list*

MSC AniMet leverages data from the 24/7 mission critical [MSC GeoMet web services](../msc-geomet/readme_en.md). We encourage users to subscribe to the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement mailing list to be informed of enhancements and changes to MSC AniMet.


#### *Demonstration video*

A [demonstration video showcasing MSC AniMet](https://vimeo.com/1093850245?share=copy#t=2058.364) features is available on Vimeo. This is a demonstration of a previous version of AniMet (June 2025).

#### *Source code*

The MSC AniMet source code is publicly available on GitHub: [https://github.com/ECCC-MSC/msc-animet](https://github.com/ECCC-MSC/msc-animet)

## Support

MSC AniMet is a MSC Open Data demonstration tool. User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).
