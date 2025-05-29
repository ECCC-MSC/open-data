[En français](changelog_hrepa_fr.md)

![ECCC logo](../../img_eccc-logo.png)

[TOC](../../readme_en.md) > [MSC data](../readme_en.md) > [HREPA](readme_hrepa_en.md) > HREPA Changelog

# Chronology of changes to the High Resolution Ensemble Precipitation Analysis (HREPA)

## Thursday May 1, 2025

### The High Resolution Ensemble Precipitation Analysis (HREPA) is declared operational at the Canadian Meteorological Centre

Effective May 1st, 2025, the Canadian Meteorological Centre (CMC) of the Meteorological Service of Canada declared operational the High Resolution Ensemble Precipitation Analysis (HREPA, v2.0.1).

## Wednesday September 11, 2024

### Temporary removal of the Fire Weather network observations (OMNRF) from the High Resolution Ensemble Precipitation Analysis System (HREPA) assimilation at the Canadian Meteorological Centre (CMC)

Starting on September 11, 2024, Fire Weather network observations from the Ontario Ministry of Natural Resources and Forestry (OMNRF) have been temporarily removed from the set of observations assimilated into the High Resolution Ensemble Precipitation Analysis (HREPA). This update is effective at 06UTC for the final and at 12UTC for the preliminary analyses.

This update was required to prevent the influence of some erroneous observations from the OMNRF network on the final HREPA analysis over certain regions in Southern Ontario – particularly in the Kingston-Ottawa and Huron-Erie regions. This has a minor impact on system performance, since in most cases, the gaps are properly filled by observations from the other networks, particularly the synoptic gauges, as well as the radar and satellite QPEs.

An investigation is in progress to identify the problematic stations and exclude them from the HREPA analysis once the network is reinstated. The issue appears to mostly stem from false zero observations reported by certain gauges in the OMNRF network.

## Tuesday June 11, 2024

### Upgrade to Version 2.0.0 of the High Resolution Ensemble Precipitation Analysis (HREPA) at the Canadian Meteorological Centre

On Tuesday June 11, 2024, starting with the 1200 UTC run, the Meteorological Service of Canada's Canadian Meteorological Centre (CMC) will upgrade the High Resolution Ensemble Precipitation Analysis (HREPA) to v2.0.0.

Significant changes:

* Addition of 86 additional stations from partner network Saskatchewan Fire Weather Network (SKForestry) to improve analyses for this province.
* Assimilation of dual-polarized radar data for 32 Canadian S-band radars (DPQPE) and 65 US NEXRAD radars (DAA). Addition of 3 US radars.
* These changes lead to a significant improvement in skill Brier scores for all precipitation thresholds.

The official note announcing this implementation is available [at this link](https://dd.meteo.gc.ca/doc/genots/2024/06/10/NOCN03_CWAO_101857___46443).

## Tuesday June 28, 2022

### Upgrade to Version 1.4.0 of the HREPA adapted to the New High Performance Computing Infrastructure.

See details [at this link](../changelog_multisystems_en.md).

## Wednesday December 1st, 2021

### Upgrade to Version 1.3.0 of the High Resolution Ensemble Precipitation Analysis (HREPA) at the Canadian Meteorological Centre

Effective Wednesday, December 1st, 2021, the Canadian Meteorological Centre (CMC) will update the High Resolution Ensemble Precipitation Analysis (HREPA) to v1.3.0.


The official note announcing this implementation is available [at this location](https://dd.meteo.gc.ca/doc/genots/2021/11/26/NOCN03_CWAO_262118___50159).

For more information, please consult the technical specifications document for HREPA v1.3.0 available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_specifications/tech_specifications_HREPA_1.3.0_e.pdf).

A technical note with more details on this change is available [at this link](https://collaboration.cmc.ec.gc.ca/cmc/CMOI/product_guide/docs/tech_notes/technote_capa_hrepa-130_e.pdf).


