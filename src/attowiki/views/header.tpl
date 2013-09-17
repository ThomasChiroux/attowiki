<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
%if name is None:
    <title></title>
%else:
    <title>{{name}}</title>
%end
    <style type="text/css">
%include attowiki_docutils_css
    </style>
    <style type="text/css">
        html {height:100%}
        body {
            margin:0;
            height:100%;
        }

        body.edit {
            overflow: hidden;
        }

        .header {
            width: 100%;
            height: 20px;
            font-family: "Consolas", "Monaco", "Lucida Console", "Liberation Mono", "Deja Vu Sans Mono", "Bitstream Vera Sans Mono", "Courier New", monospace;
            font-size: 12px;
            border-bottom-style:solid;
            border-width: 1px;
        }

        .header_edit {
            background-color: #ff8532;
        }

        .header_view {
            background-color: #6cb3ff;
        }

        .header_history {
            background-color: #b2b2b2;
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

        .header div.history {
            position:absolute;
            right:180px;
            top:2px;
        }

        .header div.history #history {
            background-color:#ededed;
            -moz-border-radius:6px;
            -webkit-border-radius:6px;
            border-radius:6px;
            border:1px solid #dcdcdc;
            display:inline-block;
            color:#777777;
            font-size:10px;
            padding:0px 5px;
            height: 16px;
            text-decoration:none;
        }

        .header #btn_pdf {
            position:absolute;
            right:5px;
            top:2px;
        }

        .header #btn_edit {
            position:absolute;
            right:50px;
            top:2px;
        }

        .header #btn_save {
            position:absolute;
            right:50px;
            top:2px;
        }

        .header #btn_new {
            position:absolute;
            right:100px;
            top:2px;
        }

        .header #btn_cancel {
            position:absolute;
            right:100px;
            top:2px;
        }

        .header #btn_html {
            position:absolute;
            right:363px;
            top:2px;
            padding:2px 5px;
        }

        .header #btn_source {
            position:absolute;
            right:323px;
            top:2px;
            padding:2px 5px;
        }

        .header #btn_diff {
            position:absolute;
            right:343px;
            top:2px;
            padding:2px 5px;
        }

        a#btn_save.saving {
            color:#ff0000;
            border:1px solid #777777;
        }

        .header .warning {
            position:absolute;
            top:3px;
            right:190px;
            color:darkred;
            font-weight:bold;
        }

        form.edit_form {
            /*position: absolute;*/
            top: 0;
            left: 0;
            bottom: 0;
            right:0;
            overflow: hidden;
            height: 95%;
            width: 100%;

        }

        #textcontent {
            font-family: "Consolas", "Monaco", "Lucida Console", "Liberation Mono", "Deja Vu Sans Mono", "Bitstream Vera Sans Mono", "Courier New", monospace;
            /*margin-right: 5px;*/
            margin: 0;
            padding: 0;
            width:100%;
            height:100%;
            /*height:100%;
            width:100%;*/
        }

        div.view_source {
            font-family: "Consolas", "Monaco", "Lucida Console", "Liberation Mono", "Deja Vu Sans Mono", "Bitstream Vera Sans Mono", "Courier New", monospace;
            font-size: 10px;
            margin:2px;
            padding:0;
            white-space: nowrap;
        }

        div.view_diff {
            font-family: "Consolas", "Monaco", "Lucida Console", "Liberation Mono", "Deja Vu Sans Mono", "Bitstream Vera Sans Mono", "Courier New", monospace;
            font-size: 10px;
            margin:2px;
            padding:0;
            white-space: nowrap;
        }

        div.view_diff p.add {
            color:green;
            margin:0;
        }

        div.view_diff p.sub {
            color:red;
            margin:0;
        }

        div.view_diff p.detail {
            color: #000000;
            margin:0;
        }

        div.view_diff p.unchanged {
            color:gray;
            margin:0;
        }
    </style>
    <script type="text/javascript">
        function hasClass(ele,cls) {
            return ele.className.match(new RegExp('(\\s|^)'+cls+'(\\s|$)'));
        }

        function addClass(ele,cls) {
            if (!hasClass(ele,cls)) ele.className += " "+cls;
        }

        function removeClass(ele,cls) {
            if (hasClass(ele,cls)) {
                var reg = new RegExp('(\\s|^)'+cls+'(\\s|$)');
                ele.className=ele.className.replace(reg,' ');
            }
        }
    </script>
</head>
