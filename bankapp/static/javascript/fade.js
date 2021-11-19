var fade_out = function(){
    $('.dash-alert').fadeOut().empty();
}

setTimeout(fade_out, 15000)




$(document).ready(function (){
    $("#deposit").click(function(){
        $('#transfer-form').css('display', 'none')
        $('#deposit-form').css('display', 'block');
    })

    $("#transfer").click(function(){
        $('#deposit-form').css('display', 'none')
        $('#transfer-form').css('display', 'block');
    })

});