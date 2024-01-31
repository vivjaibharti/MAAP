$(document).ready(function(){
    $(document).on("click","#home_btn_div",function(){
        alert("home_btn_div clicked");
        window.location.href = "/loginApp/ahome";
    });

    $(document).on('click','#nav_btn_logout',function(){
        alert("nav_btn_logout clicked");
        window.location.href = "/loginApp/login";
    });
});