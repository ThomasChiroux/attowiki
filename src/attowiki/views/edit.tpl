%include header name=name
<body>
<script type="text/javascript">
    function quickSave()
    {
        var httpRequest;
        httpRequest = new XMLHttpRequest();
        httpRequest.onreadystatechange = function(){handleResponse(httpRequest)};

%if name is None:
            if (document.forms['page_edit'].filename.value != "")
            {
                httpRequest.open('PUT','/.tmp.'+document.forms['page_edit'].filename.value,true);
            } else {
                return;
            }
%else:
            httpRequest.open('PUT','/{{display_name}}',true);
%end
        // change the color of 'save' button
        addClass(document.getElementById("btn_save"), 'saving');

        httpRequest.setRequestHeader("Content-Type", "text/plain; charset=UTF-8");
        httpRequest.send(document.forms['page_edit'].content.value);
    }


    function handleResponse(request)
    {
        if(request.readyState == 4) {
            if(request.status == 200) {
                // small trick to actually see the saving: wait for more 500ms
                setTimeout(resetSaveStatus, 500);
            }
        }
    }

    function resetSaveStatus()
    {
        // change the color of 'save' button
        btn_elt = document.getElementById("btn_save");
        removeClass(btn_elt, 'saving');
    }

    function automatic_quick_save()
    {
        quickSave();
        setTimeout(automatic_quick_save, 10000); // quick save every 10s
    }
</script>
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
%if name is None:
        <a href="/cancel-edit/" id="btn_cancel">cancel</a>
%else:
        <a href="/cancel-edit/{{display_name}}" id="btn_cancel">cancel</a>
%end
        <a href="#" id="btn_save" onclick="document.forms['page_edit'].submit();">save</a>
    </div>
</div>
<div class="main_content">

%if name is None:
        <form name="page_edit" method="post" action="/" class="main_content">
        filename: <input name="filename" size="20" value="{{today}}_"></input>
%else:
        <form name="page_edit" method="post" action="/{{display_name}}" class="main_content">
%end
        <textarea id="textcontent" name="content" cols="80" rows="40" class="textcontent">{{content}}</textarea>

    </form>
</div>

</body>
<script type="text/javascript">
window.onload = function() {
    setTimeout(automatic_quick_save, 10000);
};
</script>
</html>
