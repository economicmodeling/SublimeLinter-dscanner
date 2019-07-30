#
# linter.py
# Linter for SublimeLinter version 4.
#
# Written by Brian Schott (Hackerpilot)
# Copyright © 2014-2019 Economic Modeling Specialists, Intl.
#
# License: MIT
#

"""This module exports the D-Scanner plugin class."""

from SublimeLinter.lint import Linter, STREAM_STDOUT


class Dscanner(Linter):

    """Provides an interface to dscanner."""

    cmd = ("dscanner", "-S", "${file}")
    regex = r'^.+?\((?P<line>\d+):(?P<col>\d+)\)\[((?P<warning>warn)|(?P<error>error))\]: (?P<message>.+)$'
    multiline = False
    tempfile_suffix = "-"
    word_re = None
    defaults = {
        "selector": "source.d"
    }
    name = "D-Scanner"
