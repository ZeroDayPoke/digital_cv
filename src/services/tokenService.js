// services/tokenService.js

import jwt from "jsonwebtoken";
import crypto from "crypto";

const JWT_SECRET = process.env.JWT_SECRET;

/**
 * A class that provides helper functions for generating and validating JWT tokens.
 */
export default class TokenService {
  /**
   * Helper function to sign a JWT.
   * @param {Object} payload - The payload to be signed.
   * @returns {string} - The signed JWT.
   */
  static _signJwt(payload) {
    return jwt.sign(payload, JWT_SECRET);
  }

  /**
   * Helper function to verify a JWT.
   * @param {string} token - The JWT to be verified.
   * @returns {Object} - An object containing a boolean indicating whether the JWT is valid and the payload of the JWT if it is valid.
   */
  static _verifyJwt(token) {
    try {
      return { isValid: true, payload: jwt.verify(token, JWT_SECRET) };
    } catch (e) {
      return { isValid: false, payload: null };
    }
  }

  /**
   * Generates an access token.
   * @param {string} userId - The ID of the user associated with the token.
   * @param {string} email - The email address of the user associated with the token.
   * @param {Array} roles - An array of roles associated with the user.
   * @returns {string} - The generated access token.
   */
  static generateAccessToken(
    userId,
    email,
    roles = [],
  ) {
    const today = new Date();
    const expirationDate = new Date(today);
    expirationDate.setDate(today.getDate() + 60);

    const payload = {
      email,
      id: userId,
      roles,
      exp: parseInt(expirationDate.getTime() / 1000, 10),
    };

    return this._signJwt(payload);
  }

  /**
   * Generates a verification token.
   * @returns {string} - The generated verification token.
   */
  static generateVerificationToken() {
    return crypto.randomBytes(20).toString("hex");
  }

  /**
   * Generates a password reset token.
   * @param {string} userId - The ID of the user associated with the token.
   * @returns {string} - The generated password reset token.
   */
  static generateResetToken(userId) {
    const today = new Date();
    const expirationDate = new Date(today);
    expirationDate.setHours(today.getHours() + 1);

    const payload = {
      id: userId,
      exp: parseInt(expirationDate.getTime() / 1000, 10),
    };

    return this._signJwt(payload);
  }

  /**
   * Validates an access token.
   * @param {string} token - The access token to be validated.
   * @returns {Object} - The payload of the validated access token.
   */
  static validateAccessToken(token) {
    return this._verifyJwt(token).payload;
  }

  /**
   * Verifies a password reset token.
   * @param {string} token - The password reset token to be verified.
   * @returns {string|null} - The ID of the user associated with the token if the token is valid, or null if the token is invalid.
   */
  static verifyResetToken(token) {
    const { isValid, payload } = this._verifyJwt(token);
    return isValid ? payload.id : null;
  }

  /**
   * Refreshes an existing token.
   * @param {string} token - The token to be refreshed.
   * @returns {string|null} - The refreshed token if the original token is valid, or null if the original token is invalid.
   */
  static refreshToken(token) {
    const { isValid, payload } = this._verifyJwt(token);

    if (!isValid) {
      return null;
    }

    const { id, email } = payload;
    return this.generateAccessToken(id, email);
  }
}
