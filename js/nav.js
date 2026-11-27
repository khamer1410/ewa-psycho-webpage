/*
  Menu mobilne (≤760px).
  Bez JS strona działa w pełni: linki nawigacji są wtedy ukryte na mobile,
  a „Umów wizytę” prowadzi do #kontakt. Ten skrypt odsłania przycisk menu
  i obsługuje otwieranie/zamykanie listy kotwic.
*/
(function () {
  'use strict';

  var nav = document.querySelector('.nav');
  var toggle = nav && nav.querySelector('.nav__toggle');
  var menu = toggle && document.getElementById(toggle.getAttribute('aria-controls'));
  if (!nav || !toggle || !menu) return;

  toggle.hidden = false;

  function isOpen() {
    return toggle.getAttribute('aria-expanded') === 'true';
  }

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.querySelector('.visually-hidden').textContent = open ? 'Zamknij menu' : 'Menu';
    nav.classList.toggle('is-open', open);
  }

  toggle.addEventListener('click', function () {
    setOpen(!isOpen());
  });

  // Zamknięcie po kliknięciu w link z menu.
  menu.addEventListener('click', function (event) {
    if (event.target.closest('a')) setOpen(false);
  });

  // Zamknięcie klawiszem Escape (fokus wraca na przycisk).
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && isOpen()) {
      setOpen(false);
      toggle.focus();
    }
  });

  // Zamknięcie po kliknięciu poza nawigacją.
  document.addEventListener('click', function (event) {
    if (isOpen() && !nav.contains(event.target)) setOpen(false);
  });

  // Po powiększeniu okna powyżej 760px menu wraca do stanu zamkniętego.
  var desktop = window.matchMedia('(min-width: 761px)');
  var onChange = function (e) { if (e.matches) setOpen(false); };
  if (desktop.addEventListener) desktop.addEventListener('change', onChange);
  else if (desktop.addListener) desktop.addListener(onChange);
})();

/*
  Aktywny link w menu na stronie głównej: link do sekcji, na której jest
  czytelnik, dostaje aria-current="location" (styl w css/styles.css).
  Na podstronach aktywny link ma aria-current="page" wpisane w HTML.
*/
(function () {
  'use strict';

  var items = [].slice.call(document.querySelectorAll('.nav__links a[href^="#"]'))
    .map(function (a) { return { a: a, el: document.getElementById(a.getAttribute('href').slice(1)) }; })
    .filter(function (item) { return item.el; });
  if (!items.length) return;

  var queued = false;

  function update() {
    queued = false;
    var line = window.innerHeight * 0.35;
    var current = null;
    items.forEach(function (item) {
      if (item.el.getBoundingClientRect().top <= line) current = item;
    });
    // Na samym dole strony aktywny jest ostatni link (Kontakt).
    if (window.innerHeight + window.pageYOffset >= document.documentElement.scrollHeight - 2) {
      current = items[items.length - 1];
    }
    items.forEach(function (item) {
      if (item === current) item.a.setAttribute('aria-current', 'location');
      else item.a.removeAttribute('aria-current');
    });
  }

  function queue() {
    if (!queued) { queued = true; window.requestAnimationFrame(update); }
  }

  window.addEventListener('scroll', queue, { passive: true });
  window.addEventListener('resize', queue);
  update();
})();
