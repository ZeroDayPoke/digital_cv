// ./errors/AuthenticationError.js

/**
 * Custom error class for authentication errors.
 * @class
 * @extends Error
 */
class AuthenticationError extends Error {
  /**
   * Creates an instance of AuthenticationError.
   * @param {string} message - The error message.
   */
  constructor(message) {
    super(message);
    this.name = "AuthenticationError";
    this.statusCode = 401;
  }
}

export default AuthenticationError;
