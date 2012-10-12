%include header name=name
<body>
<div class="header header_edit">
    <div class="text">
%if name is None:
        [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:
%else:
        [<a href="/__index__">i</a>]:<a href="/">attowiki</a>:<a href="/{{display_name}}">{{display_name}}</a>
%end
    </div>
%if not is_repo:
    <span class="warning">WARNING: no git repository found !!</span>
%end
    <div class="buttons">
        <a href="#" id="btn_cancel" onclick="history.back()">cancel</a>
        <a href="#" id="btn_save" onclick="document.forms['page_edit'].submit();">save</a>
    </div>
</div>
<div style="width: 100%;position: absolute;top: 21px;left: 0px;bottom: 0;">

%if name is None:
        <form name="page_edit" method="post" action="/">
        filename: <input name="filename" size="20"></input>
%else:
        <form name="page_edit" method="post" action="/{{display_name}}">
%end
        <textarea name="content" cols="80" rows="40" style="height:100%; width:100%">{{content}}</textarea>

    </form>
</div>
</body>
</html>
