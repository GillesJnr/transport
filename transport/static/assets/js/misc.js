(function ($) {
  'use strict';
  $(function () {
    var sidebar = $('.mdc-drawer-menu');
    var body = $('body');

    if($('.mdc-drawer').length) {
      var drawer = mdc.drawer.MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
      // toggler icon click function
      document.querySelector('.sidebar-toggler').addEventListener('click', function () {
        drawer.open = !drawer.open;
      });
    }

    // Initially collapsed drawer in below desktop
    if(window.matchMedia('(max-width: 991px)').matches) {
      if(document.querySelector('.mdc-drawer.mdc-drawer--dismissible').classList.contains('mdc-drawer--open')) {
        document.querySelector('.mdc-drawer.mdc-drawer--dismissible').classList.remove('mdc-drawer--open'); 
      }
    }

    //Add active class to nav-link based on url dynamically
    //Active class can be hard coded directly in html file also as required
    var current = location.pathname.split("/").slice(-1)[0].replace(/^\/|\/$/g, '');
    $('.mdc-drawer-item .mdc-drawer-link', sidebar).each(function () {
      var $this = $(this);
      if (current === "") {
        //for root url
        if ($this.attr('href').indexOf("index.html") !== -1) {
          $(this).addClass('active');
          if ($(this).parents('.mdc-expansion-panel').length) {
            $(this).closest('.mdc-expansion-panel').addClass('expanded');
          }
        }
      } else {
        //for other url
        if ($this.attr('href').indexOf(current) !== -1) {
          $(this).addClass('active');
          if ($(this).parents('.mdc-expansion-panel').length) {
            $(this).closest('.mdc-expansion-panel').addClass('expanded'); 
            $(this).closest('.mdc-expansion-panel').show();
          }
        }
      }
    });

    // Toggle Sidebar items
    $('[data-toggle="expansionPanel"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel1"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel1').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel1').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel1"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel2"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel2').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel2').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel2"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel3"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel3').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel3').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel3"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel4"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel4').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel4').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel4"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel5"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel5').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel5').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel5"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel6"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel6').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel6').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel6"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel7"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel7').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel7').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel7"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel8"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel8').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel8').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel8"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });

    $('[data-toggle="expansionPanel9"]').on('click', function () {
      // close other items
      $('.mdc-expansion-panel9').not($('#' + $(this).attr("data-target"))).hide(300);
      $('.mdc-expansion-panel9').not($('#' + $(this).attr("data-target"))).prev('[data-toggle="expansionPanel9"]').removeClass("expanded");
      // Open toggle menu
      $('#' + $(this).attr("data-target")).slideToggle(300, function() {
        $('#' + $(this).attr("data-target")).toggleClass('expanded');
      });
    });




    // Add expanded class to mdc-drawer-link after expanded
    $('.mdc-drawer-item .mdc-expansion-panel').each(function () {
      $(this).prev('[data-toggle="expansionPanel"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel1').each(function () {
      $(this).prev('[data-toggle="expansionPanel1"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel2').each(function () {
      $(this).prev('[data-toggle="expansionPanel2"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel3').each(function () {
      $(this).prev('[data-toggle="expansionPanel3"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel4').each(function () {
      $(this).prev('[data-toggle="expansionPanel4"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel5').each(function () {
      $(this).prev('[data-toggle="expansionPanel5"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel6').each(function () {
      $(this).prev('[data-toggle="expansionPanel6"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel7').each(function () {
      $(this).prev('[data-toggle="expansionPanel7"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel8').each(function () {
      $(this).prev('[data-toggle="expansionPanel8"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    $('.mdc-drawer-item .mdc-expansion-panel9').each(function () {
      $(this).prev('[data-toggle="expansionPanel9"]').on('click', function () {
        $(this).toggleClass('expanded');
      })
    });

    //Applying perfect scrollbar to sidebar
    if (!body.hasClass("rtl")) {
      if ($('.mdc-drawer .mdc-drawer__content').length) {
        const chatsScroll = new PerfectScrollbar('.mdc-drawer .mdc-drawer__content');
      }
    }

  });
})(jQuery);