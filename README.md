What is it?
===========
This is the Adventurer's Codex testing framework for UAT tests.

Requirements and setup
======================

* Install python 3
* Install requirements `pip install -r requirements.txt`
* Download chrome and/or firefox webdriver (https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)
* Add path of webdriver executable to PATH environment variable

Currently Firefox and Chrome are supported.

Usage
=====

The script requires two paramaters:

* url
* web_driver

By default, url is https://adventurerscodex.com, and web_driver is chrome

Sample usage:

*always run in verbose mode and no capture (no params will default to https://adventurerscodex.com and chrome web_driver)*

`py.test --verbose --capture=no tests/`

*with explicit url and web_driver*

`py.test --verbose --capture=no --web_driver=chrome --url=https://adventurerscodex.com tests/`
