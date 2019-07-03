$(document).ready(function(){
  $(window).scroll(function(){
    var scrollTop = $(window).scrollTop();
    console.log(scrollTop);
    if(scrollTop > 110){
      $('#main-header').addClass('header-fixed');
    } else {
      $('#main-header').removeClass('header-fixed');
    }
  });
});
