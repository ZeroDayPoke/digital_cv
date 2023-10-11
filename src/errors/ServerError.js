// ./errors/ServerError.js

/**
 * Represents an error that occurs on the server side.
 * @class
 * @extends Error
 */
class ServerError extends Error {
  /**
   * Creates a new instance of ServerError.
   * @param {string} message - The error message.
   */
  constructor(message) {
    super(message);
    this.name = "ServerError";
    this.statusCode = 500;
  }
}

export default ServerError;
