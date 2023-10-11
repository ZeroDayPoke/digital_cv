// back-end/middleware/rateLimiter.js

import rateLimit from "express-rate-limit";

/**
 * Rate limiter middleware to limit the number of requests per IP address within a specified time window.
 * @param {Object} options - The options object for rate limiter middleware.
 * @param {number} options.windowMs - The time window in milliseconds.
 * @param {number} options.max - The maximum number of requests per IP address within the time window.
 */
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

export default limiter;
