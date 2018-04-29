<div style="background-color:#2c3e50;">
<h1 style="text-align: center; margin-top: 0.0em; margin-bottom: 0.5em; padding-bottom:0.3em; font-size: 29px; font-family: HelveticaNeue-Bold; page-break-inside: avoid; page-break-after: avoid; color: rgb(51, 51, 51); font-style: normal; color:white;">
<center><img class="tl-email-image" data-id="455053" height="100" src="https://adventurerscodex.com/images/logo-full-circle.png" style="padding-top: 10px; width: 100px; max-width: 100px;" width="100" /></center>
Welcome to Adventurer&rsquo;s&nbsp;Codex</h1>
</div>

[![Build Status](https://travis-ci.org/adventurerscodex/uat.svg?branch=master)](https://travis-ci.org/adventurerscodex/uat)

Experience the next step in tabletop RPGs

What is it?
===========
This is the Adventurer's Codex testing framework for UAT tests.

Requirements and setup
======================

* Install python 3
* Create a virtual environment
* Install requirements `pip install -r requirements.txt`
* Download chrome and/or firefox webdriver (https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)
* Add path of webdriver executable to PATH environment variable

Current test coverage supports Chrome, Firefox and Safari.

Usage
=====

The script requires two paramaters:

* url
* web_driver

By default, url is https://nightly.adventurerscodex.com, and web_driver is chrome

Sample usage:

*always run in verbose mode and no capture (no params will default to https://nightly.adventurerscodex.com and chrome web_driver)*

`py.test --verbose --capture=no tests/`

*with csv report*

`py.test --verbose --capture=no tests/ --csv tests.csv --csv-columns id,module,name,file,doc,status,message,browser,created_at,duration_formatted`

*with explicit url and web_driver*

`py.test --verbose --capture=no --web_driver=chrome --url=https://nightly.adventurerscodex.com tests/`

*run specific test file*

`py.test --verbose --capture=no tests/core/player_tools/test_player_wizard.py::test_attributes_required`

How to contribute
=================

* fork the repo
* navigate to the uat_docs folder and find a user story to test (focus is player tools first)
* add a test to the appropriate test file in tests/player_tools/
* if no test file exists, make a new test file (be sure that file matches the patter test_*)
* write the test (be sure to inlcude a print statement of the user story in the test, see other tests for example)
* mark the test as complete in the uat_docs folder by appending '[complete]' to the end of the user story
* make a pr
* thanks for the contribution!
