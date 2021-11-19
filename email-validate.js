import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import { config } from "dotenv";
import validate from "deep-email-validator";
import * as EmailValidator from "email-validator";
config();

const port = process.env.PORT || 8080;
const app = express();

(async () => {
  app.use(cors());
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

  app.post("/api/checkEmail", async (req, res) => {
    console.log("email", req.body.email);
    res.json({ ...EmailValidator.validate(req.body.email) });
  });
  app.get("/api/checkEmail", async (req, res) => {
    const result = EmailValidator.validate("wolfmaccvn199311gmcail.com");
    console.log('result', result);
    res.json({ mail: "no email" });
  });

  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
})();
