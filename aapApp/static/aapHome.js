$(document).ready(function(){
    $(document).on('click','#nav_btn_logout',function(){
        alert("nav_btn_logout clicked");
        window.location.href = "/loginApp/logout";
    });

    $('#session_details').on('change',function(){
        var session=$(this).val()
        var session_details=$(this).find('option:selected').text()
        alert(session)
        alert(session_details)
        
        $.ajax({
            url:"/aapApp/sessionAjax",
            type:"POST",
            dataType:"json",
            data:{"session":session,"action":"sessionAjax",
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            },
            beforeSend:function(){
                 alert("About to send an ajax call.");
                 alert($("input[name=csrfmiddlewaretoken]").val(),
                 );
                 $('#session_title').text(session_details)
                //alert(username+password);
            },
            success:function(result){
                console.log(result);
                // console.log("Ajax handled Successful.");
                if (result && result.length > 0) {

                    console.log(result[0]['course_code']+" "+result[0]['course_name'])

                    var length=result.length
                    $('#course_list').empty()
                    for(i=0;i<length;i++)
                    {
                        var div_col=$('<div>');
                        div_col.attr("class","col d-flex justify-content-center")
                        var button=$('<button>');
                        button.attr("class","courseBtn");
                        button.attr("id",result[i]['course_id']);
                        var div=$('<div>');
                        div.attr("class","text-center")
                        div.text(result[i]['course_code']+" "+ result[i]['course_name'])
                        button.append(div);
                        div_col.append(button)
                        $('#course_list').append(div_col)
                        // var dynamicAjax="console.log('Dynamically Added')";
                        // $('script[src="aapHome.js"]').attr('src', 'data:application/javascript,' + encodeURIComponent(dynamicAjax));
                    }
                 } 
                else
                {
                    // console.log("invalid user/password")
                    $('#course_list').empty()
                    $("#loginError").html('INVALID USER/PASSWORD');
                    $("#loginError").css({
                        "color": "black",
                        "font-weight": "bold"
                    });
                }
                
            },
            error:function(xhr, status, error){
                console.error("AJAX Request Failed",xhr.responseText);
            }

        });
        
    });

    $(document).on('click','.courseBtn',function(){
        var courseId=$(this).attr('id');

    });

});