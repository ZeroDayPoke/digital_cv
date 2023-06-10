// Load environment variables
require('dotenv').config()

const express = require('express');
const app = express();
const mailService = require('./services/mailService');

// Middleware to parse JSON bodies from the request
app.use(express.json());

// Define routes
app.post('/send-email', async (req, res) => {
  const { to } = req.body;
  const result = await mailService.sendVerificationEmail(to);
  
  if(result.status === 'error') {
    return res.status(500).send({ error: result.error });
  }
  
  return res.status(200).send({ message: "Email sent successfully!", token: result.token });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
