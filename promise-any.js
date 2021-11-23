
var any = require('promise.any');
//err: promise.any method is only used over node.js version 15"


const SlowlyDone = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, "Done slowly");
}); //resolves after 500ms

const QuicklyDone = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, "Done quickly");
}); //resolves after 100ms

const Rejection = new Promise((resolve, reject) => {
  setTimeout(reject, 100, "Rejected"); //always rejected
});

any([SlowlyDone, QuicklyDone, Rejection])
  .then((value) => {
    console.log(value);
    //  QuicklyDone fulfils first
  })
  .catch((err) => {
    console.log(err);
  });
