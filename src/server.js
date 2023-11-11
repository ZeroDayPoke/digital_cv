// src/server.js

import dotenv from "dotenv";
import express from "express";
import mailService from "./services/mailService.js";
import cors from "cors";
import helmet from "helmet";
import compression from "compression";
import rateLimit from "express-rate-limit";
import { logger } from "./middleware/index.js";

// Load environment variables
dotenv.config({ path: '.env', debug: true })

// Create the Express app
const app = express();

// Set up middleware
app.use(helmet());
app.use(compression());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(
  rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 100,
  })
);

// Define allowed origins
const allowedOrigins = ["https://zerodaypoke.com", "https://www.zerodaypoke.com", "node-app:3000", "localhost:8000"];

// Set up CORS policy
app.use(
  cors({
    origin: function (origin, callback) {
      if (!origin) return callback(null, true);
      if (
        allowedOrigins.some((allowedOrigin) => origin.includes(allowedOrigin))
      ) {
        return callback(null, true);
      } else {
        /**
         * Error message for when the CORS policy for this site does not allow access from the specified Origin.
         * @type {string}
         */
        const msg =
          "The CORS policy for this site does not allow access from the specified Origin.";
        return callback(new Error(msg), false);
      }
    },
    credentials: true,
  })
);

/**
 * Route for sending email.
 * @name POST/send-email
 * @function
 * @memberof module:server
 * @inner
 * @param {string} to - The email address to send the email to.
 * @returns {Object} - Returns a response object with a message and token property.
 * @throws {Object} - Returns an error object with an error property if there was an error sending the email.
 */
app.post("/send-email", async (req, res) => {
  const { to } = req.body;
  logger.info(to);
  try {
    const result = await mailService.sendVerificationEmail(to);
    return res.status(200).send({ message: "Email sent successfully!", token: result.token });
  } catch (error) {
    logger.error(error);
    return res.status(500).send({ error: error.error });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
