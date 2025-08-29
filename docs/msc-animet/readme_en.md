[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC AniMet

# MSC AniMet

MSC AniMet is a simple tool enabling users to interact with MSC Open Data weather, climate, water and environmental data and create custom weather animations for any area in the world. The resulting animations can be downloaded and shared with a permalink.

MSC AniMet can be used to showcase a diversity of weather events such as storms, heat waves, hurricane trajectories, air quality events, extreme wind gusts, and much more.

MSC AniMet provides access to [GeoMet-Weather and GeoMet-Climate](../msc-geomet/readme_en.md) layers.

# Access

**Access to MSC AniMet: [https://eccc-msc.github.io/msc-animet/](https://eccc-msc.github.io/msc-animet/)**

A simple example of an MSC AniMet animation showing thunderstorms at dusk, with GOES satellite imagery and radar layers:

<video controls width="66%">
  <source src="https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-animet/MSC-AniMet_20240522T2230Z_Thunderstorms_2024-05-22.mp4" type="video/mp4">
</video>
<br>


# Usage

The main usage workflow:

1. Add weather and climate layers to the map
2. Customize the content of the map
3. Configure the animation
4. Create and share the map and animation

## 1 - Add weather and climate layers

Layers:

* Add layers from the `GeoMet-Weather` or `GeoMet-Climate` panel. Additional data sources may be added via the `+` button.
* Browse the layer tree to find the desired layer
* Use the search box to filter available layers
* Click on the `+` sign to add a layer to the map

Overlays:

* Select the 'Overlays' panel to add information on top of displayed layers
* Currently available overlays are Canadian geopolitical boundaries, cities and waterbodies from Natural Resource Canada. They are available only at certain zoom levels

## 2 - Customize content of the map

Configure layers in the `Layers configuration` panel and customize the map.

Layers:

* When available, change layer's corresponding model run
* Reorder layers with the up and down arrows
  * Arrows are shown only if multiple layers have been added
* Change layer colors
    * View and select the layer color ramp from available styles
* Adjust layer opacity
* Toggle layer visibility
    * A layer's visibility eye icon will turn red if the current map time is outside of the layer's temporal range

Time:

* The current time displayed on the map is displayed above the temporal controller
* The start and end of the animation can be modified via the sliders on the left and right of the temporal controller
* Playback controls allow for playing, stopping, and moving between time steps
    * Playback options are located above the play/pause button and allow the user to loop the animation continuously or play the animation in reverse
    * The temporal extent of added layers are updated and the temporal bounds of the map maybe updated as previous timesteps are no longer available
* The orange dot on the playback bar shows the current displayed timestep in relation to the defined temporal extent
* The timestep interval can be selected via the dropdown menu to the right of the temporal controller
* Choose whether to display the time in the user's local time (determined via the browser) or in UTC via the `Local time` switch
* Via the chevron located next to the UTC/local switch, users can select a specific timezone for the map. Users can revert to their system's time zone via the blue revert arrow in the timezone dropdown menu
* The temporal range and interval can be reset to match a specific layer by clicking on the clock icon next to the layer name in the Layers configuration panel
* Hovering over a layer's clock icon provides the temporal dimensions: the current timestep, model run range and interval

Map:

* Zoom and pan the map to your area of interest
* Resize the map and the animation with the handle at the bottom right corner of the map
* Rotate the map by pressing the _alt-shift_ keys and dragging on the map.
* Select which legends to display via the `LEGENDS` overlay button. Legends can be resized and moved on the map and these changes will be reflected in the outputted animation
* The globe icon at the top of the map allows users to switch between map projections, show map graticules and alter the colour of the basemap

## 3 - Configure the animation

Configure the animation in the `Animation configuration` panel:

* Provide a custom animation title, if desired
* Set animation speed in frames per second
* Toggle basemap between the light and dark basemaps
* The red outline shows what will be included in the animation output and the white elements show the space used by the animation header, footer and wall clock
    * A warning message will be displayed if displayed legends are not entirely contained within the area of the animation output
* Various aspect ratios can be selected for the animation output to match the user's needs and allow for easy sharing on social media platforms

## 4 - Create and share the map and animation

After clicking on the `Create animation` button and the generation process is completed, the `Download animation` button will appear.

Retrieve and share the permalink with the `Share` button at the top-right:

* You can copy and save the permalink for later use
* Directly share the permalink by email or on social media services
    * To share the animation on social media, the file must first be saved locally

The [permalink](https://en.wikipedia.org/wiki/Permalink) allows you to open MSC AniMet with a determined set of layers and their configuration, as well as a specific map zoom, extent and size. The temporal dimensions are not included in the permalink due to the evolving nature and availability of archived data.

# Additional information

## Announcement mailing list

MSC AniMet leverages data from the 24/7 mission critical [MSC GeoMet web services](../msc-geomet/readme_en.md). We encourage users to subscribe to the [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement mailing list to be informed of enhancements and changes to MSC AniMet.

## Demonstration video

A demonstration video showcasing MSC AniMet features is available on Vimeo: [https://vimeo.com/1093850245?share=copy#t=2058.364](https://vimeo.com/1093850245?share=copy#t=2058.364)

## Source code

The MSC AniMet source code is publicly available on GitHub: [https://github.com/ECCC-MSC/msc-animet](https://github.com/ECCC-MSC/msc-animet)

## Support

MSC AniMet is a MSC Open Data demonstration tool. User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).
