# Use the latest Node.js image as the base
FROM node:latest

# Set the working directory inside the container to /app
WORKDIR /app

# Copy package.json and package-lock.json (if available) to the working directory
COPY ../package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of the application's source code
COPY . .

# Expose the port
EXPOSE 3000

# Run the app
CMD ["node", "server.js"]
