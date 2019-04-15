# Full stack Web Developer - Udacity - Part 4 ITEM CATALOG PROJECT

<br>

## Overview of Requirements Installation
* Clone the repo with the VM, setup files, and app code.
* Verify Python 3.7 and pip are installed correctly
* Install python 3.7 on your VM
* Install pip for python 3.7
* Install project dependencies
* Check that the database is intact
* Run the appliation and connect to it from the browser
* Optionally run tests to verify code integrity [SHA this?]

<br><br>

## Verify Python 3.7 and pip are installed correctly

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

## Install Project Dependencies, Including pip
Ensure that python 3.7 is installed (see above). From /vagrant/ in your vm execute the following:

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

## Issue Tracking
* ~~Possible issue with foreign keys being disabled by default in sqlite.~~
~~It seems the f_keys should be enabled on a pre-transaction basis.~~
~~Research and tracking required.~~


<br><br><br><br><br><br>