# MSC Public Data Documentation

Welcome! This documentation will tell you how to update and deploy new version of the MSC public data documentation.

ADD TOC

# Scope

MSC public data documentation which is published at the following locations:
* [MSC Datamart](http://dd.weather.gc.ca/)
* [ECCC-MSC on GitHub](https://github.com/ECCC-MSC)

# File structure

Files are stored on GCcode, in the DPS repository: http://gitlab.ssc.etg.gc.ca/ec-msc/dps/tree/master/public-data-documentation/

Files in this repository:
* README.md
 * This readme file!
* public-data-documentation-md
 * The output Markdown documentation for publication on GitHub
* public-data-documentation-src
 * The source documentation in the Markdown format
* public-data-documentation-txt
 * The output raw text documentation for publication on MSC Datamart
* scripts
 * Location of scripts, such as the scripts that create tables and the raw text version of the documentation
* templates
 * Location of templates to be used for documenting MSC data

# Preliminary steps

## Requirements

Requirement to update the source documentation:
* A GCcode account

Requirements to create the output versions of the documentation:
* Requirements associated with running [the scripts](scripts/)
 * Python 2.7 with virtualenv and pip installed

Requirements to accept and publish modifications
* Write permissions to the dps GCcode repository
* A GitHub account and being member of [the ECCC-MSC organisation on GitHub](https://github.com/orgs/ECCC-MSC/people)

## Getting ready

INCOMPLETE

1. Fork this repository
 * Log on GCcode
 * Fork the dps rep
 * Clone your fork on your local filesystem

# Updating the documentation

INCOMPLETE

1. Sync your Fork
 * spécifier ici comment !
2. Make changes the public-data-documentation-src folder in your local fork
 * Changes must be made in the English and French versions of the documentation
3. Run [the documentation generation script](scripts/)
4. Validate the resulting documentation
 * Both the [Markdown](public-data-documentation-md) and [raw text](public-data-documentation-txt) versions
 * Validate both languages
5. Submit merge requests
 * spécifier ici comment !

# Deploying the documentation

INCOMPLETE
