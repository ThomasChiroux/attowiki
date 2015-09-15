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
"""Custom docutils htmlwriter."""

from docutils import nodes
from docutils.writers.html4css1 import Writer, HTMLTranslator


class AttowikiWriter(Writer):
    """Custom Html Writer for attowiki."""

    def __init__(self):
        Writer.__init__(self)
        self.translator_class = AttowikiHTMLTranslator


class AttowikiHTMLTranslator(HTMLTranslator):
    """Custom HtmlTranslator for attowiki.

    adds a 'target="_blank"' to the external links
    """

    def visit_reference(self, node):
        atts = {'class': 'reference'}
        if 'refuri' in node:
            atts['href'] = node['refuri']
            if (self.settings.cloak_email_addresses
               and atts['href'].startswith('mailto:')):
                    atts['href'] = self.cloak_mailto(atts['href'])
                    self.in_mailto = True
            atts['class'] += ' external'
            atts['target'] = '_blank'
        else:
            assert 'refid' in node, \
                   'References must have "refuri" or "refid" attribute.'
            atts['href'] = '#' + node['refid']
            atts['class'] += ' internal'
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts['class'] += ' image-reference'
        self.body.append(self.starttag(node, 'a', '', **atts))
