'use strict';
document.documentElement.classList.add('js');
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.getElementById('navigation');
if (menuButton && navigation) {
  menuButton.hidden = false;
  const closeMenu = (restoreFocus = false) => {
    const wasOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('is-open');
    if (wasOpen && restoreFocus) menuButton.focus();
  };
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  });
  navigation.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeMenu(true);
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.site-header')) closeMenu();
  });
  const mobileQuery = window.matchMedia('(max-width: 800px)');
  const syncMenu = () => {
    menuButton.hidden = !mobileQuery.matches;
    if (!mobileQuery.matches) closeMenu();
  };
  mobileQuery.addEventListener('change', syncMenu);
  syncMenu();
}
const form = document.getElementById('contact-form');
if (form && window.fetch) {
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const button = form.querySelector('button[type="submit"]');
    if (button.disabled) return;
    const status = document.getElementById('form-status');
    const original = button.innerHTML;
    const abort = new AbortController();
    const timer = window.setTimeout(() => abort.abort(), 20000);
    button.disabled = true;
    button.textContent = 'Envoi en cours…';
    status.classList.remove('error');
    status.textContent = '';
    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' },
        signal: abort.signal
      });
      if (!response.ok) throw new Error('Contact request failed');
      form.reset();
      status.textContent = 'Votre message a bien été envoyé. Merci de m’avoir écrit !';
    } catch (error) {
      status.classList.add('error');
      status.textContent = error.name === 'AbortError'
        ? 'Le service n’a pas répondu à temps. Votre message est conservé ici. Réessayez dans un instant.'
        : 'L’envoi n’a pas abouti. Votre message est conservé ici : vérifiez votre connexion et réessayez.';
    } finally {
      window.clearTimeout(timer);
      button.disabled = false;
      button.innerHTML = original;
    }
  });
}
