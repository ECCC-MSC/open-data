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
        * [Updates to Jupyter Notebooks](#424-updates-to-jupyter-notebooks)
        * [Changes to the Licence](#425-changes-to-the-licence)
    * [Update workflow](#43-update-workflow)
    * [GitHub content update](#44-github-content-update)
5. [Deploying the documentation](#5-deploying-the-documentation)
    * [Permission requirements](#51-permission-requirements)
    * [Getting ready](#52-getting-ready)
    * [Deployment to GitHub Pages with mkdocs](#53-deploy-documentation-on-github-with-mkdocs)

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

Files are stored on GCcode, in the public-doc repository: https://gccode.ssc-spc.gc.ca/ec-msc/public-doc/ . A copy is publicly available on GitHub at https://github.com/ECCC-MSC/open-data

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
    * Go to [the public-doc repository](https://gccode.ssc-spc.gc.ca/ec-msc/public-doc) and ensure you are logged to GCcode
2. Fork the `public-doc` repository
    * Click on `Fork` to fork the `public-doc` repository
    * At the desired location on your local filesystem, run: `git clone https://gccode.ssc-spc.gc.ca/YOUR-GITLAB-USERNAME/public-doc.git`
3. Configure your fork by specifying the upstream reference:
    * `cd public-doc`
    * `git remote add upstream https://gccode.ssc-spc.gc.ca/ec-msc/public-doc.git`
4. Add a remote reference to the GitHub repository:
    * `git remote add github https://github.com/ECCC-MSC/open-data.git`
5. [Setup an SSH key](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/checking-for-existing-ssh-keys) for GitHub access
    * Open Git Bash application (if on Windows) and check for existing SSH keys with the `cat ~/.ssh/known_hosts | grep github` command. If an output comes out, a SSH key already exists and you can skip to the 4.2 section of this document.
    * Generate a new SSH key with the command `ssh-keygen -t ed25519 -C "your_email@example.com"` (Replace `your_email@example.com` with the email address associated with your GitHub account) and press the Enter key when a message pops up
    * Copy the whole content of the newly create public key. You can use a command like `cat .ssh/id_ed25519.pub` to see the content of the key (change `.ssh/id_ed25519.pub` in the command by the path specified in the output of the previous command above)
    * Go on the [Github Settings page](https://github.com/settings/keys). Then, click on `New SSH Key` and fill the blanks. The `Key` field should contain the content of the key retrieved in the previous step.
    * Click on the `Add SSH key` button
    * You can then test if everything works on Git Bash by running the command `ssh -T git@github.com`, and answering `yes` to the message coming up on Git Bash (`Are you sure you want to continue connecting (yes/no/[fingerprint])`)

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

## 4.2.4 - Updates to Jupyter Notebooks

To update the Jupyter Notebooks in the documentation:

1. [Install Jupyter Notebook](https://jupyter.org)
2. Launch Jupyter Notebook and edit the target notebook
3. Commit and push changes as usual

Note: if you need to move or rename the Jupyter Notebooks, the live examples in mybinder.org will need to the updated accordingly.

## 4.2.5 - Changes to the licence

Prior applying any change to the [licence accompanying the documentation](licence/), the following must be completed:
* Get formal management approval for the change
* Bump the Licence version number
* Announce changes to the Licence to users
    * e.g. [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) and [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement lists

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

## 4.4 - GitHub content update

To accommodate remote students, in the spirit of 'open by default' and to allow outside contributions, the `master` branch of this repository is available on GitHub in addition to the `gh-pages` branch required for GitHub Pages. Given the main repository remains the internal GCcode one, it is important to keep the `master` branch on GitHub in sync when changes are known to be made to it.

1. Retrieve the latest GCcode version: `git pull upstream master`
2. Update the GitHub version with the GCcode one: `git push github master`

For changes committed and merged on GitHub's `master` branch, retrieve the version on GitHub and push the changes to GCcode:
1. `git pull github master`
2. `git push upstream master`

Pull current GCcode version before making changes and commit and merge changes often to avoid conflicts.


# 5 - Deploying the documentation

## 5.1 - Permission requirements

The list of colleagues with appropriate permissions to publish on the GitHub repos is found [here](https://github.com/ECCC-MSC/open-data/settings/collaboration): Sandrine for CMOA, Benoit and David for CMOI, and Alex, Tom, Étienne and Félix for GODS.

The `eccc-msc` codepen.io account is managed by Étienne.

## 5.2 - Getting ready

In order to properly deploy the documentation using [mkdocs](https://www.mkdocs.org/), the user will also need to create a conda environment with Python 3.7 installed. Below is a step-by-step guide for publishing the documentation to the GitHub [eccc-msc/open-data repository](https://github.com/ECCC-MSC/open-data).

It is a best practice to [review existing open tickets](http://gccode.ssc-spc.gc.ca/ec-msc/public-doc/issues) before proceeding with a documentation deployment.

### 5.2.1 - Install Conda and create a mkdocs virtual environment

This process is known to work on (a) CMC Linux machines on the EC network and (b) on the `ppp4` machine on the Science network. It does _not_ work on `joule`.

Validate if Conda is already installed on your computer. Type `conda --version`. If a Conda version is provided, Conda is installed and skip the installation and go directly to deployment steps at 5.2.2 below. Otherwise, proceed with the Conda installation.

To install Conda, please choose a location in your work environment that has a sufficient amount of disk space. It is not recommended that you install Conda in your home directory due to limited disk space allocated to this directory.

1. Download [miniconda3](https://docs.conda.io/en/latest/miniconda.html) by clicking [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) or on the console, running `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
2. To install, navigate to the folder containing the downloaded file and run `bash Miniconda3-latest-Linux-x86_64.sh`
3. Follow the installation instructions and:
    * accept the License terms
    * indicate a location outside your Linux home directory for the conda installation directory
    * when asked about running the `conda init`, set to `yes`
4. Start a new terminal session so you can access conda commands
5. Run `conda config --set auto_activate_base false`. This makes it so conda does not start by default
6. Create a new conda environment named **mkdocs**: `conda env create -f public-doc-environment.yml`.
7. To activate the environment run the `conda activate mkdocs` command. Once activated, you can deactivate the environment with `conda deactivate`.

### 5.2.2 - Removing an existing conda environment

If you ever need to recreate your environment from scratch you may remove the environment.

1. Deactivate your current environment if it is the one you wish to delete
2. Remove the environment with `conda remove --name mkdocs --all`
3. Follow the instructions above to recreate your mkdocs virtual environment

## 5.3 - Deploy documentation on GitHub.io

The following instructions show how to deploy the documentation on GitHub Pages. This process is now automated via a GitHub Action triggered when a new GitHub release is created.

1. Ensure the ECCC-MSC/open-data repository is up to date with the latest changes from the GCcode repository
    * `git pull upstream master`
    * `git push github master`
2. Create a new tag and release via the [GitHub UI](https://github.com/ECCC-MSC/open-data/releases/new):
    * Click `Choose a tag` and type the version number and the `+ Create new tag: <version number>`.
    * Add the release version number as the title and a description for the release.
    * Optionally, you can save a draft of the release by clicking `Save draft` and come back to it later.
    * When ready to publish the release, click `Publish release`. This will trigger the GitHub Action to automatically deploy the documentation
4. Verify that the triggerring of the GitHub Action was successful by checking the [Actions tab](https://github.com/ECCC-MSC/open-data/actions). Within a minute or two, two new jobs should appear, one with the name of the release and the other with the name `pages build and deployment`. When both have green checkmarks, the deployment is complete and should be available at [https://eccc-msc.github.io/open-data/](https://eccc-msc.github.io/open-data/).
5. Inform colleagues of the release in the Public Doc channel: https://message.gccollab.ca/group/msc-public-data-documentation
6. If applicable, prepare and send announcement to [dd_info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/dd_info/) and [GeoMet-Info](https://comm.collab.science.gc.ca/mailman3/postorius/lists/geomet-info/) announcement lists based on the [changelog](CHANGELOG.md)
