%include header name=name
<body>

<ul>
%for file in filelist:
        <li><a target="_parent" href="{{file}}">{{file}}</a></li>
%end
</ul>
</body>
</html>