// ./errors/ValidationError.js

/**
 * Represents a validation error.
 * @class
 * @extends Error
 */
class ValidationError extends Error {
  /**
   * Creates a new instance of ValidationError.
   * @param {string} message - The error message.
   */
  constructor(message) {
    super(message);
    this.name = "ValidationError";
    this.statusCode = 400;
  }
}

export default ValidationError;
