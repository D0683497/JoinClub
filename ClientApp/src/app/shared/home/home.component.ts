import { Component, ElementRef, OnInit } from '@angular/core';

import * as AOS from 'aos';

declare var $: any;
declare var stellar: any;
declare var Scrollax: any;
declare var waypoints: any;
declare var animateNumber: any;

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private elementRef: ElementRef) { }

  ngOnInit(): void {
    AOS.init({duration: 800, easing: 'slide'});
    $(window).stellar({
      responsive: true,
      parallaxBackgrounds: true,
      parallaxElements: true,
      horizontalScrolling: false,
      hideDistantElements: false,
      scrollProperty: 'scroll'
    });
    this.fullHeight();
    this.loader();
    $.Scrollax();

    $('nav .dropdown').hover(() => {
      const $this = $('nav .dropdown');
      $this.addClass('show');
      $this.find('> a').attr('aria-expanded', true);
      $this.find('.dropdown-menu').addClass('show');
    }, () => {
      const $this = $('nav .dropdown');
      $this.removeClass('show');
      $this.find('> a').attr('aria-expanded', false);
      $this.find('.dropdown-menu').removeClass('show');
    });

    $('#dropdown04').on('show.bs.dropdown', () => { console.log('show'); });

    this.scrollWindow();
    this.counter();
    this.contentWayPoint();
    this.OnePageNav();
  }

  fullHeight(): void {
    $('.js-fullheight').css('height', $(window).height());
    $(window).resize(() => {
      $('.js-fullheight').css('height', $(window).height());
    });
  }

  loader(): void {
    setTimeout(() => {
      if ($('#ftco-loader').length > 0) {
        $('#ftco-loader').removeClass('show');
      }
    }, 1);
  }

  scrollWindow(): void {
    $(window).scroll(() => {
      const $w = $(window);
      const st = $w.scrollTop();
      const navbar = $('.ftco_navbar');
      const sd = $('.js-scroll-wrap');

      if (st > 150) {
        if (!navbar.hasClass('scrolled')) { navbar.addClass('scrolled'); }
      }
      if (st < 150) {
        if (navbar.hasClass('scrolled')) { navbar.removeClass('scrolled sleep'); }
      }
      if (st > 350) {
        if (!navbar.hasClass('awake')) { navbar.addClass('awake'); }
        if (sd.length > 0) { sd.addClass('sleep'); }
      }
      if (st < 350) {
        if (navbar.hasClass('awake')) {
          navbar.removeClass('awake');
          navbar.addClass('sleep');
        }
        if (sd.length > 0) { sd.removeClass('sleep'); }
      }
    });
  }

  counter(): void {
    $('#section-counter').waypoint((direction) => {
      if (direction === 'down' && !$('#section-counter').hasClass('ftco-animated')) {
        // tslint:disable-next-line: variable-name
        const comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',');
        $('.number').each(() => {
          const $this = $('.number');
          const num = $this.data('number');
          console.log(num);
          $this.animateNumber({
            number: num,
            numberStep: comma_separator_number_step
          }, 7000);
        });
      }
    }, { offset: '95%' });
  }

  contentWayPoint(): void {
    let i = 0;
    $('.ftco-animate').waypoint((direction) => {
      if ( direction === 'down' && !$('.ftco-animate').hasClass('ftco-animated') ) {
        i++;
        $('.ftco-animate').addClass('item-animate');
        setTimeout(() => {
          $('body .ftco-animate.item-animate').each((k) => {
            const el = $('body .ftco-animate.item-animate');
            setTimeout(() => {
              const effect = el.data('animate-effect');
              if ( effect === 'fadeIn') {
                el.addClass('fadeIn ftco-animated');
              } else if ( effect === 'fadeInLeft') {
                el.addClass('fadeInLeft ftco-animated');
              } else if ( effect === 'fadeInRight') {
                el.addClass('fadeInRight ftco-animated');
              } else {
                el.addClass('fadeInUp ftco-animated');
              }
              el.removeClass('item-animate');
            },  k * 50, 'easeInOutExpo' );
          });
        }, 100);
      }
    } , { offset: '95%' } );
  }

  OnePageNav(): void {
    $(`.smoothscroll[href^='#'], #ftco-nav ul li a[href^='#']`).on('click', (e) => {
      e.preventDefault();
      const hash = $(`.smoothscroll[href^='#'], #ftco-nav ul li a[href^='#']`);
      const navToggler = $('.navbar-toggler');
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 700, 'easeInOutExpo', () => {
        window.location.hash = hash;
      });
      if (navToggler.is(':visible')) { navToggler.click(); }
    });
    $('body').on('activate.bs.scrollspy', () => { console.log('nice'); });
  }

}
