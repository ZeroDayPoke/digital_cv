import jwt from "jsonwebtoken";
import crypto from "crypto";

const JWT_SECRET = process.env.JWT_SECRET;

export default class TokenService {
  // Helper function to sign a JWT
  static _signJwt(payload) {
    return jwt.sign(payload, JWT_SECRET);
  }

  // Helper function to verify a JWT
  static _verifyJwt(token) {
    try {
      return { isValid: true, payload: jwt.verify(token, JWT_SECRET) };
    } catch (e) {
      return { isValid: false, payload: null };
    }
  }

  static generateAccessToken(
    userId,
    email,
    roles = [],
    bookedTourId,
    favoriteExhibitsIds
  ) {
    const today = new Date();
    const expirationDate = new Date(today);
    expirationDate.setDate(today.getDate() + 60);

    const payload = {
      email,
      id: userId,
      roles,
      bookedTourId,
      favoriteExhibitsIds,
      exp: parseInt(expirationDate.getTime() / 1000, 10),
    };

    return this._signJwt(payload);
  }

  // Generate a verification token
  static generateVerificationToken() {
    return crypto.randomBytes(20).toString("hex");
  }

  // Generate a password reset token
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

  // Validate an access token
  static validateAccessToken(token) {
    return this._verifyJwt(token).payload;
  }

  // Verify a password reset token
  static verifyResetToken(token) {
    const { isValid, payload } = this._verifyJwt(token);
    return isValid ? payload.id : null;
  }

  // Refresh an existing token
  static refreshToken(token) {
    const { isValid, payload } = this._verifyJwt(token);

    if (!isValid) {
      return null;
    }

    const { id, email } = payload;
    return this.generateAccessToken(id, email);
  }
}
