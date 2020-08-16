# coursenotes

Our shared repository of course notes and exercises.  
Many of the exercises are set up to run in jupyter lab.  
The readme of this repo explains how to install and run jupyter.

## To use the repo

* Clone this repo
* Fetch updates at least weekly
* Make a branch and a merge request for adding materials


### To use the jupyter notebooks
  * You can install locally and run off your own machine:
      * You can pull the docker image our docker image and run jupyter on that
      * you can install jupyter locally on your machine (no docker required)
      * use jupyter.socs.uoguelph.ca (setup instructions below)

### Docker Option
####  install Docker (docker.com)
  *  from a command line: docker pull socsguelph/jupyter-java
  * If you are on windows you will have to tell docker desktop that it can share your local drive.  OS/X just does this.

#### to run Jupyter  
  *  cd to the directory that you wish to read in jupyter (probably your fork of this repo)
  * You have a choice of how to run Jupyter
    * I put a python3 script in the root of the repo that will run it:  jupyter.py
    * You can run it manually:
        docker run -p 8888:8888 -v "${PWD}:/home/jovyan/coursenotes" socsguelph/jupyter-java start.sh jupyter lab
  *  point your browser at the  URI that is provided after the above command runs

### Install Locally option (no docker)
   
  1. Install Anaconda (makes everything simpler): https://www.anaconda.com/distribution/
  2. Install Jupyter Lab: conda install -c conda-forge jupyterlab
  	* https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
  3. Install beakerx:  conda install -c conda-forge ipywidgets beakerx
  	* http://beakerx.com/
  4. CD to the directory with the git repo in it and type: jupyter lab

### Run on remote server option

1. #### Set up folder for notebooks:  Do these steps ONCE only. 
	1. ssh to jupyter.socs.uoguelph.ca
	1. Log in with your central login credentials
	1. In your home directory make a subfolder called notebooks
		- mkdir notebooks
	1. CD to the jupyter home directory for you
		- cd /srv/jupyterhub/yourloginname
	1. Make a symbolic link back to the subdirectory that you just made in your home folder
		- ln -s /home/student/yourloginname/notebooks notebooks
	1. logout of the ssh
1. #### Add a repository to your notebook collection
	1. ssh to linux.socs.uoguelph.ca
		- you can do this step logged in to jupyter.socs if you want
	1. cd to the notebooks subdirectory that you made
	1. clone the git repo that you want to display in jupyter
		- or make a folder for a notebook that you just want to create from scratch
1. #### View your notebook collection
	1. Point your browser at jupyter.socs.uoguelph.ca
	1. Log in with your central login credentials
	1. click on 'notebooks' in the left hand panel
	1. You should see your notebook collection
