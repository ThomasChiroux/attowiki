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

import glob
# dependencies imports
from bottle import request, response, template, abort
from docutils.core import publish_string

def index():
    """looks for index.rst file and serve it.
    If not found, list all the available files
    """
    index_files = glob.glob("./[Ii][Nn][Dd][Ee][Xx].rst")
    if len(index_files) == 0:
        rst_files = [file[2:-4] for file in glob.glob("./*.rst")]
        return template('index', filelist=rst_files)
    else:
        file = open(index_files[0], 'r')
        return publish_string(file.read(), writer_name='html')
        #return template('page', page_name="index",
        #                page_content=publish_string(file.read(),
        #                                            writer_name='html'))


def page(name):
    """serve a page name
    """
    files = glob.glob("{0}.rst".format(name))
    print files
    if len(files) > 0:
        file = open(files[0], 'r')
        return publish_string(file.read(), writer_name='html')
        #return template('page', page_name=files[0][2:-4],
        #                 page_content=publish_string(file.read(),
        #                                             writer_name='html'))
    else:
        return abort(404)