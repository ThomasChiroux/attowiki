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
"""bottle views for attowiki
"""

__authors__ = [
    # alphabetical order by last name
    'Thomas Chiroux', ]


import glob
import datetime

# dependencies imports
from bottle import request, response, template, abort, redirect
import docutils
from docutils.core import publish_string, publish_parts
from docutils.writers.html4css1 import Writer as HisWriter
from docutils import io, nodes
from git import Repo, InvalidGitRepositoryError

# project imports
from attowiki.tools import attowiki_distro_path
from attowiki.rstdirective_todo import todo


def check_repo():
    """checks is local git repo is present or not

    Keywords Arguments:
        <none>

    Returns:
        boolean -- True if git repo is present, False if not
    """
    try:
        Repo()
    except InvalidGitRepositoryError:
        return False
    return True


def commit(filename):
    """Commit (git) a specified file

    This method does the same than a ::

        $ git commit -a "message"

    Keyword Arguments:
        :filename: (str) -- name of the file to commit

    Returns:
        <nothing>
    """
    try:
        repo = Repo()
        #gitcmd = repo.git
        #gitcmd.commit(filename)
        index = repo.index
        index.commit("Updated file: {0}".format(filename))
    except Exception:
        pass


def add_file_to_repo(filename):
    """Add a file to the git repo

    This method does the same than a ::

        $ git add filename

    Keyword Arguments:
        :filename: (str) -- name of the file to commit

    Returns:
        <nothing>
    """
    try:
        repo = Repo()
        index = repo.index
        index.add([filename])
    except Exception:
        pass


def reset_to_last_commit():
    """reset a modified file to his last commit status

    This method does the same than a ::

        $ git reset --hard

    Keyword Arguments:
        <none>

    Returns:
        <nothing>
    """
    try:
        repo = Repo()
        gitcmd = repo.git
        gitcmd.reset(hard=True)
    except Exception:
        pass

def view_meta_cheat_sheet():
    """Display a cheat sheet of reST syntax
    """
    response.set_header('Content-Type', 'text')
    return template('rst_cheat_sheet')

def view_meta_index():
    """List all the available .rst files in the directory

    view_meta_index is called by the 'meta' url : /__index__
    """
    rst_files = [filename[2:-4] for filename in sorted(glob.glob("./*.rst"))]
    rst_files.reverse()
    return template('index',
                    filelist=rst_files,
                    name="__index__",
                    is_repo=check_repo())


def view_meta_todos():
    """List all todos from all the rst files found in directory

    view_meta_todos is called by the 'meta' url: /__todos__
    """
    doc2_content=""

    doc2_output, doc2_pub = docutils.core.publish_programmatically(
                                source_class=io.StringInput,
                                source=doc2_content,
                                source_path=None,
                                destination_class=io.StringOutput,
                                destination=None, destination_path=None,
                                reader=None, reader_name='standalone',
                                parser=None, parser_name='restructuredtext',
                                writer=HisWriter(), writer_name=None,
                                settings=None, settings_spec=None,
                                settings_overrides=None,
                                config_section=None,
                                enable_exit_status=False)

    section1 = nodes.section("todo_list_file")
    doc2_pub.reader.document.append(section1)
    title1 = nodes.title("TODO LIST", "TODO LIST")
    doc2_pub.reader.document.append(title1)
    rst_files = [filename[2:-4] for filename in sorted(glob.glob("./*.rst"))]
    rst_files.reverse()
    for file in rst_files:
        file_title = False
        file_handle = open(file + '.rst', 'r')
        file_content = file_handle.read()
        file_handle.close()
        file_content = file_content.decode('utf-8')

        output, pub = docutils.core.publish_programmatically(
            source_class=io.StringInput, source=file_content,
            source_path=None,
            destination_class=io.StringOutput,
            destination=None, destination_path=None,
            reader=None, reader_name='standalone',
            parser=None, parser_name='restructuredtext',
            writer=None, writer_name='html',
            settings=None, settings_spec=None,
            settings_overrides=None,
            config_section=None,
            enable_exit_status=False)

        my_settings = pub.get_settings()
        parser = docutils.parsers.rst.Parser()
        document = docutils.utils.new_document('test', my_settings)
        parser.parse(file_content, document)
        for node in document.traverse(todo):  # docutils.nodes.note):  # todo):
            if not file_title:
                file_title = True
                # new section
                section2 = nodes.section(file)
                doc2_pub.reader.document.append(section2)
                # add link to the originating file
                paragraph = nodes.paragraph()
                file_target = nodes.target(ids=[file],
                                           names=[file],
                                           refuri="/"+file)
                file_ref = nodes.reference(file, file,
                                           name=file,
                                           refuri="/"+file)
                paragraph.append(nodes.Text("in "))
                paragraph.append(file_ref)
                paragraph.append(file_target)
                paragraph.append(nodes.Text(":"))
                doc2_pub.reader.document.append(paragraph)
                #doc2_pub.reader.document.append(file_target)

            doc2_pub.reader.document.append(node)
        doc2_pub.apply_transforms()

    doc2_pub.writer.write(doc2_pub.document, doc2_pub.destination)
    doc2_pub.writer.assemble_parts()
    return template('page',
                    name='__todo__',
                    is_repo=check_repo(),
                    content=doc2_pub.writer.parts['html_body'])



