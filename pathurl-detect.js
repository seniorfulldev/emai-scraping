const Humanoid = require("humanoid-js");
let humanoid = new Humanoid((autoBypass = false));
var cheerio = require("cheerio");
humanoid
  .sendRequest("https://www.freelancer.com/")
  .then((res) => {
    $ = cheerio.load(res.body);
    links = $("a"); //jquery get all hyperlinks
    let i = 0;
    $(links).each(function (i, link) {
      if ($(link).attr("href") !== undefined) {
        i++;
        const url =
          $(link).attr("href") && $(link).attr("href").includes("http")
            ? $(link).attr("href")
            : "https://www.freelancer.com" + $(link).attr("href");

        console.log(url);
        humanoid.sendRequest(url).then((res) => {
          var emails = res.body.match(/([a-zA-Z0-9._-]+@freelancer.com)/gi);
          if (emails) {
            console.log("email", emails);
          }
        });
      }
    });
  })
  .catch((err) => {
    console.error(err);
  });
