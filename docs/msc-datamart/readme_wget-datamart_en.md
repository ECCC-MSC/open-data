[En français](readme_wget-datamart_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > [MSC Datamart](readme_en.md) > wget


# Use of wget for the MSC Datamart data

Before using 'wget', users should consider using the [AMQPS data retrieval service](amqp_en.md) and review the [service usage policy](../usage-policy/readme_en.md).

Here is a brief set of examples and usage notes, offered here to illustrate the possibilities for selective batch downloading from the MSC Datamart open data server. Please refer to the official [wget](https://www.gnu.org/software/wget/) manual for detailed usage. Examples shown here were tested under Linux and the Windows XP command line.

These examples are given for single use cases, or to access past data. To retrieve data in real time, we strongly encourage users to use the [Advanced Message Queuing Protocol (AMQP)](amqp_en.md).

Note:

Users of the Windows command shell should replace the single quotes (') in the examples with double quotes (").

## __Retrieving a single file__ in the 00Z GDPS (Global Deterministic Prediction System) model database:

    wget https://dd.meteo.gc.ca/today/model_gdps/15km/00/HHH/nom_de_fichier

    wget -nd -r -l1 -A '*GeopotentialHeight_Isbl-0175*.grib2' https://dd.meteo.gc.ca/today/model_gdps/15km/00/036/


Comments:

* The -r and -A options enable the use of wildcards. It is possible to take advantage of powerful automatic file selection capabilities by combining wildcarding with knowledge of the file naming convention. When passing an argument to the -A switch, double quotes should be used under the Windows command line, and single quotes under Unix-like systems
* In order to perform file selection according to a given set of wildcards, wget downloads the index.html file. With some older versions of wget, the index.html file is left lying around after the download is completed. Updating to the latest version should resolve this problem. Also, see next example for a way to avoid downloading index.html altogether

## __Retrieving fields from a locally generated list of file names__:

    wget -nd -nc -i file-list -P target-directory -B base-URL

Comments:

* "file-list" is a plain text file containing a list of desired files
* The file names in file-list must be complete and conform to the naming convention, including a current date-stamp. This requires you to generate a new list every day, a step that can be automated. The payoff is in a savings of bandwidth and download time

* Here is an example of a correct base-URL value: https://dd.meteo.gc.ca/today/radar/DPQPE/GIF/CASRA/

## Retrieving 00Z 00-hour RDPS (Regional Deterministic Prediction System) temperature at surface and all isobaric levels:

    wget -nd -r -l1 -A '*AirTemp_AGL-2m*.grib2,*AirTemp_Isbl*.grib2' -R '*Isbl-0[12]00' https://dd.meteo.gc.ca/today/model_rdps/10km/00/000/

Comment:

* The use of the `-R` switch to reject isobaric fields at 100 and 200 mb
