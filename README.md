# MSC Open Data Documentation

Welcome! This documentation will tell you how to update and deploy new version of the MSC public data documentation.


# Table of Contents

1. [Scope](#scope-and-objectives)
2. [Workflow overview](#workflow-overview)
3. [File structure](#file-structure)
4. [Monitoring documentation changes](#monitoring-documentation-changes)
5. [Updating the documentation](#updating-the-documentation)
  * [Requirements](#requirements)
  * [Getting ready](#getting-ready)
  * [Update workflow](#update-workflow)
  * [Images in the documentation](#images-in-the-documentation)
  * [Files in the documentation](#files-in-the-documentation)
  * [Changes to the Licence](#changes-to-the-licence)
6. [Deploying the documentation](#deploying-the-documentation)


# Scope and objectives

MSC public data documentation is currently published at the following locations:
* [MSC Datamart](https://dd.meteo.gc.ca/about_dd_apropos.txt)
* [Canada.ca](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data.html): 1 root pages and 3 sub-pages
* [weather.gc.ca](https://weather.gc.ca/mainmenu/modelling_menu_e.html), especially in the 'Analyses and Modelling' section
* [Collaboration server](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html), where the CMC Product Guide is currently hosted, along with various other related documentation

The main objective is to build a new 'MSC Public data documentation' that will encompasses current documentation hosted on (A) MSC Datamart, (B) canada.ca's DPS pages and (C) the CMC Product Guide. This new documentation will replace the current DPS documentation on Canada.ca

The writing of the documentation must consider the [Canada.ca Content Style Guide](https://www.canada.ca/en/treasury-board-secretariat/services/government-communications/canada-content-style-guide.html) ([French version](https://www.canada.ca/fr/secretariat-conseil-tresor/services/communications-gouvernementales/guide-redaction-contenu-canada.html)).


# Workflow overview

Here's an overview of the Public data documentation update process. Detailed procedures provided below.

1. Retrieve a local copy of the current public data documentation repository
2. Update the source documentation
3. (likely not required / obsolete) Run the script which generates the output versions of the documentation
4. Validate the output documentation
6. A 'MSC public data documentation' steward publishes the new version to canada.ca


# File structure

Files are stored on GCcode, in the DPS repository: http://gccode.ssc-spc.gc.ca/ec-msc/dps/tree/master/public-data-documentation/

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
1. [Log into GCcode](http://gccode.ssc-spc.gc.ca/)
2. [Go to the DPS repository project page](http://gccode.ssc-spc.gc.ca/ec-msc/dps)
3. Enable watch mode for the repository by selecting `Watch` in the dropdown menu alongside the alarm bell icon

This enables receiving modifications for the entire DPS repository.


# Updating the documentation

## Requirements

Requirement to update the source documentation:
* A [GCcode](http://gccode.ssc-spc.gc.ca/) account

Requirements to run the optional [scripts](scripts/):
* Python 3.4 with virtualenv and pip installed

Requirements to accept and publish modifications:
* Write permissions to [the dps GCcode repository](http://gccode.ssc-spc.gc.ca/ec-msc/dps)
* Canada.ca Adobe Experience Manager (AEM) account with permission to sumbit changes. At the moment, Sandrine and Alexandre at DPS have the privileges to submit new versions to Canada.ca

## Getting ready

1. Log to GCcode
 * Go to [the DPS repository](http://gccode.ssc-spc.gc.ca/ec-msc/dps) and ensure you are logged to GCcode
2. Fork the DPS repository
 * Click on `Fork` to fork the `dps` repository
 * At the desired location on your local filesystem, run: `git clone http://gccode.ssc-spc.gc.caYOUR-GITLAB-USERNAME/dps.git`
3. Configure your fork by specifying the upstream reference:
  * `cd dps`
  * `git remote add upstream http://gccode.ssc-spc.gc.ca/ec-msc/dps.git`

## Markdown requirements

Given we use mkdocs to style the documentation, extra care is required when creating the documentation in Markdown.

* Links must be explicit, a direct link such as http://foo.bar won't work with mkdocs, it must be specifically set as a link with `[name or url](url)`
* Lists must begin with an empty line before the initial bullet (`*`)
* The second level of lists must begin with 4 spaces before the `*`

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
    * Go to your fork on GitLab: `http://gccode.ssc-spc.gc.ca/YOUR-GITLAB-USERNAME/dps/`
    * Click on 'Merge Requests' on the top-level menu
    * Click on 'New merge request'
    * Select the appropriate branch from your fork (the 'Source branch'), select `master` on the Target branch (ec-msc/dps), and then click 'Compare branches and continue'
    * Assign the merge request and click 'Submit merge request'
    * If you're allowed to merge and are confident with the changes, you can click `Merge` right away. Otherwise, followup with the merge request's assignee. Please understand the best practice is to have someone else validate the change before merging
7. Update your fork's master branch
  * Go to your fork master branch: `git checkout master`
  * Update local master with dps source code: `git pull upstream master`
  * (optional) Push updated master to your fork: `git push`
   
Tips:
  * Use `git status` to learn on which branch you currently are and get additional status info
  * Use `git remote -v` to confirm `origin` and `upstream` are properly set
  * Use `git checkout master` to go back to the master branch of your fork

## Images in the documentation

Readying images for publication:
* Images must be optimized for the web, the following tips can be leveraged to reduce the size of images without significantly reducing quality
* Use [GIMP](https://gimp.org) to manipulate the images. GIMP is already installed on CCMEP Linux desktops and installed on many Windows machines
* Resize the image to the desired size `menu: Image > Scale Image`. A maximum width of 800px is suggested
* Export the image in either `jpg` or `png` depending on the image content, `menu: File > Export as`. In case of doubt, export to both formats and validate which one is smaller. 
  * jpg: don't save the thumbnail, remove the 'Comment', and select a quality around 80% (while previewing the result)
  * png: disable all image metadata ('Save ...') and try with a Compression level of 8 or so

Hosting images for the documentation on GitHub:
* Images must **not** be added to the GCcode repository
* Images are instead copied to the publicly accessible Collaboration server at `https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/` with the same corresponding directory structure as the path in this Git repository
  * Example: an image associated to `https://gccode.ssc-spc.gc.ca/ec-msc/dps/tree/master/public-data-documentation/canada.ca_upcoming/msc-data/nwp_rdps` is hosted in `https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp-rdps/`
* Sandrine and other colleagues at [CMOA](https://wiki.cmc.ec.gc.ca/wiki/CMOA) have permissions to copy images in those Collaboration folders
  * Send images by email to Sandrine along with the desired path

Adding images to the documentation:
* In the markdown documentation, images are referenced by using `![image alt text](path to image)`

Hosting images for the documentation on Canada.ca:
* Images are added to Canada.ca directly as part of the documentation update process

## Files in the documentation

Just like [images](#images-in-the-documentation), any file including binary files in the `.pdf` and `.docx` formats need to be hosted on the Collaboration server in the corresponding directory and a link to those files is used in the actual documentation. 

## Changes to the Licence

Prior applying any change to the [licence accompanying the documentation](licence/), the following must be completed:
* Get formal management approval for the change
* Bump the Licence version number
* Announce change to the Licence to users
  * e.g. [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) and [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement lists


# Deploying the documentation

## Initial deployment

* Update and validate [the list of URL redirections](MSC-Datamart_URL-redirections.md) to create on the MSC Datamart
* Request SSC to publish the URL redirections

## Regular releases

TO VALIDATE

1. Validate [status of open tickets](http://gccode.ssc-spc.gc.ca/ec-msc/dps/issues?label_name%5B%5D=Public+documentation)
2. Management sign-off
3. Publication to canada.ca: TO COMPLETE
4. Add or update remote images on the Collaboration server, if needed
5. Announce the new version of the documentation through the appropriate channels
  * Channels to consider, internally: TBD, externally: [dd-info] and [GeoMet-Info]
  
## Deployment to GitHub Pages with mkdocs

The deployment of the MSC Open Data Documentation to GitHub requires a user to have write access to the [eccc-msc/open-data repository](https://github.com/ECCC-MSC/open-data). In order to properly deploy the documentation using [mkdocs](https://www.mkdocs.org/), the user will also need to create a conda environment with Python 3.7 installed. Below is a step-by-step guide for publishing the documentation to the GitHub [eccc-msc/open-data repository](https://github.com/ECCC-MSC/open-data).

### Install Conda and create mkdocs virtual environment

Validate if Conda is already installed on your computer. Type `conda --version`. If a Conda version is provided, Conda is installed and slip the installation steps. Otherwise, proceed with the Conda installation.

To install Conda, please choose a location in your work environment that has a sufficient amount of disk space. It is not recommended that you install Conda in your home directory due to limited diskspace allocated to this directory.

1. Download [miniconda3](https://docs.conda.io/en/latest/miniconda.html) by clicking [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
2. To install, navigate to the folder containing the downloaded file and run `bash Miniconda3-latest-Linux-x86_64.sh`
3. Follow the installation instructions and:
   * accept the License terms
   * provide a location outside your Linux home directory
   * when asked about running the `conda init`, set to `yes`
4. Run `conda config --set auto_activate_base false`. This makes it so conda does not start by default
5. Start a new terminal session so you can access conda commands
6. Create a new conda environment named **mkdocs**: `conda create -n mkdocs python=3.7 && conda activate mkdocs`
7. Use pip to install the mkdocs package: `pip install mkdocs`
8. You can deactivate the environment with `conda deactivate`
 

### Deploy documentation on GitHub with mkdocs

Your new deploy branch should now be updated and available on the open-data GitHub repository. Create a pull request in GitHub to merge the deploy branch into the master branch. 

1. In your fork, ensure the `github` remote exists `git remote -v`, otherwise create it with `git remote add github https://github.com/ECCC-MSC/open-data.git`
1. Navigate to your local GCcode fork $USERNAME/open-data repository and pull the master branch that you finished merging: `git pull upstream master`
2. Verify that the newest release tag is available with `git tag`:
3. Create the new tag with `git tag $VERSION`
4. Checkout the newest tag: `git checkout $VERSION` 
5. Activate your mkdocs environment: `conda activate mkdocs`
6. Test and validate the documentation by running `mkdocs serve`, pay close attention to warnings (if any) and head to `http://127.0.0.1:8000`
6. At the root of your fork $USERNAME/open-data repository (where mkdocs.yml is located) run: `mkdocs gh-deploy -m "Your commit message for mkdocs here"`. The message should indicate the current version of the documentation.
7. Verify that the gh-pages branch was updated on GitHub and that the documentation is available at [https://eccc-msc.github.io/open-data](https://eccc-msc.github.io/open-data).