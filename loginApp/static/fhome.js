$(document).ready(function(e){
    $(document).on('click','#nav_btn_logout',function(){
        alert("nav_btn_logout clicked");
        window.location.href = "/loginApp/logout";
    });

    $(document).on('click','#btnAap',function(){
        alert("btnAap clicked");
        window.location.href = "/aapApp/aap";
    });
});