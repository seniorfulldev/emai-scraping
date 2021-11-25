const Humanoid = require("humanoid-js");
const services = require("./services");
let humanoid = new Humanoid((autoBypass = false));
var cheerio = require("cheerio");
console.time("total-time");
const domain = "freelancer.com/";

let responses = [];
let fulldomain = domain.includes("http") ? domain : "https://" + domain;
// const inputUrl = req.body.domain;
const hostName = services.parseURL(fulldomain).rootdomain;
humanoid
  .sendRequest(fulldomain)
  .then((res) => {
    const $ = cheerio.load(res.body);
    // links = $("a"); //jquery get all hyperlinks
    console.log($("a"));
    $("a").each(function (i, link) {
      console.time("emailresult" + i);
      if ($(link).attr("href") !== undefined) {
        i++;
        const url =
          $(link).attr("href") && $(link).attr("href").includes("http")
            ? $(link).attr("href")
            : fulldomain + $(link).attr("href");

        const res = getEmailFn(url);
        responses.push(res);
      }
    });
    var results = Promise.race(responses);
    results
      .then((data) => {
        console.log("data", data);
        console.timeEnd("total-time");
      })
      .catch((err) => {
        console.error("small Issues", err);
      });
  })
  .catch((err) => {
    console.error("Big Issues", err);
  });

const getEmailFn = function asyncMultiplyBy2(url) {
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      throw new Error("timeout error");
    }, 10000);
    humanoid
      .sendRequest(url)
      .then((res) => {
        let myReg = new RegExp("[a-zA-Z0-9._-]+@" + hostName, "gi");

        let emails = res.body.match(myReg);
        if (emails) {
          resolve({ email: emails, url: url });
        }
      })
      .catch((error) => {
        console.log("error6", error);
      });
  });
};
