$(document).ready( ()=>{
    console.log('links here');
    let counter = 0;
    links = {};
    $("a").each( function() {
        counter+=1;
        $(this).after(`<a class="regular_text" id="link_${counter}" href="#">edit</a>`);
        links[`link_${counter}`] = $(this).attr('href');
    });

    $('.regular_text').click(function(){
        console.log('click edit');
        $('#link_edit_modal').modal('toggle');
    })

});