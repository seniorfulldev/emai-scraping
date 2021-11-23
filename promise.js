const Humanoid = require("humanoid-js");
var request = require("request");
let humanoid = new Humanoid((autoBypass = false));
let emailList = [];
let count = 0;
console.time("emailresult");
request(
  "https://api.proxycrawl.com/scraper?token=iVcCNRKgIHEEX4UtIEIBgA&url=homedecorexpert.com",
  function (error, response, body) {
    
    if (!error && response.statusCode == 200) {
      let urlList = JSON.parse(body).body.links;
      console.log(urlList.length);
      var actions = urlList.map(getEmailFn);
      console.log("actions", actions);
      var results = Promise.all(actions); // pass array of promises
      results.then(
        (
          data // or just .then(console.log)
        ) => {
          console.log(data); // [2, 4, 6, 8, 10]
          const result = filterEmails(data);
          console.log("result ", result);
          console.timeEnd("emailresult");
        }
      );
    }
  }
);

const getEmailFn = function asyncMultiplyBy2(url) {
  // sample async action
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      console.log("timeout", url);
      throw 'timeout';
    }, 5000);
    humanoid
      .sendRequest(url)
      .then((res) => {
        var emails = res.body.match(
          /([a-zA-Z0-9._-]+@homedecorexpert.com)/gi
        );
        if (emails) {
          console.log("email", emails);
          resolve({ email: emails, url: url });
        } else {
          resolve({});
        }
      })
      .catch((error) => {
        reject(error);
      });
  });
};

const filterEmails = (list) => {
  let mailArray = [];
  list.forEach((emailElements) => {
    console.log("emailElements", emailElements);
    const emails = [...new Set(emailElements.email)];
    emails.map((e) => {
      let validversion = e.match(/(@[0-9]+\.[0-9.]+)/gi);
      console.log("valid", validversion);
      if (!validversion && !e.includes("x")) {
        mailArray.push({ email: e, url: emailElements.url });
      }
    });
  });

//   console.log("mailArray", mailArray);
  return mailArray;
};

