// ./errors/AuthorizationError.js

/**
 * Represents an error that occurs when a user is not authorized to perform an action.
 * @class
 * @extends Error
 */
class AuthorizationError extends Error {
  /**
   * Creates an instance of AuthorizationError.
   * @param {string} message - The error message.
   */
  constructor(message) {
    super(message);
    this.name = "AuthorizationError";
    this.statusCode = 403;
  }
}

export default AuthorizationError;
