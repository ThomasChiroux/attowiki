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

__authors__ = [
    # alphabetical order by last name
    'Thomas Chiroux', ]

# dependencies imports
import bottle
from git import Repo, InvalidGitRepositoryError
from docutils.parsers.rst import directives
from docutils import nodes, languages

# project imports
from attowiki import views
from attowiki.rst_directives import add_node
from attowiki.rst_directives import todo, visit_todo, depart_todo, Todo
from attowiki.rst_directives import done, visit_done, depart_done, Done
from attowiki.tools import attowiki_distro_path


def main():
    """main entry point

    launches the webserver locally
    """

    # register specific rst directives
    # small trick here: get_language will reveal languages.en
    labels = languages.get_language('en').labels
    # add the label
    languages.en.labels["todo"] = "Todo"
    # add node
    add_node(todo,
             html=(visit_todo, depart_todo),
             latex=(visit_todo, depart_todo),
             text=(visit_todo, depart_todo))
    #nodes._add_node_class_names(['todo'])

    # register the new directive todo
    directives.register_directive('todo', Todo)

    # add the label
    languages.en.labels["done"] = "Done"
    # add node
    add_node(done,
             html=(visit_done, depart_done),
             latex=(visit_done, depart_done),
             text=(visit_done, depart_done))
    #nodes._add_node_class_names(['todo'])

    # register the new directive todo
    directives.register_directive('done', Done)

    # Check if the directory is under git, if not, create the repo
    try:
        Repo()
    except InvalidGitRepositoryError:
        Repo.init()

    # add view path from module localisation
    views_path = attowiki_distro_path() + '/views/'
    bottle.TEMPLATE_PATH.insert(0, views_path)

    app = bottle.Bottle()

    # All the Urls of the project
    # index or __index__
    app.route('/', method='GET')(views.view_page)
    # new page
    app.route('/', method='POST')(views.view_page)
    # meta pages
    app.route('/__index__')(views.view_meta_index)
    app.route('/__cheatsheet__')(views.view_meta_cheat_sheet)
    app.route('/__history__/<gitref>/<name>.__source__')(views.view_history_source)
    app.route('/__history__/<gitref>/<name>.__diff__')(views.view_history_diff)
    app.route('/__history__/<gitref>/<name>')(views.view_history)
    app.route('/__<admonition_name>__')(views.view_meta_admonition)

    # new page
    app.route('/edit/')(views.view_edit)
    # edit an existing page
    app.route('/edit/<name>')(views.view_edit)

    # cancel the edition of an existing page
    app.route('/cancel-edit/')(views.view_cancel_edit)
    app.route('/cancel-edit/<name>')(views.view_cancel_edit)

    # meta page for one single document
    app.route('/<name>.__source__')(views.view_history_source)
    app.route('/<name>.__diff__')(views.view_history_diff)
    app.route('/<name>.__<admonition_name>__')(views.view_meta_admonition)
    # view an existing page
    app.route('/<name>', method='GET')(views.view_page)

    # write new content to an existing page
    app.route('/<name>', method='POST')(views.view_page)
    # write new content to an existing page (without commit - for quick save)
    app.route('/<name>', method='PUT')(views.view_quick_save_page)

    # for devt purpose: set bottle in debug mode
    bottle.debug(True)  # this line may be commented in production mode

    # run locally by default
    from optparse import OptionParser
    cmd_parser = OptionParser(usage="usage: %prog package.module:app")
    cmd_options, cmd_args = cmd_parser.parse_args()
    if len(cmd_args) >= 2:
        host, port = (cmd_args[0] or 'localhost'), (cmd_args[1] or 8080)
    elif len(cmd_args) == 1:
        host, port = (cmd_args[0] or 'localhost'), (8080)
    else:
        host, port = ('localhost'), (8080)
    if ':' in host:
        host, port = host.rsplit(':', 1)
    bottle.run(app, host=host, port=port)
