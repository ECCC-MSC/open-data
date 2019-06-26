<?xml version="1.0" encoding='ISO-8859-1'?>

<!--  
 (C) Environment Canada, 2010

   XSLT to transform Environment Canada CMML version > 3.01 format into CSV
   
   Author: Miguel Tremblay
   Date: January 5th 2010

   Note: Use Xalan library to write multiple file with one XSLT:
    http://xml.apache.org/xalan-j/

    Do not forget to import the CLASSPATH to invoke this XSLT in command line.
   Exemple for a Debian GNU/Linux workstation:
    export CLASSPATH='/usr/share/xalan/lib/serializer.jar: \
                                   /usr/share/java/lib/xalan2.jar: \
                                  /usr/share/xerces-2/lib/xercesImpl.jar: \
                                 /usr/share/xml-commons-external-1.3/lib/xml-apis-ext.jar:\
                                /usr/share/xml-commons-external-1.3/lib/xml-apis.jar'

   Exemple for a Ubuntu GNU/Linux workstation (tested under 10.04):
    export CLASSPATH='/usr/share/java/serializer.jar: \
			/usr/share/java/xalan2.jar: \
			/usr/share/java/xercesImpl.jar: \
			/usr/share/java/xml-apis-ext.jar:\
			/usr/share/java/xml-apis.jar'

   Call is:
    java org.apache.xalan.xslt.Process -IN cmml.xml -XSL cmml2csv.xsl -OUT foo.out -PARAM CMML_FILENAME cmml.xml -PARAM OUTPUT_DIRECTORY path_to_directory

  -IN :  Filename, including the path, of the CMML file
  -XSL : The XSLT file. This file.
 -OUT: File for the output XML. Usually, one XML file is transformed in one other XML file. 
   This is the path of this file. It is not used with this script. However, you can not use /dev/null
  for value.
 -PARAM CMML_FILENAME: This should be set with the same value than -IN. It is used to know
  from which CMML file a particular CSV file is obtained. The -IN parameter can not be found with
 the XSLT specification.
  -PARAM OUTPUT_DIRECTORY : Directory where all the CSV file will be created. If the directory does not
  exits, it will be created the same way the command "mkdir -p" works.

   The CSV file is written in the directory 'output' where the command is executed.

  2010-09-02: 
    * update to Ubuntu 10.04. 
    * Add the timezone in CSV file.

  2016-10-05:
    * Bugfix for the bulletin_header section 
    * Add production of wind gust CSV files
-->

<xsl:transform version="1.0"  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:redirect="http://xml.apache.org/xalan/redirect" extension-element-prefixes="redirect" >

<xsl:output method="text"/>
<xsl:param name="CMML_FILENAME"/>
<xsl:param name="OUTPUT_DIRECTORY"/>

<xsl:template match="/">

<!-- Bulletin header -->
<xsl:variable  name="bulletin_header"  select="substring($CMML_FILENAME, 10, 6)" />

<!--  Input filename -->
<xsl:variable name="start_string_filename">; CMML : &apos;</xsl:variable>
<xsl:variable name="end_string_filename">&apos;</xsl:variable>
<xsl:variable name="InputFilename" select="concat($start_string_filename, $CMML_FILENAME, $end_string_filename)"/>

<!-- Directory for output  -->
<xsl:variable name="OutputDirectory" select="$OUTPUT_DIRECTORY"/>

