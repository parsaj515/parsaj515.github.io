// sw.js
self.addEventListener('install', (event) => {
  console.log('Service Worker installed');
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker activated');
});

self.addEventListener('push', (event) => {
  const options = {
    body: event.data.text(),
    icon: 'icon.png',
    badge: 'badge.png'
  };
  
  event.waitUntil(
    self.registration.showNotification('Super Chat', options)
  );
});
