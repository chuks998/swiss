$(document).ready(function (){

    

    // $('.alert').click(function(e) {
    //     e.preventDefault();

    //     $('html, body').animate({scrollTop: $('#alert').offset().top}, 1000);
    // });

    // $('#about').click(function() {
    //     $('html, body').animate({scrollTop: $('#about').offset().top}, 1000);
    // });

    $('a[href^=\\#]').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({scrollTop: $(this.hash).offset().top -99}, 3000)

    })

    if(window.location.hash){
        var hash = window.location.hash;
        $('html, body').animate({scrollTop: $(hash).offset().top}, 1000)
    }
});