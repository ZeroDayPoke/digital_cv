// middleware/requestLogger.js

import winston from "winston";

/**
 * Middleware for logging incoming requests.
 * @module requestLogger
 */

// FILEPATH: digital_cv/src/middleware/requestLogger.js

/**
 * Creates a logger instance with specified configuration.
 * @type {Object}
 * @property {string} level - The minimum level of messages to log.
 * @property {Object} format - The log message format.
 * @property {Object} defaultMeta - The default metadata to attach to log messages.
 * @property {Array} transports - The log transports to use.
 */
export const logger = winston.createLogger({
  level: "info",
  format: winston.format.json(),
  defaultMeta: { service: "user-service" },
  transports: [
    new winston.transports.File({ filename: "error.log", level: "error" }),
    new winston.transports.File({ filename: "combined.log" }),
  ],
});

if (process.env.NODE_ENV !== "production") {
  logger.add(
    new winston.transports.Console({
      format: winston.format.simple(),
    })
  );
}

/**
 * Middleware function to log HTTP requests.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @param {Function} next - The next middleware function.
 */
export const requestLogger = (req, res, next) => {
  const now = new Date().toISOString();
  const meta = {
    time: now,
    ip: req.ip,
    method: req.method,
    path: req.path,
    body: req.body,
    query: req.query,
    // headers: req.headers,
  };
  logger.info(`HTTP Request`, meta);
  next();
};
