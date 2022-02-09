var cloudscraper = require('cloudscraper');
 
cloudscraper.get('https://www.sportsmansguide.com/productlist?k=walther-ppk').then(console.log, console.error);