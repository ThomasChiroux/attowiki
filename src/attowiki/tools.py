#! /usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Thomas Chiroux
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.
# If not, see <http://www.gnu.org/licenses/lgpl-3.0.html>
#
"""common tools for the project
"""

__authors__ = [
    # alphabetical order by last name
    'Thomas Chiroux', ]

import os


def attowiki_distro_path():
    """return the absolute complete path where attowiki is located

    .. todo:: use pkg_resources ?
    """
    attowiki_path = os.path.abspath(__file__)
    if attowiki_path[-1] != '/':
        attowiki_path = attowiki_path[:attowiki_path.rfind('/')]
    else:
        attowiki_path = attowiki_path[:attowiki_path[:-1].rfind('/')]
    return attowiki_path
