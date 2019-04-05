# Full stack Web Developer - Udacity - Part 4 ITEM CATALOG PROJECT

## Overview of Requirements Installation
* Clone the repo with the VM, setup files, and app code.
* Install python 3.7 on your VM
* Install pip for python 3.7
* Install project dependencies
* Check that the database is intact
* Run the appliation and connect to it from the browser
* Optionally run tests to verify code integrity [SHA this?]

### Install python 3.7 on your VM
`cd` to /vagrant/ and execute the following:

```
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
```


### Install Project Dependencies, including pip
After ensuring that python 3.7 is installed, from /vagrant/ in your vm execute:

* To install pip for python3.7: `sudo python3.7 get-pip.py`

* Verify the installation with `pip3 -V`. It should return something like:

`pip 19.0.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)`

* Other project dependencies:

`sudo pip3 install flask sqlalchemy`



## Issue Tracking
*Possible issue with foreign keys being disabled by default in sqlite.
It seems the f_keys should be enabled on a pre-transaction basis.
Research and tracking required.