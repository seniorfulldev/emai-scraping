const Humanoid = require("humanoid-js");
let request = require("request");
let cheerio = require("cheerio");
var utils = require("../utils");
// let groupByUniqueValue = utils.containsArg("-g");
let humanoid = new Humanoid((autoBypass = false));
let emailList = [];
let count = 0;
request(
  "http://api.scraperapi.com?api_key=a746f647646b410e486e00da3b11f453&url=https://www.google.com/search?num=100&start=1&hl=en&q=site%3Alinktracker.pro",
  function (error, response, body) {
    if (!error && response.statusCode == 200) {
      $ = cheerio.load(body);
      links = $("a"); //jquery get all hyperlinks
      // console.log("links", links);
      $(links).each(function (i, link) {
        console.log("href", $(link).attr("href"));
        // console.time("emailresult" + i);
        // if (
        //   $(link).attr("href") !== undefined &&
        //   $(link).attr("href").includes("http")
        // ) {
        //   i++;
        //   const url = $(link).attr("href");

        //   console.log(url);
        //   humanoid._asyncTimeout(3000);
        //   humanoid.sendRequest(url).then((res) => {
        //     var emails = res.body.match(/([a-zA-Z0-9._-]+@freelancer.com)/gi);
        //     if (emails) {
        //       console.log("email", emails);
        //       console.timeEnd("emailresult" + i);
        //     }
        //   });
        // }
      });
      //   console.log("links", JSON.parse(body));
      // let urlList = JSON.parse(body).body.links;
      // console.log(urlList.length);
      // urlList.forEach((url) => {
      //   humanoid
      //     .sendRequest(url)
      //     .then((res) => {
      //       count++;
      //       console.log("count", count);
      //       var emails = res.body.match(
      //         /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi
      //       );

      //       try {
      //         if (emails) {
      //           Array.prototype.push.apply(emailList, emails);
      //           console.log("url", url);
      //           console.log(emails.join(", ")); // Show all the emails found
      //         }
      //         if (count == urlList.length) {
      //           const result = [...new Set(emailList)];
      //           console.log("result", result);
      //         }
      //       } catch (e) {
      //         console.log("No emails found :(");
      //       }
      //     })
      //     .catch((err) => {
      //       count++;
      //       console.log("err count", count);
      //       console.error("errs");
      //       if (count == urlList.length) {
      //           const result = [...new Set(emailList)];
      //           console.log("err_result", result);
      //       }
      //       // return;
      //     });
      // });
    } else {
      console.log("There was a problem connecting to the url requested");
      console.log("returerrsresult", emailList);
    }
  }
);
