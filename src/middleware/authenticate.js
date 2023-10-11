// middleware/authenticate.js

import { logger } from "./requestLogger.js";
import asyncErrorHandler from "./asyncErrorHandler.js";
import { AuthenticationError } from "../errors/index.js"; //

const ensureAuthenticated = asyncErrorHandler(async (req, res, next) => {
  if (req.session.userId && req.user.id == req.session.userId) {
    logger.info(`Authenticated successfully: ${req.session.userId}`);
    return next();
  }

  const errorMsg = `Failed to authenticate: session userId: ${req.session.userId}, token userId: ${req.user.id}`;
  logger.error(errorMsg);

  throw new AuthenticationError("Not authenticated");
});

export default ensureAuthenticated;
