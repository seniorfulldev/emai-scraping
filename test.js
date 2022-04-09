let  {validate}  = require("deep-email-validator");
const main = async () => {
  let res = await validate("data@ko-fi.com");
  // const res = await validate({
  //     email: "hr@infidigit.com",
  //     sender: "vasya99110@gmail.com",
  //     validateRegex: true,
  //     validateMx: true,
  //     validateTypo: true,
  //     validateDisposable: true,
  //     validateSMTP: true,
  //   });
    console.log("res", res);
};

main();
