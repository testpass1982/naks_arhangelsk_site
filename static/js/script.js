// Кнопка поиска
window.onload = function() {
$( ".btn" ).click(function() {
    $('.search, btn').toggleClass('open');
 });
 
//  

$(document).ready(function() {
   $('#pop-up').click(function() {
      $('#modal-window').addClass('active');
   });
   $('.modal-close').click(function() {
      $(this).parent().removeClass('active');
   });
});


function check() {
    var submit = document.getElementsByName('submit')[0];
    if (document.getElementById('politics').checked)
    submit.disabled = '';
    else
    submit.disabled = 'disabled';
    }

    $('#box').click(function(){
      $('.drop__menu').hide(); // Скрывает начальное содержимое.
      $('.drop__menu').show(); // Показывает содержимое диалога.
  });

  $(document).ready(function () {
    $(".sb-icon-search").click(function () {
      if (!$(".sb-search").hasClass("sb-search-open")) {
        $(".sb-search").addClass("sb-search-open");
      }
    });
    
    $(".sb-search-submit").click(function(){
      if ($(".sb-search").hasClass("sb-search-open") && $.trim($(".sb-search-input").val()).length==0) {
        event.preventDefault();
        $(".sb-search").removeClass("sb-search-open");
      }
    });
  });


// Бургер меню
 
$(document).ready(function () {
  $('.animated-icon1,.animated-icon3,.animated-icon4').click(function () {
    $(this).toggleClass('open');
  });
});

// Works everywhere
$(document).ready(function () {

  // Hide/show animation hamburger function
  $('.navbar-toggler').on('click', function () {

    // Take this line to first hamburger animations
    $('.animated-icon1').toggleClass('open');

    // Take this line to second hamburger animation
    $('.animated-icon3').toggleClass('open');

    // Take this line to third hamburger animation
    $('.animated-icon4').toggleClass('open');
  });

});


// Выбрать несколько элементов

$('.sort').click(function () {
  var mylist = $('.items');
  var listitems = mylist.children('li').get();
  listitems.sort(function (a, b) {
    var compA = $(a).data('selected');
    var compB = $(b).data('selected');
    return (compA < compB) ? 1 : (compA > compB) ? 1 : 0;
  });
  $.each(listitems, function (idx, itm) { mylist.append(itm); });
})

$('li', '.items').click(function (){
  var checks = $('[type="checkbox"]', '.checks');
  var item = $(this);
  
  if(item.data('selected') == '0') {
    item.data('selected', '1');
    item.addClass('selected');
  } else {
    item.data('selected', '0');
    item.removeClass('selected');
  }
  
  checks.filter('[data-guid="'+item.data('guid')+'"]').prop('checked', item.data('selected') == '1');
});

$(document).on('change', '.file-input-field', function() {  
  var $value = $(this).parent().next();  
  $value.addClass("added").text($(this).val().replace(/C:\\fakepath\\/i, ''));
});
$("#phone").mask("+8 (999) 999 - 99 - 99",{completed:function(){alert("Да, этой мой номер");}});
  $("#phone2").mask("+8 (999) 999 - 99 - 99",{completed:function(){alert("Да, этой мой номер");}});
};

require(["popper"], function(popper) {
  window.Popper = popper;
  require(["bootstrap"]);
});

