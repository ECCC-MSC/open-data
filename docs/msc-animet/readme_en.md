# TODO

* French translation (Félix)
* create and add usage examples with the latest version of AniMet (Alex)

# BEGINNING OF NEW DOC

[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC AniMet

# MSC AniMet

MSC AniMet is a simple tool enabling users to interact with MSC Open Data weather data and create custom weather animations for any area in the world. The resulting animations can be downloaded and shared with a permalink. 

MSC AniMet can be used to showcase a diversity of weather events such as storms, heat waves, hurricane trajectories, air quality events, extreme wind gusts, and much more.

In its current incarnation, MSC AniMet provides access to [GeoMet-Weather](../msc-geomet/readme_en.md) layers.

# Access

**Access to MSC AniMet: [https://eccc-msc.github.io/msc-animet/](https://eccc-msc.github.io/msc-animet/)**

# Usage

The main usage workflow: 

1. Add weather layers to the map
2. Customize the content of the map
3. Configure the animation
4. Create and share the map and animation

## 1 - Add weather layers

Add layers in the `Add GeoMet-Weather layers` panel:

* Browse the layer tree to find the desired layer
* Use the search box to filter available layers
* Click on the `+` sign to add a layer to the map

Tip: click on the panel name, `Add GeoMet-Weather layers`, to expand or collapse the panel.

## 2 - Customize content of the map

Configure layers in the `Layers configuration` panel and customize the map.

Layers:

* Reorder layers with the up and down arrows
  * Arrows are shown only if there multiple layers have been added
* Change layer colors
  * View and select the layer color ramp from available styles
* Adjust layer opacity
* Toggle layer visibility

Time:

* The map controls at the bottom left of the map enable users to visualize the available timesteps
* The current timestep and dataset model run (when applicable) are displayed at the bottom right of the map
* The desired temporal range and interval can be adjusted at the top of the 'Layers configuration' panel
* The temporal range and interval can be reset to match a specific layer by clicking on the clock icon next to the layer name

Map:

* Zoom and pan the map to your area of interest
* Resize the map with the handle at the bottom right of the map
* Rotate the map by pressing alt-shift and dragging on the map

## 3 - Configure the animation

Configure the animation in the `Animation configuration` panel:

* Provide a custom animation title, if desired
* Select which legend to display
* Set animation speed in frames per second
* Toogle time display between local time and UTC
* Toggle basemap between the light and dark basemaps

## 4 - Create and share the map and animation

After clicking on the `Create animation` button and the generation process completes, the `Download animation` button will appear.

Retrieve and share the permalink with the `Share` button at the top-right:

* You can copy and save the permalink for later use
* Directly share the permalink by email or on social media services
  * To share the animation on social media, the file must first be saved locally

The [permalink](https://en.wikipedia.org/wiki/Permalink) allows you to open MSC AniMet with a determined set of layers and their configuration, as well as a specific map zoom, extent and size. The temporal dimensions are not included in the permalink due to the evolving nature and availability of archived data.

# Additional information

## Announcement mailing list

MSC AniMet leverages data from the 24/7 mission critical [MSC GeoMet web services](../msc-geomet/readme_en.md). We encourage users to subscribe to the [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement mailing list to be informed of enhancements and changes to MSC AniMet.

## Source code

The MSC AniMet source code is publicly available on GitHub: [https://github.com/ECCC-MSC/msc-animet](https://github.com/ECCC-MSC/msc-animet)

## Support

MSC AniMet is a MSC Open Data demonstration tool and is not operationally supported. User support is provided on a best effort basis during normal business hours. Users requesting support are invited to [contact us](https://www.weather.gc.ca/mainmenu/contact_us_e.html).
