const Humanoid = require("humanoid-js");
var request = require("request");
var utils = require("./utils");
// let groupByUniqueValue = utils.containsArg("-g");
let humanoid = new Humanoid((autoBypass = false));
let emailList = [];
let count = 0;
request(
  "https://api.proxycrawl.com/scraper?token=iVcCNRKgIHEEX4UtIEIBgA&url=https://seniorfulldev.tech/",
  function (error, response, body) {
    if (!error && response.statusCode == 200) {
      //   console.log("links", JSON.parse(body));
      let urlList = JSON.parse(body).body.links;
      console.log(urlList.length);
      //   console.log("urlList", urlList);
      urlList.forEach((url) => {
        humanoid
          .sendRequest(url)
          .then((res) => {
            count++;
            console.log("count", count);
            var emails = res.body.match(
              /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi
            );

            try {
              if (emails) {
                Array.prototype.push.apply(emailList, emails);
                console.log("url", url);
                console.log(emails.join(", ")); // Show all the emails found
              }
              if (count == urlList.length) {
                const result = [...new Set(emailList)];
                console.log("result", result);
              }
            } catch (e) {
              console.log("No emails found :(");
            }
          })
          .catch((err) => {
            count++;
            console.log("err count", count);
            console.error("errs");
            if (count == urlList.length) {
                const result = [...new Set(emailList)];
                console.log("err_result", result);
            }
            // return;
          });
      });
    } else {
      console.log("There was a problem connecting to the url requested");
      console.log("returerrsresult", emailList);
    }
  }
);
