import { Component, OnInit } from '@angular/core';

import * as Aos from 'aos';
declare var particlesJS: any;

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    Aos.init({duration: 800, easing: 'ease'});

    $(window).stellar({
      responsive: true,
      parallaxBackgrounds: true,
      parallaxElements: true,
      horizontalScrolling: false,
      hideDistantElements: false,
      scrollProperty: 'scroll'
    });

    this.loader();
    $(window).Scrollax();
    this.scrollWindow();
    this.contentWayPoint();

    particlesJS.load('particles-js', 'assets/particles.json', () => {
      console.log('callback - particles.js config loaded');
    });
  }

  loader(): void {
    setTimeout(() => {
      if ($('#ftco-loader').length > 0) {
        $('#ftco-loader').removeClass('show');
      }
    }, 1);
  }

  // navbar 伸縮動畫
  scrollWindow(): void {
    $(window).scroll(() => {
      const $w = $(window);
      const st = $w.scrollTop();
      const navbar = $('.ftco_navbar');

      if (st > 150) {
        if (!navbar.hasClass('scrolled')) { navbar.addClass('scrolled'); }
      }
      if (st < 150) {
        if (navbar.hasClass('scrolled')) { navbar.removeClass('scrolled sleep'); }
      }
      if (st > 350) {
        if (!navbar.hasClass('awake')) { navbar.addClass('awake'); }
      }
      if (st < 350) {
        if (navbar.hasClass('awake')) {
          navbar.removeClass('awake');
          navbar.addClass('sleep');
        }
      }
    });
  }

  // 頁面上方按鈕動畫
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
    }, { offset: '95%' } );
  }

}
