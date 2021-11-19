'use strict';

//Define all dependencies needed
const express = require('express');
const responseTime = require('response-time')
const axios = require('axios');
const redis = require('redis');
const client = redis.createClient();

//Load Express Framework
var app = express();

//Create a middleware that adds a X-Response-Time header to responses.
app.use(responseTime());

const getBook = (req, res) => {
  let isbn = req.query.isbn;
  let url = `https://api.proxycrawl.com/scraper?token=iVcCNRKgIHEEX4UtIEIBgA&url=chinanews.com`;
  return axios.get(url)
    .then(response => {
      let book = response.data;
      // Set the string-key:isbn in our cache. With he contents of the cache : title
      // Set cache expiration to 1 hour (60 minutes)
      client.setex(isbn, 3600, JSON.stringify(book));

      res.send(book);
    })
    .catch(err => {
      res.send('The book you are looking for is not found !!!');
    });
};

const getCache = (req, res) => {
  let isbn = req.query.isbn;
  //Check the cache data from the server redis
  client.get(isbn, (err, result) => {
    console.log('error',err)
    if (result) {
      console.log('result',result)
      res.send(result);
    } else {
      getBook(req, res);
    }
  });
}

app.get('/book', getCache);

app.listen(3000, function() {
  console.log('Your node is running on port 3000 !!!')
});