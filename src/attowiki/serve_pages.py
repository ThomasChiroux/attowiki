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
from git import Repo, InvalidGitRepositoryError

def index():
    """looks for index.rst file and serve it.
    If not found, list all the available files
    """
    rst_files = [file[2:-4] for file in glob.glob("./*.rst")]
    return template('index', filelist=rst_files, name="__index__")


def check_repo():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        return False
    return True

def commit(filename):
    try:
        repo = Repo()
        index = repo.index
        index.commit("Updated file: {0}".format(filename))
    except:
        pass

def add_file_to_repo(filename):
    try:
        repo = Repo()
        index = repo.index
        index.add([filename])
    except:
        pass

def edit(name=None):
    """edit or creates a new page
    """
    response.set_header('Cache-control', 'no-cache')
    response.set_header('Pragma', 'no-cache')
    if name is None:
        # new page
        return template('edit', name=name, display_name=name,
                        is_repo=check_repo(),
                        content="")
    else:
        files = glob.glob("{0}.rst".format(name))
        if len(files) > 0:
            file = open(files[0], 'r')
            return template('edit', name=name, display_name=name,
                            is_repo=check_repo(),
                            content=file.read())
        else:
            return abort(404)

def page(name=None):
    """serve a page name
    """
    if request.method == 'POST':
        if name is None:
            # new file
            if len(request.forms.filename) > 0:
                name = request.forms.filename

        if name is not None:
            filename = "{0}.rst".format(name)
            file = open(filename, 'w')
            file.write(request.forms.content.encode('utf-8'))
            file.close()
            add_file_to_repo(filename)
            commit(filename)

    response.set_header('Cache-control', 'no-cache')
    response.set_header('Pragma', 'no-cache')
    if name is None:
        # we try to find an index file
        index_files = glob.glob("./[Ii][Nn][Dd][Ee][Xx].rst")
        if len(index_files) == 0:
            # not found
            # redirect to __index__
            name = "__index__"
        else:
            name = index_files[0][2:-4]
    return template('page', name=name, display_name=name, is_repo=check_repo())

def iframe(name):
    """serve the iframe : the html converted rst file
    """
    response.set_header('Cache-control', 'no-cache')
    response.set_header('Pragma', 'no-cache')
    if name == '__index__':
        # we should generate and index page
        return index()
    else:
        files = glob.glob("{0}.rst".format(name))
        if len(files) > 0:
            file = open(files[0], 'r')
            return publish_string(file.read(), writer_name='html')
            #return template('page', page_name=files[0][2:-4],
            #                 page_content=publish_string(file.read(),
            #                                             writer_name='html'))
        else:
            return abort(404)
