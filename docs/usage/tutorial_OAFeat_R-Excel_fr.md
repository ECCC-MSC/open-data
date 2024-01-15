[In English](tutorial_OAFeat_R-Excel_en.md)

![ECCC logo](../img_eccc-logo.png)

[TdM](../readme_fr.md) > [Aperçu de l'utilisation](readme_fr.md) > Utilisation d'OGC API - Features en R et en VBA

# Tutoriel: faire une requête à l'aide de GeoMet-OGC-API Features en utilisant les langages de programmation R et VBA

Les services web [OGC API - Features](https://eccc-msc.github.io/open-data/msc-geomet/ogc_api_en/#ogc-api-features) disponibles dans GeoMet-OGC-API offrent la possibilité d'envoyer une requête pour obtenir les données géospatiales vectorielles et de les récupérer aux formats CSV et GeoJSON. Le fichier de sortie peut ensuite être utilisé pour l'affichage ou le traitement ultérieur des données. Ce tutoriel vous montrera comment vous pouvez :

* Interroger et récupérer des données géospatiales vectorielles à partir de GeoMet-OGC-API avec [R](https://www.r-project.org/) et Excel [VBA](https://learn.microsoft.com/fr-fr/office/vba/library-reference/concepts/getting-started-with-vba-in-office)
* Charger les données dans l'éditeur de code [R](https://www.r-project.org/) et afficher des données de séries temporelles avec un graphique simple
* Charger les données dans une feuille Excel et afficher des données de séries temporelles avec un graphique simple

## Exemple avec R

Obtenir un simple bout de code fonctionnel en ``R`` est très simple en utilisant la fonction [plot()](https://www.rdocumentation.org/packages/graphics/versions/3.6.2/topics/plot). Cependant, les options de personnalisation sont inexistantes et nous allons plutôt créer un graphique qui est un peu plus complexe, mais qui montre vraiment ce que vous pouvez faire avec nos données et avec ``R`` :

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
  scale_size_continuous(range=c(1, 4)) +
  geom_line(size=1) +
  labs(title="AQHI en fonction du temps pour Ottawa",
       subtitle="Provenance weather.gc.ca",
       y="AQHI",
       x="Date et heure d'observation",
       caption="Exemple de code en R") +
  scale_x_datetime(
    breaks=seq(min(obs_datetime), max(obs_datetime), by="6 hours"),
    date_labels="%m-%d %H:%M",
    expand=c(0.005, 0))
print(p)
```

Premièrement, avant de pouvoir exécuter ce code, nous devons installer les bons outils (bien sûr, passez ces étapes si vous les avez déjà) :

- Installez [RStudio](https://www.rstudio.com/products/rstudio/download/)
- Téléchargez le [langage R](https://cran.r-project.org/bin/windows/base/)
- Téléchargez la version appropriée de [RTools](https://cran.r-project.org/bin/windows/Rtools/) en fonction de la version de RStudio que vous avez. Cette sélection est nécessaire pour que les librairies qui seront ajoutées au code fonctionnent correctement.

Nous avons maintenant tout ce dont nous avons besoin, alors ouvrons d'abord [RStudio](https://www.rstudio.com/products/rstudio/download/) afin que nous puissions passer aux prochaines étapes! Une fois ouvert, allez dans l'onglet appelé ``Console`` et tapez ces deux lignes (appuyez sur la touche ``Entrée`` après chaque ligne) :

- ``install.packages("ggplot2")``
- ``install.packages("scales")``

[ggplot2](https://ggplot2.tidyverse.org/) est une excellente librairie pour tracer des graphiques qui donne beaucoup d'options de personnalisation et [scales](https://scales.r-lib.org/) est une librairie utilisée avec [ggplot2](https://ggplot2.tidyverse.org/) qui aide à redimensionner le tracé final.

Ensuite, nous allons faire ``File > New File > R Script``, ce qui ouvrira un fichier vide sans titre. Nous copierons et collerons ensuite le code montré ci-dessus à l'intérieur de ce fichier et nous sauvegarderons ce dernier (soit en cliquant sur l'icône ``Save``, soit en appuyant sur ``Ctrl+S``). Vous pouvez le nommer comme vous le souhaitez, assurez-vous simplement que l'extension du fichier est .R (c'est-à-dire ``monfichier.R``). Pour exécuter le code, il suffit de cliquer sur le bouton ``Source`` (le bouton ``Run`` n'exécute que les lignes que vous avez sélectionnées dans le fichier). Le résultat devrait ressembler à ceci :

![Vue complète sur RStudio](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_R_fr.jpg)

Nous allons maintenant expliquer le code que nous venons d'exécuter ligne par ligne afin que vous compreniez ce qui a été fait :

Les deux premières lignes avec ``library`` ne servent qu'à indiquer au code que nous allons utiliser ces deux librairies. L'[options(scipen=999)](https://cran.r-project.org/web/packages/Tplyr/vignettes/options.html#:~:text=The%20value%20of%20scipen%20is,to%20understand%20with%20an%20example.&text=In%20'Tplyr'%2C%20we%20have%20the%20option%20tplyr.) n'est pas nécessaire dans cet exemple particulier, mais elle supprime la notation scientifique si jamais vous en avez besoin.

À l'intérieur de la fonction [read.csv()](https://swcarpentry.github.io/r-novice-inflammation/11-supp-read-write-csv/), vous mettez l'URL souhaité avec tous les paramètres que vous désirez. Par exemple, ici, nous voulons les données ``aqhi-observations-realtime``, nous voulons que les données soient triées selon le champ ``observation_datetime``, nous voulons une ``limit`` de 100 lignes de données et nous voulons seulement les données pour ``Ottawa``. Enfin, nous ajoutons simplement ``&f=csv`` à la fin pour que les données soient au format CSV. Cela chargera ainsi toutes les données du fichier CSV à l'intérieur de la variable nommée ``X`` en tant que ``dataset`` à l'intérieur de R Studio.

Le ``format_str`` est utilisé pour dire au code comment nos dates sont formatées afin qu'il sache comment les interpréter. Vous pouvez trouver plus d'info sur ce que signifie chaque lettre [ici](https://www.stat.berkeley.edu/~s133/dates.html). La ligne suivante est pour que le code sache que les valeurs dans ``observation_datetime`` ne sont pas seulement du texte, elles représentent la date et l'heure. Nous utiliserons donc [as.POSIXct()](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/as.POSIX*) pour atteindre cet objectif. Nous lui donnerons ``aqhi_obs_realtime$observation_datetime``, ce qui signifie "toutes les données à l'intérieur du ``dataset`` ``aqhi_obs_realtime`` sous le champ ``observation_datetime``". Nous spécifierons également que le fuseau horaire est ``GMT`` et nous lui dirons comment les dates et les heures sont formatées afin qu'il puisse les comprendre, en utilisant le ``format_str`` que nous venons de définir. Nous écrirons ensuite ``aqhi_obs_realtime$observation_datetime`` avec les dates formatées comme des données de temps plutôt que simplement comme du texte.

Maintenant, nous arrivons à la fonction [ggplot](https://ggplot2.tidyverse.org/reference/ggplot.html) et à toutes les options de formatage que nous avons ajoutées à celle-ci :

- Tout d'abord, la fonction elle-même. Nous devons lui passer le ``dataset`` que nous voulons utiliser pour le tracé, puis nous devons lui passer nos [mappages esthétiques aes](https://ggplot2.tidyverse.org/reference/aes.html), où tout ce que nous avons fait est de lui dire quelles colonnes nous souhaitons utiliser. Cette ligne seule ne montrera qu'un graphique vide car tout ce que nous avons fait ici est de lui dire ce que nous allons tracer, pas comment.
- Maintenant, disons-lui comment le tracer ! Nous utiliserons [geom_point()](https://ggplot2.tidyverse.org/reference/geom_point.html) pour lui dire de tracer les données en tant que points. À l'intérieur, nous avons ajouté quelques mappages esthétiques supplémentaires, qui coloreront les points en fonction de la valeur à l'intérieur de ``aqhi`` et changeront la taille du point en fonction de ``aqhi`` également. Vous auriez pu sauter l'esthétique et simplement lui donner une couleur et une taille, c'est seulement pour montrer que c'est possible de le faire de cette manière.
- Problème maintenant, les points varient énormément en taille, donc nous utiliserons [scale_size_continuous()](https://www.rdocumentation.org/packages/ggplot2/versions/0.9.0/topics/scale_size_continuous) et lui dirons d'avoir une taille minimale de 1 et une taille maximale de 3 pour les points. L'autre problème est qu'il y a maintenant deux légendes, une pour la taille et une autre pour la couleur. Pour remédier à cela, nous utiliserons [scale_fill_viridis_c](https://ggplot2.tidyverse.org/reference/scale_viridis.html) pour lui dire que les deux sont de type ``legend``, ce qui combinera les deux en une seule.
- Par la suite, connectons ces points avec une ligne! Nous utiliserons [geom_line()](https://plotly.com/ggplot2/geom_line/) à cet effet et lui donnerons une taille constante.
- Ensuite, nous ajouterons toutes les étiquettes que nous voulons tout autour du tracé avec [labs](https://www.rdocumentation.org/packages/ggplot2/versions/3.3.6/topics/labs).
- Enfin, notre axe des x contient actuellement toutes les dates avec leur notation complète, ce qui est difficile à lire. De ce fait, nous le formaterons en utilisant [scale_x_datetime()](https://www.rdocumentation.org/packages/ggplot2/versions/1.0.0/topics/scale_x_datetime). Tout d'abord, nous utiliserons l'argument ``breaks`` pour lui dire de commencer au premier temps et de se terminer au dernier temps (placer l'étiquette du premier temps sous le premier point et ne pas aller plus loin que la dernière valeur). À cet effet, nous utiliserons le générateur de séquence [seq()](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/seq), qui retournera une liste de toutes les étiquettes qui sont entre le début et la fin et nous utiliserons l'argument ``by`` pour lui donner l'intervalle souhaité. Ensuite, nous n'avons pas besoin de voir chaque date sous le format ``2022-01-01 00:00:00``. Au lieu de cela, disons-lui en utilisant l'argument ``date_labels`` que nous voulons seulement ``01-01 00:00`` avec le format de date ``%m-%d %H:%M``. [ggplot](https://ggplot2.tidyverse.org/reference/ggplot.html) conserve toujours un tampon au début et à la fin du tracé qui représente 5% de l'ensemble du graphique de chaque côté, donc nous le réduirons à 0,5% en utilisant l'argument ``expand``.

Nous sommes à la fin du script. Tout ce qui reste est la ligne [print()](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/print), qui ne fait que dire à RStudio d'afficher le tracé que nous venons de créer. Si vous aviez décidé de coller toutes ces lignes directement dans la console, vous n'auriez pas besoin de cette instruction print car, dans la console, il est toujours implicite que vous voulez voir le résultat de ce que vous faites. À noter que c'est une bien meilleure pratique de garder tout à l'intérieur d'un fichier et de l'exécuter à la place car vous ne risquez pas de perdre votre travail.

## Exemple avec Excel

L'objectif ici est de faire une requête et de créer un tracé dans Excel en utilisant uniquement le langage de programmation de Excel : [VBA](https://learn.microsoft.com/fr-fr/office/vba/library-reference/concepts/getting-started-with-vba-in-office). Avant de commencer, il faut noter que vous devrez changer le nom de la feuille ``Feuil1`` par le nom de votre feuille (sauf si c'est déjà le même nom). La raison est que nous vidons toute la feuille et mettons de nouvelles données à l'intérieur, on s'assure donc que vous n'avez pas la mauvaise feuille Excel sélectionnée et que vous n'effacerez tout ce qui se trouve dedans.

Voici les étapes à suivre pour utiliser ``VBA`` dans Excel :

- Activer l'onglet Développeur : Sur l'onglet Fichier, allez dans ``Options > Personnaliser le ruban``. Sous ``Personnaliser le ruban`` et sous ``Onglets principaux``, cochez la case ``Développeur``.
- Allez dans l'onglet ``Développeur`` nouvellement ajouté et cliquez sur ``Visual Basic``.
- Faites un clic droit sur la feuille Excel dans l'onglet ``VBAProject`` dans la nouvelle fenêtre ouverte, puis ``Insertion > Module``.
- Copiez et collez le code ci-dessous à l'intérieur du Module de code (n'oubliez pas de changer chaque ``Feuil1`` dans le code si ce n'est pas le nom de votre feuille) et appuyez sur le bouton ``Run``.

Et voilà! Vous venez de peupler votre feuille Excel avec les données de ``aqhi-observations-realtime`` et vous avez tracé un ``ScatterLineChart`` en utilisant les données des champs ``observation_datetime`` et ``aqhi``. Voici le code dont vous avez besoin pour accomplir cela (code écrit avec des commentaires pour aider les usagers à comprendre chaque étape) :

```VB
' Explicit -> Les variables utilisées doivent toutes être définies à l'aide de Dim avant d'être utilisées
Option Explicit

Sub MakeRequest()
    
    Dim baseURL As String
    Dim params As String
    Dim reqURL As String
    
    ' URL pour la requête avec les paramètres
    baseURL = "https://api.weather.gc.ca/collections/aqhi-observations-realtime/items"
    params = "sortby=observation_datetime&limit=100&location_name_fr=Ottawa"
    
    ' On concatène le tout en prenant soin d'ajouter "&f=csv" pour obtenir les valeurs en format csv
    reqURL = baseURL & "?" & params & "&f=csv"

    Application.ScreenUpdating = False
    
    ' On efface le contenu des colonnes A à Z avant d'ajouter nos nouvelles valeurs
    ThisWorkbook.Worksheets("Feuil1").Range("A:Z").ClearContents
    
    ' On sélectionne la feuille excel qui se nomme "Feuil1"
    Sheets("Feuil1").Select
        
    Dim ConnString As String
    
    ' On envoie la requête pour le fichier csv et on lui dit de mettre ça dans "Feuil1"
    ConnString = "TEXT;" & reqURL
        With ThisWorkbook.Worksheets("Feuil1").QueryTables.Add(Connection:=ConnString, Destination:=Worksheets("Feuil1").Cells(1, 1))
            .Name = "Contact List"
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
    
    
    ' Le scénario ici est que nous voulons un LineChart de aqhi en fonction de observation_datetime
    Dim WS As Worksheet
    Dim ColxNum As Integer
    Dim ColyNum As Integer
    Dim ColxLetter As String
    Dim ColyLetter As String
    Dim lastRow As Long
    Dim ValuesRange As String
    
    Set WS = ActiveSheet
    
    ' On trouve le numéro de colonne de observation_datetime et on trouve la lettre qui correspond
    ColxNum = Application.WorksheetFunction.Match("observation_datetime", WS.Rows(1), 0)
    ColxLetter = Split(Cells(1, ColxNum).Address, "$")(1)
    
    ' On trouve le numéro de colonne de aqhi et on trouve la lettre qui correspond
    ColyNum = Application.WorksheetFunction.Match("aqhi", WS.Rows(1), 0)
    ColyLetter = Split(Cells(1, ColyNum).Address, "$")(1)
    
    ' On trouve le nombre total de lignes
    lastRow = ActiveSheet.Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row
    
    ' On met sous forme H1:H62 pour sélectionner la colonne des dates et reformatter sous forme "Mois:Jour Heure:Minute"
    Dim c As Range
    Dim ColDatetimeValues As String
    ColDatetimeValues = ColxLetter & "1:" & ColxLetter & lastRow
    WS.Range(ColDatetimeValues).Select
    Selection.NumberFormat = "mm-dd hh:mm"
    For Each c In Selection
        c.Value = Replace(c.Value, "T", " ")
        c.Value = Replace(c.Value, "Z", "")
    Next c
    
    ' On met sous la forme H1:H62,J1:J62 pour le LineChart
    ValuesRange = ColxLetter & "1:" & ColxLetter & lastRow & "," & ColyLetter & "1:" & ColyLetter & lastRow
    
    ' On sélectionne les valeurs selon les intervals trouvés
    WS.Range(ValuesRange).Select
    
    ' On crée un LineChart avec les valeurs sélectionnées
    Dim myChart
    Set myChart = WS.Shapes.AddChart2(227, xlXYScatterLines)
    myChart.Select
    
    ' On place les étiquettes(labels) et on met les titres dedans en les formattant de la bonne façon
    With myChart
        .chart.SetElement msoElementChartTitleAboveChart
        .chart.SetElement msoElementPrimaryCategoryGridLinesMinor
        .chart.SetElement msoElementPrimaryCategoryAxisTitleBelowAxis
        .chart.SetElement msoElementPrimaryValueAxisTitleRotated
        .chart.ChartTitle.Text = "AQHI en fonction du temps pour Ottawa"
        .chart.Axes(Type:=xlCategory, AxisGroup:=xlPrimary).AxisTitle.Text = "Date et heure d'observation"
        .chart.Axes(Type:=xlCategory).TickLabels.Orientation = 45
        .chart.Axes(Type:=xlCategory).MinimumScale = Range(ColxLetter & "2").Value
        .chart.Axes(Type:=xlCategory).MaximumScale = Range(ColxLetter & lastRow).Value
        .chart.Axes(Type:=xlValue, AxisGroup:=xlPrimary).AxisTitle.Text = "AQHI"
    End With

End Sub
```

Voici le résultat après avoir roulé le code:

![Vue complète sur la feuille Excel et VB](https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/usage/tutorial_OAFeat_Excel_VBA_fr.jpg)
