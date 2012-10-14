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
"""adds restructured text directives to docutils
"""

__authors__ = [
    # alphabetical order by last name
    'Thomas Chiroux', ]

from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils import nodes


class todo(nodes.Admonition, nodes.Element):
    """todo node for docutils"""
    pass


class Todo(BaseAdmonition):
    """todo directive for docutils

    uses BaseAdmonition from docutils (like .. note:: of .. warning:: etc..)
    """
    node_class = todo