<!--    Remove the special characters from the ISO8601 creation date -->
  <xsl:variable name="date_iso8601" select="//creation-date"/>
  <xsl:variable name="date_for_filename">
    <xsl:call-template name="replaceCharsInString">
      <xsl:with-param name="stringIn" select="string($date_iso8601)"/>
      <xsl:with-param name="charsIn" select="':'"/>
      <xsl:with-param name="charsOut" select="'-'"/>
    </xsl:call-template>
  </xsl:variable>

  <!-- Get the timezone: one time zone per CMML  -->
  <xsl:variable name="TZ" select="concat('; Time zone | Fuseau horaire : ', //timezone)" />

   <!--  For each forecast -->
   <xsl:for-each select="cmml/data/forecast/meteocode-forecast">
   <!-- City name/Nom de la ville -->
    <xsl:for-each select="./location">
      <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/',$date_for_filename, '_',  $bulletin_header, '_', ./msc-zone-code,'_TA.csv')" />
      <xsl:value-of select="$OutputFilename"/>
      <xsl:variable name="villes_en_fr" select="concat(msc-zone-name[@lang='en'], ' | ', msc-zone-name[@lang='fr'], $InputFilename, $TZ, '&quot;')"/>
      <xsl:variable name="valid_time" select="',&quot;Valid time | Heure de validit&#233;;'"/>;
      <!-- TA :: Air temperature -->
      <xsl:variable name="title">Air temperature (&#176; Celsius) | Temp&#233;rature de l&apos;air (&#176; Celsius)</xsl:variable>
      <xsl:variable name="element_temps" select="concat($villes_en_fr,  $valid_time, $title, '&quot;')"/>
      <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>
</xsl:text>
      <xsl:for-each select="../parameters/temperature-list[@type='air']/temperature-value">
      <xsl:value-of select="@start"/>,<xsl:value-of select="./upper-limit"/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write> 
      <!--    TD :: Dew point -->
       <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/', $date_for_filename, '_', $bulletin_header, '_', ./msc-zone-code,'_TD.csv')" />
         <xsl:variable name="element_temps" select="concat($villes_en_fr, $valid_time, 'Dew point (&#176; Celsius) | Point de ros&#233;e (&#176; Celsius)&quot;')"/>
         <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>
</xsl:text>
            <xsl:for-each select="../parameters/temperature-list[@type='dew-point']/temperature-value">
                <xsl:value-of select="@start"/>,<xsl:value-of select="./upper-limit"/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write> 

      <!--    WS :: Wind speed-->
       <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/', $date_for_filename, '_', $bulletin_header, '_', ./msc-zone-code,'_WS.csv')" />
         <xsl:variable name="element_temps" select="concat($villes_en_fr, ',&quot;Start | D&#233;but;End | Fin;Wind speed min (km/h) | Vitesse du vent min (km/h);Wind speed max (km/h) | Vitesse du vent max (km/h);Wind direction | Direction du vent&quot;,&quot;&quot;')"/>
         <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>
</xsl:text>
            <xsl:for-each select="../parameters/wind-list/wind">
                <xsl:value-of select="@start"/>,<xsl:value-of select="@end"/>,<xsl:value-of select="./wind-speed/lower-limit"/>,<xsl:value-of select="./wind-speed/upper-limit"/>,<xsl:value-of select="@direction"/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write> 
     
      <!--    WG :: Wind gust-->
       <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/', $date_for_filename, '_', $bulletin_header, '_', ./msc-zone-code,'_WG.csv')" />
         <xsl:variable name="element_temps" select="concat($villes_en_fr, ',&quot;Start | D&#233;but;End | Fin;Wind gust min (km/h) | Vitesse des rafales min (km/h);Wind gust max (km/h) | Vitesse des rafales max (km/h)&quot;')"/>
         <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>
</xsl:text>
            <xsl:for-each select="../parameters/wind-list/wind">
                <xsl:value-of select="@start"/>,<xsl:value-of select="@end"/>,<xsl:value-of select="./gust-speed/lower-limit"/>,<xsl:value-of select="./gust-speed/upper-limit"/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write>     

      <!--    CC :: Cloud cover -->
       <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/', $date_for_filename, '_', $bulletin_header, '_', ./msc-zone-code,'_CC.csv')" />
         <xsl:variable name="element_temps" select="concat($villes_en_fr, $valid_time, 'Cloud cover (tenth) | Couverture nuageuse (dixi&#232;me)&quot;')"/>
         <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>
</xsl:text>
            <xsl:for-each select="../parameters/cloud-list/cloud-cover">
                <xsl:value-of select="@start"/>,<xsl:value-of select="."/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write> 

      <!--    PA Precipitation accumulation -->
       <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/', $date_for_filename, '_', $bulletin_header, '_', ./msc-zone-code,'_PA.csv')" />
         <xsl:variable name="element_temps" select="concat($villes_en_fr, ',&quot;Start | D&#233;but;End | Fin;Total accumulation min (mm) | Accumulation totale min (mm);Total accumulation max (mm | Accumulation totale max (mm);Hourly accumulation min (mm) | Accumulation horaire min (mm);Hourly accumulation max (mm) | Accumulation horaire max (mm);Precipitation type | Type de pr&#233;cipitation&quot;')"/>
         <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>,"","","","",""
</xsl:text>
            <xsl:for-each select="../parameters/accum-list/accum-amount">
                <xsl:value-of select="@start"/>,<xsl:value-of select="@end"/>,<xsl:value-of select="lower-limit/@cumul-inf"/>,<xsl:value-of select="upper-limit/@cumul-sup"/>,<xsl:value-of select="./lower-limit"/>,<xsl:value-of select="./upper-limit"/>,<xsl:value-of select="@type"/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write> 


      <!--    POP -->
       <xsl:variable name="OutputFilename" select="concat($OutputDirectory, '/', $date_for_filename, '_', $bulletin_header, '_', ./msc-zone-code,'_POP.csv')" />
         <xsl:variable name="element_temps" select="concat($villes_en_fr,  ',&quot;Start | D&#233;but;End | Fin;Probability of precipitation (%) | Probabilit&#233; de pr&#233;cipitation (%)&quot;,&quot;&quot;')"/>
         <redirect:write select="$OutputFilename">"<xsl:value-of select="$element_temps"/><xsl:text>
</xsl:text>
            <xsl:for-each select="../parameters/probability-of-precipitation-list/probability-of-precipitation">
                <xsl:value-of select="@start"/>,<xsl:value-of select="@end"/>,<xsl:value-of select="."/><xsl:text>
</xsl:text>
      </xsl:for-each> 
      </redirect:write> 



   </xsl:for-each>
   </xsl:for-each>
</xsl:template>


<!--    Template for character replacement. Copied from http://www.dpawson.co.uk/xsl/sect2/replace.html#d9563e43 -->
<xsl:template name="replaceCharsInString">
  <xsl:param name="stringIn"/>
  <xsl:param name="charsIn"/>
  <xsl:param name="charsOut"/>
  <xsl:choose>
    <xsl:when test="contains($stringIn,$charsIn)">
      <xsl:value-of select="concat(substring-before($stringIn,$charsIn),$charsOut)"/>
      <xsl:call-template name="replaceCharsInString">
        <xsl:with-param name="stringIn" select="substring-after($stringIn,$charsIn)"/>
        <xsl:with-param name="charsIn" select="$charsIn"/>
        <xsl:with-param name="charsOut" select="$charsOut"/>
      </xsl:call-template>
    </xsl:when>
    <xsl:otherwise>
      <xsl:value-of select="$stringIn"/>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>


</xsl:transform>
