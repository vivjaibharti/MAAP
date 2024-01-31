$(document).ready(function(){
    $(document).on("click","#aloginbtn",function(e){ 
        e.preventDefault();
        var userid=$("#userid").val();
        var password=$("#password").val();
        alert(userid+password);

        $.ajax({
            url:"/loginApp/aloginajax",
            type:"POST",
            dataType:"json",
            data:{"userid":userid,"password":password,"action":"aloginajax",
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
        },
            beforeSend:function(){
                 alert("About to send an ajax call.");
                 alert($("input[name=csrfmiddlewaretoken]").val(),
                 );
                //alert(username+password);
            },
            success:function(result){
                console.log(result);
                // alert(result);
                // console.log("Ajax handled Successful.");
                if (result.status==="OK") {
                    document.location.replace('/loginApp/ahome');
                } 
                else
                {
                    console.log("invalid user/password")
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


    $(document).on("click","#floginbtn",function(e){ 
        e.preventDefault();
        var userid=$("#userid").val();
        var password=$("#password").val();
         alert(userid+password);

        $.ajax({
            url:"/loginApp/floginajax",
            type:"POST",
            datatype:"json",
            data:{"userid":userid,"password":password,"action":"floginajax",
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
        },
            beforeSend:function(){
                 alert("About to send an ajax call.");
                 alert($("input[name=csrfmiddlewaretoken]").val());
                alert(userid+password);
            },
            success:function(result){
                //console.log(result);
                // alert(result);
                // console.log("Ajax handled Successful.");
                if (result.status=="OK") {
                    document.location.replace('/loginApp/fhome');
                } 
                else
                {
                    $("#loginError").html('INVALID USER/PASSWORD');
                    $("#loginError").css({
                        "color": "black",
                        "font-weight": "bold"
                    });
                }
                
            },
            error:function(xhr, status, error){
                console.error(xhr.responseText);
            }

        });
        
    });
});