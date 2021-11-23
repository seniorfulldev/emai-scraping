const Humanoid = require("humanoid-js");
let humanoid = new Humanoid((autoBypass = false));
var cheerio = require("cheerio");
console.time("total-time");
humanoid
  .sendRequest("https://www.freelancer.com/")
  .then((res) => {
    $ = cheerio.load(res.body);
    links = $("a"); //jquery get all hyperlinks
    let i = 0;
    console.timeEnd("total-time");
    $(links).each(function (i, link) {
      console.time("emailresult" + i);
      if ($(link).attr("href") !== undefined) {
        i++;
        const url =
          $(link).attr("href") && $(link).attr("href").includes("http")
            ? $(link).attr("href")
            : "https://www.freelancer.com" + $(link).attr("href");

        const sss = getEmailFn(url);
        // humanoid.sendRequest(url).then((res) => {
        //   var emails = res.body.match(/([a-zA-Z0-9._-]+@freelancer.com)/gi);
        //   if (emails) {
        //     console.log("email", emails);
        //     console.timeEnd("emailresult" + i);
        //   }
        // });
      }
    });
  })
  .catch((err) => {
    console.error("Big Issues", err);
  });

const getEmailFn = function asyncMultiplyBy2(url) {
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      console.log("timeout", url);
      resolve({});
    }, 4000);
    humanoid
      .sendRequest(url)
      .then((res) => {
        let emails = res.body.match(/([a-zA-Z0-9._-]+@freelancer.com)/gi);
        
        if (emails) {
          console.log("email", emails);
          resolve({ email: emails, url: url });
        } else {
          resolve({});
        }
      })
      .catch((error) => {
        console.log("error6", error);
        resolve({});
      });
  });
};
