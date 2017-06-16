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

# Scope

MSC public data documentation which is published at the following locations:
* [MSC Datamart](http://dd.weather.gc.ca/)
* [ECCC-MSC on GitHub](https://github.com/ECCC-MSC)

# Workflow overview

Here's an overview of the Public data documentation update process. Detailed procedures provided below.

1. Retrieve a local copy of the current public data documentation repository
2. Update the source documentation
3. Run the script which generates the output versions of the documentation
4. Validate the output documentation
5. Request that these modifications are merged in the authoritative repository
6. A Public data documentation steward publishes the new version to the MSC Datamart and GitHub

# File structure

Files are stored on GCcode, in the DPS repository: http://gitlab.ssc.etg.gc.ca/ec-msc/dps/tree/master/public-data-documentation/

Files in this repository:
* README.md
 * This readme file!
* public-data-documentation-md/
 * The output Markdown documentation for publication on GitHub
* public-data-documentation-src/
 * The source documentation in the Markdown format
* public-data-documentation-txt/
 * The output raw text documentation for publication on MSC Datamart
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
* A GCcode account

Requirements to create the publication-ready versions of the documentation:
* Requirements associated with running [the scripts](scripts/)
 * Python 2.7 with virtualenv and pip installed

Requirements to accept and publish modifications
* Write permissions to [the dps GCcode repository](http://gitlab.ssc.etg.gc.ca/ec-msc/dps)
* A GitHub account and being member of [the ECCC-MSC organisation on GitHub](https://github.com/orgs/ECCC-MSC/people)

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
 * In a Terminal, while in your `dps` fork directory, update your local code with the source:
 * `git pull upstream master`
2. Create and switch to a 'branch' where you'll make your changes
 * `git checkout -b mybranchname` , where 'mybranchname' should be refer to the changes at stake, examples: 'fix for issue #123', 'gdps-doc-fix'
3. Make changes the `public-data-documentation-src` folder in your local fork
 * Changes must include the English and French versions of the documentation
4. Run [the documentation generation script](scripts/)
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
   
Tips:
 * Use `git status` to learn on which branch you currently are and get additional status info
 * Use `git remote -v` to confirm `origin` and `upstream` are properly set
 * Use `git checkout master` to go back to the master branch of your fork

# Deploying the documentation

INCOMPLETE
* Validate [status of open tickets](http://gitlab.ssc.etg.gc.ca/ec-msc/dps/issues?label_name%5B%5D=Public+documentation)
* Management sign-off
* Publication to MSC Datamart and GitHub
* Announce the new version of the documentation to the appropriate channels
 * Channels to consider, internally: TBD, externally: [dd-info] and [GeoMet-Info]
