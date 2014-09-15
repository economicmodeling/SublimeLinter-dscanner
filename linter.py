#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Brian Schott (Hackerpilot)
# Copyright © 2014 Economic Modeling Specialists, Intl.
#
# License: MIT
#

"""This module exports the D-Scanner plugin class."""

from SublimeLinter.lint import Linter, util


class Dscanner(Linter):

    """Provides an interface to dscanner."""

    syntax = 'd'
    cmd = 'dscanner -S'
    executable = None
    version_args = '--version'
    version_re = r'^.*(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'
    regex = r'^.+?\((?P<line>\d+):(?P<col>\d+)\)\[((?P<warning>warn)|(?P<error>error))\]: (?P<message>.+)$'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = "d.temp"
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
