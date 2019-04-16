# Full stack Web Developer - Udacity - Part 4 ITEM CATALOG PROJECT

<br>


## Overview of Requirements Installation
1. Clone the repo with the VM, setup files, and app code.
1. Verify Python 3.7 and pip are installed correctly
1. Install python 3.7 on your VM
1. Install project dependencies and pip for python 3.7
1. Set up the database
1. Run the appliation and connect to it from the browser
1. Optionally run tests to verify code integrity [SHA this?]

<br><br>


## Clone The Project And Set Up the Virtual Machine
Download and install Vagrant, Virtual Box 5.1, and fork the application repo:

1. Vagrant: [download](https://www.vagrantup.com/downloads.html)
2. VirtualBox 5.1 for your system: [download](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3. A clone of the project with the vagrant file for setting up the VM. **Fork** the repository, then clone it to a local directory. You'll be working inside this directory from now on: [the repo](https://github.com/udacity/fullstack-nanodegree-vm).

<br><br>


## Install Python 3.7 on your VM
Perform this step if executing `python3.7` does not start the Python 3.7 interpreter.

`cd` to /vagrant/ and execute the following:

Install Python 3.7 dependencies:
`sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev`

Copy the provided Python 3.7 to the folder it will be installed in:
`sudo cp Python-3.7.2.tgz /usr/src/`

Extract the files:
`sudo tar xzf Python-3.7.2.tgz`

Move into the extracted directory and execute in order:

`cd Python-3.7.2`

`sudo ./configure --enable-optimizations`

`sudo make altinstall`

<br><br>


## Install Project Dependencies, Including pip for Python 3.7
If you installed Python 3.7 from the above, you shouldn't need to reinstall pip for it. If not, you can do so by executin the following from /vagrant/ in your vm:

<br>

To install pip **for python3.7**:

`sudo python3.7 get-pip.py`

<br>

**Verify the installation** refers to python 3.7 with `pip3 -V`. It should return something like:
>`pip 19.0.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)`

<br>


Install **other project dependencies** with the command:

`sudo pip3 install flask sqlalchemy httplib2 requests`

Dependencies:
* Flask
* SQLAlchemy
* httplib2
* requests

<br><br>


## Set Up The Database
Run database_setup.py and notes_data.py

`python3.7 database_setup.py && python3.7 notes_data.py commit`

<br><br>


## Run the appliation and connect to it from the browser
From the terminal execute `python3.7 notes.py`

Then from your browser navigate to "localhost:5000" to view the index page.

<br><br>


## Issue Tracking
* ~~Possible issue with foreign keys being disabled by default in sqlite.~~
~~It seems the f_keys should be enabled on a pre-transaction basis.~~
~~Research and tracking required.~~

<br><br><br><br><br><br>