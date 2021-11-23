const Humanoid = require("humanoid-js");
let humanoid = new Humanoid((autoBypass = false));
var cheerio = require("cheerio");
console.time("total-time");
humanoid
  .sendRequest("https://www.google.com/search?num=100&start=1&hl=en&q=site%3Afreelancer.com")
  .then((res) => {
    $ = cheerio.load(res.body);
    links = $("a"); //jquery get all hyperlinks
    console.log("links", links);
    let i = 0;
    console.timeEnd("total-time");
    $(links).each(function (i, link) {
      console.time("emailresult"+i);
      if ($(link).attr("href") !== undefined && $(link).attr("href").includes("http")) {
        i++;
        const url = $(link).attr("href");

        console.log(url);
        humanoid._asyncTimeout(3000);
        humanoid.sendRequest(url).then((res) => {
          var emails = res.body.match(/([a-zA-Z0-9._-]+@freelancer.com)/gi);
          if (emails) {
            console.log("email", emails);
            console.timeEnd("emailresult"+i);
          }
        });
      }
    });
  })
  .catch((err) => {
    console.error("Big Issues", err);
  });
