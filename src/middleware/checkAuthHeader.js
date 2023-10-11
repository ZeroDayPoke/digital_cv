// middleware/checkAuthHeader.js

import asyncErrorHandler from "./asyncErrorHandler.js";
import { logger } from "./requestLogger.js";

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
