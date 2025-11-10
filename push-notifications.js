self.addEventListener('push',function(e){const options={body:e.data.text(),icon:'IMG_0054.ico',badge:'IMG_0054.ico'};e.waitUntil(self.registration.showNotification('New Message',options))});
