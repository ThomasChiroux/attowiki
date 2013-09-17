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
"""use rst2pdf to produce a pdf file based on the given rst content
"""
import string
import random
import os

from rst2pdf.createpdf import RstToPdf


def produce_pdf(rst_content=None, doctree_content=None, filename=None):
    """produce a pdf content based of a given rst content

    If filename is given, it will store the result using the given filename
    if no filename is given, it will generate a pdf in /tmp/ with a random
    name
    """
    if filename is None:
        filename = os.path.join(
            "/tmp", ''.join([random.choice(string.ascii_letters +
            string.digits) for n in range(15)]) + '.pdf')
    r2p = RstToPdf(stylesheets=['pdf.style'],
                   style_path=[os.path.join(os.path.dirname(__file__),
                                            'styles')],
                   breaklevel=0,
                   splittables=True,
                   footer="""###Title### - ###Page###/###Total###""")
    r2p.createPdf(text=rst_content,
                  doctree=doctree_content,
                  output=filename)
    return filename
