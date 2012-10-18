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

def add_node(node, **kwds):
    """add_node from Sphinx
    """
    nodes._add_node_class_names([node.__name__])
    for key, val in kwds.iteritems():
        try:
            visit, depart = val
        except ValueError:
            raise ValueError('Value for key %r must be a '
                                 '(visit, depart) function tuple' % key)
        if key == 'html':
            from docutils.writers.html4css1 import HTMLTranslator as translator
        elif key == 'latex':
            from docutils.writers.latex2e import LaTeXTranslator as translator
        else:
            # ignore invalid keys for compatibility
            continue
        setattr(translator, 'visit_'+node.__name__, visit)
        if depart:
            setattr(translator, 'depart_'+node.__name__, depart)

class todo(nodes.Admonition, nodes.Element):
    """todo node for docutils"""
    pass


def visit_todo(self, node):
    self.visit_admonition(node)


def depart_todo(self, node):
    self.depart_admonition(node)


class Todo(BaseAdmonition):
    """todo directive for docutils

    uses BaseAdmonition from docutils (like .. note:: of .. warning:: etc..)
    """
    optional_arguments = 0
    node_class = todo


class done(nodes.Admonition, nodes.Element):
    """done node for docutils"""
    pass


def visit_done(self, node):
    self.visit_admonition(node)


def depart_done(self, node):
    self.depart_admonition(node)


class Done(BaseAdmonition):
    """done directive for docutils

    uses BaseAdmonition from docutils (like .. note:: of .. warning:: etc..)
    """
    optional_arguments = 0
    node_class = done
