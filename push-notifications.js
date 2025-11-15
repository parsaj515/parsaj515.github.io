// sw.js - Service Worker for Push Notifications
self.addEventListener('push', function(event) {
  const options = {
    body: event.data.text(),
    icon: 'IMG_0054.ico',
    badge: 'IMG_0054.ico',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: '2'
    },
    actions: [
      {
        action: 'explore',
        title: 'Open Chat',
        icon: 'IMG_0054.ico'
      },
      {
        action: 'close',
        title: 'Close',
        icon: 'IMG_0054.ico'
      }
    ]
  };
  event.waitUntil(
    self.registration.showNotification('Super Chat', options)
  );
});

self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  if (event.action === 'explore') {
    clients.openWindow('/');
  }
});
