const transporter = require('../config/mail');
const { generateToken } = require('../utils/tokenGenerator');

const sendVerificationEmail = async (recipientEmail) => {
  try {
    console.log(recipientEmail);
    // Generate a new verification token
    const token = generateToken();

    // Create the verification link
    const verificationLink = `https://zerodaypoke.com/verify-account/${token}`;

    // Define email content
    const mailOptions = {
      from: process.env.EMAIL, // sender address
      to: recipientEmail, // list of receivers
      subject: 'Account Verification', // Subject line
      text: `Please click on the following link to verify your account: ${verificationLink}`
    };
    console.log(mailOptions);

    // Send email
    const info = await transporter.sendMail(mailOptions);

    console.log(`Message sent: ${info.messageId}`);
    return { status: 'success', messageId: info.messageId, token };

  } catch (error) {
    console.error(`Error occurred: ${error.message}`);
    return { status: 'error', error: error.message };
  }
};

module.exports = {
  sendVerificationEmail
};
