[En français](readme_fr.md)

![ECCC logo](../img_eccc-logo.png)

[TOC](../readme_en.md) > MSC Data


MSC Public Data
===============

Short description here

Table of Content
----------------

1. [Change log](changelog_en.md)
  * Changes to datasets and associated systems

2. MSC Datasets
    * [Weather alerts](alerts/readme_en.md)
    * Weather observations
        * [Weather radar](obs_radar/readme_en.md)
        * [Observations at stations](obs_stations/readme.md)
        * [Hydrometric](obs_hydrometric/readme_en.md)
        * [Vertical profiles](obs_vertical-profiles/readme.md)
    * Numerical weather prediction
        * How it works
            * Weather variables, MR, FH, FHI, extent
        * Deterministic NWP systems
            * _mettre ces noms au long..._
            * [GDPS](nwp_gdps/readme_en.md)
            * [RDPS](nwp_rdps/readme_en.md)
            * [HRDPS](nwp_hrdps/readme_en.md)
            * [RDPA](nwp_rdpa/readme_en.md)
            * [RAQDPS](nwp_raqdps/readme_en.md)
            * [GIOPS](nwp_giops/readme_en.md)
            * [RDWPS](nwp_rdwps/readme_en.md)
        * Probabilistic NWP systems
            * [GEPS](nwp_geps/readme_en.md)
            * [NAEFS](nwp_naefs/readme_en.md)
            * [REPS](nwp_reps/readme_en.md)
            * [CanSIPS](nwp_cansips/readme_en.md)
    * Other datasets
        * [AQHI](aqhi/readme_en.md)
        * [Barometry](barometry/readme_en.md)
        * [Bulletins](bulletins/readme_en.md)
        * [Citypage](citypage/readme_en.md)
        * Forecast polygons
        * [Hurricanes](hurricanes/readme_en.md)
        * Lightning strikes
        * [Marine forecasts](marine-forecasts/readme_en.md)
        * [Meteocode](meteocode/readme_en.md)
        * [Nowcasting](nowcasting/readme.md)
        * [Weatheradio](weatheradio/readme_en.md)


# Summary Table
Dataset                                                                                         | Id              | MR        | FH                  | FHI | N.  
------------------------------------------------------------------------------------------------|-----------------|-----------|---------------------|-----|-----
[Canadian Weather](citypage/geomet-citypage_en.md)                                              | weather         | N/A       | N/A                 | N/A | 1   
[Canadian Weather](alerts/geomet-alerts_en.md)                                                  | alerts          | N/A       | N/A                 | N/A | 1   
[Regional Air Quality Deterministic Prediction System (RAQDPS)](firework/geomet-firework_en.md) | firework        | N/A       | N/A                 | N/A | 1   
[Other Weather Data](weatheradio/geomet-weatheradio_en.md)                                      | weatheradio     | N/A       | N/A                 | N/A | 1   
[Hurricane trajectories](hurricanes/geomet-hurricanes_en.md)                                    | hurricanetracks | N/A       | N/A                 | N/A | 4   
[North American radar mosaic](obs_radar/geomet-radar_en.md)                                     | radar           | N/A       | N/A                 | N/A | 4   
[Global Deterministic Prediction System (GDPS)](nwp_gdps/geomet-gdps-en.md)                     | gdps            | 0,12      | 240,240             | 3   | 41  
[Regional Ensemble Prediction System (REPS)](nwp_reps/geomet-reps_fr.md)                        | reps            | 0,12      | 72,72               | 3   | 1205
[Regional Deterministic Precipitation Analysis (RDPA)](nwp_rdpa/geomet-rdpa_en.md)              | rdpa            | 0,6,12,18 | -720,-720,-720,-720 | 6   | 3   
[Regional Deterministic Prediction System (RDPS)](nwp_rdps/geomet-rdps_en.md)                   | rdps            | 0,6,12,18 | 48,54,48,54         | 1   | 41  
[High Resolution Deterministic Prediction System (HRDPS)](nwp_hrdps/geomet-hrdps_en.md)         | hrdps           | 0,6,12,18 | 48,48,48,48         | 1   | 33  
[Oceanography](nwp_giops/geomet-giops-en.md)                                                    | giops           | 0         | 240                 | 3   | 16  


NOTES:
* We mentioned a Table, but it may end up using a list given it's error-prone to manually manage a Markdown table that will show up fine as raw text and interpreted Markdown
* Let's use a Template for all of these dataset subpages: Sandrine is going to work on a draft template
* Let's review the folder names! For instance, is 'marine_forecasts' appropriate? There are other marine forecasts (GIOPS, RDWPS, etc)...
* Content of the [CMC Product Guide](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html) will be included in the dataset pages or subpages



