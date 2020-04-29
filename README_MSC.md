# MSC Open Data Documentation

Welcome! This documentation will tell you how to update and deploy the MSC Open Data public documentation.

# Table of Contents

1. [Scope](#1-scope-and-objectives)
2. [File structure](#2-repository-file-structure)
3. [Monitoring documentation changes](#3-monitoring-documentation-changes)
4. [Updating the documentation](#4-updating-the-documentation)
    * [Getting ready](#41-getting-ready)
    * [Editing the documentation](#42-editing-the-documentation)
        * [Markdown requirements](#421-markdown-requirements)
        * [Images in the documentation](#422-images-in-the-documentation)
        * [Files in the documentation](#423-files-in-the-documentation)
        * [Changes to the Licence](#424-changes-to-the-licence)
    * [Update workflow](#43-update-workflow)
5. [Deploying the documentation](#5-deploying-the-documentation)
    * [Permission requirements](#51-permission-requirements)
    * [Getting ready](#52-getting-ready)
    * [Deployment to GitHub Pages with mkdocs](#53-deployment-to-github-pages-with-mkdocs)


# 1 - Scope and objectives

The main objective of the 'MSC Open Data documentation' is to consolidate public documentation at a single location with links, images and interactive content, and maintained up to date and iteratively improved over time. Improvements and actions pertaining to this documentation is coordinated by the [Comité de la documentation publique (ComDoc)](https://wiki.cmc.ec.gc.ca/wiki/Comit%C3%A9_de_la_documentation_publique#Composition_du_comit.C3.A9).

The repository manages the documentation published on https://eccc-msc.github.io/open-data/ which should be eventually published on Canada.ca pages.

Other MSC public data documentation is published at the following locations:
* [MSC Datamart](https://dd.meteo.gc.ca/about_dd_apropos.txt)
* [Canada.ca](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/weather-tools-specialized-data.html): 1 root pages and 3 sub-pages
* [weather.gc.ca](https://weather.gc.ca/mainmenu/modelling_menu_e.html), especially in the 'Analyses and Modelling' section
* [Collaboration server](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/index_e.html), where the decommissioned CMC Product Guide is hosted, along with various other related documentation

The writing of the documentation must consider the [Canada.ca Content Style Guide](https://www.canada.ca/en/treasury-board-secretariat/services/government-communications/canada-content-style-guide.html) ([French version](https://www.canada.ca/fr/secretariat-conseil-tresor/services/communications-gouvernementales/guide-redaction-contenu-canada.html)).


# 2 - Repository file structure

Files are stored on GCcode, in the public-doc repository: http://gccode.ssc-spc.gc.ca/ec-msc/public-doc/ . A copy is publicly available on GitHub at https://github.com/ECCC-MSC/open-data

Files in this repository:
* README_MSC.md
    * This readme file!
* README.md
    * The welcome page for GitHub visitors
* [CHANGELOG.md](CHANGELOG.md)
    * User-oriented list of what's new and what's changed for new public documentation versions
* docs/
    * The actual documentation
* docs-dev/
    * Documentation pages in development and ignored during the deployment process
* docs/msc/
    * Public documentation that is deployed but not linked to from the main documentation pages. It is used for *public* documentation of data that is not yet available as open data. Directory structure is the same as the main documentation
* templates/
    * Location of templates to be used for documenting MSC data
* scripts/
    * Location of scripts, such as the scripts that create tables and the raw text version of the documentation
* mkdocs.yml
    * The mkdocs configuration file
* custom_theme/
    * Local mkdocs theme files

# 3 - Monitoring documentation changes

How to monitor changes to this documentation by receiving emails when changes are committed to the documentation:
1. [Log into GCcode](http://gccode.ssc-spc.gc.ca/)
2. [Go to the `public-doc` repository project page](http://gccode.ssc-spc.gc.ca/ec-msc/public-doc)
3. Enable watch mode for the repository by selecting `Watch` in the dropdown menu alongside the alarm bell icon

This enables receiving modifications for the entire `public-doc` repository.


# 4 - Updating the documentation

## 4.1 - Getting ready

1. Log to GCcode
    * Go to [the public-doc repository](http://gccode.ssc-spc.gc.ca/ec-msc/public-doc) and ensure you are logged to GCcode
2. Fork the `public-doc` repository
    * Click on `Fork` to fork the `public-doc` repository
    * At the desired location on your local filesystem, run: `git clone http://gccode.ssc-spc.gc.caYOUR-GITLAB-USERNAME/public-doc.git`
3. Configure your fork by specifying the upstream reference:
    * `cd public-doc`
    * `git remote add upstream http://gccode.ssc-spc.gc.ca/ec-msc/public-doc.git`

## 4.2 - Editing the documentation

## 4.2.1 - Markdown requirements

Given we use mkdocs to style the documentation, extra care is required when creating the documentation in Markdown.

* Links:
    * Links must be explicit, a direct link such as `https://foo.bar` won't work with mkdocs, it must be specifically set as a link with `[name or url](url)`
    * Ensure links always use `https://` instead of `http://` whenever available
* Lists:
    * Lists must begin with an empty line before the initial bullet `*`
    * The second level of lists must begin with 4 spaces before the `*`
* Spaces:
    * Do not begin a line with spaces, otherwise this line will be interpreted as a text/code block

## 4.2.2 - Images in the documentation

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
    * Example: an image associated to `https://gccode.ssc-spc.gc.ca/ec-msc/public-doc/tree/master/docs/msc-data/nwp_rdps` is hosted in `https://collaboration.cmc.ec.gc.ca/cmc/cmos/public_doc/msc-data/nwp-rdps/`
* Sandrine and other colleagues at [CMOA](https://wiki.cmc.ec.gc.ca/wiki/CMOA) and Alex have permissions to copy images in those Collaboration folders
    * Send images by email to Sandrine along with the desired path

Adding images to the documentation:
* In the markdown documentation, images are referenced by using `![image alt text](path to image)`

## 4.2.3 - Files in the documentation

Just like [images](#images-in-the-documentation), any file including binary files in the `.pdf` and `.docx` formats need to be hosted on the Collaboration server in the corresponding directory and a link to those files is used in the actual documentation. 

## 4.2.4 - Changes to the licence

Prior applying any change to the [licence accompanying the documentation](licence/), the following must be completed:
* Get formal management approval for the change
* Bump the Licence version number
* Announce changes to the Licence to users
    * e.g. [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) and [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement lists

## 4.3 - Update workflow

1. Sync your fork
    * In a Terminal, while in your `public-doc` fork directory, update your local code with the public-doc source: `git pull upstream master`
2. Create and switch to a 'branch' where you'll make your changes
    * `git checkout -b mybranchname` , where 'mybranchname' should be refer to the changes at stake, examples: 'fix for issue #123', 'gdps-doc-fix', 'new wcps pages'
3. Make changes in the `docs/` folder in your local fork
    * Changes must include the English and French versions of the documentation
4. Update the repository changelog
    * Update the [changelog](changelog.md) with a summary of your changes
5. Update your `public-doc` fork
    * Make certain you're still on the branch you created at step 2 with the `git status` command
    * Commit changes made to your fork with `git commit -a -m "short log explaining changes"`
    * Push branch changes to your fork with `git push -u origin mybranchname` while using the `mybranchname` you created at step 2
6. Validate the resulting documentation in your fork in a browser
    * Go to `http://gccode.ssc-spc.gc.ca/YOUR-GCCODE-USERNAME/public-doc/blob/master/docs/index.md`
    * Validate content in Markdown in both languages
    * Validate breadcrumbs and links ([see 4.2.1](#421-markdown-requirements))
    * Validate table and list layouts
7. Submit a merge request to push the changes to the common repository
    * Go to your fork on GitLab: `http://gccode.ssc-spc.gc.ca/YOUR-GCCODE-USERNAME/public-doc/`
    * Click on 'Merge Requests' on the top-level menu
    * Click on 'New merge request'
    * Select the appropriate branch from your fork (the 'Source branch'), select `master` on the Target branch (ec-msc/public-doc), and then click 'Compare branches and continue'
    * Assign the merge request and click 'Submit merge request'
    * If you're allowed to merge and are confident with the changes, you can click `Merge` right away. Otherwise, followup with the merge request's assignee. Please understand the best practice is to have someone else validate the change before merging
8. Update your fork's master branch
    * Go to your fork master branch: `git checkout master`
    * Update local master with `public-doc` source code: `git pull upstream master`
    * (optional) Push updated master to your fork: `git push`
   
Tips:
    * Use `git status` to learn on which branch you currently are and get additional status info
    * Use `git remote -v` to confirm `origin` and `upstream` are properly set
    * Use `git checkout master` to go back to the master branch of your fork
    

# 5 - Deploying the documentation
  
## 5.1 - Permission requirements
  
The list of colleagues with appropriate permissions to publish on the GitHub repos is found [here](https://github.com/ECCC-MSC/open-data/settings/collaboration): Sandrine for CMOA, Benoit and David for CMOI, and Alex, Tom and Étienne for GODS.

The `eccc-msc` codepen.io account is managed by Étienne.
 
## 5.2 - Getting ready

In order to properly deploy the documentation using [mkdocs](https://www.mkdocs.org/), the user will also need to create a conda environment with Python 3.7 installed. Below is a step-by-step guide for publishing the documentation to the GitHub [eccc-msc/open-data repository](https://github.com/ECCC-MSC/open-data).

Is is a best practice to [review existing open tickets](http://gccode.ssc-spc.gc.ca/ec-msc/public-doc/issues) before proceeding with a documentation deployment.

### 5.2.1 - Install Conda and create a mkdocs virtual environment

Validate if Conda is already installed on your computer. Type `conda --version`. If a Conda version is provided, Conda is installed and skip the installation and go directly to deployment steps at 5.2.2 below. Otherwise, proceed with the Conda installation.

To install Conda, please choose a location in your work environment that has a sufficient amount of disk space. It is not recommended that you install Conda in your home directory due to limited disk space allocated to this directory.

1. Download [miniconda3](https://docs.conda.io/en/latest/miniconda.html) by clicking [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
2. To install, navigate to the folder containing the downloaded file and run `bash Miniconda3-latest-Linux-x86_64.sh`
3. Follow the installation instructions and:
    * accept the License terms
    * indicate a location outside your Linux home directory for the conda installation directory
    * when asked about running the `conda init`, set to `yes`
4. Start a new terminal session so you can access conda commands
5. Run `conda config --set auto_activate_base false`. This makes it so conda does not start by default
6. Create a new conda environment named **mkdocs**: `conda create -n mkdocs python=3.7 && conda activate mkdocs`
7. Use pip to install the mkdocs package: `pip install mkdocs`
8. You can deactivate the environment with `conda deactivate`

### 5.2.2 Update mkdocs

To update mkdocs:

1. Activate conda: `conda activate mkdocs`
2. Validate current version: `mkdocs --version`
    * Compare with [current official mkdocs version](https://github.com/mkdocs/mkdocs/releases)
3. Remove current mkdocs from conda: `pip uninstall mkdocs`
4. Install latest version: `pip install mkdocs`
5. Deactivate the conda environment with `conda deactivate`
 
## 5.3 - Deploy documentation on GitHub with mkdocs

The following instructions take the current documentation version from `https://gccode.ssc-spc.gc.ca/ec-msc/public-doc/` and publish it in the `gh-pages` branch of the `https://eccc-msc.github.io/open-data/` repository to make the documentation available on `https://eccc-msc.github.io/open-data/`.

1. Ensure you have `mkdocs` version 1.1 or newer installed in your `conda` environment (see 5.2.2)
2. In a terminal window, `cd` to the root of your `public-doc` repository fork
    1. Run `git remote -v` and validate that the `github` remote exists, otherwise create it with `git remote add github https://github.com/ECCC-MSC/open-data.git`
3. Pull the current version of the documentation you want to publish: `git pull upstream master`
4. Update the changelog:
    1. Confirm the version number to publish in the [changelog](CHANGELOG.md)
    2. Verify that the version number ($VERSION) tag is available on https://gccode.ssc-spc.gc.ca/ec-msc/public-doc/-/tags
    3. In the [changelog](CHANGELOG.md), update the version publication date and release notes if needed and commit changes made to your fork with `git commit CHANGELOG.md -m "updated changelog for release $VERSION"`
5. Tag the version:
    1. Create the new tag: `git tag $VERSION`
    3. Checkout the newest tag: `git checkout $VERSION`
6. Activate your mkdocs environment: `conda activate mkdocs`
7. Test and validate the documentation:
    1. Run `mkdocs serve`, pay close attention to warnings (if any)
    2. Head to http://127.0.0.1:8000 in a web browser, once validation completed, stop `mkdocs serve` with control-c
    3. If validation succeeded:
        1. Push the tag to upstream: `git push upstream $VERSION`
    4. If validation failed:
        1. Leave conda: `conda deactivate`
        2. Return to master: `git checkout master`
        3. Delete the tag: `git tag -d 2.x.y` where `2.x.y` corresponds to the tag to replace
        4. Make and commit the changes to upstream master
        5. Return to step 2
8. Deploy the documentation on GitHub:
    1. Run `mkdocs gh-deploy --ignore-version --force -m "version 2.x.y"` where `2.x.y` corresponds to the actual version number to publish
        * The user must have the [permissions to push to GitHub](#permission-requirements)
        * Using `--force` is required if another user pushed the previous version to GitHub
9. Verify that the [gh-pages branch was updated on GitHub](https://github.com/ECCC-MSC/open-data) and that the documentation is available and updated at [https://eccc-msc.github.io/open-data](https://eccc-msc.github.io/open-data)
10. Desactivate your mkdocs environment with `conda deactivate` and return to the master branch with `git checkout master`
11. Inform colleagues of the release in the Public Doc channel: https://message.gccollab.ca/group/msc-public-data-documentation
12. If applicable, prepare and send announcement to [dd_info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/dd_info) and [GeoMet-Info](https://lists.ec.gc.ca/cgi-bin/mailman/listinfo/geomet-info) announcement lists based on the [changelog](CHANGELOG.md)
