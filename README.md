# MSC Public Data Documentation

Welcome! This documentation will tell you how to update and deploy new version of the MSC public data documentation.

# Table of Contents

1. [Scope](#scope)
2. [Workflow overview](#workflow-overview)
3. [File structure](#file-structure)
4. [Monitoring documentation changes](#monitoring-documentation-changes)
5. [Updating the documentation](#updating-the-documentation)
 * [Requirements](#requirements)
 * [Getting ready](#getting-ready)
 * [Update workflow](#update-workflow)
6. [Deploying the documentation](#deploying-the-documentation)

# Scope and objective

MSC public data documentation is currently published at the following locations:
* [MSC Datamart](https://dd.weather.gc.ca/)
* [Canada.ca](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data.html): 1 root pages and 3 sub-pages
* [weather.gc.ca](https://weather.gc.ca/mainmenu/modelling_menu_e.html), especially in the 'Analyses and Modelling' section
* [Collaboration server](http://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html), where the CMC Product Guide is currently hosted, along with various other related documentation

The objective is to build a new 'MSC Public data documentation' that will encompasses current documentation hosted on (A) MSC Datamart, (B) canada.ca's DPS pages and (C) the CMC Product Guide. This new documentation will replace the current DPS documentation on Canada.ca

# Workflow overview

Here's an overview of the Public data documentation update process. Detailed procedures provided below.

1. Retrieve a local copy of the current public data documentation repository
2. Update the source documentation
3. (likely not required / obsolete) Run the script which generates the output versions of the documentation
4. Validate the output documentation
6. A 'MSC public data documentation' steward publishes the new version to canada.ca

# File structure

Files are stored on GCcode, in the DPS repository: http://gitlab.ssc.etg.gc.ca/ec-msc/dps/tree/master/public-data-documentation/

Files in this repository:
* README.md
 * This readme file!
* canada.ca_current/
 * Documentation currently published on canada.ca
* canada.ca_upcoming/
 * The development version of the new 'MSC public data documentation'
* scripts/
 * Location of scripts, such as the scripts that create tables and the raw text version of the documentation
* templates/
 * Location of templates to be used for documenting MSC data
 
# Monitoring documentation changes

How to monitor changes to this documentation by receiving emails when changes are committed to the documentation:
1. [Log into GCcode](http://gitlab.ssc.etg.gc.ca/)
2. [Go to the DPS repository project page](http://gitlab.ssc.etg.gc.ca/ec-msc/dps)
3. Enable watch mode for the repository by selecting `Watch` in the dropdown menu alongside the alarm bell icon

This enables receiving modifications for the entire DPS repository.

# Updating the documentation

## Requirements

Requirement to update the source documentation:
* A [GCcode](http://gitlab.ssc.etg.gc.ca/) account

Requirements to run the optional [scripts](scripts/):
* Python 3.4 with virtualenv and pip installed

Requirements to accept and publish modifications:
* Write permissions to [the dps GCcode repository](http://gitlab.ssc.etg.gc.ca/ec-msc/dps)
* Canada.ca Adobe Experience Manager (AEM) account with permission to sumbit changes. At the moment, Sandrine and Alexandre at DPS have the privileges to submit new versions to Canada.ca

## Getting ready

1. Log to GCcode
 * Go to [the DPS repository](http://gitlab.ssc.etg.gc.ca/ec-msc/dps) and ensure you are logged to GCcode
2. Fork the DPS repository
 * Click on `Fork` to fork the `dps` repository
 * At the desired location on your local filesystem, run: `git clone http://gitlab.ssc.etg.gc.ca/YOUR-GITLAB-USERNAME/dps.git`
3. Configure your fork by specifying the upstream reference:
 * `cd dps`
 * `git remote add upstream http://gitlab.ssc.etg.gc.ca/ec-msc/dps.git`

## Update workflow

1. Sync your fork
 * In a Terminal, while in your `dps` fork directory, update your local code with the dps source:
 * `git pull upstream master`
2. Create and switch to a 'branch' where you'll make your changes
 * `git checkout -b mybranchname` , where 'mybranchname' should be refer to the changes at stake, examples: 'fix for issue #123', 'gdps-doc-fix'
3. Make changes the `canada.ca_upcoming` folder in your local fork
 * Changes must include the English and French versions of the documentation
4. (optional) Run [the documentation generation script](scripts/)
5. Validate the resulting documentation in your fork
 * Both the Markdown and raw text versions
 * Validate both languages
 * Validate breadcrumbs
 * Validate tables layout and content
6. Update the official repository
 * Make certain you're still on the branch you created at step 2 with the `git status` command
 * Commit changes made to your fork with `git commit -a -m "short log explaining changes"`
 * Push branch changes to your fork with `git push -u origin mybranchname` while using the `mybranchname` you created at step 2
 * Submit a merge request to push new changes to your fork to the official repository. To proceed:
   * Go to your fork on GitLab: `http://gitlab.ssc.etg.gc.ca/YOUR-GITLAB-USERNAME/dps/`
   * Click on 'Merge Requests' on the top-level menu
   * Click on 'New merge request'
   * Select the appropriate branch from your fork and then 'Compare branches and continue'
   * Assign the merge request and click 'Submit merge request'
   * If you're allowed to merge and are comfortable with the changes, you can `merge` right away. Otherwise, followup with the merge request's assignee
7. Update your fork's master branch
 * Go to your fork master branch: `git checkout master`
 * Update local master with dps source code: `git pull upstream master`
 * (optional) Push updated master to your fork: `git push`
   
Tips:
 * Use `git status` to learn on which branch you currently are and get additional status info
 * Use `git remote -v` to confirm `origin` and `upstream` are properly set
 * Use `git checkout master` to go back to the master branch of your fork

# Deploying the documentation

## Initial deployment

* Update and validate [the list of URL redirections](MSC-Datamart_URL-redirections.md) to create on the MSC Datamart
* Request SSC to publish the URL redirections

## Regular releases

TO VALIDATE

1. Validate [status of open tickets](http://gitlab.ssc.etg.gc.ca/ec-msc/dps/issues?label_name%5B%5D=Public+documentation)
2. Management sign-off
3. Publication to canada.ca: TO COMPLETE
4. Announce the new version of the documentation through the appropriate channels
  * Channels to consider, internally: TBD, externally: [dd-info] and [GeoMet-Info]
