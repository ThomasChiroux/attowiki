<div class="header header_{{type}}">
    <div class="text">
        %if type == 'edit':
            %if name is None:
                [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:
            %else:
                [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:<a href="/{{name}}">{{name}}</a>
            %end
        %else:
            %if extended_name is None:
                [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:<a href="/{{name}}">{{name}}</a>
            %else:
                [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:<a href="/{{name}}">{{name}}</a>:{{extended_name}}
            %end
        %end
    </div>
    %if not is_repo:
        <span class="warning">WARNING: no git repository found !!</span>
    %end
    %if len(history) > 0:
        <div class="buttons">
            %if gitref is not None:
                %if extended_name is not None:
                    <a href="/__history__/{{gitref}}/{{name}}" id="btn_html">H</a>
                    %if extended_name != '__diff__':
                        <a href="/__history__/{{gitref}}/{{name}}.__diff__" id="btn_diff">D</a>
                    %end
                    %if extended_name != '__source__':
                    <a href="/__history__/{{gitref}}/{{name}}.__source__"  id="btn_source">S</a>
                    %end
                %else:
                    <a href="/__history__/{{gitref}}/{{name}}.__diff__" id="btn_diff">D</a>
                    <a href="/__history__/{{gitref}}/{{name}}.__source__"  id="btn_source">S</a>
                %end
            %else:
                %if extended_name is not None:
                    <a href="/{{name}}" id="btn_html">H</a>
                %else:
                    <a href="/{{name}}.__source__"  id="btn_source">S</a>
                %end
            %end
        </div>
        <div class="history">
            <select name="history" id="history"
                %if extended_name is None:
                onchange="window.location.assign(this.value+'/{{name}}')">
                <option value="">--- current version ---</option>
                %else:
                onchange="window.location.assign(this.value+'/{{name}}.{{extended_name}}')">
                %end


                %for element in history:
                    <option value="/__history__/{{element['hexsha']}}"
                    %if gitref == element['hexsha']:
                        selected="selected"
                    %end
                    >{{element['date']}}
                    </option>
                %end
            </select>
        </div>
    %end

    <div class="buttons">
        %if type == 'edit':
            %if name is None:
                <a href="/cancel-edit/" id="btn_cancel">cancel</a>
            %else:
                 <a href="/cancel-edit/{{name}}" id="btn_cancel">cancel</a>
            %end
            <a href="#" id="btn_save" onclick="document.forms['page_edit'].submit();">save</a>
        %else:
            <a href="/edit/" id="btn_new">new page</a>
            %if not name.startswith('__') and gitref is None:
                <a href="/edit/{{name}}" id="btn_edit">edit</a>
                <a href="/pdf/{{name}}" id="btn_pdf">pdf</a>
            %end

        %end
    </div>
</div>
