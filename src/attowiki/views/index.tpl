%include header name=name
<body>
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