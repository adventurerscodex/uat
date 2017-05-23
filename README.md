What is it?
===========
This is the Adventurer's Codex testing framework for UAT tests.

Requirements
============

* Python 3
* Web Drivers

For the tests to run, please include the drivers in the path envirnonment variable.

Currently Firefox and Chrome are supported.

Usage
=====

The script requires two paramaters:

* url
* web_driver

By default, url is https://adventurerscodex.com, and web_driver is chrome

Sample usage:

*always run in verbose mode and no capture (defaults for url and web_driver)*

`py.test --verbose --capture=no tests/`

*with explicit url and web_driver*

`py.test --verbose --capture=no --web_driver=chrome --url=https://adventurerscodex.com tests/`
