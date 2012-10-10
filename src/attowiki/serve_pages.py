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
from bottle import request, response

def index():
    """looks for index.rst file and serve it.
    If not found, list all the available files
    """
    index_files = glob.glob("./[Ii][Nn][Dd][Ee][Xx].rst")
    if len(index_files) == 0:
        rst_files = glob.glob("./*.rst")
        return rst_files
    else:
        index = open(index_files[0], 'r')
        return index
    #try:
    #    file_index = open('Index.rst')

def page(name):
    """serve a page name
    """
    print glob.glob("./{0}.rst".format(name))