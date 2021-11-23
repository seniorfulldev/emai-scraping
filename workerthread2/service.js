const { workerData, parentPort } = require('worker_threads')
console.time("dbsave");
// You can do any heavy stuff here, in a synchronous way
// without blocking the "main thread"
let element = 0;
for (let index = 0; index < 9; index++) {
    
    element += index;
    
}
for (let index = 0; index < 9; index++) {
    
    element += index;
    
}
console.timeEnd("dbsave");
parentPort.postMessage({ hello: workerData, element: element })
