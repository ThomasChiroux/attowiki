<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
%if name is None:
    <title>edition</title>
%else:
    <title>{{display_name}} edition</title>
%end
    <style type="text/css">
        html {height:100%}
        body {
            margin:0;
            height:100%;
            overflow:hidden;
        }

        .header {
            background-color: #ff8532;
            width: 100%;
            height: 20px;
            font-family:monospace;
            font-size: 12px;
            border-bottom-style:solid;
            border-width: 1px;
        }

        .header .text {
            padding-top:2px;
            padding-left:4px;
            color:#ff0000;
        }

        .header .buttons a {
            background-color:#ededed;
            -moz-border-radius:6px;
            -webkit-border-radius:6px;
            border-radius:6px;
            border:1px solid #dcdcdc;
            display:inline-block;
            color:#777777;
            font-family:monospace;
            font-size:10px;
            font-weight:bold;
            padding:2px 10px;
            height: 10px;
            text-decoration:none;
            text-shadow:1px 1px 0px #ffffff;
        }

        .header .buttons a:hover {
            background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #ededed), color-stop(1, #dfdfdf) );
            background:-moz-linear-gradient( center top, #ededed 5%, #dfdfdf 100% );
            filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ededed', endColorstr='#dfdfdf');
            background-color:#dfdfdf;
        }

        .header .buttons a:active {
            background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #dfdfdf), color-stop(1, #ededed) );
            background:-moz-linear-gradient( center top, #dfdfdf 5%, #ededed 100% );
            filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#dfdfdf', endColorstr='#ededed');
            color:#0000ff;
        }

        #btn_new {
            position:absolute;
            right:60px;
            top:2px;
        }

        #btn_edit {
            position:absolute;
            right:5px;
            top:2px;
        }

        #btn_cancel {
            position:absolute;
            right:60px;
            top:2px;
        }

        #btn_save {
            position:absolute;
            right:5px;
            top:2px;
        }
    </style>
</head>
<body>
<div class="header">
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
