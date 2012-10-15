%include header name=name
<body onload = "parent.htmlpage.location='/{{name}}.__iframe__'">
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
{{!content}}
</body>
</html>
