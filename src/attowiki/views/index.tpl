%include header name=name
<body>
%include header_bar name=name, history=history, gitref=gitref, extended_name=extended_name, is_repo=is_repo, type=type
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