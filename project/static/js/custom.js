  
  (function ($) {
  "use strict";
    jQuery('.counter-thumb').appear(function() {
      jQuery('.counter-number').countTo();
    });
    $('.hero-section').backstretch([
    
      "/static/images/slideshow/1.jpeg",
      "/static/images/slideshow/2.jpeg",
      "/static/images/slideshow/3.jpeg"
    ],  {duration: 2000, fade: 750});
    $('.smoothscroll').click(function(){
      var el = $(this).attr('href');
      var elWrapped = $(el);
      scrollToDiv(elWrapped);
      return false;
      function scrollToDiv(element){
        var offset = element.offset();
        var offsetTop = offset.top;
        var totalScroll = offsetTop-navheight;

        $('body,html').animate({
        scrollTop: totalScroll
        }, 300);
      }
    });
    
  })(window.jQuery);
