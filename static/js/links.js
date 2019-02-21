$(document).ready( ()=>{
    console.log('links here');
    let counter = 0;
    links = {};
    $("a").each( function() {
        counter+=1;
        $(this).after(`<a class="edit_link" data-link_id="${counter}" id="link_${counter}" href="#">edit</a>`);
        links[`link_${counter}`] = $(this).attr('href');
    });

    $('.edit_link').click(function(){
        console.log('click edit');
        $('#link_edit_modal').modal('toggle');
        // load from db this link information
        $.ajax({
            link_id = this.dataset.link_id,
            url: `/api/menu/${link_id}`,
            success: function(data) {
                $("#link_url").text(data.url);
                $("#link_text").text(data.title);
            }
        });
        // load from db all available publications
    })

});