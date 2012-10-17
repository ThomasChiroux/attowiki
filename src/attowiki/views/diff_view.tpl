%include header name=name
<body>
%include header_bar name=name, history=history, gitref=gitref, extended_name=extended_name, is_repo=is_repo, type=type
<div class="view_diff">
%for line in content:
    %if line.startswith('-'):
        <p class="sub">{{line}}</p>
    %elif line.startswith('+'):
        <p class="add">{{line}}</p>
    %elif line.startswith('?'):
        <p class="detail">{{line}}</p>
    %else:
        <p class="unchanged">{{line}}</p>
    %end
%end
</div>
</body>
</html>