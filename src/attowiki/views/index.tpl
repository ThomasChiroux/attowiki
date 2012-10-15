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
Main Meta pages:
<ul>
    <li><a target="_parent" href="/__index__">__index__</a> (this page)</li>
    <li><a target="_blank" href="/__cheatsheet__">__cheatsheet__</a> (reST cheat sheet)</li>
    <li><a target="_parent" href="/__todo__">__todo__</a> (list all todo admonitions for this directory)</li>
    <li><a target="_parent" href="/__done__">__done__</a> (list all done admonitions for this directory)</li>
</ul>

Pages:
<ul>
%for file in filelist:
        <li><a target="_parent" href="{{file}}">{{file}}</a></li>
%end
</ul>

Other Meta pages:
<ul>
    <li><a target="_parent" href="/__attention__">__attention__</a></li>
    <li><a target="_parent" href="/__caution__">__caution__</a></li>
    <li><a target="_parent" href="/__danger__">__danger__</a></li>
    <li><a target="_parent" href="/__error__">__error__</a></li>
    <li><a target="_parent" href="/__hint__">__hint__</a></li>
    <li><a target="_parent" href="/__important__">__important__</a></li>
    <li><a target="_parent" href="/__note__">__note__</a></li>
    <li><a target="_parent" href="/__tip__">__tip__</a></li>
    <li><a target="_parent" href="/__warning__">__warning__</a></li>
    <li><a target="_parent" href="/__admonition__">__admonition__</a></li>
</ul>

</body>
</html>