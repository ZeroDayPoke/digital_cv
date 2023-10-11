// ./errors/NotFoundError.js

/**
 * Represents a NotFoundError, which is thrown when a requested resource is not found.
 * @class
 * @extends Error
 */
class NotFoundError extends Error {
  /**
   * Creates a new instance of NotFoundError.
   * @param {string} message - The error message.
   */
  constructor(message) {
    super(message);
    this.name = "NotFoundError";
    this.statusCode = 404;
  }
}

export default NotFoundError;
