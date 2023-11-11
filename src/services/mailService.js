// ./services/emailService.js

/**
 * EmailService Module
 * 
 * This module provides functionalities to send various types of emails.
 * 
 * @module services/EmailService
 */

import dotenv from "dotenv";
import crypto from "crypto";
import nodemailer from "nodemailer";
import { logger } from "../middleware/requestLogger.js";

dotenv.config({ path: '../.env', debug: true })

/**
 * Transporter object responsible for sending emails.
 */
const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: process.env.EMAIL_USERNAME,
    pass: process.env.EMAIL_PASSWORD,
  },
});

export default class EmailService {
  /**
   * Sends a verification email to the user.
   * 
   * @param {string} userEmail - The email address of the user.
   * @param {string} token - The verification token.
   * @returns {Promise<Object>} - Promise resolving to the email sending result.
   */
  static sendVerificationEmail(userEmail, token) {
    return new Promise((resolve, reject) => {
      token = crypto.randomBytes(20).toString("hex");
      const mailOptions = {
        from: process.env.EMAIL_USERNAME,
        to: userEmail,
        subject: "Email Verification",
        text: `Please verify your email by clicking the following link: https://zerodaypoke.com/verify_account_email/${token}`,
      };

      transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
          reject({ status: "error", error });
        } else {
          resolve({ status: "success", response: info.response, token });
        }
      });
    });
  }

  /**
   * Sends a password reset email to the user.
   * 
   * @param {string} userEmail - The email address of the user.
   * @param {string} token - The password reset token.
   */
  static sendResetPasswordEmail(userEmail, token) {
    const mailOptions = {
      from: process.env.EMAIL_USERNAME,
      to: userEmail,
      subject: "Password Reset Request",
      text: `You have requested to reset your password. Please click the following link to reset your password: ${process.env.BASE_URL}/reset-password?token=${token}`,
    };

    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.log(error);
      } else {
        console.log(`Email sent: ${info.response}`);
      }
    });
  }
}
