// middleware/checkAuthHeader.js

import asyncErrorHandler from "./asyncErrorHandler.js";
import { logger } from "./requestLogger.js";

/**
 * Middleware function to check for the presence of an Authorization header in the request.
 * If the header is missing, it destroys the session and returns a 401 Unauthorized response.
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Express next middleware function.
 * @returns {Object} - Express response object or calls the next middleware function.
 */
const checkAuthorizationHeader = asyncErrorHandler(
  async (req, res, next) => {
    const authHeader = req.headers.authorization;
    logger.info("Checking for Authorization header");

    if (!authHeader) {
      if (req.session) await req.session.destroy();
      return res.status(401).json({ message: "Authorization header missing" });
    }
    next();
  }
);

export default checkAuthorizationHeader;
