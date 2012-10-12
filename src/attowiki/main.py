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
"""file for main entry point
"""
import os
import bottle
from git import Repo,InvalidGitRepositoryError

import serve_pages

def main():
    """main entry point

    launches the webserver locally
    """
    # Check if the directory is under git, if not, create the repo
    try:
        Repo()
    except InvalidGitRepositoryError:
        Repo.init()

    # add view path from module localisation
    # todo: use pkg_resources ?
    views_path = os.path.abspath(__file__)
    if views_path[-1] != '/':
        views_path = views_path[:views_path.rfind('/')]
    else:
        views_path = views_path[:views_path[:-1].rfind('/')]
    views_path = views_path + '/views/'
    print views_path
    bottle.TEMPLATE_PATH.insert(0, views_path)

    app = bottle.Bottle()
    # Mission
    app.route('/', method='GET')(serve_pages.page)
    app.route('/', method='POST')(serve_pages.page)
    app.route('/edit/')(serve_pages.edit)
    app.route('/edit/<name>')(serve_pages.edit)
    app.route('/<name>.__iframe__', method='GET')(serve_pages.iframe)
    app.route('/<name>', method='GET')(serve_pages.page)
    app.route('/<name>', method='POST')(serve_pages.page)

    bottle.debug(True)
    bottle.run(app, host='localhost', port=8080)
