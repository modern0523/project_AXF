$(function () {
    //点击时样式已经添加，但这是a标签，一点击需要重新获取页面，
    //一刷新就没有点击事件了，所以黄块会立马显示立马消失

    //解决方案：点击时记录操作的位置
    //当页面刷新后，js就获取对应操作位置并设置对应的样式

    //点击外面获取cookie
    typeIndex = $.cookie('typeIndex');
    if (typeIndex)
    {
        $(".type-slider .type_item").eq(typeIndex).addClass("active")
    }
    else
    {
        $(".type-slider .type_item").eq(0).addClass("active")
    }


    $(".type_item").click(function () {
        // $(this).addClass("active")


        // cookie
        // 设置cookie
        // $.cookie(key, value, options)   options >> {expires:过期时间, path: 路径}
        $.cookie('typeIndex',$(this).index(),{expires:3,path:'/'})

        // 获取cookie
        // $.cookie(key)

        // 删除cookie
        // $.cookie(key, null)
    });

    //点击顶部导航　
    // 全部类型
    left_top = false;　
    $("#left_top").click(function ()
    {
        left_top = !left_top;
        left_top ? left_top_show() : left_top_hide()

    });

    // 综合排序
    right_top = false;
    $("#right_top").click(function ()
    {
        right_top = !right_top;
        right_top ? right_top_show() : right_top_hide()

    });

    //点击灰色蒙层，导航栏全收
    $(".bounce-view").click(function () {
        right_top = false;
        right_top_hide();
        left_top = false;
        left_top_hide()
    });


    function left_top_show()
    {
        right_top = false;
        right_top_hide();

        $(".main-content .type-view").show();
        $("#left_top i").attr("class","glyphicon glyphicon-chevron-down")
    }

    function left_top_hide()
    {
        $(".main-content .type-view").hide();
        $("#left_top i").attr("class","glyphicon glyphicon-chevron-up")
    }

    function right_top_show()
    {
        left_top = false;
        left_top_hide();
        $(".main-content .sort-view").show();
        $("#right_top i").attr("class","glyphicon glyphicon-chevron-down")
    }

    function right_top_hide()
    {
        $(".main-content .sort-view").hide();
        $("#right_top i").attr("class","glyphicon glyphicon-chevron-up")
    }



});