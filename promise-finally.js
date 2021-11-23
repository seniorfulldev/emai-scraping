const addition = (a, b) =>
  new Promise((resolve, reject) => {
    if (typeof a == "number" && typeof b == "number") {
      resolve(a + b);
    } else {
      reject("Not a Number");
    }
  });

addition(10, 5)
  .then((response) => {
    console.log(response);
  })
  .catch((err) => {
    console.log(err);
  })
  .finally(() => {
    console.log("Numbers are added");
  });
