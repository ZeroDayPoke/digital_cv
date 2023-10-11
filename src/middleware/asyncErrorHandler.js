// middleware/asyncErrorHandler.js
import { logger } from "./requestLogger.js";

/**
 * Wraps an async route handler function with error handling middleware.
 * @param {function} fn - The async route handler function to wrap.
 * @returns {function} - The wrapped async route handler function with error handling middleware.
 */
const asyncErrorHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch((err) => {
    logger.error("An error occurred: " + err.toString());
    next(err);
  });
};

export default asyncErrorHandler;
