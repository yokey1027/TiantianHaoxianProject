
=====================
##启动
* export ops_config=local|production && python manage.py runserver

##flask-sqlacodegen

    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/user.py"  --flask



    <script src="{{ buildStaticUrl('/plugins/ueditor/ueditor.config.js') }}"></script>
    <script src="{{ buildStaticUrl('/plugins/ueditor/ueditor.all.min.js') }}"></script>
    <script src="{{ buildStaticUrl('/plugins/ueditor/lang/zh-cn/zh-cn.js') }}"></script>


    UE.getEditor('editor',{
       toolbars: [
            [ 'undo', 'redo', '|',
                'bold', 'italic', 'underline', 'strikethrough', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall',  '|','rowspacingtop', 'rowspacingbottom', 'lineheight'],
            [ 'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
                'directionalityltr', 'directionalityrtl', 'indent', '|',
                'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
                'link', 'unlink'],
            [ 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
                'insertimage', 'insertvideo', '|',
                'horizontal', 'spechars','|','inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols' ]

        ],
        enableAutoSave:true,
        saveInterval:60000,
        elementPathEnabled:false,
        zIndex:4,
        serverUrl:common_ops.buildUrl(  '/upload/ueditor' )
    });




