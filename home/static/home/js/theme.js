;(function ($) {
    "use strict";     
    
    //* SearchFrom
    function searchFrom(){
        if ( $('.search_here').length ){  
             $('.search_icon').on('click',function(){
                $('.search_from').toggleClass('show');
                return false
            });
            $('.form_hide').on('click',function(){
                $('.searchForm').removeClass('show')
            });
        };
    };
    
    // Code Here 
    function calendar() {
        if ($('.calendar').length) {
            $('.calendar').dcalendar();
        }
    }
    
    //* modal_popup
    function modal_popup() {
        if ($('body').length) {
              $('.modal').modal({
                  dismissible: true, 
                  opacity: 1,  
              });
        }
    }
    
    //* Tags
    function tagPlaceholder() {
        if ($('body').length) {
                $('.chips-placeholder').material_chip({
                    placeholder: 'Add tags...',
                    secondaryPlaceholder: '+Tag',
                });
        }
    } 
    
    // Loding next
    function infiniteScroll() {
        if ($('.middle_section, .notifications_area').length) {
           $('.middle_section').jscroll({
                loadingHtml: '<img src="staticfiles/home/images/preloader.svg" alt="Loading" />',
                padding: 0, 
                autoTriggerUntil: 2, 
                nextSelector: 'a.load-mor:last',
                contentSelector: '.post', 
                callback: false, 
           });
            
           $('.notifications_content').jscroll({
                loadingHtml: '<img src="staticfiles/home/images/preloader.svg" alt="Loading" />',
                padding: 0, 
                autoTriggerUntil: 3,  
                contentSelector: '.notifications_content li', 
                callback: false, 
           }); 
        }
    }
    
    //* Check button  
    function flipswitch() {
        if ($('.flipswitch').length) {
            $(".flipswitch").flipswitch({
                texts : {
                    left  : "YES",
                    right : "NO"
                }
            });
        };
    }; 
    
    //* Graph Chart  
    function graphChart() {
        if ($('#bars').length) { 
              $("#bars li .bar").each(function (key, bar) {
                  var percentage = $(this).data('percentage'); 
                  $(this).css('height', percentage + '%');
              });
        };
    };
    
    
    /*Function Calls*/
    $(".button-collapse").sideNav(); 
    $('select').material_select();
    searchFrom(); 
    calendar();
    infiniteScroll();
    modal_popup ();
    tagPlaceholder ();
    flipswitch ();
    graphChart ();
    
})(jQuery);
 