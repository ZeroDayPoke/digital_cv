// middleware/requestLogger.js

import winston from "winston";

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
