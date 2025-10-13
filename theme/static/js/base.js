document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('[data-toggle="nav"]');
  if (!toggle) {
    return;
  }

  const targetId = toggle.getAttribute('aria-controls');
  const navigation = targetId ? document.getElementById(targetId) : null;

  if (!navigation) {
    return;
  }

  toggle.addEventListener('click', () => {
    const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!isExpanded));
    navigation.classList.toggle('is-open');
  });

  navigation.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 720 && navigation.classList.contains('is-open')) {
        navigation.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  });
});
