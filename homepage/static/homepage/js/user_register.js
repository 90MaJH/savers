function idCheck() {
if (!$('#username').val()){
    alert("please enter the ID");
    return;
}

$.ajax({
    type:"POST",
    url:"/homepage/user_register_idcheck/",
    data: {
        'username': $('#username').val(),
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
            $('#idcheck-result').html(response);
        },
    }
});

function changeEmailDomain() {
    var result = confirm("realy want to cancel?");

    if(result){
        $(location).attr('href', '/homepage/login');
    }
}

function userRegister(){
    if(!$('#username').val()){
        alert("please enter the ID");
        return;
    }

    if(!$('#IDCheckResult').val()){
        alert("please confirm your ID");
        return;
    }

    if(!$('#password').val()){
        alert("please enter the PW");
        return;
    }

    if($('#password').val() != $('#password_check').val()){
        alert("wrong password");
        return;
    }

    if(!$('#last_name').val()){
        alert("please enter the last_name");
        return;
    }

    if(!$('#phone1').val() || !$('#phone2').val() || !$('#phone3').val()){
        alert("please enter the phone");
        return;
    }

    if(!$('#email_id').val() || !$('#email_domain').val()){
        alert("please enter the email");
        return;
    }

    if(!$('#birth_year').val() || !$('#birth_month').val() || !$('#birth_day').val()){
        alert("please enter the birth day");
        return;
    }

    $('#register_form').submit();

}

}