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

Currently Firefox and Chrome are supported.

Usage
=====

The script requires two paramaters:

* url
* web_driver

By default, url is https://nightly.adventurerscodex.com, and web_driver is chrome

Sample usage:

*always run in verbose mode and no capture (no params will default to https://nightly.adventurerscodex.com and chrome web_driver)*

`py.test --verbose --capture=no tests/`

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
