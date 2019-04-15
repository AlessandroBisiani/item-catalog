# Full stack Web Developer - Udacity - Part 4 ITEM CATALOG PROJECT

<br>


## Overview of Requirements Installation
1. Clone the repo with the VM, setup files, and app code.
1. Verify Python 3.7 and pip are installed correctly
1. Install python 3.7 on your VM
1. Install project dependencies and pip for python 3.7
1. Set up the database
1. Run the appliation and connect to it from the browser

<br><br>


## Clone The Project And Set Up the Virtual Machine
Download and install Vagrant, Virtual Box 5.1, and fork the application repo:

1. Vagrant: [download](https://www.vagrantup.com/downloads.html)
1. VirtualBox 5.1 for your system: [download](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
1. A clone of the project with the vagrant file for setting up the VM. **Fork** the repository, then clone it to a local directory. You'll be working inside this directory from now on: [the repo](https://github.com/AlessandroBisiani/item-catalog).

`cd` into the /vagrant/ directory and run `vagrant up && vagrant ssh`. This will download the necessary components and install the virtual machine, then log you into it. It will take some time.

When you see the prompt, `cd` to "/vagrant/setup" directory.


<br><br>



<br><br>


## Install Python 3.7 on your VM
Perform this step if executing `python3.7` does not start the Python 3.7 interpreter.

Execute the following from inside "/vagrant/setup":

Install Python 3.7 dependencies:
`sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev`

Copy the provided Python 3.7 to the folder it will be installed in:
`sudo cp Python-3.7.2.tgz /usr/src/`

Extract the files:
`sudo tar xzf Python-3.7.2.tgz`

Move into the extracted directory with `cd Python-3.7.2` and execute the following in order:

`sudo ./configure --enable-optimizations`

`sudo make altinstall`

`sudo pip3.7 install --upgrade pip`

<br><br>


## Verify Python 3.7 and pip are installed correctly
`which python3.7` should return:
>

and

`pip3.7 -V` should return:
>pip [VERSION NUMBER] from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

use `sudo pip3.7 install --upgrade pip` to install the latest version of pip

<br><br>


## Install Project Dependencies
Ensure that python 3.7 is installed (see above). From /vagrant/ in your vm execute the following:

<br>

Install **all project dependencies** with the command:

`sudo pip3.7 install flask sqlalchemy httplib2 requests oauth2client`

Dependencies:
* Flask
* SQLAlchemy
* httplib2
* requests
* oauth2client

<br><br>


## Set Up The Database
Run database_setup.py and notes_data.py with the following command:

`python3.7 database_setup.py && python3.7 notes_data.py commit`

<br><br>


## Run the appliation and connect to it from the browser
From the terminal execute `python3.7 notes.py`

Then from your browser navigate to "localhost:5000" to view the index page. Leave the program running in the terminal while you want to access the application.

<br><br>


## Issue Tracking
* ~~Possible issue with foreign keys being disabled by default in sqlite.~~
~~It seems the f_keys should be enabled on a pre-transaction basis.~~
~~Research and tracking required.~~

<br><br><br><br><br><br>