[En français](readme_dcs_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > CanDCS-U6

# Data and products of statistically downscaled climate scenarios datasets based on an ensemble of global climate model projections from the Coupled Model Intercomparison Project Phase 6 (CMIP6)  

ECCC’s Climate Research Division (CRD) and the Pacific Climate Impacts Consortium (PCIC) previously produced statistically downscaled climate scenarios based on simulations from climate models that participated in the Coupled Model Intercomparison Project phase 5 (CMIP5) in 2015. ECCC and PCIC have now updated the CMIP5-based downscaled scenarios with a new set of downscaled scenarios based on the next generation of climate projections from the Coupled Model Intercomparison Project phase 6 (CMIP6). CMIP6 climate projections are based on both updated global climate models and new emissions scenarios called “Shared Socioeconomic Pathways” (SSPs). Statistically downscaled datasets have been produced from 26 CMIP6 GCMs under three different emission scenarios (i.e., SSP1-2.6, SSP2-4.5, and SSP5-8.5) using the same downscaling method (BCCAQv2) and downscaling target data (NRCANmet/ANUSPLIN) as the CMIP5-based downscaled scenarios. Downscaled daily maximum and minimum temperatures and daily precipitation are available across Canada at 10km grid spatial resolution for the 1950-2014 historical period and for the 2015-2100 period following each of the three emission scenarios.


## Access

### How to access the data

This data is available from the [MSC GeoMet](../../msc-geomet/readme_en.md) API / web services and on the [MSC Datamart](../../msc-datamart/readme_en.md) data server.


### Licence

The [end-user licence for Environment and Climate Change Canada's data servers](../../licence/readme_en.md) specifies the conditions of use of this data.

### MSC Open Data Service Usage Policy

The [MSC Open Data Service Usage Policy](../../usage-policy/readme_en.md) determines what constitutes an acceptable use of MSC Open Data services and provides users best practices for optimal use.



## Technical documentation

* [Technical note](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/climate_candcs-u6/CMIP6_DCS_Tech_Docs_EN.pdf)
* [Statistically downscaled climate scenarios](http://climate-scenarios.canada.ca/?page=statistical-downscaling)


<style>
  #legend-img {
    margin: 0px;
    height:280px;
  }
  #legend-popup {
    position: absolute;
    top: 40px;
    right: 8px;
    z-index: 2;
  }
  .legend-switch{
    top: 8px;
    right: .5em;
  }
  .ol-touch .legend-switch {
    top: 80px;
  }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.3.0/ol.css" type="text/css"/>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
<script src="https://cdn.jsdelivr.net/npm/ol@v7.3.0/dist/ol.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/1.3.3/FileSaver.min.js"></script>
<script>
    function isIE() {
      return window.navigator.userAgent.match(/(MSIE|Trident)/);
    }
    var head = document.getElementsByTagName('head')[0];
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (isIE())
    {
        js.src = "../../../js/dcs_ie.js";
        document.getElementById("controller").setAttribute("hidden", true);
    }
    else
    {
        js.src = "../../../js/dcs.js";
    }
    head.appendChild(js);
</script>
