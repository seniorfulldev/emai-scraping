const express = require("express");
const cluster = require("cluster");

// Check the number of available CPU.
const numCPUs = require("os").cpus().length;

const app = express();
const PORT = 3000;

// For Master process
if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  console.log("numCPUs", numCPUs);
  // Fork workers.
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  // This event is firs when worker died
  cluster.on("exit", (worker, code, signal) => {
    console.log(`worker ${worker.process.pid} died`);
  });
}

// For Worker
else {
  // Workers can share any TCP connection
  // In this case it is an HTTP server
  app.listen(PORT, (err) => {
    err
      ? console.log("Error in server setup")
      : console.log(`Worker ${process.pid} started`);
  });
}
app.get("/welcome", (req, res) => {
  res.json({ message: "Welcome to node api application." });
});
