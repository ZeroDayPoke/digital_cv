// ./middleware/index.js

import errorHandler from "./errorHandler.js";
import asyncErrorHandler from "./asyncErrorHandler.js";
import rateLimiter from "./rateLimiter.js";
import checkAuthorizationHeader from "./checkAuthHeader.js";
import ensureAuthenticated from "./authenticate.js";
import { requestLogger, logger } from "./requestLogger.js";

export {
  errorHandler,
  rateLimiter,
  requestLogger,
  logger,
  asyncErrorHandler,
  checkAuthorizationHeader,
  ensureAuthenticated,
};
