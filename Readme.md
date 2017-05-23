This is the Adventurer's Codex testing framework for UAT tests.
Python 3 is required.

For the tests to run, please include the drivers in the path envirnonment
variable.

Currently Firefox and Chrome are supported.

The script requires two paramaters:
    * url
    * web_driver

By default, url is https://adventurerscodex.com, and web_driver is chrome

Sample usage:

# always run in verbose mode and no capture (defaults for url and web_driver)
py.test --verbose --capture=no uat_player_tools.py

# with explicit url and web_driver
py.test --verbose --capture=no --web_driver=chrome --url=https://adventurerscodex.com uat_player_tools.py