if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/static/sw.js')
      .then(reg => console.log('Service Worker Rejistradu!', reg))
      .catch(err => console.log('Erro iha SW:', err));
  });
}
