let urlList = [1, 2, 3, 4];

const getEmailFn = function asyncMultiplyBy2(index) {
  // sample async action
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      console.log("timeout", index);
      resolve(index);
    }, index * 1000);
  });
};

let actions = urlList.map(getEmailFn);
console.log("actions", actions);
let results = Promise.race(actions);
results.then((res) => {
  console.log(res);
});
