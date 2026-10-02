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
