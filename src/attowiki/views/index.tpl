%include header name=name
<body>
<div class="header header_view">
    <div class="text">
        [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:<a href="/{{name}}">{{name}}</a>
    </div>
%if not is_repo:
    <span class="warning">WARNING: no git repository found !!</span>
%end
    <div class="buttons">
        <a href="/edit/" id="btn_new">new page</a>
        %if name != '__index__':
        <a href="/edit/{{name}}" id="btn_edit">edit</a>
        %end
    </div>
</div>
Meta pages:
<ul>
    <li><a target="_blank" href="__cheatsheet__">__cheatsheet__</a> (reST cheat sheet)</li>
    <li><a target="_parent" href="__index__">__index__</a> (this page)</li>
    <li><a target="_parent" href="__todo__">__todo__</a> (list all todos for this directory)</li>
</ul>

Pages:
<ul>
%for file in filelist:
        <li><a target="_parent" href="{{file}}">{{file}}</a></li>
%end
</ul>
</body>
</html>