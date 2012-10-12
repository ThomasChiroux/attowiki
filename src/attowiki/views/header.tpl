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
        html {height:100%}
        body {
            margin:0;
            height:100%;
            overflow:hidden;
        }

        .header {
            width: 100%;
            height: 20px;
            font-family:monospace;
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

        .warning {
            position:absolute;
            top:3px;
            right:150px;
            color:darkred;
            font-weight:bold;
        }
    </style>
</head>