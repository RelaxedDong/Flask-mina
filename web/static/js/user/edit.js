var user_edit_ops = {
    init:function () {
        this.eventBind();
    },
    eventBind:function () {
        $(".user_edit_wrap .save").click(function () {
            var btn_target = $(this);

            if(btn_target.hasClass('disabled')){
                common_ops.alert('正在处理，请不要重复提交')
                return;
            }
            var nickname_target = $(".user_edit_wrap input[name='nickname']");
            var nickanme = nickname_target.val();

            var email_target = $(".user_edit_wrap input[name='email']");
            var email = email_target.val();

            if(!nickanme || nickanme.length<2){
                common_ops.tip('姓名至少两个字符',nickname_target)
                return;
            }

            if(!email || email.length<2){
                common_ops.tip('请输入规范的邮箱',email_target)
                return;
            }
            var data = {
                nickname : nickanme,
                email : email,
            };
            btn_target.addClass('disabled');
            $.ajax({
                url:common_ops.buidUrl("/user/edit/"),
                type:"POST",
                data:data,
                dataType:'json',
                'success':function (res) {
                    btn_target.removeClass('disabled');
                    var callback = null;
                    if(res.code==200){
                        callback = function () {
                            window.location.reload()
                        }
                    }
                    common_ops.alert(res.msg,callback)
                }
            })
        })
    }
}

$(document).ready(function () {
    user_edit_ops.init()
})
