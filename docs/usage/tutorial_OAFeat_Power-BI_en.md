[En français](tutorial_OAFeat_Power-BI_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > Using OGC API - Features with Power BI

# Tutorial: querying and using data with OGC API - Features using Power BI

The [OGC API - Features](https://eccc-msc.github.io/open-data/msc-geomet/ogc_api_en/#ogc-api-features) web services available in GeoMet-OGC-API offer the capability to query vector geospatial data and retrieve it in GeoJSON and CSV formats. The output file can then be used for display or additional data processing ([check out the R and Excel/VBA examples using those same files!](../tutorial_OAFeat_R-Excel_en/)). This tutorial will show you how you can:

* Query and retrieve vector geospatial data from GeoMet-OGC-API with [Power BI](https://www.microsoft.com/en-au/power-platform/products/power-bi/) as CSV
* Specify what data you want from the [Open Data Collections](https://api.weather.gc.ca/collections/)
* Load the data inside the [Power BI Report page](https://www.microsoft.com/en-au/power-platform/products/power-bi/) and display data with a simple map.

## Building the URL to get the data you want

So, the way we'll be adding the data to [Power BI](https://powerbi.microsoft.com/en-au/) is going to be by specifying a Web URL. You can also download the data as CSV on your station and load it to [Power BI](https://powerbi.microsoft.com/en-au/) from there, but since you don't need to, it's usually better to just query from the Web.

First things first, we'll get to the [Open Data Collections](https://api.weather.gc.ca/collections/) URL and select the one that we want. In this case we'll be choosing Real-time hydrometric data, then we'll click on ``Browse through the items of "Real-time hydrometric data"``. If you're following along, the page URL should look something like ``https://api.weather.gc.ca/collections/hydrometric-realtime/items``. Now we could use it like this, but let's filter on some values first!

We will scroll down to the table and click on ``DATETIME`` twice to sort the table by dates descending. Let's also change the ``Limit`` under the table to 100. Let's also decide to select a specific ``PROV_TERR_STATE_LOC``, we'll take ``BC``. Now that we've done that, we can see that the URL's changed to reflect our selection and now looks like ``https://api.weather.gc.ca/collections/hydrometric-realtime/items?lang=en&limit=100&offset=0&sortby=-DATETIME&PROV_TERR_STATE_LOC=BC``. There are more things we could play with, but for the sake of this example let's stick to this URL.

Take note that if you were actually looking to download this data as CSV, you can simply click on the ``CSV`` link on the top right of the screen, but as we've discussed earlier, there is no need to download it to use inside ``Power BI``.

## Simple scenario using Power BI

Now let's open ``Power BI``! Once opened, we click on ``Get data``, in the search bar we'll look for ``Web``, select it and click on ``Connect``. In the Dialog Box that just opened, we will select ``Advanced`` and paste our URL in the first Text Box. To tell ``Power BI`` we want the data as CSV, we'll add on the second line ``&f=csv``. You can now click on the ``OK`` button and on the next Dialog Box that opens click ``Connect``.

You will now be shown the table with all the values in it. If you're used to ``Power BI``, you can decide to use ``Transform Data`` to format the table any way you like. Otherwise you can simply click on ``Load``.

Now that we've brought in our table, we can start by changing the name since it defaulted to the end of the URL as its name. We'll just name it ``Real-time hydrometric data BC``. For this example, let's go inside the Visualizations pane on the right and Select ``Map``. Let's drag the corner to extend it enough that we can see everything inside.

We can now drag the data we want inside the appropriate field from the ``Fields`` pane to the ``Visualizations`` pane. Let's drag ``x`` into Longitude and ``y`` inside Latitude. We can also drag ``DISCHARGE`` inside ``Size`` to get varying circle sizes depending on that value. We can also switch ``Sub-Pane`` inside ``Visualizations`` and go into ``Format`` and change the data colors by pressing on the ``fx`` button. We'll put a gradient of colors with green, yellow and red scaling with the ``LEVEL``(see image below). We'll also specify some values instead of leaving it at Minimum, Middle and Maximum since there are lots of outliers and the colors would be different for only 2-3 points otherwise. Finally we can just change the title of the Map to something else, let's rename it ``Discharge and Level by Station, BC``, center it and increase its size a bit.

And there you go! With this simple example you now understand how you can query data from our OGC API - Features services and use it in any way your heart desires! You can also either Setup a Scheduled Refresh for your own Dashboard (which will not be explained here) or simply use the ``Refresh`` button inside to refresh the data manually. Here's an image that shows the final result as well as the fields that have been mentionned during this tutorial:

![Power BI full Map view with Fields](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_Power-BI_Map_en.jpg)

![Power BI full Color Formatting](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_Power-BI_Format_en.jpg)