def view_cancel_edit(name=None):
    """cancel the edition of an existing page and render the last modification
    status

    .. note:: this is a bottle view

    if no page name is given, do nothing (it may leave some .tmp. files in
    the directory).

    Keyword Arguments:
        :name: (str) -- name of the page (OPTIONAL)

    Returns:
        bottle response object
    """
    if name is None:
        return redirect('/')
    else:
        files = glob.glob("{0}.rst".format(name))
        if len(files) > 0:
            reset_to_last_commit()
            return redirect('/'+name)
        else:
            return abort(404)


def view_edit(name=None):
    """edit or creates a new page

    .. note:: this is a bottle view

    if no page name is given, creates a new page.

    Keyword Arguments:
        :name: (str) -- name of the page (OPTIONAL)

    Returns:
        bottle response object
    """
    response.set_header('Cache-control', 'no-cache')
    response.set_header('Pragma', 'no-cache')
    if name is None:
        # new page
        return template('edit',
                        name=name,
                        is_repo=check_repo(),
                        today=datetime.datetime.now().strftime("%Y%m%d"),
                        content="")
    else:
        files = glob.glob("{0}.rst".format(name))
        if len(files) > 0:
            file_handle = open(files[0], 'r')
            return template('edit',
                            name=name,
                            is_repo=check_repo(),
                            today=datetime.datetime.now().strftime("%Y%m%d"),
                            content=file_handle.read())
        else:
            return abort(404)


def view_page(name=None):
    """serve a page name

    .. note:: this is a bottle view

    * if the view is called with the POST method, write the new page
      content to the file, commit the modification and then display the
      html rendering of the restructured text file

    * if the view is called with the GET method, directly display the html
      rendering of the restructured text file

    This view dot not render the .rst file directly: it display a small
    header at the top of the page and an iframe below which is directed
    to a meta page : name.__iframe__ (see :func:`view_iframe` for more infos)

    Keyword Arguments:
        :name: (str) -- name of the rest file (without the .rst extension)
                        OPTIONAL

    if no filename is given, first try to find a "index.rst" file in the
    directory and serve it. If not found, serve the meta page __index__

    Returns:
        bottle response object
    """
    if request.method == 'POST':
        if name is None:
            # new file
            if len(request.forms.filename) > 0:
                name = request.forms.filename

        if name is not None:
            filename = "{0}.rst".format(name)
            file_handle = open(filename, 'w')
            file_handle.write(request.forms.content.encode('utf-8'))
            file_handle.close()
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
            return view_meta_index()
        else:
            name = index_files[0][2:-4]

    files = glob.glob("{0}.rst".format(name))
    if len(files) > 0:
        file_handle = open(files[0], 'r')
        html_body = publish_parts(file_handle.read(),
                                   writer=HisWriter(),
                                   settings=None,
                                   settings_overrides=None)['html_body']
        return template('page',
                        name=name,
                        is_repo=check_repo(),
                        content=html_body)
    else:
        return abort(404)


def view_quick_save_page(name=None):
    """quick save a page

    .. note:: this is a bottle view

    * this view must be called with the PUT method
      write the new page content to the file, and not not commit or redirect

    Keyword Arguments:
        :name: (str) -- name of the rest file (without the .rst extension)

    Returns:
        bottle response object (200 OK)
    """
    response.set_header('Cache-control', 'no-cache')
    response.set_header('Pragma', 'no-cache')
    if request.method == 'PUT':
        if name is None:
            # new file
            if len(request.forms.filename) > 0:
                name = request.forms.filename

        if name is not None:
            filename = "{0}.rst".format(name)
            file_handle = open(filename, 'w')
            content = request.body.read()
            content = content.decode('utf-8')
            file_handle.write(content.encode('utf-8'))
            file_handle.close()
            return "OK"
        else:
            return abort(404)
