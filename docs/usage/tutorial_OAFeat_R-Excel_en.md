[En français](tutorial_OAFeat_R-Excel_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [Usage overview](readme_en.md) > Using OGC API - Features with R and VBA

# Tutorial: querying data with GeoMet-OGC-API Features using R and VBA programming languages

The [OGC API - Features](https://eccc-msc.github.io/open-data/msc-geomet/ogc_api_en/#ogc-api-features) web services available in GeoMet-OGC-API offer the capability to query vector geospatial data and retrieve it in GeoJSON and CSV formats. The output file can then be used for display or further data processing. This tutorial will show you how you can:

* Query and retrieve vector geospatial data from GeoMet-OGC-API with [R](https://www.r-project.org/) and Excel's [VBA](https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office)
* Load the data inside the [R](https://www.r-project.org/) code editor and display time series data with a simple graph
* Load the data inside an Excel sheet and display time series data with a simple graph

## R example

Getting a simple piece of code working in ``R`` is very simple using the [plot()](https://www.rdocumentation.org/packages/graphics/versions/3.6.2/topics/plot) function. However, the costumization options are non-existent and as such we'll be making a plot that is a little more complex, but that really shows what you can do with our data and with ``R``:

```R
library(ggplot2)
library(scales)

options(scipen=999)
aqhi_obs_realtime <- read.csv("https://api.weather.gc.ca/collections/aqhi-observations-realtime/items?sortby=observation_datetime&limit=100&location_name_fr=Ottawa&f=csv")
format_str="%Y-%m-%dT%H:%M:%OSZ"
obs_datetime <- as.POSIXct(aqhi_obs_realtime$observation_datetime, tz="GMT", format=format_str)

aqhi_obs_realtime$observation_datetime <- obs_datetime

p <- ggplot(aqhi_obs_realtime, aes(x=observation_datetime, y=aqhi)) +
  geom_point(aes(fill=aqhi, size=aqhi), shape=21) +
  scale_fill_viridis_c(guide = "legend") +
  scale_size_continuous(range=c(1, 3)) +
  geom_line(size=1) +
  labs(title="AQHI as a function of time for Ottawa",
       subtitle="From weather.gc.ca",
       y="AQHI",
       x="Observation datetime",
       caption="Working with R example") +
  scale_x_datetime(
    breaks=seq(min(obs_datetime), max(obs_datetime), by="6 hours"),
    date_labels="%m-%d %H:%M",
    expand=c(0.005, 0))
print(p)
```

First things first, before we can run this code, we'll need to install the proper tools (of course skip steps if you already have them):

- Install [RStudio](https://www.rstudio.com/products/rstudio/download/)
- Download the [R language](https://cran.r-project.org/bin/windows/base/)
- Download the appropriate version of [RTools](https://cran.r-project.org/bin/windows/Rtools/) depending on the version of RStudio you have. This is necessary so that the libraries we will be adding to our code work properly.

We now have everything we need, so let's first open [RStudio](https://www.rstudio.com/products/rstudio/download/) so we can move to the next steps! Once opened, go in the tab called ``Console`` and type these two lines (press ``Enter`` key after each):

- ``install.packages("ggplot2")``
- ``install.packages("scales")``

[ggplot2](https://ggplot2.tidyverse.org/) is a great plotting library that gives us lots of costumization options and [scales](https://scales.r-lib.org/) is a library used with [ggplot2](https://ggplot2.tidyverse.org/) that helps with rescaling the final plot.

Next we'll go to ``File > New File > R Script``, which will open an empty untitled file. We will then copy and paste the code shown above inside it and we'll save the file (either by clicking on the ``Save`` icon or by pressing ``Ctrl S``). You may name it however you like, just make sure the extension of the file is ``.R`` (i.e. ``myfilename.R``). To run the entire code, simply click on the ``Source`` button (the ``Run`` button only runs lines you've highlighted inside your file). The result should look like this:

![RStudio complete overview](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_R_en.jpg)

We will now explain the code we've just run line by line so that you understand what has been done:

The first two lines with ``library`` are just to tell the code we'll be using these two libraries. The [options(scipen=999)](https://cran.r-project.org/web/packages/Tplyr/vignettes/options.html#:~:text=The%20value%20of%20scipen%20is,to%20understand%20with%20an%20example.&text=In%20'Tplyr'%2C%20we%20have%20the%20option%20tplyr.) isn't used in this particular example, but it removes scientific notation if you ever need it. 

Inside the [read.csv()](https://swcarpentry.github.io/r-novice-inflammation/11-supp-read-write-csv/) function, you put the desired url with whatever parameters you want to have. For example, here we want the ``aqhi-observations-realtime`` data, we want the data to be sorted according to the ``observation_datetime`` field, we want a ``limit`` of 100 lines of data and we only want the data for ``Ottawa``. Finally, we just add ``&f=csv`` at the end so that the data is in CSV format. It will thus load all the data from the CSV file inside the variable named ``X`` as a ``dataset`` inside R Studio. 

The ``format_str`` is used to tell the code how our dates are formatted so it knows how to interpret them. You can find more info on what each letter means [here](https://www.stat.berkeley.edu/~s133/dates.html). The next line is so the code understands that the values in ``observation_datetime`` aren't just text, they represent the date and time. We will thus use [as.POSIXct()](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/as.POSIX*) to achieve this goal. We will give it ``aqhi_obs_realtime$observation_datetime``, which means "all data inside the ``aqhi_obs_realtime`` dataset under the ``observation_datetime`` field". We'll also specify that the timezone is ``GMT`` and we will tell it how the dates and times are formatted so that it can understand it, using the ``format_str`` we've just defined. We then overwrite ``aqhi_obs_realtime$observation_datetime`` with the datetimes formatted as datetimes instead of just as text.

Now we come to the [ggplot](https://ggplot2.tidyverse.org/reference/ggplot.html) function and all the formatting options that we've added to it:

- First the function itself. We need to pass it the dataset that we want to use to plot, then we need to pass it our [aesthetic mappings aes](https://ggplot2.tidyverse.org/reference/aes.html), in which all we've done is tell it what columns we wish to be using. This line by itself will only show an empty graph since all we've done here is tell it what we'll be plotting, not how.
- Now let's tell it how to plot it! We'll use [geom_point()](https://ggplot2.tidyverse.org/reference/geom_point.html) to tell it to plot the data as points. Inside we've added some more [aesthetic mappings](https://ggplot2.tidyverse.org/reference/aes.html), which will color the points according to the value inside ``aqhi`` and change the point's size according to ``aqhi`` as well. You could've skipped the aesthetics and simply given it a color and a size, it's just there to show it is possible.
- Problem now is the points vary a LOT with size, so we'll use [scale_size_continuous()](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.0/topics/scale_size_continuous) and tell it to have a minimum size of 1 and a maximum size of 3 for points. The other problem is that there are now two legends, one with sizes and one with color. To remedy that, we're using [scale_fill_viridis_c](https://ggplot2.tidyverse.org/reference/scale_viridis.html) to tell the code they're both of type ``legend``, which will combine the two of them together.
- After that, let's connect these points with a line while we're at it! We'll be using [geom_line()](https://plotly.com/ggplot2/geom_line/) for that purpose and give it a constant size.
- Next we'll add all the labels that we want all around the plot with [labs](https://www.rdocumentation.org/packages/ggplot2/versions/3.3.6/topics/labs).
- Finally, our x axis currently contains all of the dates with their full notation and we can't read a single thing on the x axis. As such, we'll format it using [scale_x_datetime()](https://www.rdocumentation.org/packages/ggplot2/versions/1.0.0/topics/scale_x_datetime). First we'll use the ``breaks`` argument to tell it to start at the first time and end at the last time (meaning put the first time label under the first point and don't go further than the last value). For that purpose we'll use the sequence generator [seq()](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/seq), which will return a list of all the labels that are between start and end and we'll use the ``by`` argument to give it the desired interval. Next, we don't need to see every date as for example ``2022-01-01 00:00:00``. Instead, let's tell it using the ``date_labels`` argument that we only want ``01-01 00:00`` with the date format ``%m-%d %H:%M``. [ggplot](https://ggplot2.tidyverse.org/reference/ggplot.html) also always keeps a buffer at the start and end of the plot that represent 5% of the entire graph on each side, so we'll reduce that to 0.5% by using the ``expand`` argument.

We are at the end of the script. All that's left is the [print()](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/print) line, which only tells RStudio to display the plot we've just created. Had you decided to paste all of these lines directly inside the console, you wouldn't need that print statement as within the console it is always implicit that you wish to see the result of what you're doing. Although it is a better practice to keep everything within a file and run that instead as you don't run the risk of losing your work.

## Excel example

The goal here is to query and make the plot in Excel using only the Excel programming language: [VBA](https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office). Before we start, something to note is that you will need to change the sheet name ``Sheet1`` to the name of your sheet (unless it's already the same name). The reason is we are clearing the entire sheet and putting new data inside it, so this makes sure you don't have the wrong Excel sheet selected and clear everything that's in it.

Steps to follow to use ``VBA`` in Excel:

- Enable the Developer tab: On the File tab, go to ``Options > Customize Ribbon``. Under ``Customize the Ribbon`` and under ``Main Tabs``, select the ``Developer`` check box;
- Go in the newly added ``Developer`` tab and click on ``Visual Basic``;
- Right click on the Excel sheet in the ``VBAProject`` tab in the newly opened window, then ``Insert > Module``;
- Copy paste the code shown below inside the code Module (don't forget to change every ``Sheet1`` in the code if that's not the name of your sheet) and press the ``Run`` button.

And that's it! You've just populated your Excel sheet with the data from ``aqhi-observations-realtime`` and you've plotted a ``ScatterLineChart`` using the data from the ``observation_datetime`` and ``aqhi`` fields. Here is the code that you need to accomplish this (code made with added comments to help users understand each step):

```VB
' Explicit -> The variables used must be defined with Dim before being used
Option Explicit

Sub MakeRequest()

     Dim baseURL As String
     Dim params As String
     Dim reqURL As String

     ' URL for the request with parameters
     baseURL = "https://api.weather.gc.ca/collections/aqhi-observations-realtime/items"
     params = "sortby=observation_datetime&limit=100&location_name_fr=Ottawa"

     ' We concatenate into a single URL and we add "&f=csv" at the end to get the data in CSV format
     reqURL = baseURL & "?" & params & "&f=csv"

     Application.ScreenUpdating = False

     ' We clear the content of the cell in columns A to Z before adding the new data
     ThisWorkbook.Worksheets("Sheet1").Range("A:Z").ClearContents

     ' We select the Excel sheet named "Sheet1"
     Sheets("Sheet1").Select

     Dim ConnString As String

     ' We send the request for the CSV file and we tell it to put the data inside "Sheet1"
     ConnString = "TEXT;" & reqURL
          With ThisWorkbook.Worksheets("Sheet1").QueryTables.Add(Connection:=ConnString, Destination:=Worksheets("Sheet1").Cells(1, 1))
               .Name = "AQHI Observations Realtime"
               .FieldNames = True
               .RowNumbers = False
               .FillAdjacentFormulas = False
               .PreserveFormatting = True
               .RefreshOnFileOpen = False
               .BackgroundQuery = True
               .RefreshStyle = xlInsertDeleteCells
               .SavePassword = True
               .SaveData = True
               .AdjustColumnWidth = True
               .RefreshPeriod = 0
               .TextFileStartRow = 1
               .TextFileParseType = xlDelimited
               .TextFileCommaDelimiter = True
               .Refresh

          End With

     ' We will be making a LineChart of AQHI (aqhi) as a function of time (observation_datetime)
     Dim WS As Worksheet
     Dim ColxNum As Integer
     Dim ColyNum As Integer
     Dim ColxLetter As String
     Dim ColyLetter As String
     Dim lastRow As Long
     Dim ValuesRange As String

     Set WS = ActiveSheet

     ' We need to find the column number of "observation_datetime" and the corresponding column letter
     ColxNum = Application.WorksheetFunction.Match("observation_datetime", WS.Rows(1), 0)
     ColxLetter = Split(Cells(1, ColxNum).Address, "$")(1)

     ' We need to find the column number of "aqhi" and the corresponding column letter
     ColyNum = Application.WorksheetFunction.Match("aqhi", WS.Rows(1), 0)
     ColyLetter = Split(Cells(1, ColyNum).Address, "$")(1)

     ' We find the total number of lines for the data selection
     lastRow = ActiveSheet.Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row

     ' We select all the values from observation_datetime column and format it into a datetime format in the form "month-day hour:minute"
     Dim c As Range
     Dim ColDatetimeValues As String
     ColDatetimeValues = ColxLetter & "1:" & ColxLetter & lastRow
     WS.Range(ColDatetimeValues).Select
     Selection.NumberFormat = "mm-dd hh:mm"
     For Each c In Selection
          c.Value = Replace(c.Value, "T", " ")
          c.Value = Replace(c.Value, "Z", "")
     Next c

     ' We format lines and columns for data selection as H1:H62,J1:J62 for the LineChart
     ValuesRange = ColxLetter & "1:" & ColxLetter & lastRow & "," & ColyLetter & "1:" & ColyLetter & lastRow

     ' We select the values according to the formatted intervals
     WS.Range(ValuesRange).Select

     ' We create a ScatterLine chart with the selected data
     Dim myChart
     Set myChart = WS.Shapes.AddChart2(227, xlXYScatterLines)
     myChart.Select
    
     ' We add and format the labels
     With myChart
          .chart.SetElement msoElementChartTitleAboveChart
          .chart.SetElement msoElementPrimaryCategoryGridLinesMinor
          .chart.SetElement msoElementPrimaryCategoryAxisTitleBelowAxis
          .chart.SetElement msoElementPrimaryValueAxisTitleRotated
          .chart.ChartTitle.Text = "AQHI as a function of time for Ottawa"
          .chart.Axes(Type:=xlCategory, AxisGroup:=xlPrimary).AxisTitle.Text = "Observation datetime"
          .chart.Axes(Type:=xlCategory).TickLabels.Orientation = 45
          .chart.Axes(Type:=xlCategory).MinimumScale = Range(ColxLetter & "2").Value
          .chart.Axes(Type:=xlCategory).MaximumScale = Range(ColxLetter & lastRow).Value
          .chart.Axes(Type:=xlValue, AxisGroup:=xlPrimary).AxisTitle.Text = "AQHI"
     End With

End Sub
```

Here's the result after running the code:

![Excel and VB Window complete overview](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_Excel_VBA_en.jpg)
