$(document).ready(function(){
    $(document).on('click','#nav_btn_logout',function(){
        alert("nav_btn_logout clicked");
        window.location.href = "/loginApp/logout";
    });

});