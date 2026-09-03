const https = require('https');
https.get('https://streams.ilovemusic.de/iloveradio17.mp3', (res) => {
  console.log("iloveradio17 status:", res.statusCode);
});
