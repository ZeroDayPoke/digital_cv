// middleware/asyncErrorHandler.js
import { logger } from "./requestLogger.js";

const asyncErrorHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch((err) => {
    logger.error("An error occurred: " + err.toString());
    next(err);
  });
};

export default asyncErrorHandler;
